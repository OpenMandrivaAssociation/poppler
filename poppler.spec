%define major		43
%define glibmajor	8
%define qt3major	3
%define qt4major	4
%define qt5major	1
%define cppmajor	0
%define girmajor	0.18
%define libname		%mklibname %{name} %{major}
%define libnameglib	%mklibname %{name}-glib %{glibmajor}
%define libnameqt5	%mklibname %{name}-qt5- %{qt5major}
%define libnameqt4	%mklibname %{name}-qt4- %{qt4major}
%define libnameqt	%mklibname %{name}-qt %{qt3major}
%define libnamecpp	%mklibname %{name}-cpp %{cppmajor}
%define girname		%mklibname %{name}-gir %{girmajor}
%define libnamedev	%mklibname -d %{name}
%define libnameglibdev	%mklibname -d %{name}-glib
%define libnameqtdev	%mklibname -d %{name}-qt
%define libnameqt4dev	%mklibname -d %{name}-qt4
%define libnameqt5dev	%mklibname -d %{name}-qt5
%define libnamecppdev	%mklibname -d %{name}-cpp

Summary:	PDF rendering library
Name:		poppler
Version:	0.24.1
Release:	2
License:	GPLv2+
Group:		Office
URL:		http://poppler.freedesktop.org
Source0:	http://poppler.freedesktop.org/%{name}-%{version}.tar.xz
## upstreamable patches
Patch1:		poppler-0.12-CVE-2009-3608,3609.patch
Patch2:		poppler-0.18.4-linkage.patch

BuildRequires:	gtk-doc
BuildRequires:	gettext-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(cairo) >= 1.8.4
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libopenjpeg1)
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtGui)
BuildRequires:	pkgconfig(QtXml)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)

%description
Poppler is a PDF rendering library based on the xpdf-3.0 code base.

%package -n %{libname}
Summary:	PDF rendering library
Group:		System/Libraries
Conflicts:	%{_lib}poppler12
Suggests:	poppler-data

%description -n %{libname}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.

%package -n %{girname}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries
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
Obsoletes:	%{libname}-devel < 0.20.2

%description -n %{libnamedev}
Development files for %{name}

%package -n %{libnameqt}
Summary:	PDF rendering library - QT backend
Group:		System/Libraries

%description -n %{libnameqt}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.
This is the QT backend version.

%package -n %{libnamecpp}
Summary:	PDF rendering library - C++ backend
Group:		System/Libraries

%description -n %{libnamecpp}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.
This is the C++ backend version.

%package  -n %{libnameqt4dev}
Summary:	Development files for %{name}-qt4
Group:		Development/C++
Provides:	lib%{name}-qt4-devel = %{version}
Requires:	%{libnameqt4} = %{version}
Requires:	%{libnamedev} = %{version}
Obsoletes:	%{libnameqt4}-devel < 0.20.2

%description -n %{libnameqt4dev}
Development files for %{name}-qt4

%package -n %{libnameqt4}
Summary:	PDF rendering library - Qt4 backend
Group:		System/Libraries

%description -n %{libnameqt4}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.
This is the Qt backend version.

%package  -n %{libnameqt5dev}
Summary:	Development files for %{name}-qt5
Group:		Development/C++
Provides:	lib%{name}-qt5-devel = %{version}
Requires:	%{libnameqt5} = %{version}
Requires:	%{libnamedev} = %{version}

%description -n %{libnameqt5dev}
Development files for %{name}-qt5

%package -n %{libnameqt5}
Summary:	PDF rendering library - QT4 backend
Group:		System/Libraries

%description -n %{libnameqt5}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.
This is the Qt 5.x backend version.

%package -n %{libnameglib}
Summary:	PDF rendering library - glib binding
Group:		System/Libraries
Conflicts:	%{libname} < %{version}-%{release}

%description -n %{libnameglib}
Poppler is a PDF rendering library based on the xpdf-3.0 code base.

%package -n %{libnameglibdev}
Summary:	Development files for %{name}'s glib binding
Group:		Development/C++
Provides:	lib%{name}-glib-devel = %{version}
Requires:	%{libnameglib} = %{version}
Requires:	%{libnamedev} = %{version}
Conflicts:	%{libnamedev} < %{version}-%{release}
Obsoletes:	%{libnameglib}-devel < 0.20.2

%description -n %{libnameglibdev}
Development files for %{name}'s glib binding.

%package glib-demo
Summary:	Tool demonstrating %{libnameglib}
Group:		Development/C++
Requires:	%{libnameglib} = %{version}-%{release}
BuildRequires:	pkgconfig(gtk+-3.0) pkgconfig(gdk-pixbuf-2.0)

%description glib-demo
Tool demonstrating %{libnameglib} by retrieving
information about PDF files and displaying them

%package -n %{libnamecppdev}
Summary:	Development files for %{name}-cpp
Group:		Development/C++
Provides:	lib%{name}-cpp-devel = %{version}
Requires:	%{libnamecpp} = %{version}
Requires:	%{libnamedev} = %{version}

%description -n %{libnamecppdev}
Development files for %{name}-cpp

%prep
%setup -q
%apply_patches

#needed by patch2
libtoolize --force
autoheader
aclocal
automake -a --add-missing
autoconf

%build
export CPPFLAGS="-I%{_includedir}/freetype2"
export PATH="%qt4dir/bin:%qt5dir/bin:${PATH}"

%configure2_5x \
	--enable-cairo-output \
	--enable-poppler-qt4 \
	--enable-poppler-qt5 \
	--disable-poppler-qt \
	--enable-xpdf-headers \
	--enable-gtk-doc \
	--disable-static
%make

%install
%makeinstall_std
cp -a config.h %{buildroot}%{_includedir}/poppler/

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/*
%exclude %{_bindir}/poppler-glib-demo
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libpoppler.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Poppler-0.18.typelib

%files -n %{libnamedev}
%{_libdir}/libpoppler.so
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
%{_libdir}/libpoppler-glib.so
%{_libdir}/pkgconfig/poppler-glib.pc
%{_includedir}/poppler/glib

%files -n %{libnameqt4dev}
%{_includedir}/poppler/qt4
%{_libdir}/pkgconfig/poppler-qt4.pc
%{_libdir}/libpoppler-qt4.so

%files -n %{libnameqt4}
%{_libdir}/libpoppler-qt4.so.%{qt4major}*

%files -n %{libnameqt5dev}
%{_includedir}/poppler/qt5
%{_libdir}/pkgconfig/poppler-qt5.pc
%{_libdir}/libpoppler-qt5.so

%files -n %{libnameqt5}
%{_libdir}/libpoppler-qt5.so.%{qt5major}*

%files -n %{libnamecpp}
%{_libdir}/libpoppler-cpp.so.%{cppmajor}*

%files -n %{libnamecppdev}
%{_libdir}/libpoppler-cpp.so
%{_libdir}/pkgconfig/poppler-cpp.pc
%{_includedir}/poppler/cpp

%changelog
* Mon Jul 16 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.20.2-1
+ Revision: 809807
- version update 0.20.2

* Tue May 15 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.20.0-2
+ Revision: 799018
- split out gir pkg to avoid upgrade conflicts

* Mon May 14 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.20.0-1
+ Revision: 798830
- Update to 0.20.0

* Thu May 03 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.18.4-2
+ Revision: 795215
- rebuild for typelib
- cleaned up spec

* Fri Feb 17 2012 Götz Waschk <waschk@mandriva.org> 0.18.4-1
+ Revision: 775940
- new version
- rediff patch 2

* Tue Jan 31 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.18.3-1
+ Revision: 770048
- Update to 0.18.3
- Fix build in current environment
- Split poppler-glib-demo into a separate package to avoid
  okular->poppler->gtk dependency

* Sat Nov 26 2011 Oden Eriksson <oeriksson@mandriva.com> 0.18.1-3
+ Revision: 733645
- nuke the *.la files because it was removed in fontconfig

* Fri Nov 04 2011 Rafael da Veiga Cabral <cabral@mandriva.com> 0.18.1-2
+ Revision: 717619
- omit g_thread_init from glib-demo (gathered from fedora)
- add gettext-devel buildrequire to fix autotools configure issue
- poppler-glib.pc pkgconfig file broken (gathere from fedora)

* Mon Oct 31 2011 Götz Waschk <waschk@mandriva.org> 0.18.1-1
+ Revision: 707963
- new version
- new major

* Sun Oct 30 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.18.0-1
+ Revision: 707951
- version update

* Sun Oct 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.16.7-4
+ Revision: 702439
- attempt to relink against libpng15.so.15

* Mon Sep 12 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.16.7-3
+ Revision: 699507
- Rebuild against new libpng
  Remove Qt3 support

  + Götz Waschk <waschk@mandriva.org>
    - rebuild

* Wed Jun 29 2011 Götz Waschk <waschk@mandriva.org> 0.16.7-1
+ Revision: 688306
- update to new version 0.16.7

* Sun May 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0.16.6-1
+ Revision: 681621
- 0.16.6

* Sat Apr 30 2011 Funda Wang <fwang@mandriva.org> 0.16.5-1
+ Revision: 660804
- new version 0.16.5

* Thu Mar 31 2011 Funda Wang <fwang@mandriva.org> 0.16.4-1
+ Revision: 649351
- update to new version 0.16.4

* Fri Mar 11 2011 Funda Wang <fwang@mandriva.org> 0.16.3-2
+ Revision: 643743
- add conflicts on older lib package

* Thu Mar 10 2011 Götz Waschk <waschk@mandriva.org> 0.16.3-1
+ Revision: 643654
- new version
- new major

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0.16.2-2
+ Revision: 640210
- rebuild to obsolete old packages

* Sun Jan 30 2011 Funda Wang <fwang@mandriva.org> 0.16.2-1
+ Revision: 634030
- update to new version 0.16.2

* Sat Jan 29 2011 Funda Wang <fwang@mandriva.org> 0.16.1-1
+ Revision: 633773
- update to new version 0.16.1

* Thu Dec 30 2010 Götz Waschk <waschk@mandriva.org> 0.16.0-1mdv2011.0
+ Revision: 626088
- new version
- new major numbers
- enable introspection

* Mon Nov 08 2010 Götz Waschk <waschk@mandriva.org> 0.14.5-1mdv2011.0
+ Revision: 595097
- update to new version 0.14.5

* Wed Nov 03 2010 Götz Waschk <waschk@mandriva.org> 0.14.4-2mdv2011.0
+ Revision: 592855
- fix conflict to make glib devel package installable

* Thu Oct 14 2010 Götz Waschk <waschk@mandriva.org> 0.14.4-1mdv2011.0
+ Revision: 585596
- update to new version 0.14.4

* Sat Sep 11 2010 Funda Wang <fwang@mandriva.org> 0.14.3-1mdv2011.0
+ Revision: 577579
- update to new version 0.14.3

* Sun Aug 22 2010 Funda Wang <fwang@mandriva.org> 0.14.2-1mdv2011.0
+ Revision: 571790
- New version 0.14.2

* Thu Aug 05 2010 Götz Waschk <waschk@mandriva.org> 0.14.1-1mdv2011.0
+ Revision: 566130
- new version
- drop patch 0 (not needed anymore according to Fedora)
- fix build
- new version
- new major
- add poppler-cpp
- drop patches 2,4

  + Funda Wang <fwang@mandriva.org>
    - we are using standard qt dir, so no need to tweak configure

* Sun Jun 06 2010 Colin Guthrie <cguthrie@mandriva.org> 0.12.4-2mdv2010.1
+ Revision: 547156
- Bump release to ensure version is > 2010.0 update version

* Thu Feb 18 2010 Götz Waschk <waschk@mandriva.org> 0.12.4-1mdv2010.1
+ Revision: 507684
- new version
- drop patch 3

* Wed Jan 27 2010 Frederic Crozat <fcrozat@mandriva.com> 0.12.3-6mdv2010.1
+ Revision: 497255
- Patch4 (Carlos): fix rotation (fdo #26264)

* Wed Jan 27 2010 Frederic Crozat <fcrozat@mandriva.com> 0.12.3-5mdv2010.1
+ Revision: 497092
- Patch3 (GIT): fix mask (fdo bug #16906)

* Fri Jan 22 2010 Frederic Crozat <fcrozat@mandriva.com> 0.12.3-4mdv2010.1
+ Revision: 494982
- New version for patch2

* Fri Jan 15 2010 Frederic Crozat <fcrozat@mandriva.com> 0.12.3-3mdv2010.1
+ Revision: 491777
- Patch2 (Huug):  improve cairo prescaling (fdo #5589)

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.12.3-2mdv2010.1
+ Revision: 488795
- rebuilt against libjpeg v8

* Sat Dec 26 2009 Frederik Himpe <fhimpe@mandriva.org> 0.12.3-1mdv2010.1
+ Revision: 482370
- update to new version 0.12.3

* Tue Dec 22 2009 Funda Wang <fwang@mandriva.org> 0.12.2-2mdv2010.1
+ Revision: 481221
- use openjpeg for jpeg2000

* Thu Nov 19 2009 Oden Eriksson <oeriksson@mandriva.com> 0.12.2-1mdv2010.1
+ Revision: 467454
- 0.12.2

* Thu Oct 22 2009 Frederic Crozat <fcrozat@mandriva.com> 0.12.1-2mdv2010.0
+ Revision: 458892
- Force rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - 0.12.1
    - new ObjStream patch (fedora)
    - rediffed the CVE-2009-3608 CVE-2009-3609 patch

* Sat Oct 17 2009 Paulo Andrade <pcpa@mandriva.com.br> 0.12.0-3mdv2010.0
+ Revision: 457970
- Correct CVE-2009-3608 and CVE-2009-3609

* Sun Oct 11 2009 Olivier Blin <blino@mandriva.org> 0.12.0-2mdv2010.0
+ Revision: 456647
- fix group

* Thu Sep 10 2009 Frederik Himpe <fhimpe@mandriva.org> 0.12.0-1mdv2010.0
+ Revision: 437102
- Update to new verison 0.12.0
- Remove string format patch: not needed anymore

* Wed Aug 19 2009 Frederik Himpe <fhimpe@mandriva.org> 0.11.3-1mdv2010.0
+ Revision: 417957
- update to new version 0.11.3

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 0.11.2-2mdv2010.0
+ Revision: 416530
- rebuilt against libjpeg v7

* Tue Aug 04 2009 Frederik Himpe <fhimpe@mandriva.org> 0.11.2-1mdv2010.0
+ Revision: 409399
- Update to new version 0.11.2

* Fri Jul 10 2009 Götz Waschk <waschk@mandriva.org> 0.11.1-1mdv2010.0
+ Revision: 394162
- new version
- update file list
- rediff patch 1

* Tue May 19 2009 Götz Waschk <waschk@mandriva.org> 0.11.0-1mdv2010.0
+ Revision: 377467
- new version, needed by evince 2.27
- bump deps
- new major
- update file list

* Sun May 17 2009 Funda Wang <fwang@mandriva.org> 0.10.7-1mdv2010.0
+ Revision: 376734
- New version 0.10.7

* Fri Apr 17 2009 Frederic Crozat <fcrozat@mandriva.com> 0.10.6-1mdv2009.1
+ Revision: 367901
- Remove patch0 (useless)
- Merge patch 1 and 3 and remove most unneeeded changes and error in it

  + Rafael da Veiga Cabral <cabral@mandriva.com>
    - This version update provides security fixes for CVE-2009-0799,
      CVE-2009-0800, CVE-2009-1179, CVE-2009-1180, CVE-2009-1181,
      CVE-2009-1182, CVE-2009-1183, CVE-2009-1187 and CVE-2009-1188
      and other bug fixes
    - poppler-0.8.7-qt3-configure.patch rediff

* Sun Mar 15 2009 Götz Waschk <waschk@mandriva.org> 0.10.5-1mdv2009.1
+ Revision: 355261
- update to new version 0.10.5

* Wed Feb 11 2009 Götz Waschk <waschk@mandriva.org> 0.10.4-1mdv2009.1
+ Revision: 339448
- update to new version 0.10.4

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 0.10.3-2mdv2009.1
+ Revision: 333149
- Fix qt3 build and add patch for str format
- Add patch for ObjStream

* Sun Jan 11 2009 Funda Wang <fwang@mandriva.org> 0.10.3-1mdv2009.1
+ Revision: 328164
- New version 0.10.3

* Fri Dec 26 2008 Funda Wang <fwang@mandriva.org> 0.10.2-1mdv2009.1
+ Revision: 319271
- New version 0.10.2
- fix str fmt

* Tue Nov 11 2008 Götz Waschk <waschk@mandriva.org> 0.10.1-1mdv2009.1
+ Revision: 302103
- update to new version 0.10.1

* Fri Nov 07 2008 Götz Waschk <waschk@mandriva.org> 0.10.0-2mdv2009.1
+ Revision: 300761
- rebuild for new libxcb

* Sat Oct 11 2008 Götz Waschk <waschk@mandriva.org> 0.10.0-1mdv2009.1
+ Revision: 292463
- new version
- new majors

* Tue Sep 23 2008 Helio Chissini de Castro <helio@mandriva.com> 0.8.7-2mdv2009.0
+ Revision: 287631
- Renable qt3 support in poppler by fixing compilation against as-needed

* Tue Sep 02 2008 Helio Chissini de Castro <helio@mandriva.com> 0.8.7-1mdv2009.0
+ Revision: 279064
- New upstream regression fix version

* Thu Aug 21 2008 Helio Chissini de Castro <helio@mandriva.com> 0.8.6-2mdv2009.0
+ Revision: 274459
- Finally build against jpeg

* Wed Aug 20 2008 Helio Chissini de Castro <helio@mandriva.com> 0.8.6-1mdv2009.0
+ Revision: 274208
- New upstream version. Fix bug for evince and okular https://qa.mandriva.com/show_bug.cgi?id=42204 ( [Bug 42204] poppler, ASSIGNED: Some PDFs show corrupted colors )

* Tue Jul 29 2008 Helio Chissini de Castro <helio@mandriva.com> 0.8.5-1mdv2009.0
+ Revision: 252726
- New upstream version bugfix release.

* Fri Jul 18 2008 Götz Waschk <waschk@mandriva.org> 0.8.4-1mdv2009.0
+ Revision: 238067
- new version
- drop patch 1

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jun 03 2008 Helio Chissini de Castro <helio@mandriva.com> 0.8.3-1mdv2009.0
+ Revision: 214845
- New upstream 0.8.3
- Disable ( finally ) qt3 support. Now qt4 is default

* Wed Apr 30 2008 Götz Waschk <waschk@mandriva.org> 0.8.2-1mdv2009.0
+ Revision: 199614
- new version

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream minor release
    - Update for latest stable revision. Required by kdegraphica 4.0.68

* Wed Mar 19 2008 Frederic Crozat <fcrozat@mandriva.com> 0.6.4-2mdv2008.1
+ Revision: 188831
- poppler package now obsoletes / provides xpdf-tools

* Sat Jan 26 2008 Helio Chissini de Castro <helio@mandriva.com> 0.6.4-1mdv2008.1
+ Revision: 158290
- Update for new upstream minor version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 13 2007 Helio Chissini de Castro <helio@mandriva.com> 0.6.3-1mdv2008.1
+ Revision: 119382
- New upstream version 0.6.3

  + Thierry Vignaud <tv@mandriva.org>
    - do not package big ChangeLog

* Tue Nov 20 2007 Pascal Terjan <pterjan@mandriva.org> 0.6.2-2mdv2008.1
+ Revision: 110785
- Fix update from 2006.0 (#35652)

* Sat Nov 10 2007 Funda Wang <fwang@mandriva.org> 0.6.2-1mdv2008.1
+ Revision: 107459
- comment out patch that seems merged upstream
- New version 0.6.2

* Sat Oct 13 2007 Funda Wang <fwang@mandriva.org> 0.6.1-1mdv2008.0
+ Revision: 97843
- New version 0.6.1

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.6-3mdv2008.0
+ Revision: 90166
- rebuild

* Sun Sep 09 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6-2mdv2008.0
+ Revision: 83504
- fix provides on poppler-glib-devel

* Tue Sep 04 2007 Götz Waschk <waschk@mandriva.org> 0.6-1mdv2008.0
+ Revision: 79036
- new version

  + Pascal Terjan <pterjan@mandriva.org>
    - Update major
    - 0.6

* Mon Aug 20 2007 Funda Wang <fwang@mandriva.org> 0.5.91-2mdv2008.0
+ Revision: 67320
- suggests poppler-data (bug#26509)

* Wed Aug 15 2007 Funda Wang <fwang@mandriva.org> 0.5.91-1mdv2008.0
+ Revision: 63607
- New devel package policy
- New version 0.5.91

* Tue Aug 14 2007 Pascal Terjan <pterjan@mandriva.org> 0.5.9-4mdv2008.0
+ Revision: 63404
- Add P2 for CVE 2007-3387 (#32248)

* Sat Aug 04 2007 David Walluck <walluck@mandriva.org> 0.5.9-3mdv2008.0
+ Revision: 58856
- include config.h since it is included by many headers

* Sat Jun 23 2007 Götz Waschk <waschk@mandriva.org> 0.5.9-2mdv2008.0
+ Revision: 43474
- split out glib binding

* Tue Jun 19 2007 Götz Waschk <waschk@mandriva.org> 0.5.9-1mdv2008.0
+ Revision: 41327
- new version
- drop patches 2,3
- update file list

* Tue Apr 24 2007 Pascal Terjan <pterjan@mandriva.org> 0.5.4-4mdv2008.0
+ Revision: 17819
- Obsoletes/Provides pdftohtml

