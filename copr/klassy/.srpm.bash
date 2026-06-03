#!/bin/bash
set -euo pipefail

SPEC=klassy.spec

spectool -g "$SPEC"
fedpkg srpm
