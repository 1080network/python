#!/usr/bin/env python
"""Mica client SDK module"""

import io
from pathlib import Path

from setuptools import setup, find_packages

# Get the long description from the README file
with io.open('README.md', encoding='utf-8') as strm:
    long_description = strm.read()

with io.open('../requirements.txt') as f:
    install_require = [l.strip() for l in f if not l.startswith('#')]

with io.open('requirements.txt') as f:
    extras = [l.strip() for l in f if not l.startswith('#')]
    install_require.extend(extras)

with io.open('../requirements-dev.txt') as f:
    test_require = [l.strip() for l in f if not l.startswith('#')]

with io.open('requirements-dev.txt') as f:
    extras = [l.strip() for l in f if not l.startswith('#')]
    test_require.extend(extras)


# read the common indicators
about = {}
parent = Path().resolve().parent
about_path = parent.joinpath('about.py')
print(about_path.absolute())
with about_path.open(mode="r", encoding="utf-8") as f:
    exec(f.read(), about)

packages = find_packages(exclude=["tests"])

setup_params = dict(
    name="micaconnect",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    version=about["__version__"],
    license=about["__license__"],
    python_requires=about["__python_requires__"],
    description="MICA network connect sdk for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=install_require,
    tests_require=test_require,
    packages=packages
)


def main():
    """Package installation entry point."""
    setup(**setup_params)


if __name__ == '__main__':
    main()
