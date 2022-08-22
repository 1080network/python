.PHONY: build
build: clean test
	python setup.py bdist_wheel

.PHONY: clean
clean:
	rm -rf build dist *.egg-info .pytest_cache

.PHONY: test
test:
	python3 -m pytest tests

.PHONY: package_check
package_check: build
	twine check dist/*
	twine upload -r testpypi dist/*

.PHONY: publish
publish: package_check
	twine upload dist/*

