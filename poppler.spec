%define	name		poppler
%define version 0.5.4
%define release %mkrel 4
%define major 1
%define qtmajor 1
%define libname		%mklibname %name %major
%define libnameqt	%mklibname %name-qt %qtmajor
%define libnameqt4	%mklibname %name-qt4- %qtmajor

%define qt4support 1

Summary:	PDF rendering library
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Libraries
URL:		http://poppler.freedesktop.org
Source:		%{name}-%{version}.tar.bz2
Patch0:		poppler-0.5.3-refcount.patch
Patch1:		poppler-0.5.3-init.patch
Patch2:		poppler-0.5.3-CVE-2007-0104.patch
Patch3:		poppler-qt4-pedantic.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:  qt3-devel
%if %qt4support
BuildRequires:	qt4-devel
%endif
BuildRequires:  gtk2-devel
BuildRequires:  cairo-devel >= 0.5.0
BuildRequires:  automake1.9
Conflicts: 	xpdf-tools
Obsoletes:	pdftohtml
Provides:	pdftohtml

%description
Poppler is a PDF rendering library based on the xpdf-3.0 code base.

%package -n %{libname}
Summary:	PDF rendering library
Group:          System/Libraries

%description -n %{libname}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.

%package -n %{libname}-devel
Summary:	Development files for %{name}
Group:		Development/C++
Provides:	lib%{name}-devel = %{version}
Requires:	%{libname} = %{version}

%description -n %{libname}-devel
Development files for %{name}

%package -n %{libnameqt}
Summary:	PDF rendering library - QT backend
Group:          System/Libraries

%description -n %{libnameqt}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.
This is the QT backend version.

%package -n %{libnameqt}-devel
Summary:	Development files for %{name}-qt
Group:		Development/C++
Provides:	lib%{name}-qt-devel = %{version}
Requires:	%{libnameqt} = %{version}
Requires:	%libname-devel = %version

%description -n %{libnameqt}-devel
Development files for %{name}-qt


%if %qt4support
%package  -n %{libnameqt4}-devel
Summary:    Development files for %{name}-qt4
Group:      Development/C++
Provides:   lib%{name}-qt4-devel = %{version}
Requires:   %{libnameqt4} = %{version}
Requires:   %libname-devel = %version

%description -n %{libnameqt4}-devel
Development files for %{name}-qt4

%package -n %{libnameqt4}
Summary:    PDF rendering library - QT4 backend
Group:          System/Libraries

%description -n %{libnameqt4}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.
This is the QT backend version.

%endif

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p1 -b .cve-2007-0104
%patch3 -p1 -b .qt4_pedantic

perl -pi -e "s@/lib(\"|\b[^/])@/%_lib\1@g if /(kde|qt|qt4)_(libdirs|libraries)=/" configure

perl -pi -e "s@/lib(\"|\b[^/])@/%_lib\1@g if /(kde|qt|qt4)_(libdirs|libraries)=/" configure
perl -pi -e 's@qt4_incdirs="/usr/local/qt/include.*$@qt4_incdirs="/usr/lib/qt4/include"@' configure
perl -pi -e 's@qt4_libdirs="/usr/local/qt/lib.*$@qt4_libdirs="/usr/lib/qt4/%_lib"@' configure

%build

export CPPFLAGS="-I%_includedir/freetype2"
%configure2_5x \
	--enable-a4-paper \
	--enable-poppler-qt \
	--enable-cairo-output \
%if %qt4support	
	--enable-poppler-qt4 \
%else
	--disable-poppler-qt4 \
%endif	
	--enable-xpdf-headers
%make

%install
rm -rf %{buildroot}
%makeinstall

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%post -n %{libnameqt} -p /sbin/ldconfig
%postun -n %{libnameqt} -p /sbin/ldconfig

%if %qt4support
%post -n %{libnameqt4} -p /sbin/ldconfig
%postun -n %{libnameqt4} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%_bindir/*
%_mandir/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libpoppler-glib.so.%{major}*
%{_libdir}/libpoppler.so.%{major}*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/libpoppler-glib.so
%{_libdir}/libpoppler.so
%attr(644,root,root) %{_libdir}/libpoppler-glib.*a
%attr(644,root,root) %{_libdir}/libpoppler.*a
%dir %{_includedir}/poppler
%{_includedir}/poppler/glib
%{_includedir}/poppler/poppler-page-transition.h
%{_includedir}/poppler/[A-Z]*
%{_includedir}/poppler/goo
%{_includedir}/poppler/splash
%{_includedir}/poppler/poppler-config.h
%{_libdir}/pkgconfig/poppler-cairo.pc
%{_libdir}/pkgconfig/poppler-glib.pc
%{_libdir}/pkgconfig/poppler-splash.pc
%{_libdir}/pkgconfig/poppler.pc
%_datadir/gtk-doc/html/%name

%files -n %{libnameqt}
%defattr(-,root,root)
%{_libdir}/libpoppler-qt.so.%{qtmajor}*

%files -n %{libnameqt}-devel
%defattr(-,root,root)
%{_libdir}/libpoppler-qt.so
%attr(644,root,root) %{_libdir}/libpoppler-qt.*a
%{_libdir}/pkgconfig/poppler-qt.pc
%_includedir/poppler/poppler-qt.h
%_includedir/poppler/poppler-link-qt3.h

%if %qt4support
%files -n %{libnameqt4}-devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/poppler-qt4.pc
%_includedir/poppler/poppler-qt4.h
%{_includedir}/poppler/poppler-annotation.h
%{_includedir}/poppler/poppler-link.h
%{_libdir}/libpoppler-qt4.so
%attr(644,root,root) %{_libdir}/libpoppler-qt4.*a

%files -n %{libnameqt4}
%defattr(-,root,root)
%{_libdir}/libpoppler-qt4.so.%{qtmajor}*
%endif

