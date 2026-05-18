#!/bin/bash

dnf install -y cargo2rpm cargo-vendor-filterer
spectool -g ciel.spec

# https://github.com/U2FsdGVkX1/fedora-ashell/blob/75cd65b05e667cffc58d39cf346073a7393f4845/vendor.sh
version="$(rpmspec -q --qf "%{VERSION}" ciel.spec)"
workdir="$(mktemp -d)"

tar xf "v${version}.tar.gz" -C "$workdir"

pushd "$workdir/ciel-rs-${version}"
cargo-vendor-filterer --versioned-dirs vendor > "${OLDPWD}/vendor.toml"
tar \
    --sort=name \
    --mtime="@${SOURCE_DATE_EPOCH:-0}" \
    --owner=0 --group=0 --numeric-owner \
    -cJf "${OLDPWD}/ciel-${version}-vendor.tar.xz" vendor
popd

fedpkg srpm
