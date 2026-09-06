Name:           systemd-boot-friend-rs
Version:        0.28.0
Release:        1%{?dist}
Summary:        A kernel version manager for systemd-boot

License:        MIT
URL:            https://github.com/AOSC-Dev/systemd-boot-friend-rs
Source0:        %{url}/archive/v%{version}/v%{version}.tar.gz
Source1:        %{name}-%{version}-vendor.tar.xz
Source2:        vendor.toml
Source3:        systemd-boot-friend.conf

BuildRequires:  cargo-rpm-macros >= 24

%description
A kernel version manager for systemd-boot

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

%install
%cargo_install
install -Dvm644 completions/sbf.bash %{buildroot}%{bash_completions_dir}/sbf
install -Dvm644 completions/_sbf %{buildroot}%{zsh_completions_dir}/_sbf
install -Dvm644 completions/sbf.fish %{buildroot}%{fish_completions_dir}/sbf.fish
install -Dvm644 %{S:3} %{buildroot}%{_sysconfdir}/systemd-boot-friend.conf

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_sysconfdir}/systemd-boot-friend.conf
%{_bindir}/sbf
%{bash_completions_dir}/sbf
%{zsh_completions_dir}/_sbf
%{fish_completions_dir}/sbf.fish
