%define oname   devilutionX

Name:           devilutionx
Version:        1.0.0
Release:        1
Summary:        An open source implementation of the Diablo 1 game engine
License:        Public Domain
Group:          Games/Adventure
URL:            https://github.com/diasurgical/devilutionX
Source:         https://github.com/diasurgical/devilutionX/archive/%{version}/%{oname}-%{version}.tar.gz
#Patch0:         devilutionx-fix-build-libsodium-openmandriva.patch
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  desktop-file-utils

#Requires:       fonts-ttf-charis-sil
Requires:       SDL2_mixer-player


%description
DevilutionX is a open source implementation of the game engine used
in Diablo1.
This package only includes the binary files, you still need the data
files from the original Diablo1 CD.

%prep
%setup -q -n devilutionX-%{version}
%autopatch -p0
sed -i 's/\r$//' README.md

%build
export CXXFLAGS='%{optflags} -DTTF_FONT_PATH=\"/usr/share/fonts/truetype/CharisSILB.ttf\"'
%cmake \
  -DBINARY_RELEASE=ON
%make_build

%install
install -D -m 0755 build/devilutionx %{buildroot}%{_bindir}/devilutionx
install -p -D -m644 Packaging/resources/16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -p -D -m644 Packaging/resources/Diablo_32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -D -m644 Packaging/resources/Diablo_48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -p -D -m644 Packaging/fedora/devilutionx.desktop %{buildroot}%{_datadir}/applications/devilutionx.desktop

install -m 755 build/devilutionx %{buildroot}%{_bindir}/%{name}


%post
echo "copy diabdat.mpq to ~/.local/share/diasurgical/devilution/"

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/*
