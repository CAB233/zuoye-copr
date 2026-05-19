# This versions need to be checked manually
%global upstream_ver 0.3.0
%global dict_ver 20260416

Name:           fcitx5-pinyin-zhwiki
Version:        %{upstream_ver}.%{dict_ver}
Release:        1%{?dist}
Summary:        Fcitx 5 Pinyin Dictionary from zh.wikipedia.org

License:        CC-BY-SA-4.0 GFDL-1.3-or-later
URL:            https://github.com/felixonmars/fcitx5-pinyin-zhwiki
Source0:        %{url}/releases/download/%{upstream_ver}/web-slang-%{dict_ver}.dict
Source1:        %{url}/releases/download/%{upstream_ver}/zhwiki-%{dict_ver}.dict
Source2:        %{url}/releases/download/%{upstream_ver}/zhwikisource-%{dict_ver}.dict 
Source3:        %{url}/releases/download/%{upstream_ver}/zhwiktionary-%{dict_ver}.dict
Source4:        https://raw.githubusercontent.com/felixonmars/fcitx5-pinyin-zhwiki/refs/tags/%{upstream_ver}/LICENSE

BuildArch:      noarch

%description
Fcitx 5 Pinyin Dictionary from zh.wikipedia.org

%prep
%autosetup -c -T
cp %{S:4} .

%build
# we're using prebuilt binaries.

%install
install -Dvm644 %{S:0} %{buildroot}%{_datadir}/fcitx5/pinyin/dictionaries/web-slang.dict
install -Dvm644 %{S:1} %{buildroot}%{_datadir}/fcitx5/pinyin/dictionaries/zhwiki.dict
install -Dvm644 %{S:2} %{buildroot}%{_datadir}/fcitx5/pinyin/dictionaries/zhwikisource.dict
install -Dvm644 %{S:3} %{buildroot}%{_datadir}/fcitx5/pinyin/dictionaries/zhwiktionary.dict

%files
%license LICENSE
%{_datadir}/fcitx5/pinyin/dictionaries/

%changelog
%autochangelog
