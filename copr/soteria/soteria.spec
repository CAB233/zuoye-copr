Name:           soteria
Version:        0.3.2
Release:        1%{?dist}
Summary:        A GTK-based polkit authentication agent

License:        Apache-2.0
URL:            https://github.com/imvaskel/soteria
Source0:        %{url}/archive/v%{version}/v%{version}.tar.gz
Source1:        %{name}-%{version}-vendor.tar.xz
Source2:        vendor.toml

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  gettext
BuildRequires:  gtk4-devel
BuildRequires:  polkit-devel

%description
A GTK-based polkit authentication agent

%prep
%autosetup -a1
%cargo_prep -N

# include full configuration for vendored dependencies
cat %{S:2} >> .cargo/config.toml

%build
%cargo_build
%cargo_vendor_manifest
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

for file in po/*.po; do
    lang=$(basename $file .po)
    msgfmt $file -o po/${lang}.mo
done

%install
%cargo_install

for file in po/*.po; do
    lang=$(basename $file .po)
    install -Dvm644 po/$lang.mo %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/soteria.mo
done
%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/soteria
