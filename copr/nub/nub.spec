%global         __brp_mangle_shebangs %{nil}

Name:           nub
Version:        0.11.2
Release:        1%{?dist}
Summary:        The fast all-in-one Node.js toolkit

License:        MIT AND Apache-2.0 AND ISC
URL:            https://github.com/nubjs/nub
Source0:        %{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  clang-devel

%description
Nub is a TypeScript-first toolkit for Node.js: a file runner with support for
TypeScript, JSX and modern syntax, a script runner, the nubx package runner, a
package manager, a Node.js version manager and Corepack-style package-manager
shims. It is a single native Rust binary that augments stock Node.js rather than
replacing it, with automatic .env loading, data-format loaders and a built-in
watch mode.

%prep
%autosetup
%cargo_prep -N
%{__cargo} fetch --locked --config net.offline=false

%build
%cargo_build -- --frozen
%cargo_vendor_manifest
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
install -Dvm755 target/rpm/nub %{buildroot}%{_bindir}/nub
ln -sv nub %{buildroot}%{_bindir}/nubx
ln -sv nub %{buildroot}%{_bindir}/nubr

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/nub
%{_bindir}/nubx
%{_bindir}/nubr
