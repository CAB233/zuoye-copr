#!/bin/bash

dnf -y install go-vendor-tools
spectool -g sing-box.spec
go_vendor_archive create --config ./go-vendor-tools.toml ./sing-box.spec
fedpkg srpm
