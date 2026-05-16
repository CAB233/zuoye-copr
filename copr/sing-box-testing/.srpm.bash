#!/bin/bash

dnf -y install go2rpm go-vendor-tools
spectool -g sing-box-testing.spec
go_vendor_archive create sing-box-testing.spec
fedpkg srpm
