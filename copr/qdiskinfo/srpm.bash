#!/bin/bash
set -euo pipefail

SPEC=qdiskinfo.spec

spectool -g "$SPEC"
fedpkg srpm
