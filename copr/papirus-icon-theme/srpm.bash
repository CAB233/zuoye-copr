#!/bin/bash
set -euo pipefail

SPEC="$(basename $(pwd)).spec"
REPO=https://github.com/PapirusDevelopmentTeam/papirus-icon-theme
WORKDIR="$(mktemp -d)"
_commit="$(grep -E '^%global[[:space:]]+commit[[:space:]]+' "$SPEC" | awk '{print $3}')"

dnf install -y git
spectool -g "$SPEC"

git clone --filter=tree:0 "$REPO" "$WORKDIR"
pushd "$WORKDIR"
upstream_version="$(git describe --tags --abbrev=0 $_commit)"
commit_date="$(git show -s --format=%cd --date=format:%Y%m%d $_commit)"
popd

rpmbuild -bs "$SPEC" \
    --define "_sourcedir $(pwd)" \
    --define "_srcrpmdir $(pwd)" \
    --define "upstream_version $upstream_version" \
    --define "commit_date $commit_date"
