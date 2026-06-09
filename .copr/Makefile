srpm:
	dnf install -y \
		rpmspectool fedpkg git python3-specfile \
	    cargo2rpm cargo-vendor-filterer \
	    go2rpm go-vendor-tools
	bash ./.srpm.bash
	cp ./*.src.rpm $(outdir)
