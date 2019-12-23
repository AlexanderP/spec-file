Name:          leptonica
Version:       1.78.0
Release:       2.2%{?dist}
Summary:       C library for efficient image processing and image analysis operations

License:       BSD-2-Clause
Group:         System/Libraries
URL:           https://github.com/danbloomberg/leptonica
Source0:       https://github.com/DanBloomberg/leptonica/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf

%define major   5

BuildRequires: gcc
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: giflib-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libwebp-devel
BuildRequires: zlib-devel
BuildRequires: gdb
# Needed for baseline_reg test
BuildRequires: gnuplot


%description
The library supports many operations that are useful on
 * Document images
 * Natural images

Fundamental image processing and image analysis operations
 * Rasterop (aka bitblt)
 * Affine transforms (scaling, translation, rotation, shear)
   on images of arbitrary pixel depth
 * Projective and bi-linear transforms
 * Binary and gray scale morphology, rank order filters, and
   convolution
 * Seed-fill and connected components
 * Image transformations with changes in pixel depth, both at
   the same scale and with scale change
 * Pixelwise masking, blending, enhancement, arithmetic ops,
   etc.


%if 0%{?suse_version} > 1130
%package -n liblept%{major}
Summary:        Library for image processing and image analysis applications
Group:          System/Libraries

%description -n liblept%{major}
Library for efficient image processing and image analysis operations.
%endif


%package devel
Summary:       Development files for %{name}
%if 0%{?suse_version} > 1130
Requires:       liblept%{major} = %{version}
Provides:       liblept-devel = %{version}
Obsoletes:      liblept-devel < 1.70
%else
Requires:      %{name}%{?_isa} = %{version}-%{release}
%endif
Group:          Development/Libraries/C and C++

%description devel
The %{name}-devel package contains header files for
developing applications that use %{name}.

%package tools
Summary:       Leptonica utility tools
%if 0%{?suse_version} > 1130
Requires:       liblept%{major} = %{version}
%else
Requires:      %{name}%{?_isa} = %{version}-%{release}
%endif


%description tools
The %{name}-tools package contains leptonica utility tools.


%prep
%autosetup -p1


%build
autoreconf -ifv
%configure --disable-static --program-prefix=leptonica-
make %{?_smp_mflags}


%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_bindir}/{*gen,*reg,*test*}
install -Dpm 0644 lept.pc %{buildroot}/%{_libdir}/pkgconfig


%check
make check VERBOSE=1


%if 0%{?suse_version} > 1130
%post -n liblept%{major} -p /sbin/ldconfig
%postun -n liblept%{major} -p /sbin/ldconfig
%files -n liblept%{major}
%defattr(-,root,root)
%{_libdir}/liblept.so.*
%else
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%files
%defattr(-,root,root)
%license leptonica-license.txt
%doc README.html version-notes.html
%{_libdir}/liblept.so.5*
%endif


%files devel
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/liblept.so
%{_libdir}/pkgconfig/lept.pc

%files tools
%defattr(-,root,root)
%{_bindir}/*


%changelog

* Tue Apr 09 2019 Alexander Pozdnyakov <almipo@mail.ru> - 1.78.0-1
- Update to 1.78.0

* Sun May 20 2018 Sandro Mani <manisandro@gmail.com> - 1.76.0-1
- Update to 1.76.0

* Tue Mar 06 2018 Alexander Pozdnyakov <almipo@mail.ru>  - 1.75.3-2.2
- fix build

* Tue Feb 27 2018 Sandro Mani <manisandro@gmail.com> - 1.75.3-2
- Make test-failures on big-endian fatal again

* Thu Feb 22 2018 Sandro Mani <manisandro@gmail.com> - 1.75.3-1
- Update to 1.75.3

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 1.75.2-1
- Update to 1.75.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.74.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.74.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.74.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 11 2017 Sandro Mani <manisandro@gmail.com> - 1.74.4-1
- Update to 1.74.4

* Sun Jun 11 2017 Sandro Mani <manisandro@gmail.com> - 1.74.3-1
- Update to 1.74.3

* Sat Jun 03 2017 Sandro Mani <manisandro@gmail.com> - 1.74.2-2
- Backport 069bbc0897e8b939e93db8730b3f10b18e9d0885

* Sat Jun 03 2017 Sandro Mani <manisandro@gmail.com> - 1.74.2-1
- Update to 1.74.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.74.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 1.74.1-2
- Rebuild (libwebp)

* Tue Jan 03 2017 Sandro Mani <manisandro@gmail.com> - 1.74.1-1
- Update to 1.74.1

* Sun Dec 25 2016 Sandro Mani <manisandro@gmail.com> - 1.74.0-1
- Update to 1.74.0
- Add tools subpackage
- Enable tests

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Sandro Mani <manisandro@gmail.com> - 1.73-1
- Update to 1.73

* Mon Dec 28 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.72-3
- Rebuilt for libwebp soname bump

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 27 2015 Sandro Mani <manisandro@gmail.com> - 1.72-1
- Update to 1.72

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 05 2014 Sandro Mani <manisandro@gmail.com> - 1.71-1
- Update to 1.71

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.69-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 03 2014 Kalev Lember <kalevlember@gmail.com> - 1.69-11
- Rebuilt for libwebp soname bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.69-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Ding-Yi Chen <dchen at redhat.com> - 1.69-9
- Fixed Bug 904805 - [PATCH] Provide pkg-config file


* Fri Mar 08 2013 Ding-Yi Chen <dchen at redhat.com> - 1.69-8
- Rebuild to resolves #914124

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.69-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 24 2013 Ding-Yi Chen <dchen at redhat.com> - 1.69-6
- Rebuild for dependency libwebp-0.2.1-1

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.69-5
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 28 2012 Richard W.M. Jones <rjones@redhat.com> - 1.69-4
- Rebuild, see
  http://lists.fedoraproject.org/pipermail/devel/2012-December/175685.html

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.69-3
- rebuild against new libjpeg

* Thu Aug 02 2012 Ding-Yi Chen <dchen at redhat.com> - 1.69-2
- Fixed issues addressed in Review Request comment #8.

* Wed Jul 25 2012 Ding-Yi Chen <dchen at redhat.com> - 1.69-1
- Upstream update to 1.69
- Add program-prefix in configure.

* Wed Jun 20 2012 Ding-Yi Chen <dchen at redhat.com> - 1.68-4
- Remove util package and its binary files.

* Mon Jun 11 2012 Ding-Yi Chen <dchen at redhat.com> - 1.68-3
- Split the binary into util package

* Wed May 09 2012 Ding-Yi Chen <dchen at redhat.com> - 1.68-2
- Add zlib.h to fix the koji build

* Wed May 09 2012 Ding-Yi Chen <dchen at redhat.com> - 1.68-1
- Initial import.

