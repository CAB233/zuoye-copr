#!/bin/bash
set -euo pipefail

SPEC="$(basename $(pwd)).spec"

# Need latest golang to vendor.
dnf -y --repofrompath='golang,https://download.copr.fedorainfracloud.org/results/@go-sig/golang-rawhide/fedora-$releasever-$basearch/' install golang
spectool -g "$SPEC"
go_vendor_archive create "$SPEC"
fedpkg srpm
