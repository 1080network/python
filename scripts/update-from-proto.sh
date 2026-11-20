#!/bin/bash
# Regenerate the SDK from the output of the "Generate SDKs" workflow in https://github.com/1080network/proto.
#
# Usage: scripts/update-from-proto.sh <version> <generated-dir>
#   <version>        release tag the code was generated from: vX.Y.Z or vX.Y.Z-preN
#   <generated-dir>  the downloaded workflow artifact (the directory containing python/)
#
# Download the generated code for a release with:
#   gh run download <run-id> -R 1080network/proto -n generated-sdks-<version>
#
# Set PYTHON to choose the interpreter used for the build (default: python3).
set -euo pipefail

VERSION=${1:?usage: $0 <version> <generated-dir>}
GEN=${2:?usage: $0 <version> <generated-dir>}
ROOT=$(cd "$(dirname "$0")/.." && pwd)
PYTHON=${PYTHON:-python3}

if [[ ! "$VERSION" =~ ^v([0-9]+\.[0-9]+\.[0-9]+)(-pre([0-9]+))?$ ]]; then
    echo "version '$VERSION' must look like v1.2.3 or v1.2.3-pre0" >&2
    exit 1
fi
# Python's version scheme: v2.0.0-pre0 is 2.0.0rc0
PYVERSION=${BASH_REMATCH[1]}
[[ -n "${BASH_REMATCH[3]}" ]] && PYVERSION="${PYVERSION}rc${BASH_REMATCH[3]}"

if [[ ! -d "$GEN/python/mica/issuer" ]]; then
    echo "'$GEN' does not look like generated output (expected python/mica/issuer)" >&2
    exit 1
fi

echo "Laying out $VERSION ($PYVERSION) from $GEN"
# Generated code only: hand-written code (common/mica/sdk, tests) is left alone.
rm -rf "$ROOT/common/mica/common" "$ROOT/common/mica/member" "$ROOT/common/micashared" "$ROOT/common/validate" \
       "$ROOT/issuer/mica" "$ROOT/acceptor/mica"
mkdir -p "$ROOT/common/mica" "$ROOT/issuer/mica" "$ROOT/acceptor/mica"
# validate_pb2 is imported by the generated modules and not published anywhere else, so micacommon ships it
cp -r "$GEN/python/micashared" "$GEN/python/validate" "$ROOT/common/"
cp -r "$GEN/python/mica/common" "$GEN/python/mica/member" "$ROOT/common/mica/"
cp -r "$GEN/python/mica/issuer" "$ROOT/issuer/mica/"
cp -r "$GEN/python/mica/acceptor" "$ROOT/acceptor/mica/"

for d in common issuer acceptor; do
    sed -i.bak -E "s/^version = \".*\"/version = \"$PYVERSION\"/; s/\"micacommon==[^\"]*\"/\"micacommon==$PYVERSION\"/" "$ROOT/$d/pyproject.toml"
    rm "$ROOT/$d/pyproject.toml.bak"
done

# Build the wheels, then install only the built wheels into a fresh environment and run the tests against them,
# so the test proves the packaging works and not just the source tree.
WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT
rm -rf "$ROOT/dist"
$PYTHON -m venv "$WORK/build" && "$WORK/build/bin/pip" install -q build
for d in common issuer acceptor; do
    "$WORK/build/bin/python" -m build --wheel --outdir "$ROOT/dist" "$ROOT/$d" >/dev/null
    rm -rf "$ROOT/$d/build" "$ROOT/$d"/*.egg-info
done
$PYTHON -m venv "$WORK/test"
"$WORK/test/bin/pip" install -q --find-links "$ROOT/dist" "$ROOT"/dist/micacommon-*.whl "$ROOT"/dist/micaissuer-*.whl \
    "$ROOT"/dist/micaacceptor-*.whl pytest cryptography
(cd "$WORK" && "$WORK/test/bin/python" -m pytest -q "$ROOT/common/tests" -p no:cacheprovider)
(cd "$WORK" && "$WORK/test/bin/python" -c "
import mica.issuer.service.v2.issuer_to_mica_service_pb2_grpc as i, mica.acceptor.service.v2.acceptor_to_mica_service_pb2_grpc as a
print('issuer and acceptor import OK')")
# The declared minimums (protobuf is the generated code's version, grpcio the lowest tested) must actually work
(cd "$WORK" && "$WORK/test/bin/pip" install -q "protobuf==6.32.1" "grpcio==1.74.0" \
    && "$WORK/test/bin/python" -m pytest -q "$ROOT/common/tests" -p no:cacheprovider)
echo "Done: wheels in dist/ ($PYVERSION)."
