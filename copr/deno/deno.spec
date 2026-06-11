# we're using prebuilt binaries.
%global debug_package %{nil}

Name:           deno
Version:        2.8.3
Release:        1%{?dist}
Summary:        A modern runtime for JavaScript and TypeScript

License:        MIT
URL:            https://github.com/denoland/deno
Source0:        https://raw.githubusercontent.com/denoland/deno/refs/tags/v%{version}/README.md
Source1:        https://raw.githubusercontent.com/denoland/deno/refs/tags/v%{version}/LICENSE.md
Source2:        %{url}/releases/download/v%{version}/deno-x86_64-unknown-linux-gnu.zip
Source3:        %{url}/releases/download/v%{version}/deno-aarch64-unknown-linux-gnu.zip

%description
A modern runtime for JavaScript and TypeScript.

%prep
%autosetup -c -T
cp %{S:0} .
cp %{S:1} .
%ifarch x86_64
unzip %{S:2}
%endif
%ifarch aarch64
unzip %{S:3}
%endif

%build
# we're using prebuilt binaries.

%install
install -Dvm755 deno %{buildroot}%{_bindir}/deno

%{buildroot}%{_bindir}/deno completions bash | \
    install -Dvm644 /dev/stdin %{buildroot}%{bash_completions_dir}/deno
%{buildroot}%{_bindir}/deno completions zsh | \
    install -Dvm644 /dev/stdin %{buildroot}%{zsh_completions_dir}/_deno
%{buildroot}%{_bindir}/deno completions fish | \
    install -Dvm644 /dev/stdin %{buildroot}%{fish_completions_dir}/deno.fish

%files
%license LICENSE.md
%doc README.md
%{_bindir}/deno
%{bash_completions_dir}/deno
%{zsh_completions_dir}/_deno
%{fish_completions_dir}/deno.fish
