#!/bin/bash
set -euo pipefail

SPEC=deno.spec

spectool -g "$SPEC"
fedpkg srpm
