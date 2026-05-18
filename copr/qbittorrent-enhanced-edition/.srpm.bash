#!/bin/bash
set -euo pipefail

SPEC=qbittorrent-enhanced-edition.spec

spectool -g "$SPEC"
fedpkg srpm
