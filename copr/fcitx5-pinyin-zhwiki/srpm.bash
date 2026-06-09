#!/bin/bash
set -euo pipefail

SPEC=fcitx5-pinyin-zhwiki.spec

spectool -g "$SPEC"
fedpkg srpm
