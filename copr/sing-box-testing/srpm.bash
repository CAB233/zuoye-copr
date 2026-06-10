#!/bin/bash
set -euo pipefail

SPEC="$(basename $(pwd)).spec"

spectool -g "$SPEC"
go_vendor_archive create "$SPEC"
fedpkg srpm
