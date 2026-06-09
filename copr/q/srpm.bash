#!/bin/bash
set -euo pipefail

SPEC=q.spec

dnf -y install python3-specfile go2rpm go-vendor-tools
spectool -g "$SPEC"

go_vendor_archive create "$SPEC"

fedpkg srpm
