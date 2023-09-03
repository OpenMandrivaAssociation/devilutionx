%define _disable_ld_no_undefined 1
%ifarch %{aarch64}
%global optflags %{optflags} -march=armv8+crypto
%endif

%define oname   devilutionX

Name:           devilutionx
Version:        1.5.1
Release:        1
Summary:        An open source implementation of the Diablo 1 game engine
License:        Public Domain
Group:          Games/Adventure
URL:            https://github.com/diasurgical/devilutionX
#Source:         https://github.com/diasurgical/devilutionX/archive/%{version}/%{oname}-%{version}.tar.gz
Source0:        https://github.com/diasurgical/devilutionX/releases/download/%{version}/devilutionx-src.tar.xz
BuildRequires:  cmake
BuildRequires:	ninja
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(SDL2_image)
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
%autosetup -p0 -n devilutionx-src-%{version}
sed -i 's/\r$//' README.md

%build
export CXXFLAGS='%{optflags} -DTTF_FONT_PATH=\"/usr/share/fonts/truetype/CharisSILB.ttf\"'
%cmake \
	-DBINARY_RELEASE=ON \
	-DVERSION_NUM=%{version} \
	-G Ninja
export LD_LIBRARY_PATH=$(pwd)/test:$LD_LIBRARY_PATH
%ninja_build

%install
%ninja_install -C build

%post
echo "copy diabdat.mpq to ~/.local/share/diasurgical/devilution/"

%files
%doc README.md
%{_bindir}/%{name}
%{_datadir}/diasurgical
%{_datadir}/metainfo/devilutionx.metainfo.xml
%{_datadir}/icons/hicolor/512x512/apps/devilutionx*.png
%{_datadir}/applications/*
