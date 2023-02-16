SUBDIRS := micacommon connect discount partner serviceprovider
TOPTARGETS := clean build test package publish

$(TOPTARGETS): $(SUBDIRS)
$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

.PHONY: $(TOPTARGETS) $(SUBDIRS)

.PHONY: setup_common
setup_common:
	@make -C micacommon local_install

.PHONY: generate
generate:
	./generate.sh