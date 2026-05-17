Name:           maple-font
Version:        7.9
Release:        1%{?dist}
Summary:        Monospace font with round corner, ligatures, and nerd-font integration

License:        OFL-1.1
URL:            https://github.com/subframe7536/maple-font
Source0:        %{url}/releases/download/v%{version}/MapleMono-Variable.zip
Source1:        %{url}/releases/download/v%{version}/MapleMono-TTF.zip
Source2:        %{url}/releases/download/v%{version}/MapleMono-NF-unhinted.zip
Source3:        %{url}/releases/download/v%{version}/MapleMono-CN-unhinted.zip
Source4:        %{url}/releases/download/v%{version}/MapleMono-NF-CN-unhinted.zip

BuildArch:      noarch

%description
Open source monospace font with round corner, ligatures and Nerd-Font icons for
IDE and terminal, fine-grained customization options.

%prep
%autosetup -c -T
unzip -qo %{S:0}
unzip -qo %{S:1}
unzip -qo %{S:2}
unzip -qo %{S:3}
unzip -qo %{S:4}

%install
install -Dvm644 %{_builddir}/%{name}-%{version}/*.ttf -t %{buildroot}%{_datadir}/fonts/maple-font/

%files
%license LICENSE.txt
%{_datadir}/fonts/maple-font/

%changelog
%autochangelog
