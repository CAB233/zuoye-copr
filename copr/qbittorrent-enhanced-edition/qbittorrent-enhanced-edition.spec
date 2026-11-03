Name:           qbittorrent-enhanced-edition
Version:        5.2.4.10
Release:        2%{?dist}
Summary:        Bittorrent Client, based on qBittorrent

License:        GPL-2.0-or-later
URL:            https://github.com/c0re100/qBittorrent-Enhanced-Edition
Source0:        %{url}/archive/release-%{version}/release-%{version}.tar.gz

BuildRequires: appstream
BuildRequires: boost-devel >= 1.76
BuildRequires: cmake
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: gnupg2
BuildRequires: ninja-build
BuildRequires: openssl-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: rb_libtorrent-devel >= 1.2.19
BuildRequires: systemd
BuildRequires: systemd-rpm-macros
BuildRequires: zlib-ng-compat-static

Requires:       python3
Requires:       qt6-qtsvg%{?_isa}

Recommends:     (qgnomeplatform-qt6%{?_isa} if gnome-shell)
Recommends:     (qgnomeplatform-qt6%{?_isa} if cinnamon)

Provides:       qbittorrent = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:      qbittorrent

%description
[Unofficial] qBittorrent Enhanced, based on qBittorrent

%prep
%autosetup -n qBittorrent-Enhanced-Edition-release-%{version}

%build
%cmake -GNinja -Wno-dev
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md AUTHORS Changelog
%{_bindir}/qbittorrent
%{_metainfodir}/org.qbittorrent.qBittorrent.metainfo.xml
%{_datadir}/applications/org.qbittorrent.qBittorrent.desktop
%{_datadir}/icons/hicolor/*/apps/qbittorrent.*
%{_datadir}/icons/hicolor/*/status/qbittorrent-tray*
%{_mandir}/man1/qbittorrent.1*
%{_mandir}/ru/man1/qbittorrent.1*
