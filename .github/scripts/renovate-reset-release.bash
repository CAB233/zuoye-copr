#!/bin/bash

set -euo pipefail

if [ -z "${RENOVATE_POST_UPGRADE_COMMAND_DATA_FILE:-}" ]; then
    echo "Error: RENOVATE_POST_UPGRADE_COMMAND_DATA_FILE is not set" >&2
    exit 1
fi

echo "RENOVATE_POST_UPGRADE_COMMAND_DATA_FILE: ${RENOVATE_POST_UPGRADE_COMMAND_DATA_FILE}"

spec_file=$(sed -n '1p' "$RENOVATE_POST_UPGRADE_COMMAND_DATA_FILE")

sed -i -E 's/^(Release:[[:space:]]*)[0-9]+(.*)$/\11%{?dist}/' "$spec_file"
