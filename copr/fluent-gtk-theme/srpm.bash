#!/bin/bash
set -euo pipefail

SPEC=fluent-gtk-theme.spec
REPO=https://github.com/vinceliuice/Fluent-gtk-theme.git
WORKDIR="$(mktemp -d)"

dnf install -y git
spectool -g "$SPEC"

git clone --filter=tree:0 "$REPO" "$WORKDIR"
pushd "$WORKDIR"
upstream_version="$(git tag --sort=-version:refname | head -n1)"
commit_date="$(git show -s --format=%cd --date=format:%Y%m%d HEAD)"
commit="$(git rev-parse HEAD)"
popd

fedpkg srpm -- \
    -bs "$SPEC" \
    --define "_upstream_version $upstream_version" \
    --define "commit_date $commit_date" \
    --define "commit $commit"
