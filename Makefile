SUBDIRS := micasdk
TOPTARGETS := clean build test package publish

$(TOPTARGETS): $(SUBDIRS)
$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

.PHONY: $(TOPTARGETS) $(SUBDIRS)

.PHONY: setup_sdk
## Setup the micacommon library
setup_sdk: venv
	@make -C micasdk local_install

WORKDIR=.
VENVDIR=$(WORKDIR)/venv
include Makefile.venv.mk
