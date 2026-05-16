#!/bin/bash

dnf -y install python3-specfile go2rpm go-vendor-tools
spectool -g sing-box.spec
go_vendor_archive create sing-box.spec
fedpkg srpm
