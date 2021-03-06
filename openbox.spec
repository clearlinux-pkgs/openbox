#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA5A4E99C711D3B61 (mikachu@comhem.se)
#
Name     : openbox
Version  : 3.6.1
Release  : 4
URL      : http://openbox.org/dist/openbox/openbox-3.6.1.tar.xz
Source0  : http://openbox.org/dist/openbox/openbox-3.6.1.tar.xz
Source1  : http://openbox.org/dist/openbox/openbox-3.6.1.tar.xz.asc
Summary  : Openbox Toolkit Library
Group    : Development/Tools
License  : GPL-2.0
Requires: openbox-bin = %{version}-%{release}
Requires: openbox-data = %{version}-%{release}
Requires: openbox-lib = %{version}-%{release}
Requires: openbox-libexec = %{version}-%{release}
Requires: openbox-license = %{version}-%{release}
Requires: openbox-locales = %{version}-%{release}
Requires: openbox-man = %{version}-%{release}
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(imlib2)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libstartup-notification-1.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(pangoxft)
BuildRequires : pkgconfig(xcursor)

%description
Openbox
----
This software is OSI Certified Open Source Software.
OSI Certified is a certification mark of the Open Source Initiative.

%package bin
Summary: bin components for the openbox package.
Group: Binaries
Requires: openbox-data = %{version}-%{release}
Requires: openbox-libexec = %{version}-%{release}
Requires: openbox-license = %{version}-%{release}

%description bin
bin components for the openbox package.


%package data
Summary: data components for the openbox package.
Group: Data

%description data
data components for the openbox package.


%package dev
Summary: dev components for the openbox package.
Group: Development
Requires: openbox-lib = %{version}-%{release}
Requires: openbox-bin = %{version}-%{release}
Requires: openbox-data = %{version}-%{release}
Provides: openbox-devel = %{version}-%{release}
Requires: openbox = %{version}-%{release}

%description dev
dev components for the openbox package.


%package doc
Summary: doc components for the openbox package.
Group: Documentation
Requires: openbox-man = %{version}-%{release}

%description doc
doc components for the openbox package.


%package lib
Summary: lib components for the openbox package.
Group: Libraries
Requires: openbox-data = %{version}-%{release}
Requires: openbox-libexec = %{version}-%{release}
Requires: openbox-license = %{version}-%{release}

%description lib
lib components for the openbox package.


%package libexec
Summary: libexec components for the openbox package.
Group: Default
Requires: openbox-license = %{version}-%{release}

%description libexec
libexec components for the openbox package.


%package license
Summary: license components for the openbox package.
Group: Default

%description license
license components for the openbox package.


%package locales
Summary: locales components for the openbox package.
Group: Default

%description locales
locales components for the openbox package.


%package man
Summary: man components for the openbox package.
Group: Default

%description man
man components for the openbox package.


%prep
%setup -q -n openbox-3.6.1
cd %{_builddir}/openbox-3.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605557277
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1605557277
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openbox
cp %{_builddir}/openbox-3.6.1/COPYING %{buildroot}/usr/share/package-licenses/openbox/dfac199a7539a404407098a2541b9482279f690d
%make_install
%find_lang openbox

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gdm-control
/usr/bin/gnome-panel-control
/usr/bin/obxprop
/usr/bin/openbox
/usr/bin/openbox-gnome-session
/usr/bin/openbox-kde-session
/usr/bin/openbox-session

%files data
%defattr(-,root,root,-)
/usr/share/applications/openbox.desktop
/usr/share/gnome-session/sessions/openbox-gnome-fallback.session
/usr/share/gnome-session/sessions/openbox-gnome.session
/usr/share/gnome/wm-properties/openbox.desktop
/usr/share/pixmaps/openbox.png
/usr/share/themes/Artwiz-boxed/openbox-3/themerc
/usr/share/themes/Bear2/openbox-3/close.xbm
/usr/share/themes/Bear2/openbox-3/close_pressed.xbm
/usr/share/themes/Bear2/openbox-3/desk.xbm
/usr/share/themes/Bear2/openbox-3/desk_toggled.xbm
/usr/share/themes/Bear2/openbox-3/iconify.xbm
/usr/share/themes/Bear2/openbox-3/iconify_pressed.xbm
/usr/share/themes/Bear2/openbox-3/max.xbm
/usr/share/themes/Bear2/openbox-3/max_pressed.xbm
/usr/share/themes/Bear2/openbox-3/max_toggled.xbm
/usr/share/themes/Bear2/openbox-3/shade.xbm
/usr/share/themes/Bear2/openbox-3/shade_pressed.xbm
/usr/share/themes/Bear2/openbox-3/themerc
/usr/share/themes/Clearlooks-3.4/openbox-3/themerc
/usr/share/themes/Clearlooks-Olive/openbox-3/themerc
/usr/share/themes/Clearlooks/openbox-3/themerc
/usr/share/themes/Mikachu/openbox-3/bullet.xbm
/usr/share/themes/Mikachu/openbox-3/close.xbm
/usr/share/themes/Mikachu/openbox-3/desk.xbm
/usr/share/themes/Mikachu/openbox-3/iconify.xbm
/usr/share/themes/Mikachu/openbox-3/max.xbm
/usr/share/themes/Mikachu/openbox-3/themerc
/usr/share/themes/Natura/openbox-3/close.xbm
/usr/share/themes/Natura/openbox-3/close_hover.xbm
/usr/share/themes/Natura/openbox-3/desk.xbm
/usr/share/themes/Natura/openbox-3/desk_hover.xbm
/usr/share/themes/Natura/openbox-3/desk_toggled.xbm
/usr/share/themes/Natura/openbox-3/iconify.xbm
/usr/share/themes/Natura/openbox-3/iconify_hover.xbm
/usr/share/themes/Natura/openbox-3/max.xbm
/usr/share/themes/Natura/openbox-3/max_hover.xbm
/usr/share/themes/Natura/openbox-3/max_toggled.xbm
/usr/share/themes/Natura/openbox-3/shade.xbm
/usr/share/themes/Natura/openbox-3/shade_hover.xbm
/usr/share/themes/Natura/openbox-3/themerc
/usr/share/themes/Onyx-Citrus/openbox-3/themerc
/usr/share/themes/Onyx/openbox-3/themerc
/usr/share/themes/Orang/openbox-3/themerc
/usr/share/themes/Syscrash/openbox-3/max.xbm
/usr/share/themes/Syscrash/openbox-3/max_disabled.xbm
/usr/share/themes/Syscrash/openbox-3/max_pressed.xbm
/usr/share/themes/Syscrash/openbox-3/max_toggled.xbm
/usr/share/themes/Syscrash/openbox-3/themerc
/usr/share/xsessions/openbox-gnome.desktop
/usr/share/xsessions/openbox-kde.desktop
/usr/share/xsessions/openbox.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/openbox/3.6/obrender/color.h
/usr/include/openbox/3.6/obrender/font.h
/usr/include/openbox/3.6/obrender/geom.h
/usr/include/openbox/3.6/obrender/gradient.h
/usr/include/openbox/3.6/obrender/image.h
/usr/include/openbox/3.6/obrender/instance.h
/usr/include/openbox/3.6/obrender/mask.h
/usr/include/openbox/3.6/obrender/render.h
/usr/include/openbox/3.6/obrender/theme.h
/usr/include/openbox/3.6/obrender/version.h
/usr/include/openbox/3.6/obt/display.h
/usr/include/openbox/3.6/obt/keyboard.h
/usr/include/openbox/3.6/obt/link.h
/usr/include/openbox/3.6/obt/paths.h
/usr/include/openbox/3.6/obt/prop.h
/usr/include/openbox/3.6/obt/signal.h
/usr/include/openbox/3.6/obt/util.h
/usr/include/openbox/3.6/obt/version.h
/usr/include/openbox/3.6/obt/xml.h
/usr/include/openbox/3.6/obt/xqueue.h
/usr/lib64/libobrender.so
/usr/lib64/libobt.so
/usr/lib64/pkgconfig/obrender-3.5.pc
/usr/lib64/pkgconfig/obt-3.5.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/openbox/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libobrender.so.32
/usr/lib64/libobrender.so.32.0.0
/usr/lib64/libobt.so.2
/usr/lib64/libobt.so.2.0.2

%files libexec
%defattr(-,root,root,-)
/usr/libexec/openbox-autostart
/usr/libexec/openbox-xdg-autostart

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openbox/dfac199a7539a404407098a2541b9482279f690d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/obxprop.1
/usr/share/man/man1/openbox-gnome-session.1
/usr/share/man/man1/openbox-kde-session.1
/usr/share/man/man1/openbox-session.1
/usr/share/man/man1/openbox.1

%files locales -f openbox.lang
%defattr(-,root,root,-)

