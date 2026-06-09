Name:           fluent-gtk-theme
Version:        20250417^git20251210.9fc5291
Release:        1%{?dist}
Summary:        Fluent design gtk theme for linux desktops

%global         short_commit %(bash -c "echo '%{version}' | sed 's/.*\\.//'")

License:        GPL-3.0-only
URL:            https://github.com/vinceliuice/Fluent-gtk-theme
Source:         %{url}/archive/%{short_commit}/Fluent-gtk-theme-%{short_commit}.tar.gz

BuildArch:      noarch

BuildRequires:  sassc

%description
Fluent design gtk theme for linux desktops

Requires:   filesystem
Requires:   gtk-murrine-engine

%prep
%autosetup -c -T
tar xvf %{S:0}
cp -rv Fluent-gtk-theme-*/* ./

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
