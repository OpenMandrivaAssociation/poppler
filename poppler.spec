%define major		25
%define glibmajor	8
%define qt3major	3
%define qt4major	4
%define cppmajor	0
%define girmajor	0.18
%define libname		%mklibname %{name} %major
%define libnameglib	%mklibname %{name}-glib %glibmajor
%define libnameqt4	%mklibname %{name}-qt4- %qt4major
%define libnameqt	%mklibname %{name}-qt %qt3major
%define libnamecpp	%mklibname %{name}-cpp %cppmajor
%define girname		%mklibname %{name}-gir %{girmajor}
%define libnamedev	%mklibname -d %{name}
%define libnameglibdev	%mklibname -d %{name}-glib
%define libnameqtdev	%mklibname -d %{name}-qt
%define libnameqt4dev	%mklibname -d %{name}-qt4
%define libnamecppdev   %mklibname -d %{name}-cpp

Summary: PDF rendering library
Name: poppler
Version: 0.20.0
Release: 2
License: GPLv2+
Group: Office
URL: http://poppler.freedesktop.org
Source0:	http://poppler.freedesktop.org/%{name}-%{version}.tar.gz
## upstreamable patches
Patch1: poppler-0.12-CVE-2009-3608,3609.patch
Patch2: poppler-0.18.4-linkage.patch

BuildRequires:	gtk-doc
BuildRequires:	gettext-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(cairo) >= 1.8.4
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libopenjpeg1)
BuildRequires:	pkgconfig(QtCore)

%description
Poppler is a PDF rendering library based on the xpdf-3.0 code base.

%package -n %{libname}
Summary:	PDF rendering library
Group:          System/Libraries
Conflicts:	%{_lib}poppler12
Suggests:	poppler-data

%description -n %{libname}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.

%package -n %{girname}
Summary: GObject Introspection interface library for %{name}
Group: System/Libraries
Conflicts:	%{_lib}poppler25 < 0.20.0-1
Conflicts:	%{_lib}poppler19 < 0.18.4-3

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{libnamedev}
Summary:	Development files for %{name}
Group:		Development/C++
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Obsoletes:	%{libname}-devel

%description -n %{libnamedev}
Development files for %{name}

%package -n %{libnameqt}
Summary:	PDF rendering library - QT backend
Group:          System/Libraries

%description -n %{libnameqt}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.
This is the QT backend version.

%package -n %{libnamecpp}
Summary:	PDF rendering library - C++ backend
Group:          System/Libraries

%description -n %{libnamecpp}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.
This is the C++ backend version.

%package  -n %{libnameqt4dev}
Summary:    Development files for %{name}-qt4
Group:      Development/C++
Provides:   lib%{name}-qt4-devel = %{version}
Requires:   %{libnameqt4} = %{version}
Requires:   %libnamedev = %{version}
Obsoletes:  %libnameqt4-devel

%description -n %{libnameqt4dev}
Development files for %{name}-qt4

%package -n %{libnameqt4}
Summary:	PDF rendering library - QT4 backend
Group:		System/Libraries

%description -n %{libnameqt4}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.
This is the QT backend version.

%package -n %{libnameglib}
Summary:	PDF rendering library - glib binding
Group:		System/Libraries
Conflicts:	%libname < %{version}-%{release}

%description -n %{libnameglib}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.

%package -n %{libnameglibdev}
Summary:	Development files for %{name}'s glib binding
Group:		Development/C++
Provides:	lib%{name}-glib-devel = %{version}
Requires:	%{libnameglib} = %{version}
Requires:	%{libnamedev} = %{version}
Conflicts:	%libnamedev < %{version}-%{release}
Obsoletes:	%libnameglib-devel

%description -n %{libnameglibdev}
Development files for %{name}'s glib binding.

%package glib-demo
Summary:	Tool demonstrating %libnameglib
Group:		Development/C++
Requires:	%libnameglib = %{version}-%{release}

%description glib-demo
Tool demonstrating %libnameglib by retrieving
information about PDF files and displaying them

%package -n %{libnamecppdev}
Summary:	Development files for %{name}-cpp
Group:		Development/C++
Provides:	lib%{name}-cpp-devel = %{version}
Requires:	%{libnamecpp} = %{version}
Requires:	%libnamedev = %{version}

%description -n %{libnamecppdev}
Development files for %{name}-cpp

%prep
%setup -q
%patch1 -p1 -b .cve-2009-3608,3609.patch
%patch2 -p1 -b .linkage

#needed by patch2
autoreconf

%build
export CPPFLAGS="-I%{_includedir}/freetype2"
export PATH="%qt4dir/bin:${PATH}"

%configure2_5x \
	--enable-cairo-output \
	--enable-poppler-qt4 \
	--disable-poppler-qt \
	--enable-xpdf-headers \
	--enable-gtk-doc
%make

%install
%makeinstall_std
cp -a config.h %{buildroot}%{_includedir}/poppler/

rm -f %{buildroot}%{_libdir}/*.la

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%exclude %{_bindir}/poppler-glib-demo
%_mandir/man1/*

%files -n %{libname}
%{_libdir}/libpoppler.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Poppler-0.18.typelib

%files -n %{libnamedev}
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
%{_datadir}/gtk-doc/html/%{name}
%{_datadir}/gir-1.0/Poppler-0.18.gir

%files -n %{libnameglib}
%{_libdir}/libpoppler-glib.so.%{glibmajor}*

%files glib-demo
%{_bindir}/poppler-glib-demo

%files -n %{libnameglibdev}
%attr(644,root,root) %{_libdir}/libpoppler-glib.*a
%{_libdir}/libpoppler-glib.so
%{_libdir}/pkgconfig/poppler-glib.pc
%{_includedir}/poppler/glib

%files -n %{libnameqt4dev}
%{_includedir}/poppler/qt4
%{_libdir}/pkgconfig/poppler-qt4.pc
%{_libdir}/libpoppler-qt4.so
%attr(644,root,root) %{_libdir}/libpoppler-qt4.*a

%files -n %{libnameqt4}
%{_libdir}/libpoppler-qt4.so.%{qt4major}*

%files -n %{libnamecpp}
%{_libdir}/libpoppler-cpp.so.%{cppmajor}*

%files -n %{libnamecppdev}
%{_libdir}/libpoppler-cpp.so
%attr(644,root,root) %{_libdir}/libpoppler-cpp.*a
%{_libdir}/pkgconfig/poppler-cpp.pc
%{_includedir}/poppler/cpp

