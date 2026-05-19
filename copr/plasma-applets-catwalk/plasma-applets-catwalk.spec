%define upstream_version    0
%define commit_date         20251029
%define commit              eded6e762d9e2ba7db89aa05e58cd52909e1cd49
%global short_commit        %(c=%{commit}; echo ${c:0:7})

Name:           plasma-applets-catwalk
Version:        %{upstream_version}^git%{commit_date}.%{short_commit}
Release:        1%{?dist}
Summary:        Simple plasmoid showing the total CPU usage

License:        GPL-2.0-or-later
URL:            https://invent.kde.org/heddxh/applet-catwalk
Source0:        %{url}/-/archive/master/applet-catwalk-master.tar.gz

BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)

%description
Simple plasmoid showing the total CPU usage.
Visually made like RunCat.

%prep
%autosetup -n applet-catwalk-master

%build
%cmake -GNinja -Wno-dev
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_datadir}/locale/LC_MESSAGES/
%{_datadir}/plasma/plasmoids/org.kde.plasma.catwalk/

%changelog
%autochangelog
