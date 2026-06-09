#!/bin/bash
set -euo pipefail

SPEC=nexttrace.spec

# Need latest golang to vendor.
dnf -y --repofrompath='golang,https://download.copr.fedorainfracloud.org/results/@go-sig/golang-rawhide/fedora-$releasever-$basearch/' install golang
dnf -y install python3-specfile go2rpm go-vendor-tools
spectool -g "$SPEC"

go_vendor_archive create "$SPEC"

fedpkg srpm
