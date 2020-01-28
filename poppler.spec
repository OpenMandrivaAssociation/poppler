%global optflags %{optflags} -Ofast

%bcond_without	qt5
%bcond_without	cairo
%bcond_without	gtk
%bcond_without	doc

%define major 94
%define glibmaj 8
%define qt3maj 3
%define qt5maj 1
%define cppmaj 0
%define girmaj 0.18
%define libname	%mklibname %{name} %{major}
%define libglib	%mklibname %{name}-glib %{glibmaj}
%define libqt5	%mklibname %{name}-qt5_ %{qt5maj}
%define libqt	%mklibname %{name}-qt %{qt3maj}
%define libcpp	%mklibname %{name}-cpp %{cppmaj}
%define girname	%mklibname %{name}-gir %{girmaj}
%define devname	%mklibname -d %{name}
%define glibdev	%mklibname -d %{name}-glib
%define qtdev	%mklibname -d %{name}-qt
%define qt5dev	%mklibname -d %{name}-qt5
%define cppdev	%mklibname -d %{name}-cpp

Summary:	PDF rendering library
Name:		poppler
# (tpg) BIG FAT WARNING !!!
# when you are about to update it, 
# make sure other packages that depends on poppler will build with new version
# especially texlive. Thanks.
Version:	0.84.0
Release:	2
License:	GPLv2+
Group:		Office
Url:		http://poppler.freedesktop.org
Source0:	http://poppler.freedesktop.org/%{name}-%{version}.tar.xz
# Fix #include <poppler-config.h> from C code (e.g. texlive)
Patch0:		poppler-0.84.0-non-c++.patch
%if %{with doc}
BuildRequires:	gtk-doc
BuildRequires:	python
%endif
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	jpeg-devel
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(nss)
BuildRequires:	pkgconfig(libtiff-4)
%if %{with cairo}
BuildRequires:	pkgconfig(cairo) >= 1.8.4
%endif
%if %{with gtk}
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 1.54.1
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
%endif
BuildRequires:	pkgconfig(libopenjp2) >= 2.1.2
BuildRequires:	pkgconfig(lcms2)
%if %{with qt5}
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	qtchooser
BuildRequires:	qmake5
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
%autosetup -p1
find . -type f |xargs chmod 0644
chmod 0755 make-glib-api-docs

%build
export CPPFLAGS="-I%{_includedir}/freetype2"
export PATH="%_libdir/qt5/bin:${PATH}"

%if %{with doc}
sed -i -e 's,env python3,env python,g' make-glib-api-docs
%endif

sed -i -e '/CXX_STANDARD/iadd_definitions(-fno-lto)' CMakeLists.txt

%cmake \
	-DENABLE_XPDF_HEADERS:BOOL=ON \
	-DENABLE_UNSTABLE_API_ABI_HEADERS:BOOL=ON \
	-DQT_QMAKE_EXECUTABLE=%{_libdir}/qt5/bin/qmake \
%if %{with cairo}
	-DWITH_Cairo:BOOL=ON \
%endif
%if %{with doc}
	-DENABLE_GTK_DOC:BOOL=ON \
%endif
%if !%{with gtk}
	-DENABLE_GLIB:BOOL=OFF \
%endif
	-DSPLASH_CMYK:BOOL=ON \
	-DENABLE_CMS=lcms2 \
	-DENABLE_DCTDECODER=libjpeg \
	-DENABLE_LIBOPENJPEG=openjpeg2 \
	-G Ninja

export LD_LIBRARY_PATH=$(pwd)
%ninja

%install
find build/glib/reference -type f |xargs chmod 0644

%ninja_install -C build
cp -a build/config.h %{buildroot}%{_includedir}/poppler/
%if %{with gtk}
cp build/glib/demo/poppler-glib-demo %{buildroot}%{_bindir}/
%endif

%files
%doc AUTHORS COPYING NEWS
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
%if %{with doc}
%{_datadir}/gtk-doc/html/*
%endif
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
