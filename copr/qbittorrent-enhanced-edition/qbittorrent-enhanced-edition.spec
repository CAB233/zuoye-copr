Name:           qbittorrent-enhanced-edition
Version:        5.1.3.10
Release:        1%{?dist}
Summary:        Bittorrent Client, based on qBittorrent

License:        GPL-2.0-or-later
URL:            https://github.com/c0re100/qBittorrent-Enhanced-Edition
Source0:        %{url}/archive/release-%{version}/release-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  ninja-build
BuildRequires:  systemd
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  libxkbcommon-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-linguist
BuildRequires:  rb_libtorrent-devel >= 1.2.12
BuildRequires:  desktop-file-utils
BuildRequires:  boost-devel >= 1.60
BuildRequires:  libappstream-glib
BuildRequires:  openssl-devel-engine
BuildRequires:  zlib-ng-compat-static

Requires:       python3
Requires:       qt6-qtsvg%{?_isa}

Recommends:     (qgnomeplatform-qt6%{?_isa} if gnome-shell)
Recommends:     (qgnomeplatform-qt6%{?_isa} if cinnamon)

Provides:       qbittorrent
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

%changelog
%autochangelog
