# we're using prebuilt binaries.
%global debug_package %{nil}

Name:           codex
Version:        0.130.0
Release:        1%{?dist}
Summary:        Lightweight coding agent that runs in your terminal

License:        MIT
URL:            https://github.com/openai/codex
Source0:        https://raw.githubusercontent.com/openai/codex/refs/tags/rust-v%{version}/README.md
Source1:        https://raw.githubusercontent.com/openai/codex/refs/tags/rust-v%{version}/LICENSE
Source2:        %{url}/releases/download/rust-v%{version}/codex-x86_64-unknown-linux-musl.tar.gz
Source3:        %{url}/releases/download/rust-v%{version}/codex-responses-api-proxy-x86_64-unknown-linux-musl.tar.gz
Source4:        %{url}/releases/download/rust-v%{version}/codex-aarch64-unknown-linux-musl.tar.gz
Source5:        %{url}/releases/download/rust-v%{version}/codex-responses-api-proxy-aarch64-unknown-linux-musl.tar.gz

%description
Lightweight coding agent that runs in your terminal

%prep
%autosetup -c -T
cp %{S:0} .
cp %{S:1} .
%ifarch x86_64
tar xf %{S:2}
tar xf %{S:3}
%endif
%ifarch aarch64
tar xf %{S:4}
tar xf %{S:5}
%endif

%build
# we're using prebuilt binaries.

%install
mv -v codex-responses-api-proxy-* codex-responses-api-proxy
mv -v codex-*-unknown-linux-musl codex
install -Dvm755 codex-responses-api-proxy -t %{buildroot}%{_bindir}/
install -Dvm755 codex -t %{buildroot}%{_bindir}/

%{buildroot}%{_bindir}/codex completion bash | \
    install -Dvm644 /dev/stdin %{buildroot}%{bash_completions_dir}/codex
%{buildroot}%{_bindir}/codex completion zsh | \
    install -Dvm644 /dev/stdin %{buildroot}%{zsh_completions_dir}/_codex
%{buildroot}%{_bindir}/codex completion fish | \
    install -Dvm644 /dev/stdin %{buildroot}%{fish_completions_dir}/codex.fish

%files
%license LICENSE
%doc README.md
%{_bindir}/codex
%{_bindir}/codex-responses-api-proxy
%{bash_completions_dir}/codex
%{zsh_completions_dir}/_codex
%{fish_completions_dir}/codex.fish

%changelog
%autochangelog
