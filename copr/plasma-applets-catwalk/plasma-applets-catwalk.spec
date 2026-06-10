Name:           plasma-applets-catwalk
Version:        0^git20251029.eded6e7
Release:        1%{?dist}
Summary:        Simple plasmoid showing the total CPU usage

%global         short_commit %(bash -c "echo '%{version}' | sed 's/.*\\.//'")

License:        GPL-2.0-or-later
URL:            https://invent.kde.org/heddxh/applet-catwalk
Source:         %{url}/-/archive/%{short_commit}/applet-catwalk-%{short_commit}.tar.gz

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
%autosetup -n applet-catwalk-%{short_commit}

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
