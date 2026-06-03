#!/bin/bash
set -euo pipefail

SPEC=lxgwwenkai-fonts.spec

spectool -g "$SPEC"
fedpkg srpm
