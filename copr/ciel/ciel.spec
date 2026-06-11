%global         build_rustflags %build_rustflags -Clink-arg=-fuse-ld=lld

Name:           ciel
Version:        3.10.4
Release:        2%{?dist}
Summary:        A tool for controlling AOSC OS packaging environments

SourceLicense:  MIT
# LICENSE.dependencies contains a full license breakdown
# cargo2rpm --path Cargo.toml license-breakdown
License:        %{shrink:
    (MIT OR Apache-2.0) AND Unicode-3.0: unicode-ident v1.0.24
    0BSD OR MIT OR Apache-2.0: adler2 v2.0.1
    Apache-2.0 AND ISC: ring v0.17.14
    Apache-2.0 OR ISC OR MIT: rustls v0.23.37
    Apache-2.0 OR MIT: async-channel v2.5.0
    Apache-2.0 OR MIT: async-executor v1.14.0
    Apache-2.0 OR MIT: async-io v2.6.0
    Apache-2.0 OR MIT: async-lock v3.4.2
    Apache-2.0 OR MIT: async-process v2.5.0
    Apache-2.0 OR MIT: async-signal v0.2.13
    Apache-2.0 OR MIT: async-task v4.7.1
    Apache-2.0 OR MIT: atomic-waker v1.1.2
    Apache-2.0 OR MIT: blocking v1.6.2
    Apache-2.0 OR MIT: concurrent-queue v2.5.0
    Apache-2.0 OR MIT: encode_unicode v1.0.0
    Apache-2.0 OR MIT: event-listener v5.4.1
    Apache-2.0 OR MIT: event-listener-strategy v0.5.4
    Apache-2.0 OR MIT: fastrand v2.3.0
    Apache-2.0 OR MIT: futures-lite v2.6.1
    Apache-2.0 OR MIT: idna_adapter v1.2.1
    Apache-2.0 OR MIT: parking v2.2.1
    Apache-2.0 OR MIT: pin-project-lite v0.2.17
    Apache-2.0 OR MIT: polling v3.11.0
    Apache-2.0 OR MIT: portable-atomic v1.13.1
    Apache-2.0 OR MIT: utf8_iter v1.0.4
    Apache-2.0 OR MIT: utf8parse v0.2.2
    Apache-2.0 OR MIT: uuid v1.22.0
    Apache-2.0 OR MIT: zeroize v1.8.2
    Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT: linux-raw-sys v0.12.1
    Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT: rustix v1.1.4
    Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT: wasi v0.11.1+wasi-snapshot-preview1
    Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT: wasip2 v1.0.2+wasi-0.2.9
    Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT: wasip3 v0.4.0+wasi-0.3.0-rc-2026-01-06
    Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT: wit-bindgen v0.51.0
    Apache-2.0: wincode v0.2.5
    BSD-2-Clause OR Apache-2.0 OR MIT: zerocopy v0.8.47
    BSD-3-Clause: subtle v2.6.1
    CDLA-Permissive-2.0: webpki-roots v1.0.6
    ISC: inotify v0.11.1
    ISC: inotify-sys v0.1.5
    ISC: rustls-webpki v0.103.10
    ISC: untrusted v0.9.0
    LGPL-2.1-or-later WITH GCC-exception-2.0: libsystemd-sys v0.9.4
    MIT OR Apache-2.0 OR LGPL-2.1-or-later: r-efi v5.3.0
    MIT OR Apache-2.0 OR LGPL-2.1-or-later: r-efi v6.0.0
    MIT OR Apache-2.0: anstream v1.0.0
    MIT OR Apache-2.0: anstyle v1.0.14
    MIT OR Apache-2.0: anstyle-parse v1.0.0
    MIT OR Apache-2.0: anstyle-query v1.1.5
    MIT OR Apache-2.0: anstyle-wincon v3.0.11
    MIT OR Apache-2.0: anyhow v1.0.102
    MIT OR Apache-2.0: async-broadcast v0.7.2
    MIT OR Apache-2.0: base64 v0.22.1
    MIT OR Apache-2.0: bitflags v2.11.0
    MIT OR Apache-2.0: block-buffer v0.10.4
    MIT OR Apache-2.0: cfg-if v1.0.4
    MIT OR Apache-2.0: clap v4.6.0
    MIT OR Apache-2.0: clap_builder v4.6.0
    MIT OR Apache-2.0: clap_lex v1.1.0
    MIT OR Apache-2.0: colorchoice v1.0.5
    MIT OR Apache-2.0: cpufeatures v0.2.17
    MIT OR Apache-2.0: crc32fast v1.5.0
    MIT OR Apache-2.0: crossbeam-deque v0.8.6
    MIT OR Apache-2.0: crossbeam-epoch v0.9.18
    MIT OR Apache-2.0: crossbeam-utils v0.8.21
    MIT OR Apache-2.0: crypto-common v0.1.7
    MIT OR Apache-2.0: ctrlc v3.5.2
    MIT OR Apache-2.0: deranged v0.5.8
    MIT OR Apache-2.0: digest v0.10.7
    MIT OR Apache-2.0: either v1.15.0
    MIT OR Apache-2.0: enumflags2 v0.7.12
    MIT OR Apache-2.0: env_home v0.1.0
    MIT OR Apache-2.0: errno v0.3.14
    MIT OR Apache-2.0: filetime v0.2.27
    MIT OR Apache-2.0: flate2 v1.1.9
    MIT OR Apache-2.0: form_urlencoded v1.2.2
    MIT OR Apache-2.0: fs3 v0.5.0
    MIT OR Apache-2.0: futures-core v0.3.32
    MIT OR Apache-2.0: futures-io v0.3.32
    MIT OR Apache-2.0: getrandom v0.2.17
    MIT OR Apache-2.0: getrandom v0.3.4
    MIT OR Apache-2.0: getrandom v0.4.2
    MIT OR Apache-2.0: git2 v0.20.4
    MIT OR Apache-2.0: hash32 v0.3.1
    MIT OR Apache-2.0: heapless v0.8.0
    MIT OR Apache-2.0: hermit-abi v0.5.2
    MIT OR Apache-2.0: hex v0.4.3
    MIT OR Apache-2.0: http v1.4.0
    MIT OR Apache-2.0: httparse v1.10.1
    MIT OR Apache-2.0: idna v1.1.0
    MIT OR Apache-2.0: is_terminal_polyfill v1.70.2
    MIT OR Apache-2.0: itoa v1.0.18
    MIT OR Apache-2.0: js-sys v0.3.91
    MIT OR Apache-2.0: libc v0.2.183
    MIT OR Apache-2.0: libgit2-sys v0.18.3+1.9.2
    MIT OR Apache-2.0: libmount v0.1.15 (https: OR  OR github.com OR liushuyu OR libmount?rev=6fe8dba03a6404dfe1013995dd17af1c4e21c97b#6fe8dba0)
    MIT OR Apache-2.0: libssh2-sys v0.3.1
    MIT OR Apache-2.0: libz-sys v1.1.25
    MIT OR Apache-2.0: log v0.4.29
    MIT OR Apache-2.0: lzma-sys v0.1.20
    MIT OR Apache-2.0: num-conv v0.2.0
    MIT OR Apache-2.0: once_cell v1.21.4
    MIT OR Apache-2.0: once_cell_polyfill v1.70.2
    MIT OR Apache-2.0: openssl-probe v0.1.6
    MIT OR Apache-2.0: ordered-stream v0.2.0
    MIT OR Apache-2.0: percent-encoding v2.3.2
    MIT OR Apache-2.0: piper v0.2.5
    MIT OR Apache-2.0: plain v0.2.3
    MIT OR Apache-2.0: powerfmt v0.2.0
    MIT OR Apache-2.0: ppv-lite86 v0.2.21
    MIT OR Apache-2.0: proc-macro2 v1.0.106
    MIT OR Apache-2.0: quick-error v2.0.1
    MIT OR Apache-2.0: quote v1.0.45
    MIT OR Apache-2.0: rand v0.9.2
    MIT OR Apache-2.0: rand_chacha v0.9.0
    MIT OR Apache-2.0: rand_core v0.9.5
    MIT OR Apache-2.0: rayon v1.11.0
    MIT OR Apache-2.0: rayon-core v1.13.0
    MIT OR Apache-2.0: rustls-pki-types v1.14.0
    MIT OR Apache-2.0: serde v1.0.228
    MIT OR Apache-2.0: serde_core v1.0.228
    MIT OR Apache-2.0: serde_json v1.0.149
    MIT OR Apache-2.0: serde_spanned v1.0.4
    MIT OR Apache-2.0: sha2 v0.10.9
    MIT OR Apache-2.0: shell-words v1.1.1
    MIT OR Apache-2.0: signal-hook-registry v1.4.8
    MIT OR Apache-2.0: smallvec v1.15.1
    MIT OR Apache-2.0: socket2 v0.6.3
    MIT OR Apache-2.0: stable_deref_trait v1.2.1
    MIT OR Apache-2.0: syn v2.0.117
    MIT OR Apache-2.0: tar v0.4.45
    MIT OR Apache-2.0: tempfile v3.27.0
    MIT OR Apache-2.0: terminal_size v0.4.3
    MIT OR Apache-2.0: thiserror v2.0.18
    MIT OR Apache-2.0: thread_local v1.1.9
    MIT OR Apache-2.0: time v0.3.47
    MIT OR Apache-2.0: time-core v0.1.8
    MIT OR Apache-2.0: toml v0.9.12+spec-1.1.0
    MIT OR Apache-2.0: toml_datetime v0.7.5+spec-1.1.0
    MIT OR Apache-2.0: toml_parser v1.0.10+spec-1.1.0
    MIT OR Apache-2.0: toml_writer v1.0.7+spec-1.1.0
    MIT OR Apache-2.0: typenum v1.19.0
    MIT OR Apache-2.0: unicode-width v0.2.2
    MIT OR Apache-2.0: ureq v3.3.0
    MIT OR Apache-2.0: ureq-proto v0.6.0
    MIT OR Apache-2.0: url v2.5.8
    MIT OR Apache-2.0: utf8-zero v0.8.1
    MIT OR Apache-2.0: wasm-bindgen v0.2.114
    MIT OR Apache-2.0: wasm-bindgen-shared v0.2.114
    MIT OR Apache-2.0: web-time v1.1.0
    MIT OR Apache-2.0: winapi v0.3.9
    MIT OR Apache-2.0: winapi-i686-pc-windows-gnu v0.4.0
    MIT OR Apache-2.0: winapi-x86_64-pc-windows-gnu v0.4.0
    MIT OR Apache-2.0: windows-link v0.2.1
    MIT OR Apache-2.0: windows-sys v0.52.0
    MIT OR Apache-2.0: windows-sys v0.60.2
    MIT OR Apache-2.0: windows-sys v0.61.2
    MIT OR Apache-2.0: windows-targets v0.52.6
    MIT OR Apache-2.0: windows-targets v0.53.5
    MIT OR Apache-2.0: windows_aarch64_gnullvm v0.52.6
    MIT OR Apache-2.0: windows_aarch64_gnullvm v0.53.1
    MIT OR Apache-2.0: windows_aarch64_msvc v0.52.6
    MIT OR Apache-2.0: windows_aarch64_msvc v0.53.1
    MIT OR Apache-2.0: windows_i686_gnu v0.52.6
    MIT OR Apache-2.0: windows_i686_gnu v0.53.1
    MIT OR Apache-2.0: windows_i686_gnullvm v0.52.6
    MIT OR Apache-2.0: windows_i686_gnullvm v0.53.1
    MIT OR Apache-2.0: windows_i686_msvc v0.52.6
    MIT OR Apache-2.0: windows_i686_msvc v0.53.1
    MIT OR Apache-2.0: windows_x86_64_gnu v0.52.6
    MIT OR Apache-2.0: windows_x86_64_gnu v0.53.1
    MIT OR Apache-2.0: windows_x86_64_gnullvm v0.52.6
    MIT OR Apache-2.0: windows_x86_64_gnullvm v0.53.1
    MIT OR Apache-2.0: windows_x86_64_msvc v0.52.6
    MIT OR Apache-2.0: windows_x86_64_msvc v0.53.1
    MIT OR Apache-2.0: xattr v1.6.1
    MIT OR Apache-2.0: xz2 v0.1.7
    MIT OR Apache-2.0: zstd-safe v7.2.4
    MIT OR Apache-2.0: zstd-sys v2.0.16+zstd.1.5.7
    MIT OR Zlib OR Apache-2.0: miniz_oxide v0.8.9
    MIT: ar v0.9.0
    MIT: block2 v0.6.2
    MIT: bytes v1.11.1
    MIT: ciel-rs v3.10.4
    MIT: console v0.16.3
    MIT: dialoguer v0.12.0
    MIT: dotenvy v0.15.7
    MIT: endi v1.1.1
    MIT: faster-hex v0.10.0
    MIT: fuzzy-matcher v0.3.7
    MIT: generic-array v0.14.7
    MIT: indicatif v0.18.4
    MIT: libredox v0.1.14
    MIT: memoffset v0.9.1
    MIT: mio v1.1.1
    MIT: nix v0.27.1
    MIT: nix v0.30.1
    MIT: nix v0.31.2
    MIT: objc2 v0.6.4
    MIT: objc2-encode v4.1.0
    MIT: openssl-sys v0.9.112
    MIT: redox_syscall v0.7.3
    MIT: simd-adler32 v0.3.8
    MIT: slab v0.4.12
    MIT: strsim v0.11.1
    MIT: tokio v1.50.0
    MIT: tracing v0.1.44
    MIT: tracing-core v0.1.36
    MIT: uds_windows v1.2.1
    MIT: unit-prefix v0.5.2
    MIT: unsquashfs-wrapper v0.3.1
    MIT: which v7.0.3
    MIT: which v8.0.2
    MIT: winnow v0.7.15
    MIT: winnow v1.0.0
    MIT: winsafe v0.0.19
    MIT: zbus v5.14.0
    MIT: zbus_names v4.3.1
    MIT: zmij v1.0.21
    MIT: zstd v0.13.3
    MIT: zvariant v5.10.0
    MIT: zvariant_utils v3.3.0
    Unicode-3.0: icu_collections v2.1.1
    Unicode-3.0: icu_locale_core v2.1.1
    Unicode-3.0: icu_normalizer v2.1.1
    Unicode-3.0: icu_normalizer_data v2.1.1
    Unicode-3.0: icu_properties v2.1.2
    Unicode-3.0: icu_properties_data v2.1.2
    Unicode-3.0: icu_provider v2.1.1
    Unicode-3.0: litemap v0.8.1
    Unicode-3.0: potential_utf v0.1.4
    Unicode-3.0: tinystr v0.8.2
    Unicode-3.0: writeable v0.6.2
    Unicode-3.0: yoke v0.8.1
    Unicode-3.0: zerofrom v0.1.6
    Unicode-3.0: zerotrie v0.2.3
    Unicode-3.0: zerovec v0.11.5
    Unlicense OR MIT: byteorder v1.5.0
    Unlicense OR MIT: memchr v2.8.0
    Unlicense OR MIT: same-file v1.0.6
    Unlicense OR MIT: tabwriter v1.4.1
    Unlicense OR MIT: walkdir v2.5.0
    Unlicense OR MIT: winapi-util v0.1.11
    Zlib OR Apache-2.0 OR MIT: dispatch2 v0.3.1
    Zlib: adler32 v1.2.0
}

URL:            https://github.com/AOSC-Dev/ciel-rs
Source0:        %{url}/archive/v%{version}/v%{version}.tar.gz
Source1:        ciel-%{version}-vendor.tar.xz
Source2:        vendor.toml

Requires:       systemd
Requires:       dbus
Requires:       openssl
Requires:       xz
Requires:       squashfs-tools
Requires:       systemd-container

BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc
BuildRequires:  clang
BuildRequires:  lld
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(zlib)

%description
A tool for controlling AOSC OS packaging environments using 
multi-layer filesystems and containers (version 3) 

%prep
%autosetup -a1 -n ciel-rs-%{version}
%cargo_prep -N

# include full configuration for vendored dependencies
cat %{S:2} >> .cargo/config.toml

%build
%cargo_build
%cargo_vendor_manifest
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
install -Dvm755 target/rpm/ciel-rs %{buildroot}%{_bindir}/ciel

# install plugins
install -Dvm755 plugins/* -t "%{buildroot}%{_libexecdir}/ciel-plugin/"

# install completions
install -Dvm644 completions/ciel.bash %{buildroot}%{bash_completions_dir}/ciel
install -Dvm644 completions/_ciel %{buildroot}%{zsh_completions_dir}/_ciel
install -Dvm644 completions/ciel.fish %{buildroot}%{fish_completions_dir}/ciel.fish

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/ciel
%{_libexecdir}/ciel-plugin/*
%{bash_completions_dir}/ciel
%{zsh_completions_dir}/_ciel
%{fish_completions_dir}/ciel.fish
