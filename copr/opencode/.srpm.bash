#!/bin/bash
set -euo pipefail

SPEC=opencode.spec

spectool -g "$SPEC"
fedpkg srpm
