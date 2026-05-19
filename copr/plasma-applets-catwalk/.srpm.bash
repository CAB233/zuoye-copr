#!/bin/bash
set -euo pipefail

SPEC=plasma-applets-catwalk.spec
REPO=https://invent.kde.org/heddxh/applet-catwalk
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
    --define "upstream_version ${upstream_version:-0}" \
    --define "commit_date $commit_date" \
    --define "commit $commit"
