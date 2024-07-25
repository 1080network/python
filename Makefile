SUBDIRS := networksdk micacommon discount partner serviceprovider
TOPTARGETS := clean build test publish

$(TOPTARGETS): $(SUBDIRS)
$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

.PHONY: $(TOPTARGETS) $(SUBDIRS)

.PHONY: setup_common
setup_common:
	pip install -r requirements.txt
	@make -C micacommon local_install

.PHONY: generate
generate:
	./generate.sh
