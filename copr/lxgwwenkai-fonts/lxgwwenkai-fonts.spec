Name:           lxgwwenkai-fonts
Version:        1.522
Release:        1%{?dist}
Summary:        An unprofessional open-source Chinese font derived from Fontworks' Klee One

License:        OFL-1.1
URL:            https://github.com/lxgw/LxgwWenKai
Source0:        %{url}/releases/download/v%{version}/lxgw-wenkai-v%{version}.tar.gz
Source1:        %{url}TC/releases/download/v%{version}/lxgw-wenkai-tc-v%{version}.tar.gz

BuildArch:      noarch

%description
An unprofessional open-source Chinese font derived from Fontworks' Klee One.
一款非专业的开源中文字体，基于 FONTWORKS 出品字体 Klee One 衍生。

%prep
%autosetup -c -T
tar xvf %{S:0}
tar xvf %{S:1}

cp -v lxgw-wenkai-v%{version}/* ./
cp -v lxgw-wenkai-tc-v%{version}/* ./

%install
install -Dvm644 ./*.ttf -t %{buildroot}%{_datadir}/fonts/lxgwwenkai/

%files
%license OFL.txt
%{_datadir}/fonts/lxgwwenkai/

%changelog
%autochangelog
