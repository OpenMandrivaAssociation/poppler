%define major 5
%define glibmajor 4
%define qt3major 2
%define qt4major 3
%define libname		%mklibname %name %major
%define libnameglib	%mklibname %name-glib %glibmajor
%define libnameqt4	%mklibname %name-qt4- %qt4major
%define libnameqt	%mklibname %name-qt %qt3major
%define libnamedev	%mklibname -d %name
%define libnameglibdev	%mklibname -d %name-glib
%define libnameqtdev	%mklibname -d %name-qt
%define libnameqt4dev	%mklibname -d %name-qt4

%define qt3support 1

Name: poppler
Version: 0.12.0
Release: %mkrel 1
License: GPLv2+
Group: System/Libraries
URL: http://poppler.freedesktop.org
Summary: PDF rendering library
Source:	http://poppler.freedesktop.org/%{name}-%{version}.tar.gz
Patch2: poppler-ObjStream.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: qt4-devel
%if %qt3support
BuildRequires: qt3-devel
%endif
BuildRequires: gtk2-devel
BuildRequires: cairo-devel >= 1.8.4
BuildRequires: jpeg-devel
BuildRequires: gtk-doc
Obsoletes: 	xpdf-tools < 3.02-10mdv
Provides:	xpdf-tools
# Before 3.01pl2-2mdk xpdf-tools where in xpdf package
Conflicts:	xpdf < 3.01pl2-2mdk
Obsoletes:	pdftohtml
Provides:	pdftohtml

%description
Poppler is a PDF rendering library based on the xpdf-3.0 code base.

%package -n %{libname}
Summary:	PDF rendering library
Group:          System/Libraries
Suggests:	poppler-data

%description -n %{libname}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.

%package -n %{libnamedev}
Summary:	Development files for %{name}
Group:		Development/C++
Provides:	lib%{name}-devel = %{version}
Requires:	%{libname} = %{version}
Obsoletes:	%{libname}-devel

%description -n %{libnamedev}
Development files for %{name}

%package -n %{libnameqt}
Summary:	PDF rendering library - QT backend
Group:          System/Libraries

%description -n %{libnameqt}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.
This is the QT backend version.

%if %qt3support
%package -n %{libnameqtdev}
Summary:	Development files for %{name}-qt
Group:		Development/C++
Provides:	lib%{name}-qt-devel = %{version}
Requires:	%{libnameqt} = %{version}
Requires:	%libnamedev = %version
Obsoletes:	%libnameqt-devel

%description -n %{libnameqtdev}
Development files for %{name}-qt

%endif

%package  -n %{libnameqt4dev}
Summary:    Development files for %{name}-qt4
Group:      Development/C++
Provides:   lib%{name}-qt4-devel = %{version}
Requires:   %{libnameqt4} = %{version}
Requires:   %libnamedev = %version
Obsoletes:  %libnameqt4-devel

%description -n %{libnameqt4dev}
Development files for %{name}-qt4

%package -n %{libnameqt4}
Summary:    PDF rendering library - QT4 backend
Group:          System/Libraries

%description -n %{libnameqt4}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.
This is the QT backend version.


%package -n %{libnameglib}
Summary:	PDF rendering library - glib binding
Group:          System/Libraries
Conflicts: %libname < %version-%release

%description -n %{libnameglib}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.

%package -n %{libnameglibdev}
Summary:	Development files for %{name}'s glib binding
Group:		Development/C++
Provides:	lib%{name}-glib-devel = %{version}
Requires:	%{libnameglib} = %{version}
Requires:	%{libnamedev} = %{version}
Conflicts: %libnamedev < %version-%release
Obsoletes:	%libnameglib-devel

%description -n %{libnameglibdev}
Development files for %{name}'s glib binding.

%prep
%setup -q
%patch2 -p0 -b .objstream

perl -pi -e "s@/lib(\"|\b[^/])@/%_lib\1@g if /(kde|qt|qt4)_(libdirs|libraries)=/" configure

perl -pi -e "s@/lib(\"|\b[^/])@/%_lib\1@g if /(kde|qt|qt4)_(libdirs|libraries)=/" configure
perl -pi -e 's@qt4_incdirs="/usr/local/qt/include.*$@qt4_incdirs="/usr/lib/qt4/include"@' configure
perl -pi -e 's@qt4_libdirs="/usr/local/qt/lib.*$@qt4_libdirs="/usr/lib/qt4/%_lib"@' configure

%build
%define _disable_ld_no_undefined 1
export CPPFLAGS="-I%_includedir/freetype2"
export PATH="%qt4dir/bin:${PATH}"

%if %qt3support
export POPPER_QT_LIBS="%_libdir/libqt-mt.la"
%endif

%configure2_5x \
	--enable-cairo-output \
	--enable-poppler-qt4 \
%if %qt3support
	--enable-poppler-qt \
%else
	--disable-poppler-qt \
%endif
	--enable-xpdf-headers \
	--enable-gtk-doc
%make

%install
rm -rf %{buildroot}
%makeinstall
%{__cp} -a config.h %{buildroot}%{_includedir}/poppler/

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%post -n %{libnameglib} -p /sbin/ldconfig
%postun -n %{libnameglib} -p /sbin/ldconfig

%if %qt3support
%post -n %{libnameqt} -p /sbin/ldconfig
%postun -n %{libnameqt} -p /sbin/ldconfig
%endif

%post -n %{libnameqt4} -p /sbin/ldconfig
%postun -n %{libnameqt4} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%_bindir/*
%_mandir/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libpoppler.so.%{major}*

%files -n %{libnamedev}
%defattr(-,root,root)
%{_libdir}/libpoppler.so
%attr(644,root,root) %{_libdir}/libpoppler.*a
%dir %{_includedir}/poppler
%{_includedir}/poppler/config.h
%{_includedir}/poppler/[A-Z]*
%{_includedir}/poppler/fofi
%{_includedir}/poppler/goo
%{_includedir}/poppler/splash
%{_includedir}/poppler/poppler-config.h
%{_libdir}/pkgconfig/poppler-cairo.pc
%{_libdir}/pkgconfig/poppler-splash.pc
%{_libdir}/pkgconfig/poppler.pc
%{_datadir}/gtk-doc/html/%name

%files -n %{libnameglib}
%defattr(-,root,root)
%{_libdir}/libpoppler-glib.so.%{glibmajor}*

%files -n %{libnameglibdev}
%defattr(-,root,root)
%attr(644,root,root) %{_libdir}/libpoppler-glib.*a
%{_libdir}/libpoppler-glib.so
%{_libdir}/pkgconfig/poppler-glib.pc
%{_includedir}/poppler/glib

%if %qt3support
%files -n %{libnameqt}
%defattr(-,root,root)
%{_libdir}/libpoppler-qt.so.%{qt3major}*

%files -n %{libnameqtdev}
%defattr(-,root,root)
%{_libdir}/libpoppler-qt.so
%attr(644,root,root) %{_libdir}/libpoppler-qt.*a
%{_libdir}/pkgconfig/poppler-qt.pc
%_includedir/poppler/qt3
%endif

%files -n %{libnameqt4dev}
%defattr(-,root,root)
%_includedir/poppler/qt4
%{_libdir}/pkgconfig/poppler-qt4.pc
%{_libdir}/libpoppler-qt4.so
%attr(644,root,root) %{_libdir}/libpoppler-qt4.*a

%files -n %{libnameqt4}
%defattr(-,root,root)
%{_libdir}/libpoppler-qt4.so.%{qt4major}*
