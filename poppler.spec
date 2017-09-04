%bcond_without	qt4
%bcond_without	qt5
%bcond_without	cairo
%bcond_without	gtk
%bcond_with	doc

%define major 70
%define glibmaj 8
%define qt3maj 3
%define qt4maj 4
%define qt5maj 1
%define cppmaj 0
%define girmaj 0.18
%define libname	%mklibname %{name} %{major}
%define libglib	%mklibname %{name}-glib %{glibmaj}
%define libqt5	%mklibname %{name}-qt5_ %{qt5maj}
%define libqt4	%mklibname %{name}-qt4_ %{qt4maj}
%define libqt	%mklibname %{name}-qt %{qt3maj}
%define libcpp	%mklibname %{name}-cpp %{cppmaj}
%define girname	%mklibname %{name}-gir %{girmaj}
%define devname	%mklibname -d %{name}
%define glibdev	%mklibname -d %{name}-glib
%define qtdev	%mklibname -d %{name}-qt
%define qt4dev	%mklibname -d %{name}-qt4
%define qt5dev	%mklibname -d %{name}-qt5
%define cppdev	%mklibname -d %{name}-cpp

Summary:	PDF rendering library
Name:		poppler
Version:	0.59.0
Release:	1
License:	GPLv2+
Group:		Office
Url:		http://poppler.freedesktop.org
Source0:	http://poppler.freedesktop.org/%{name}-%{version}.tar.xz
## upstreamable patches
Patch1:		poppler-0.12-CVE-2009-3608,3609.patch
%if %{with doc}
BuildRequires:	gtk-doc
%endif
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	jpeg-devel
%if %{with cairo}
BuildRequires:	pkgconfig(cairo) >= 1.8.4
%endif
%if %{with gtk}
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
%endif
BuildRequires:	pkgconfig(libopenjp2) >= 2.1.2
%if %{with qt4}
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtGui)
BuildRequires:	pkgconfig(QtXml)
%endif
BuildRequires:	pkgconfig(lcms2)
%if %{with qt5}
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	qtchooser
%endif

%description
Poppler is a PDF rendering library based on the xpdf-3.0 code base.

%package -n %{libname}
Summary:	PDF rendering library
Group:		System/Libraries
Suggests:	poppler-data >= 0.4.7

%description -n %{libname}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.

%if %{with gtk}
%package -n %{girname}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}poppler25 < 0.20.0-1
Conflicts:	%{_lib}poppler19 < 0.18.4-3

%description -n %{girname}
GObject Introspection interface library for %{name}.
%endif

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{libname}-devel < 0.20.2

%description -n %{devname}
Development files for %{name}

%package -n %{libcpp}
Summary:	PDF rendering library - C++ backend
Group:		System/Libraries

%description -n %{libcpp}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.
This is the C++ backend version.


%if %{with qt4}
%package -n %{libqt}
Summary:	PDF rendering library - QT backend
Group:		System/Libraries

%description -n %{libqt}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.
This is the QT backend version.

%package  -n %{qt4dev}
Summary:	Development files for %{name}-qt4
Group:		Development/C++
Provides:	%{name}-qt4-devel = %{version}-%{release}
Requires:	%{libqt4} = %{version}-%{release}
Requires:	%{devname} = %{version}-%{release}
Obsoletes:	%{libqt4}-devel < 0.20.2

%description -n %{qt4dev}
Development files for %{name}-qt4

%package -n %{libqt4}
Summary:	PDF rendering library - Qt4 backend
Group:		System/Libraries
Obsoletes:	%{_lib}poppler-qt4-4 < 0.24.3

%description -n %{libqt4}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.
This is the Qt backend version.
%endif

%if %{with qt5}
%package  -n %{qt5dev}
Summary:	Development files for %{name}-qt5
Group:		Development/C++
Provides:	%{name}-qt5-devel = %{version}
Requires:	%{libqt5} = %{version}-%{release}
Requires:	%{devname} = %{version}-%{release}
Obsoletes:	%{_lib}poppler-qt5-1 < 0.24.3

%description -n %{qt5dev}
Development files for %{name}-qt5

%package -n %{libqt5}
Summary:	PDF rendering library - QT4 backend
Group:		System/Libraries

%description -n %{libqt5}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.
This is the Qt 5.x backend version.
%endif

%if %{with gtk}
%package -n %{libglib}
Summary:	PDF rendering library - glib binding
Group:		System/Libraries
Conflicts:	%{libname} < %{version}-%{release}

%description -n %{libglib}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.

%package -n %{glibdev}
Summary:	Development files for %{name}'s glib binding
Group:		Development/C++
Provides:	%{name}-glib-devel = %{version}-%{release}
Requires:	%{libglib} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Requires:	%{devname} = %{version}-%{release}
Conflicts:	%{devname} < 0.24.2
Obsoletes:	%{libglib}-devel < 0.20.2

%description -n %{glibdev}
Development files for %{name}'s glib binding.

%package glib-demo
Summary:	Tool demonstrating %{libglib}
Group:		Development/C++
Requires:	%{libglib} = %{version}-%{release}

%description glib-demo
Tool demonstrating %{libglib} by retrieving
information about PDF files and displaying them
%endif

%package -n %{cppdev}
Summary:	Development files for %{name}-cpp
Group:		Development/C++
Provides:	%{name}-cpp-devel = %{version}-%{release}
Requires:	%{libcpp} = %{version}-%{release}
Requires:	%{devname} = %{version}-%{release}

%description -n %{cppdev}
Development files for %{name}-cpp

%prep
%setup -q
%apply_patches
# Qt 5.2 changes "moc -v" output from "Qt 5.x" to "moc 5.x"
sed -i -e 's,Qt 5,5,g' configure.ac
autoreconf -fi

%build
export CPPFLAGS="-I%{_includedir}/freetype2"
export PATH="%qt4dir/bin:%_libdir/qt5/bin:${PATH}"

%configure \
	--disable-static \
	--enable-compile-warnings=no \
%if %{with cairo}
	--enable-cairo-output \
%endif
%if %{with qt4}
	--enable-poppler-qt4 \
%endif
%if %{with qt4}
	--enable-poppler-qt5 \
%endif
	--disable-poppler-qt \
	--enable-xpdf-headers \
%if %{with doc}
	--enable-gtk-doc
%endif

%make MOCQT5=moc-qt5 CXXFLAGS+="-std=gnu++14"

%install
%makeinstall_std
cp -a config.h %{buildroot}%{_includedir}/poppler/

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%if %{with gtk}
%exclude %{_bindir}/poppler-glib-demo
%endif
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libpoppler.so.%{major}*

%if %{with gtk}
%files -n %{girname}
%{_libdir}/girepository-1.0/Poppler-%{girmaj}.typelib
%endif

%files -n %{devname}
%{_libdir}/libpoppler.so
%dir %{_includedir}/poppler
%{_includedir}/poppler/config.h
%{_includedir}/poppler/[A-Z]*
%{_includedir}/poppler/fofi
%{_includedir}/poppler/goo
%{_includedir}/poppler/splash
%{_includedir}/poppler/poppler-config.h
%if %{with cairo}
%{_libdir}/pkgconfig/poppler-cairo.pc
%endif
%{_libdir}/pkgconfig/poppler-splash.pc
%{_libdir}/pkgconfig/poppler.pc

%if %{with gtk}
%files -n %{libglib}
%{_libdir}/libpoppler-glib.so.%{glibmaj}*

%files glib-demo
%{_bindir}/poppler-glib-demo

%files -n %{glibdev}
%{_libdir}/libpoppler-glib.so
%{_libdir}/pkgconfig/poppler-glib.pc
%{_includedir}/poppler/glib
%{_datadir}/gir-1.0/Poppler-%{girmaj}.gir
%{_datadir}/gtk-doc/html/*
%endif

%if %{with qt4}
%files -n %{qt4dev}
%{_includedir}/poppler/qt4
%{_libdir}/pkgconfig/poppler-qt4.pc
%{_libdir}/libpoppler-qt4.so

%files -n %{libqt4}
%{_libdir}/libpoppler-qt4.so.%{qt4maj}*
%endif

%if %{with qt5}
%files -n %{qt5dev}
%{_includedir}/poppler/qt5
%{_libdir}/pkgconfig/poppler-qt5.pc
%{_libdir}/libpoppler-qt5.so

%files -n %{libqt5}
%{_libdir}/libpoppler-qt5.so.%{qt5maj}*
%endif

%files -n %{libcpp}
%{_libdir}/libpoppler-cpp.so.%{cppmaj}*

%files -n %{cppdev}
%{_libdir}/libpoppler-cpp.so
%{_libdir}/pkgconfig/poppler-cpp.pc
%{_includedir}/poppler/cpp
