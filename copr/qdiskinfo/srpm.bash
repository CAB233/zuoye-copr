#!/bin/bash
set -euo pipefail

SPEC="$(basename $(pwd)).spec"

spectool -g "$SPEC"
fedpkg srpm
