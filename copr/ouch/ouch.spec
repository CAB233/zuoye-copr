%global         __brp_mangle_shebangs %{nil}

Name:           ouch
Version:        0.8.3
Release:        1%{?dist}
Summary:        Painless compression and decompression in the terminal

License:        MIT

URL:            https://github.com/ouch-org/ouch
Source:         %{url}/archive/%{version}/%{version}.tar.gz

BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  clang-devel

%description
Painless compression and decompression in the terminal. 

%prep
%autosetup
%cargo_prep -N
%{__cargo} fetch --locked --config net.offline=false

%build
# To generate manpage and completions.
export OUCH_ARTIFACTS_FOLDER=completions

%cargo_build -- --frozen
%cargo_vendor_manifest
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
install -Dvm755 target/rpm/ouch %{buildroot}%{_bindir}/ouch

install -Dvm644 completions/ouch.bash %{buildroot}%{bash_completions_dir}/ouch
install -Dvm644 completions/_ouch %{buildroot}%{zsh_completions_dir}/_ouch
install -Dvm644 completions/ouch.fish %{buildroot}%{fish_completions_dir}/ouch.fish

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/ouch
%{bash_completions_dir}/ouch
%{zsh_completions_dir}/_ouch
%{fish_completions_dir}/ouch.fish
