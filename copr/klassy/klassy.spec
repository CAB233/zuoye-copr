# Ref: https://github.com/MajorTomDE/rpm-packages/blob/main/klassy/klassy.spec
# Drop kf5 support.

Name:           klassy
Version:        6.7.1
Release:        1%{?dist}
Summary:        A highly customizable KDE Plasma Window Decoration

License:        BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND MIT
URL:            https://github.com/paulmcauley/klassy
Source:         %{url}/archive/v%{version}.tar.gz
Patch:          0001-Remove-shebang.patch

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  cmake(KDecoration3)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6FrameworkIntegration)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)

%description
Klassy is a highly customizable binary Window Decoration and Application Style
plugin for recent versions of the KDE Plasma desktop. It provides the Klassy,
Kite, Oxygen/Breeze, and Redmond icon styles.

%prep
%autosetup -p1

%build
%cmake -GNinja -Wno-dev \
    -DBUILD_TESTING=OFF \
    -DBUILD_QT5=OFF
%cmake_build

%install
%cmake_install

echo "== plasma desktoptheme =="
find %{buildroot}%{_datadir}/plasma -maxdepth 4 -type d -print || true
find %{buildroot}%{_datadir}/plasma -maxdepth 6 \( -iname '*klassy*' -o -iname '*klassy*' \) -print || true

%files
%doc README.md AUTHORS
%license LICENSES/*.txt
%{_bindir}/klassy-settings
%{_datadir}/applications/*
%{_datadir}/color-schemes/*.colors
%{_datadir}/icons/*
%{_datadir}/kstyle/themes/klassy.themerc
%{_datadir}/plasma/*
%{_datadir}/locale/*/LC_MESSAGES/klassy_*.mo
%{_datadir}/config.kcfg/klassy*
%{_libdir}/cmake/*
%{_libdir}/libklassycommon6.so*
%{_libdir}/qt6/plugins/*
