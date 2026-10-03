SPEC := $(notdir $(CURDIR)).spec

srpm:
	dnf install -y rpmspectool fedpkg python3-specfile
	spectool -g "$(SPEC)"
	fedpkg srpm
	cp ./*.src.rpm $(outdir)
