Name:           qdiskinfo
Version:        0.4
Release:        1%{?dist}
Summary:        CrystalDiskInfo alternative for Linux

License:        GPL-3.0-only
URL:            https://github.com/edisionnano/QDiskInfo
Source0:        %{url}/archive/%{version}/QDiskInfo-%{version}.tar.gz
Source1:        https://downloads.sourceforge.net/crystalmarkretro/2.0.6/CrystalMarkRetro2_0_6Aoi.zip

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6Core)

Requires:       smartmontools

%description
QDiskInfo is a frontend for smartctl (part of the smartmontools package).
It provides a user experience similar to CrystalDiskInfo.
It shows the SMART (Self-Monitoring, Analysis, and Reporting Technology) data
of modern hard disk drives.

%prep
%autosetup -n QDiskInfo-%{version}
unzip -qo %{S:1}
cp -v Resource/Theme/Aoi/SDAoiA-100.png dist/theme/good.png
cp -v Resource/Theme/Aoi/SDAoiC-100.png dist/theme/caution.png
cp -v Resource/Theme/Aoi/SDAoiD-100.png dist/theme/bad.png
cp -v Resource/Theme/Aoi/SDAoiE-100.png dist/theme/unknown.png
cp -v Resource/Theme/AoiLight/Background-300.png dist/theme/bg_light.png
cp -v Resource/Theme/AoiNight/Background-300.png dist/theme/bg_dark.png

%build
%cmake -GNinja -Wno-dev \
    -DQT_VERSION_MAJOR=6 \
    -DENABLE_TRANSLATIONS=ON \
    -DINCLUDE_OPTIONAL_RESOURCES=ON \
    -DCHARACTER_IS_RIGHT=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/QDiskInfo
%{_datadir}/applications/QDiskInfo.desktop
%{_datadir}/icons/hicolor/scalable/apps/QDiskInfo.svg

%changelog
%autochangelog
