Name:          tesseract
Version:       4.1.0
Release:       1%{?dist}
Summary:       Tesseract command line OCR tool

License:       Apache-2.0
URL:           https://github.com/tesseract-ocr/%{name}
Source0:       tesseract_4.1.0.orig.tar.xz

Patch0:        helptext.diff
Patch3:        tesseract_datadir.patch
Patch4:        tesseract_datadir_suse.patch

BuildRequires: libtiff-devel
BuildRequires: leptonica-devel
BuildRequires: cairo-devel
BuildRequires: libicu-devel
BuildRequires: pango-devel
BuildRequires: automake libtool autoconf-archive gcc-c++ gdb
BuildRequires: libxslt-devel git
%if 0%{?suse_version} > 1130
BuildRequires: docbook-xsl-stylesheets
BuildRequires: tesseract-ocr-traineddata-english
%else
BuildRequires: tesseract-langpack-eng
BuildRequires: docbook-style-xsl
%endif

%if 0%{?rhel_version} != 700
BuildRequires: asciidoc
%endif

%if 0%{?suse_version} < 1130
Requires:      tesseract-langpack-eng >= 3.99 
Requires:      tesseract-langpack-osd >= 3.99 
%endif

%define major   4

%if 0%{?suse_version} > 1130
%define tessdata    tesseract-ocr
%else
%define tessdata    tesseract
%endif

%description
A commercial quality OCR engine originally developed at HP between 1985 and
1995. In 1995, this engine was among the top 3 evaluated by UNLV. It was
open-sourced by HP and UNLV in 2005.

%package devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
%if 0%{?suse_version} > 1130
Requires:       libtesseract%{major} = %{version}
%endif

%description devel
The %{name}-devel package contains header file for
developing applications that use %{name}.

%prep
%setup -n tesseract-4.1.0~git4026-5280bbca
%patch0 -p1
%if 0%{?suse_version} > 1130
%patch4 -p1
%else
%patch3 -p1
%endif

#sed "s/AM_MAINTAINER_MODE/AM_MAINTAINER_MODE([enable])/g" -i configure.ac

%build
autoreconf -ifv
%configure --disable-static --disable-tessdata-prefix CXXFLAGS="$RPM_OPT_FLAGS -DTESSDATA_PREFIX=/usr/share/%{tessdata}/4" LDFLAGS="-llept -Wl,-z,defs -Wl,-z,relro"

make %{?_smp_mflags}
%if 0%{?centos_version} == 700 || 0%{?scientificlinux_version} == 700 || 0%{?rhel_version} == 700
echo "no training build"
%else
make training %{?_smp_mflags} 
%endif

echo "auto_test"
./src/api/tesseract -v
./src/api/tesseract ./test/testing/phototest.tif -

%install
%make_install
%if 0%{?centos_version} == 700 || 0%{?scientificlinux_version} == 700 || 0%{?rhel_version} == 700
echo "no training install"
rm -f %{buildroot}%{_mandir}/man5/*
rm -f %{buildroot}%{_mandir}/man1/ambiguous_words*
rm -f %{buildroot}%{_mandir}/man1/cntraining*
rm -f %{buildroot}%{_mandir}/man1/combine_tessdata*
rm -f %{buildroot}%{_mandir}/man1/dawg2wordlist*
rm -f %{buildroot}%{_mandir}/man1/mftraining*
rm -f %{buildroot}%{_mandir}/man1/shapeclustering*
rm -f %{buildroot}%{_mandir}/man1/unicharset_extractor*
rm -f %{buildroot}%{_mandir}/man1/wordlist2dawg*
rm -f %{buildroot}%{_mandir}/man1/classifier_tester*
rm -f %{buildroot}%{_mandir}/man1/combine_lang_model*
rm -f %{buildroot}%{_mandir}/man1/lstmeval*
rm -f %{buildroot}%{_mandir}/man1/lstmtraining*
rm -f %{buildroot}%{_mandir}/man1/merge_unicharsets*
rm -f %{buildroot}%{_mandir}/man1/set_unicharset_properties*
rm -f %{buildroot}%{_mandir}/man1/text2image*
%else
%make_install training-install
%endif

%if 0%{?rhel_version} == 700
rm -f %{buildroot}%{_mandir}/man1/*
%endif

mkdir -p %{buildroot}%{_datadir}/%{name}/4/tessdata

find %{buildroot}%{_libdir} -type f -name '*.la' -delete

%if 0%{?suse_version} > 1130

%package ocr
Summary:       Tesseract command line OCR tool
Requires:      tesseract-ocr-traineddata-english >= 3.99
Requires:      tesseract-ocr-traineddata-orientation_and_script_detection  >= 3.99
Requires:       libtesseract%{major} = %{version}

%description ocr
A commercial quality OCR engine originally developed at HP between 1985 and
1995. In 1995, this engine was among the top 3 evaluated by UNLV. It was
open-sourced by HP and UNLV in 2005.

%package -n libtesseract%{major}
Summary:        Tesseract OCR library
Group:          System/Libraries

%description -n libtesseract%{major}
A commercial quality OCR engine originally developed at HP between 1985 and
1995. In 1995, this engine was among the top 3 evaluated by UNLV. It was
open-sourced by HP and UNLV in 2005.

%post -n libtesseract%{major} -p /sbin/ldconfig
%postun -n libtesseract%{major} -p /sbin/ldconfig

%files ocr
%license LICENSE
%doc AUTHORS ChangeLog README.md test/testing/eurotext.tif test/testing/phototest.tif
%{_bindir}/ambiguous_words
%{_bindir}/classifier_tester
%{_bindir}/cntraining
%{_bindir}/combine_lang_model
%{_bindir}/combine_tessdata
%{_bindir}/dawg2wordlist
%{_bindir}/lstmeval
%{_bindir}/lstmtraining
%{_bindir}/merge_unicharsets
%{_bindir}/mftraining
%{_bindir}/set_unicharset_properties
%{_bindir}/shapeclustering
%{_bindir}/text2image
%{_bindir}/unicharset_extractor
%{_bindir}/wordlist2dawg
%{_bindir}/tesseract
%{_bindir}/language-specific.sh
%{_bindir}/tesstrain.sh
%{_bindir}/tesstrain_utils.sh
%{_mandir}/man1/*
%{_mandir}/man5/*


%files -n libtesseract%{major}
%dir %{_datadir}/%{tessdata}
%dir %{_datadir}/%{tessdata}/4
%dir %{_datadir}/%{tessdata}/4/tessdata
%{_datadir}/%{tessdata}/4/tessdata/configs/
%{_datadir}/%{tessdata}/4/tessdata/tessconfigs/
%{_datadir}/%{tessdata}/4/tessdata/pdf.ttf
%{_libdir}/lib%{name}*.so.4*

%else
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc AUTHORS ChangeLog 
%if 0%{?centos_version} == 700 || 0%{?scientificlinux_version} == 700 || 0%{?rhel_version} == 700
%if 0%{?rhel_version} != 700
%{_mandir}/man1/tesseract.*
%endif
%else
%{_bindir}/ambiguous_words
%{_bindir}/classifier_tester
%{_bindir}/cntraining
%{_bindir}/combine_lang_model
%{_bindir}/combine_tessdata
%{_bindir}/dawg2wordlist
%{_bindir}/lstmeval
%{_bindir}/lstmtraining
%{_bindir}/merge_unicharsets
%{_bindir}/mftraining
%{_bindir}/set_unicharset_properties
%{_bindir}/shapeclustering
%{_bindir}/text2image
%{_bindir}/unicharset_extractor
%{_bindir}/wordlist2dawg
%{_bindir}/language-specific.sh
%{_bindir}/tesstrain.sh
%{_bindir}/tesstrain_utils.sh
%{_mandir}/man1/*
%{_mandir}/man5/*
%endif
%dir %{_datadir}/%{tessdata}
%dir %{_datadir}/%{tessdata}/4
%dir %{_datadir}/%{tessdata}/4/tessdata
%{_datadir}/%{tessdata}/4/tessdata/configs/
%{_datadir}/%{tessdata}/4/tessdata/tessconfigs/
%{_datadir}/%{tessdata}/4/tessdata/pdf.ttf
%{_libdir}/lib%{name}*.so.4*
%{_bindir}/tesseract
%endif

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Mon Jul 08 2019 Alexander Pozdnyakov <almipo@mail.ru>  - 4.1.0-1
- Compile
- URL: -b 4.1 git://github.com/tesseract-ocr/tesseract.git
- Branch: 4.1
- Commit: 5280bbcade4e2dec5eef439a6e189504c2eadcd9
* Wed Feb 06 2019 Alexander Pozdnyakov <almipo@mail.ru>  - 4.0.0+git3524-1
- Compile
- URL: git://github.com/tesseract-ocr/tesseract.git
- Branch: master
- Commit: ec8f02c0de853723bbc785c19fc6c96201411c8f
* Wed Oct 24 2018 Alexander Pozdnyakov <almipo@mail.ru>  - 4.00~git3241-1
- Compile
- URL: git://github.com/tesseract-ocr/tesseract.git
- Branch: master
- Commit: 1066f696dd1439c61ec04ea341666439a97f49a5
* Sun Aug 19 2018 Alexander Pozdnyakov <almipo@mail.ru>  - 4.00~git2891-1
- Compile
- URL: git://github.com/tesseract-ocr/tesseract.git
- Branch: master
- Commit: 115fe7662c33d6a5bd8423c31b4519b5d0b1435e
* Sun Jun 10 2018 Alexander Pozdnyakov <almipo@mail.ru>  - 4.00~git2581-1
- Compile
- URL: git://github.com/tesseract-ocr/tesseract.git
- Branch: master
- Commit: a4241c98170604d346a41604825f0d154e1dd3b3
* Wed May 23 2018 Alexander Pozdnyakov <almipo@mail.ru>  - 4.00~git2489-1
- Compile
- URL: git://github.com/tesseract-ocr/tesseract.git
- Branch: master
- Commit: 5a56d0c2919136c471445c3966e79345828c6118
* Sun May 20 2018 Alexander Pozdnyakov <almipo@mail.ru>  - 4.00~git2451-1
- Compile
- URL: git://github.com/tesseract-ocr/tesseract.git
- Branch: master
- Commit: 45a65463247cfc6856a186341c6918da0b1f44be
* Sat Apr 07 2018 Alexander Pozdnyakov <almipo@mail.ru>  - 4.00~git2288-1
- Compile
- URL: git://github.com/tesseract-ocr/tesseract.git
- Branch: master
- Commit: 10f4998aee3ccc68e9c4931ce744dd292ad6ff19
- Date: 1521751787
* Wed Mar 14 2018 Alexander Pozdnyakov <almipo@mail.ru>  - 4.00~git2246-1
- Compile
- URL: git://github.com/tesseract-ocr/tesseract.git
- Branch: master
- Commit: 023e1b340e6a4dd35909dde82f928790caec3ea5
- Date: 1520973390
* Thu Mar 08 2018 Alexander Pozdnyakov <almipo@mail.ru>  - 4.00~git2230-1
- Initial Release
