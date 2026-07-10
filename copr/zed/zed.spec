# we're using prebuilt binaries.
%global debug_package %{nil}

Name:           zed
Version:        1.10.1
Release:        1%{?dist}
Summary:        General-purpose, multiplayer code editor

License:        MIT
URL:            https://github.com/zed-industries/zed
Source0:        %{url}/releases/download/v%{version}/zed-linux-x86_64.tar.gz
Source1:        %{url}/releases/download/v%{version}/zed-linux-aarch64.tar.gz

%description
Code at the speed of thought - Zed is a high-performance,
multiplayer code editor from the creators of Atom and Tree-sitter. 

%prep
%autosetup -c -T
%ifarch x86_64
tar xf %{S:0}
%endif
%ifarch aarch64
tar xf %{S:1}
%endif

%build
# we're using prebuilt binaries.

%install
install -Dvm755 zed.app/bin/zed -t %{buildroot}%{_bindir}/
install -Dvm755 zed.app/libexec/zed-editor -t %{buildroot}%{_libexecdir}/
mkdir -pv %{buildroot}%{_datadir}/
cp -rv zed.app/share/* %{buildroot}%{_datadir}/

%files
%license zed.app/licenses.md
%{_bindir}/zed
%{_libexecdir}/zed-editor
%{_datadir}/applications/dev.zed.Zed.desktop
%{_datadir}/icons/hicolor/
