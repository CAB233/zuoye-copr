# we're using prebuilt binaries.
%global debug_package %{nil}
%global __brp_strip %{nil}

Name:           opencode
Version:        1.18.1
Release:        1%{?dist}
Summary:        The open source coding agent

License:        MIT
URL:            https://github.com/anomalyco/opencode
Source0:        %{url}/archive/v%{version}/v%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/opencode-linux-x64.tar.gz
Source2:        %{url}/releases/download/v%{version}/opencode-linux-arm64.tar.gz

Requires:       git
Requires:       ripgrep

%description
The open source coding agent.

%prep
%autosetup
%ifarch x86_64
tar xf %{S:1}
%endif
%ifarch aarch64
tar xf %{S:2}
%endif

%build
# we're using prebuilt binaries.

%install
install -Dvm755 opencode %{buildroot}%{_bindir}/opencode

%{buildroot}%{_bindir}/opencode completions | \
    install -Dvm644 /dev/stdin %{buildroot}%{bash_completions_dir}/opencode

%files
%license LICENSE
%doc README*.md
%{_bindir}/opencode
%{bash_completions_dir}/opencode
