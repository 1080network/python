.PHONY: build
build: venv clean
	$(VENV)/python setup.py bdist_wheel

.PHONY: clean
clean:
	rm -rf build dist *.egg-info .pytest_cache

.PHONY: test
test:
	$(VENV)/python3 -m pytest tests

.PHONY: package_check
package_check: build
	twine check dist/*
	twine upload -r testpypi dist/*

.PHONY: publish
publish: package_check
	twine upload dist/*

.PHONY: local_install
local_install: venv build
	$(VENV)/pip3 install -e .

WORKDIR=..
VENVDIR=$(WORKDIR)/venv
include ../Makefile.venv.mk
