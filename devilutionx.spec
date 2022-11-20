%define _disable_ld_no_undefined 1

%define oname   devilutionX

Name:           devilutionx
Version:        1.4.1
Release:        1
Summary:        An open source implementation of the Diablo 1 game engine
License:        Public Domain
Group:          Games/Adventure
URL:            https://github.com/diasurgical/devilutionX
#Source:         https://github.com/diasurgical/devilutionX/archive/%{version}/%{oname}-%{version}.tar.gz
Source0:        https://github.com/diasurgical/devilutionX/releases/download/%{version}/devilutionx-src.tar.xz
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gtest)
BuildRequires:  libnatpmp-devel

#Requires:       fonts-ttf-charis-sil
Requires:       SDL2_mixer-player


%description
DevilutionX is a open source implementation of the game engine used
in Diablo1.
This package only includes the binary files, you still need the data
files from the original Diablo1 CD.

%prep
%setup -q -n devilutionx-src-%{version}
%autopatch -p0
sed -i 's/\r$//' README.md

%build
export CXXFLAGS='%{optflags} -DTTF_FONT_PATH=\"/usr/share/fonts/truetype/CharisSILB.ttf\"'
%cmake \
  -DBINARY_RELEASE=ON \
  -DVERSION_NUM=%{version}
%make_build

%install
install -D -m 0755 build/devilutionx %{buildroot}%{_bindir}/devilutionx
install -p -D -m644 Packaging/resources/icon.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
install -p -D -m644 Packaging/fedora/devilutionx.desktop %{buildroot}%{_datadir}/applications/devilutionx.desktop
install -p -D -m644 Packaging/resources/CharisSILB.ttf %{buildroot}%{_datadir}/fonts/truetype/CharisSILB.ttf
install -m 755 build/devilutionx %{buildroot}%{_bindir}/%{name}


%post
echo "copy diabdat.mpq to ~/.local/share/diasurgical/devilution/"

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/512x512/apps/devilutionx.png
%{_datadir}/applications/*
%{_datadir}/fonts/truetype/CharisSILB.ttf
