#!/bin/bash
set -euo pipefail

SPEC=codex.spec

spectool -g "$SPEC"
fedpkg srpm
