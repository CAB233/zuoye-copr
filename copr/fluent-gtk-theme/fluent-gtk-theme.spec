%define _upstream_version   2025-04-17
%define commit_date         20251210
%define commit              9fc52910aeda73804c41bfcebf2bbd29205a4756
%global short_commit        %(c=%{commit}; echo ${c:0:7})
%global upstream_version    %(v=%{_upstream_version}; echo ${v//-/})

Name:           fluent-gtk-theme
Version:        %{upstream_version}^git%{commit_date}.%{short_commit}
Release:        1%{?dist}
Summary:        Fluent design gtk theme for linux desktops

License:        GPL-3.0-only
URL:            https://github.com/vinceliuice/Fluent-gtk-theme
Source:         %{url}/archive/%{commit}/Fluent-gtk-theme-%{short_commit}.tar.gz

BuildArch:      noarch

BuildRequires:  sassc

%description
Fluent design gtk theme for linux desktops

Requires:   filesystem
Requires:   gtk-murrine-engine

%prep
%autosetup -n Fluent-gtk-theme-%{commit}

%build
# stub for rpmlint

%install
./install.sh \
    --dest %{buildroot}%{_datadir}/themes \
    --theme green \
    --icon fedora \
    --libadwaita \
    --tweaks solid round noborder square

%files
%license COPYING
%doc README.md
%{_datadir}/themes/*

%changelog
%autochangelog
