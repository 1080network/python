#!/usr/bin/env python
"""Mica client SDK module"""

from setuptools import setup
import io


# Get the long description from the README file
with io.open('README.md', encoding='utf-8') as strm:
    long_description = strm.read()

install_require = []
with io.open('requirements.txt') as f:
    install_require = [l.strip() for l in f if not l.startswith('#')]


setup_params = dict(
        name="mica-sdk",
        author="1080 Network",
        version="0.0.0",
        description="MICA payment network sdk for python",
        long_description=long_description,
        long_description_content_type="text/markdown",
        include_package_data=True,
        install_requires=install_require,
        python_requires='>=3.6.*',
        packages=["mica"]
)


def main():
    """Package installation entry point."""
    setup(**setup_params)


if __name__ == '__main__':
    main()
