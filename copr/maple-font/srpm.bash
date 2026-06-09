#!/bin/bash
set -euo pipefail

SPEC=maple-font.spec

spectool -g "$SPEC"
fedpkg srpm
