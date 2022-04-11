#!/bin/zsh
set -x
for dir in common connect partner sp; do
  rm -rf mica/$dir
done

#generate using the proto all image from namely
docker run --rm -it -v $PWD:/defs namely/protoc-all -d /defs/proto -l python -o mica

for dir in common connect partner sp; do
  for pythonfile in `find mica -name "*.py"` ; do
    sed -i.bak "s/^from ${dir}/from mica.${dir}/g" $pythonfile
  done
done

for file in `find . -name "*.bak"` ; do
  rm $file
done