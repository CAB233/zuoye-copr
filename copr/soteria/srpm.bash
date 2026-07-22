#!/bin/bash
set -euo pipefail

SPEC="$(basename $(pwd)).spec"
WORKDIR="$(mktemp -d)"
# https://github.com/U2FsdGVkX1/fedora-ashell/blob/75cd65b05e667cffc58d39cf346073a7393f4845/vendor.sh
VERSION="$(rpmspec -q --qf "%{VERSION}" "$SPEC")"

spectool -g "$SPEC"

tar xf "v$VERSION.tar.gz" -C "$WORKDIR"

pushd "$WORKDIR/soteria-$VERSION"
cargo-vendor-filterer --versioned-dirs vendor > "$OLDPWD/vendor.toml"
tar \
    --sort=name \
    --mtime="@${SOURCE_DATE_EPOCH:-0}" \
    --owner=0 --group=0 --numeric-owner \
    -cJf "$OLDPWD/soteria-$VERSION-vendor.tar.xz" vendor
popd

fedpkg srpm
