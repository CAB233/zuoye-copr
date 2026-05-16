#!/bin/bash

dnf -y install go2rpm go-vendor-tools
spectool -g sing-box.spec
go_vendor_archive create sing-box.spec
fedpkg srpm
