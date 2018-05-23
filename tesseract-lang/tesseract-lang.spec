Name:          tesseract-lang
Version:       4.00~git30
Release:       1%{?dist}
Summary:       Language data

License:       Apache-2.0
URL:           https://github.com/tesseract-ocr/tessdata_fast
Source0:       tesseract-lang_4.00~git30-7274cfa.orig.tar.xz

BuildRequires: automake libtool

%description
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. 

%if 0%{?suse_version} > 1130
%define tessdata    tesseract-ocr
%else
%define tessdata    tesseract
%endif

%prep
%setup -n tesseract-lang-4.00~git30-7274cfa
%install
mkdir -p %{buildroot}/%{_datadir}/%{tessdata}/4/tessdata/
install -Dpm 0644 *.traineddata %{buildroot}/%{_datadir}/%{tessdata}/4/tessdata/
install -Dpm 0644 script/*.traineddata %{buildroot}/%{_datadir}/%{tessdata}/4/tessdata/

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-greek_ancient
Summary:       Tesseract language files for Greek, Ancient (to 1453)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-greek_ancient
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Greek, Ancient (to 1453) language.

%files -n tesseract-ocr-traineddata-greek_ancient
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/grc.*
%else
%package -n tesseract-langpack-grc
Summary:       Tesseract language files for Greek, Ancient (to 1453)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-grc
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Greek, Ancient (to 1453) language.

%files -n tesseract-langpack-grc
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/grc.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-bulgarian
Summary:       Tesseract language files for Bulgarian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-bulgarian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Bulgarian language.

%files -n tesseract-ocr-traineddata-bulgarian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/bul.*
%else
%package -n tesseract-langpack-bul
Summary:       Tesseract language files for Bulgarian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-bul
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Bulgarian language.

%files -n tesseract-langpack-bul
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/bul.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-catalan
Summary:       Tesseract language files for Catalan
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-catalan
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Catalan language.

%files -n tesseract-ocr-traineddata-catalan
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/cat.*
%else
%package -n tesseract-langpack-cat
Summary:       Tesseract language files for Catalan
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-cat
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Catalan language.

%files -n tesseract-langpack-cat
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/cat.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-czech
Summary:       Tesseract language files for Czech
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-czech
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Czech language.

%files -n tesseract-ocr-traineddata-czech
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ces.*
%else
%package -n tesseract-langpack-ces
Summary:       Tesseract language files for Czech
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-ces
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Czech language.

%files -n tesseract-langpack-ces
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ces.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-danish
Summary:       Tesseract language files for Danish
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-danish
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Danish language.

%files -n tesseract-ocr-traineddata-danish
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/dan.*
%else
%package -n tesseract-langpack-dan
Summary:       Tesseract language files for Danish
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-dan
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Danish language.

%files -n tesseract-langpack-dan
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/dan.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-german
Summary:       Tesseract language files for German
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-german
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in German language.

%files -n tesseract-ocr-traineddata-german
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/deu.*
%else
%package -n tesseract-langpack-deu
Summary:       Tesseract language files for German
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-deu
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in German language.

%files -n tesseract-langpack-deu
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/deu.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-greek
Summary:       Tesseract language files for Greek
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-greek
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Greek language.

%files -n tesseract-ocr-traineddata-greek
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ell.*
%else
%package -n tesseract-langpack-ell
Summary:       Tesseract language files for Greek
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-ell
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Greek language.

%files -n tesseract-langpack-ell
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ell.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-english
Summary:       Tesseract language files for English
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-english
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in English language.

%files -n tesseract-ocr-traineddata-english
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/eng.*
%else
%package -n tesseract-langpack-eng
Summary:       Tesseract language files for English
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-eng
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in English language.

%files -n tesseract-langpack-eng
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/eng.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-finnish
Summary:       Tesseract language files for Finnish
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-finnish
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Finnish language.

%files -n tesseract-ocr-traineddata-finnish
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/fin.*
%else
%package -n tesseract-langpack-fin
Summary:       Tesseract language files for Finnish
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-fin
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Finnish language.

%files -n tesseract-langpack-fin
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/fin.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-french
Summary:       Tesseract language files for French
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-french
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in French language.

%files -n tesseract-ocr-traineddata-french
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/fra.*
%else
%package -n tesseract-langpack-fra
Summary:       Tesseract language files for French
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-fra
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in French language.

%files -n tesseract-langpack-fra
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/fra.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-hungarian
Summary:       Tesseract language files for Hungarian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-hungarian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Hungarian language.

%files -n tesseract-ocr-traineddata-hungarian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/hun.*
%else
%package -n tesseract-langpack-hun
Summary:       Tesseract language files for Hungarian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-hun
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Hungarian language.

%files -n tesseract-langpack-hun
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/hun.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-indonese
Summary:       Tesseract language files for Indonesian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-indonese
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Indonesian language.

%files -n tesseract-ocr-traineddata-indonese
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ind.*
%else
%package -n tesseract-langpack-ind
Summary:       Tesseract language files for Indonesian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-ind
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Indonesian language.

%files -n tesseract-langpack-ind
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ind.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-italian
Summary:       Tesseract language files for Italian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-italian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Italian language.

%files -n tesseract-ocr-traineddata-italian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ita.*
%else
%package -n tesseract-langpack-ita
Summary:       Tesseract language files for Italian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-ita
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Italian language.

%files -n tesseract-langpack-ita
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ita.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-latvian
Summary:       Tesseract language files for Latvian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-latvian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Latvian language.

%files -n tesseract-ocr-traineddata-latvian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/lav.*
%else
%package -n tesseract-langpack-lav
Summary:       Tesseract language files for Latvian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-lav
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Latvian language.

%files -n tesseract-langpack-lav
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/lav.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-lithuanian
Summary:       Tesseract language files for Lithuanian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-lithuanian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Lithuanian language.

%files -n tesseract-ocr-traineddata-lithuanian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/lit.*
%else
%package -n tesseract-langpack-lit
Summary:       Tesseract language files for Lithuanian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-lit
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Lithuanian language.

%files -n tesseract-langpack-lit
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/lit.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-dutch
Summary:       Tesseract language files for Dutch
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-dutch
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Dutch language.

%files -n tesseract-ocr-traineddata-dutch
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/nld.*
%else
%package -n tesseract-langpack-nld
Summary:       Tesseract language files for Dutch
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-nld
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Dutch language.

%files -n tesseract-langpack-nld
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/nld.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-norwegian
Summary:       Tesseract language files for Norwegian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-norwegian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Norwegian language.

%files -n tesseract-ocr-traineddata-norwegian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/nor.*
%else
%package -n tesseract-langpack-nor
Summary:       Tesseract language files for Norwegian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-nor
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Norwegian language.

%files -n tesseract-langpack-nor
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/nor.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-polish
Summary:       Tesseract language files for Polish
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-polish
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Polish language.

%files -n tesseract-ocr-traineddata-polish
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/pol.*
%else
%package -n tesseract-langpack-pol
Summary:       Tesseract language files for Polish
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-pol
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Polish language.

%files -n tesseract-langpack-pol
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/pol.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-portuguese
Summary:       Tesseract language files for Portuguese
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-portuguese
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Portuguese language.

%files -n tesseract-ocr-traineddata-portuguese
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/por.*
%else
%package -n tesseract-langpack-por
Summary:       Tesseract language files for Portuguese
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-por
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Portuguese language.

%files -n tesseract-langpack-por
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/por.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-romanian
Summary:       Tesseract language files for Romanian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-romanian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Romanian language.

%files -n tesseract-ocr-traineddata-romanian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ron.*
%else
%package -n tesseract-langpack-ron
Summary:       Tesseract language files for Romanian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-ron
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Romanian language.

%files -n tesseract-langpack-ron
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ron.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-russian
Summary:       Tesseract language files for Russian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-russian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Russian language.

%files -n tesseract-ocr-traineddata-russian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/rus.*
%else
%package -n tesseract-langpack-rus
Summary:       Tesseract language files for Russian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-rus
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Russian language.

%files -n tesseract-langpack-rus
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/rus.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-slovak
Summary:       Tesseract language files for Slovakian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-slovak
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Slovakian language.

%files -n tesseract-ocr-traineddata-slovak
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/slk.*
%else
%package -n tesseract-langpack-slk
Summary:       Tesseract language files for Slovakian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-slk
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Slovakian language.

%files -n tesseract-langpack-slk
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/slk.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-slovenian
Summary:       Tesseract language files for Slovenian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-slovenian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Slovenian language.

%files -n tesseract-ocr-traineddata-slovenian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/slv.*
%else
%package -n tesseract-langpack-slv
Summary:       Tesseract language files for Slovenian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-slv
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Slovenian language.

%files -n tesseract-langpack-slv
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/slv.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-spanish
Summary:       Tesseract language files for Spanish
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-spanish
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Spanish language.

%files -n tesseract-ocr-traineddata-spanish
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/spa.*
%else
%package -n tesseract-langpack-spa
Summary:       Tesseract language files for Spanish
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-spa
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Spanish language.

%files -n tesseract-langpack-spa
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/spa.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-serbian
Summary:       Tesseract language files for Serbian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-serbian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Serbian language.

%files -n tesseract-ocr-traineddata-serbian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/srp.*
%else
%package -n tesseract-langpack-srp
Summary:       Tesseract language files for Serbian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-srp
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Serbian language.

%files -n tesseract-langpack-srp
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/srp.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-swedish
Summary:       Tesseract language files for Swedish
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-swedish
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Swedish language.

%files -n tesseract-ocr-traineddata-swedish
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/swe.*
%else
%package -n tesseract-langpack-swe
Summary:       Tesseract language files for Swedish
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-swe
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Swedish language.

%files -n tesseract-langpack-swe
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/swe.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-turkish
Summary:       Tesseract language files for Turkish
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-turkish
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Turkish language.

%files -n tesseract-ocr-traineddata-turkish
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/tur.*
%else
%package -n tesseract-langpack-tur
Summary:       Tesseract language files for Turkish
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-tur
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Turkish language.

%files -n tesseract-langpack-tur
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/tur.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-ukrainian
Summary:       Tesseract language files for Ukrainian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-ukrainian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Ukrainian language.

%files -n tesseract-ocr-traineddata-ukrainian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ukr.*
%else
%package -n tesseract-langpack-ukr
Summary:       Tesseract language files for Ukrainian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-ukr
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Ukrainian language.

%files -n tesseract-langpack-ukr
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ukr.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-vietnamese
Summary:       Tesseract language files for Vietnamese
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-vietnamese
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Vietnamese language.

%files -n tesseract-ocr-traineddata-vietnamese
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/vie.*
%else
%package -n tesseract-langpack-vie
Summary:       Tesseract language files for Vietnamese
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-vie
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Vietnamese language.

%files -n tesseract-langpack-vie
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/vie.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-chinese_simplified
Summary:       Tesseract language files for Chinese - Simplified
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-chinese_simplified
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Chinese - Simplified language.

%files -n tesseract-ocr-traineddata-chinese_simplified
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/chi_sim.*
%else
%package -n tesseract-langpack-chi-sim
Summary:       Tesseract language files for Chinese - Simplified
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-chi-sim
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Chinese - Simplified language.

%files -n tesseract-langpack-chi-sim
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/chi_sim.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-chinese_traditional
Summary:       Tesseract language files for Chinese - Traditional
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-chinese_traditional
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Chinese - Traditional language.

%files -n tesseract-ocr-traineddata-chinese_traditional
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/chi_tra.*
%else
%package -n tesseract-langpack-chi-tra
Summary:       Tesseract language files for Chinese - Traditional
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-chi-tra
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Chinese - Traditional language.

%files -n tesseract-langpack-chi-tra
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/chi_tra.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-amharic
Summary:       Tesseract language files for Amharic
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-amharic
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Amharic language.

%files -n tesseract-ocr-traineddata-amharic
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/amh.*
%else
%package -n tesseract-langpack-amh
Summary:       Tesseract language files for Amharic
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-amh
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Amharic language.

%files -n tesseract-langpack-amh
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/amh.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-assamese
Summary:       Tesseract language files for Assamese
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-assamese
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Assamese language.

%files -n tesseract-ocr-traineddata-assamese
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/asm.*
%else
%package -n tesseract-langpack-asm
Summary:       Tesseract language files for Assamese
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-asm
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Assamese language.

%files -n tesseract-langpack-asm
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/asm.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-azerbaijani_cyrillic
Summary:       Tesseract language files for Azerbaijani (Cyrillic)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99
%if 0%{?centos_version} == 700 || 0%{?scientificlinux_version} == 700
Requires:      tesseract-langpack-aze >= 3.99
%else
%if 0%{?suse_version} > 1130
Suggests:      tesseract-ocr-traineddata-azerbaijani >= 3.99
%else
Suggests:      tesseract-langpack-aze >= 3.99
%endif
%endif

%description -n tesseract-ocr-traineddata-azerbaijani_cyrillic
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Azerbaijani (Cyrillic) language.

%files -n tesseract-ocr-traineddata-azerbaijani_cyrillic
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/aze_cyrl.*
%else
%package -n tesseract-langpack-aze-cyrl
Summary:       Tesseract language files for Azerbaijani (Cyrillic)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99
%if 0%{?centos_version} == 700 || 0%{?scientificlinux_version} == 700
Requires:      tesseract-langpack-aze >= 3.99
%else
%if 0%{?suse_version} > 1130
Suggests:      tesseract-ocr-traineddata-azerbaijani >= 3.99
%else
Suggests:      tesseract-langpack-aze >= 3.99
%endif
%endif

%description -n tesseract-langpack-aze-cyrl
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Azerbaijani (Cyrillic) language.

%files -n tesseract-langpack-aze-cyrl
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/aze_cyrl.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-tibetan_standard
Summary:       Tesseract language files for Tibetan Standard
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-tibetan_standard
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Tibetan Standard language.

%files -n tesseract-ocr-traineddata-tibetan_standard
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/bod.*
%else
%package -n tesseract-langpack-bod
Summary:       Tesseract language files for Tibetan Standard
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-bod
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Tibetan Standard language.

%files -n tesseract-langpack-bod
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/bod.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-bosnian
Summary:       Tesseract language files for Bosnian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-bosnian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Bosnian language.

%files -n tesseract-ocr-traineddata-bosnian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/bos.*
%else
%package -n tesseract-langpack-bos
Summary:       Tesseract language files for Bosnian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-bos
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Bosnian language.

%files -n tesseract-langpack-bos
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/bos.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-cebuano
Summary:       Tesseract language files for Cebuano
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-cebuano
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Cebuano language.

%files -n tesseract-ocr-traineddata-cebuano
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ceb.*
%else
%package -n tesseract-langpack-ceb
Summary:       Tesseract language files for Cebuano
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-ceb
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Cebuano language.

%files -n tesseract-langpack-ceb
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ceb.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-welsh
Summary:       Tesseract language files for Welsh
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-welsh
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Welsh language.

%files -n tesseract-ocr-traineddata-welsh
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/cym.*
%else
%package -n tesseract-langpack-cym
Summary:       Tesseract language files for Welsh
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-cym
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Welsh language.

%files -n tesseract-langpack-cym
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/cym.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-dzongkha
Summary:       Tesseract language files for Dzongkha
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-dzongkha
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Dzongkha language.

%files -n tesseract-ocr-traineddata-dzongkha
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/dzo.*
%else
%package -n tesseract-langpack-dzo
Summary:       Tesseract language files for Dzongkha
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-dzo
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Dzongkha language.

%files -n tesseract-langpack-dzo
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/dzo.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-persian
Summary:       Tesseract language files for Persian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-persian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Persian language.

%files -n tesseract-ocr-traineddata-persian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/fas.*
%else
%package -n tesseract-langpack-fas
Summary:       Tesseract language files for Persian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-fas
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Persian language.

%files -n tesseract-langpack-fas
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/fas.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-irish
Summary:       Tesseract language files for Irish
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-irish
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Irish language.

%files -n tesseract-ocr-traineddata-irish
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/gle.*
%else
%package -n tesseract-langpack-gle
Summary:       Tesseract language files for Irish
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-gle
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Irish language.

%files -n tesseract-langpack-gle
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/gle.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-gujarati
Summary:       Tesseract language files for Gujarati
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-gujarati
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Gujarati language.

%files -n tesseract-ocr-traineddata-gujarati
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/guj.*
%else
%package -n tesseract-langpack-guj
Summary:       Tesseract language files for Gujarati
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-guj
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Gujarati language.

%files -n tesseract-langpack-guj
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/guj.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-haitian
Summary:       Tesseract language files for Haitian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-haitian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Haitian language.

%files -n tesseract-ocr-traineddata-haitian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/hat.*
%else
%package -n tesseract-langpack-hat
Summary:       Tesseract language files for Haitian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-hat
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Haitian language.

%files -n tesseract-langpack-hat
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/hat.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-inuktitut
Summary:       Tesseract language files for Inuktitut
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-inuktitut
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Inuktitut language.

%files -n tesseract-ocr-traineddata-inuktitut
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/iku.*
%else
%package -n tesseract-langpack-iku
Summary:       Tesseract language files for Inuktitut
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-iku
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Inuktitut language.

%files -n tesseract-langpack-iku
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/iku.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-javanese
Summary:       Tesseract language files for Javanese
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-javanese
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Javanese language.

%files -n tesseract-ocr-traineddata-javanese
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/jav.*
%else
%package -n tesseract-langpack-jav
Summary:       Tesseract language files for Javanese
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-jav
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Javanese language.

%files -n tesseract-langpack-jav
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/jav.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-georgian
Summary:       Tesseract language files for Georgian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-georgian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Georgian language.

%files -n tesseract-ocr-traineddata-georgian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/kat.*
%else
%package -n tesseract-langpack-kat
Summary:       Tesseract language files for Georgian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-kat
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Georgian language.

%files -n tesseract-langpack-kat
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/kat.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-georgian_old
Summary:       Tesseract language files for Old Georgian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-georgian_old
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Old Georgian language.

%files -n tesseract-ocr-traineddata-georgian_old
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/kat_old.*
%else
%package -n tesseract-langpack-kat-old
Summary:       Tesseract language files for Old Georgian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-kat-old
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Old Georgian language.

%files -n tesseract-langpack-kat-old
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/kat_old.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-kazakh
Summary:       Tesseract language files for Kazakh
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-kazakh
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Kazakh language.

%files -n tesseract-ocr-traineddata-kazakh
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/kaz.*
%else
%package -n tesseract-langpack-kaz
Summary:       Tesseract language files for Kazakh
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-kaz
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Kazakh language.

%files -n tesseract-langpack-kaz
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/kaz.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-khmer
Summary:       Tesseract language files for Khmer
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-khmer
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Khmer language.

%files -n tesseract-ocr-traineddata-khmer
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/khm.*
%else
%package -n tesseract-langpack-khm
Summary:       Tesseract language files for Khmer
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-khm
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Khmer language.

%files -n tesseract-langpack-khm
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/khm.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-kyrgyz
Summary:       Tesseract language files for Kyrgyz
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-kyrgyz
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Kyrgyz language.

%files -n tesseract-ocr-traineddata-kyrgyz
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/kir.*
%else
%package -n tesseract-langpack-kir
Summary:       Tesseract language files for Kyrgyz
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-kir
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Kyrgyz language.

%files -n tesseract-langpack-kir
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/kir.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-lao
Summary:       Tesseract language files for Lao
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-lao
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Lao language.

%files -n tesseract-ocr-traineddata-lao
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/lao.*
%else
%package -n tesseract-langpack-lao
Summary:       Tesseract language files for Lao
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-lao
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Lao language.

%files -n tesseract-langpack-lao
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/lao.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-latin
Summary:       Tesseract language files for Latin
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-latin
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Latin language.

%files -n tesseract-ocr-traineddata-latin
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/lat.*
%else
%package -n tesseract-langpack-lat
Summary:       Tesseract language files for Latin
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-lat
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Latin language.

%files -n tesseract-langpack-lat
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/lat.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-marathi
Summary:       Tesseract language files for Marathi
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-marathi
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Marathi language.

%files -n tesseract-ocr-traineddata-marathi
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/mar.*
%else
%package -n tesseract-langpack-mar
Summary:       Tesseract language files for Marathi
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-mar
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Marathi language.

%files -n tesseract-langpack-mar
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/mar.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-burmese
Summary:       Tesseract language files for Burmese
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-burmese
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Burmese language.

%files -n tesseract-ocr-traineddata-burmese
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/mya.*
%else
%package -n tesseract-langpack-mya
Summary:       Tesseract language files for Burmese
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-mya
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Burmese language.

%files -n tesseract-langpack-mya
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/mya.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-nepali
Summary:       Tesseract language files for Nepali
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-nepali
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Nepali language.

%files -n tesseract-ocr-traineddata-nepali
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/nep.*
%else
%package -n tesseract-langpack-nep
Summary:       Tesseract language files for Nepali
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-nep
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Nepali language.

%files -n tesseract-langpack-nep
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/nep.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-oriya
Summary:       Tesseract language files for Oriya
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-oriya
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Oriya language.

%files -n tesseract-ocr-traineddata-oriya
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ori.*
%else
%package -n tesseract-langpack-ori
Summary:       Tesseract language files for Oriya
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-ori
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Oriya language.

%files -n tesseract-langpack-ori
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ori.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-punjabi
Summary:       Tesseract language files for Punjabi
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-punjabi
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Punjabi language.

%files -n tesseract-ocr-traineddata-punjabi
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/pan.*
%else
%package -n tesseract-langpack-pan
Summary:       Tesseract language files for Punjabi
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-pan
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Punjabi language.

%files -n tesseract-langpack-pan
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/pan.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-pashto
Summary:       Tesseract language files for Pashto
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-pashto
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Pashto language.

%files -n tesseract-ocr-traineddata-pashto
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/pus.*
%else
%package -n tesseract-langpack-pus
Summary:       Tesseract language files for Pashto
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-pus
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Pashto language.

%files -n tesseract-langpack-pus
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/pus.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-sanskrit
Summary:       Tesseract language files for Sanskrit
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-sanskrit
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Sanskrit language.

%files -n tesseract-ocr-traineddata-sanskrit
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/san.*
%else
%package -n tesseract-langpack-san
Summary:       Tesseract language files for Sanskrit
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-san
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Sanskrit language.

%files -n tesseract-langpack-san
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/san.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-sinhala
Summary:       Tesseract language files for Sinhala
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-sinhala
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Sinhala language.

%files -n tesseract-ocr-traineddata-sinhala
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/sin.*
%else
%package -n tesseract-langpack-sin
Summary:       Tesseract language files for Sinhala
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-sin
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Sinhala language.

%files -n tesseract-langpack-sin
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/sin.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-serbian_latin
Summary:       Tesseract language files for Serbian (Latin)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99
%if 0%{?suse_version} > 1130
Requires:      tesseract-ocr-traineddata-serbian >= 3.99
%else
Requires:      tesseract-langpack-srp >= 3.99
%endif

%description -n tesseract-ocr-traineddata-serbian_latin
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Serbian (Latin) language.

%files -n tesseract-ocr-traineddata-serbian_latin
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/srp_latn.*
%else
%package -n tesseract-langpack-srp-latn
Summary:       Tesseract language files for Serbian (Latin)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99
%if 0%{?suse_version} > 1130
Requires:      tesseract-ocr-traineddata-serbian >= 3.99
%else
Requires:      tesseract-langpack-srp >= 3.99
%endif

%description -n tesseract-langpack-srp-latn
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Serbian (Latin) language.

%files -n tesseract-langpack-srp-latn
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/srp_latn.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-syriac
Summary:       Tesseract language files for Syriac
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-syriac
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Syriac language.

%files -n tesseract-ocr-traineddata-syriac
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/syr.*
%else
%package -n tesseract-langpack-syr
Summary:       Tesseract language files for Syriac
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-syr
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Syriac language.

%files -n tesseract-langpack-syr
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/syr.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-tajik
Summary:       Tesseract language files for Tajik
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-tajik
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Tajik language.

%files -n tesseract-ocr-traineddata-tajik
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/tgk.*
%else
%package -n tesseract-langpack-tgk
Summary:       Tesseract language files for Tajik
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-tgk
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Tajik language.

%files -n tesseract-langpack-tgk
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/tgk.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-tigrinya
Summary:       Tesseract language files for Tigrinya
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-tigrinya
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Tigrinya language.

%files -n tesseract-ocr-traineddata-tigrinya
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/tir.*
%else
%package -n tesseract-langpack-tir
Summary:       Tesseract language files for Tigrinya
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-tir
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Tigrinya language.

%files -n tesseract-langpack-tir
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/tir.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-uyghur
Summary:       Tesseract language files for Uyghur
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-uyghur
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Uyghur language.

%files -n tesseract-ocr-traineddata-uyghur
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/uig.*
%else
%package -n tesseract-langpack-uig
Summary:       Tesseract language files for Uyghur
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-uig
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Uyghur language.

%files -n tesseract-langpack-uig
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/uig.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-urdu
Summary:       Tesseract language files for Urdu
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-urdu
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Urdu language.

%files -n tesseract-ocr-traineddata-urdu
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/urd.*
%else
%package -n tesseract-langpack-urd
Summary:       Tesseract language files for Urdu
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-urd
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Urdu language.

%files -n tesseract-langpack-urd
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/urd.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-uzbek
Summary:       Tesseract language files for Uzbek
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99
%if 0%{?suse_version} > 1130
Requires:      tesseract-ocr-traineddata-uzbek_cyrillic >= 3.99
%else
Requires:      tesseract-langpack-uzb-cyrl >= 3.99
%endif

%description -n tesseract-ocr-traineddata-uzbek
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Uzbek language.

%files -n tesseract-ocr-traineddata-uzbek
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/uzb.*
%else
%package -n tesseract-langpack-uzb
Summary:       Tesseract language files for Uzbek
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99
%if 0%{?suse_version} > 1130
Requires:      tesseract-ocr-traineddata-uzbek_cyrillic >= 3.99
%else
Requires:      tesseract-langpack-uzb-cyrl >= 3.99
%endif

%description -n tesseract-langpack-uzb
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Uzbek language.

%files -n tesseract-langpack-uzb
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/uzb.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-uzbek_cyrillic
Summary:       Tesseract language files for Uzbek (Cyrillic)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99
%if 0%{?centos_version} == 700 || 0%{?scientificlinux_version} == 700
Requires:      tesseract-langpack-uzb >= 3.99
%else
%if 0%{?suse_version} > 1130
Suggests:      tesseract-ocr-traineddata-uzbek >= 3.99
%else
Suggests:      tesseract-langpack-uzb >= 3.99
%endif
%endif

%description -n tesseract-ocr-traineddata-uzbek_cyrillic
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Uzbek (Cyrillic) language.

%files -n tesseract-ocr-traineddata-uzbek_cyrillic
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/uzb_cyrl.*
%else
%package -n tesseract-langpack-uzb-cyrl
Summary:       Tesseract language files for Uzbek (Cyrillic)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99
%if 0%{?centos_version} == 700 || 0%{?scientificlinux_version} == 700
Requires:      tesseract-langpack-uzb >= 3.99
%else
%if 0%{?suse_version} > 1130
Suggests:      tesseract-ocr-traineddata-uzbek >= 3.99
%else
Suggests:      tesseract-langpack-uzb >= 3.99
%endif
%endif

%description -n tesseract-langpack-uzb-cyrl
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Uzbek (Cyrillic) language.

%files -n tesseract-langpack-uzb-cyrl
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/uzb_cyrl.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-yiddish
Summary:       Tesseract language files for Yiddish
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-yiddish
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Yiddish language.

%files -n tesseract-ocr-traineddata-yiddish
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/yid.*
%else
%package -n tesseract-langpack-yid
Summary:       Tesseract language files for Yiddish
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-yid
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Yiddish language.

%files -n tesseract-langpack-yid
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/yid.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-afrikaans
Summary:       Tesseract language files for Afrikaans
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-afrikaans
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Afrikaans language.

%files -n tesseract-ocr-traineddata-afrikaans
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/afr.*
%else
%package -n tesseract-langpack-afr
Summary:       Tesseract language files for Afrikaans
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-afr
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Afrikaans language.

%files -n tesseract-langpack-afr
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/afr.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-arabic
Summary:       Tesseract language files for Arabic
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-arabic
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Arabic language.

%files -n tesseract-ocr-traineddata-arabic
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ara.*
%else
%package -n tesseract-langpack-ara
Summary:       Tesseract language files for Arabic
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-ara
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Arabic language.

%files -n tesseract-langpack-ara
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ara.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-azerbaijani
Summary:       Tesseract language files for Azerbaijani
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99
%if 0%{?suse_version} > 1130
Requires:      tesseract-ocr-traineddata-azerbaijani_cyrillic >= 3.99
%else
Requires:      tesseract-langpack-aze-cyrl >= 3.99
%endif

%description -n tesseract-ocr-traineddata-azerbaijani
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Azerbaijani language.

%files -n tesseract-ocr-traineddata-azerbaijani
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/aze.*
%else
%package -n tesseract-langpack-aze
Summary:       Tesseract language files for Azerbaijani
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99
%if 0%{?suse_version} > 1130
Requires:      tesseract-ocr-traineddata-azerbaijani_cyrillic >= 3.99
%else
Requires:      tesseract-langpack-aze-cyrl >= 3.99
%endif

%description -n tesseract-langpack-aze
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Azerbaijani language.

%files -n tesseract-langpack-aze
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/aze.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-belarusian
Summary:       Tesseract language files for Belarusian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-belarusian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Belarusian language.

%files -n tesseract-ocr-traineddata-belarusian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/bel.*
%else
%package -n tesseract-langpack-bel
Summary:       Tesseract language files for Belarusian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-bel
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Belarusian language.

%files -n tesseract-langpack-bel
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/bel.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-bengali
Summary:       Tesseract language files for Bengali
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-bengali
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Bengali language.

%files -n tesseract-ocr-traineddata-bengali
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ben.*
%else
%package -n tesseract-langpack-ben
Summary:       Tesseract language files for Bengali
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-ben
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Bengali language.

%files -n tesseract-langpack-ben
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ben.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-cherokee
Summary:       Tesseract language files for Cherokee
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-cherokee
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Cherokee language.

%files -n tesseract-ocr-traineddata-cherokee
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/chr.*
%else
%package -n tesseract-langpack-chr
Summary:       Tesseract language files for Cherokee
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-chr
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Cherokee language.

%files -n tesseract-langpack-chr
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/chr.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-english_middle
Summary:       Tesseract language files for English, Middle (1100-1500)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-english_middle
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in English, Middle (1100-1500) language.

%files -n tesseract-ocr-traineddata-english_middle
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/enm.*
%else
%package -n tesseract-langpack-enm
Summary:       Tesseract language files for English, Middle (1100-1500)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-enm
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in English, Middle (1100-1500) language.

%files -n tesseract-langpack-enm
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/enm.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-esperanto
Summary:       Tesseract language files for Esperanto
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-esperanto
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Esperanto language.

%files -n tesseract-ocr-traineddata-esperanto
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/epo.*
%else
%package -n tesseract-langpack-epo
Summary:       Tesseract language files for Esperanto
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-epo
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Esperanto language.

%files -n tesseract-langpack-epo
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/epo.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-estonian
Summary:       Tesseract language files for Estonian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-estonian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Estonian language.

%files -n tesseract-ocr-traineddata-estonian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/est.*
%else
%package -n tesseract-langpack-est
Summary:       Tesseract language files for Estonian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-est
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Estonian language.

%files -n tesseract-langpack-est
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/est.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-basque
Summary:       Tesseract language files for Basque
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-basque
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Basque language.

%files -n tesseract-ocr-traineddata-basque
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/eus.*
%else
%package -n tesseract-langpack-eus
Summary:       Tesseract language files for Basque
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-eus
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Basque language.

%files -n tesseract-langpack-eus
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/eus.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-german_fraktur
Summary:       Tesseract language files for German (Fraktur)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-german_fraktur
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in German (Fraktur) language.

%files -n tesseract-ocr-traineddata-german_fraktur
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/frk.*
%else
%package -n tesseract-langpack-frk
Summary:       Tesseract language files for German (Fraktur)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-frk
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in German (Fraktur) language.

%files -n tesseract-langpack-frk
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/frk.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-french_middle
Summary:       Tesseract language files for French, Middle (ca.1400-1600)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-french_middle
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in French, Middle (ca.1400-1600) language.

%files -n tesseract-ocr-traineddata-french_middle
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/frm.*
%else
%package -n tesseract-langpack-frm
Summary:       Tesseract language files for French, Middle (ca.1400-1600)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-frm
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in French, Middle (ca.1400-1600) language.

%files -n tesseract-langpack-frm
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/frm.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-galician
Summary:       Tesseract language files for Galician
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-galician
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Galician language.

%files -n tesseract-ocr-traineddata-galician
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/glg.*
%else
%package -n tesseract-langpack-glg
Summary:       Tesseract language files for Galician
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-glg
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Galician language.

%files -n tesseract-langpack-glg
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/glg.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-hebrew
Summary:       Tesseract language files for Hebrew
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-hebrew
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Hebrew language.

%files -n tesseract-ocr-traineddata-hebrew
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/heb.*
%else
%package -n tesseract-langpack-heb
Summary:       Tesseract language files for Hebrew
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-heb
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Hebrew language.

%files -n tesseract-langpack-heb
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/heb.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-hindi
Summary:       Tesseract language files for Hindi
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-hindi
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Hindi language.

%files -n tesseract-ocr-traineddata-hindi
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/hin.*
%else
%package -n tesseract-langpack-hin
Summary:       Tesseract language files for Hindi
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-hin
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Hindi language.

%files -n tesseract-langpack-hin
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/hin.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-croatian
Summary:       Tesseract language files for Croatian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-croatian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Croatian language.

%files -n tesseract-ocr-traineddata-croatian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/hrv.*
%else
%package -n tesseract-langpack-hrv
Summary:       Tesseract language files for Croatian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-hrv
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Croatian language.

%files -n tesseract-langpack-hrv
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/hrv.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-icelandic
Summary:       Tesseract language files for Icelandic
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-icelandic
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Icelandic language.

%files -n tesseract-ocr-traineddata-icelandic
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/isl.*
%else
%package -n tesseract-langpack-isl
Summary:       Tesseract language files for Icelandic
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-isl
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Icelandic language.

%files -n tesseract-langpack-isl
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/isl.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-italian_old
Summary:       Tesseract language files for Italian - Old
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-italian_old
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Italian - Old language.

%files -n tesseract-ocr-traineddata-italian_old
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ita_old.*
%else
%package -n tesseract-langpack-ita-old
Summary:       Tesseract language files for Italian - Old
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-ita-old
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Italian - Old language.

%files -n tesseract-langpack-ita-old
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ita_old.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-japanese
Summary:       Tesseract language files for Japanese
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-japanese
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Japanese language.

%files -n tesseract-ocr-traineddata-japanese
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/jpn.*
%else
%package -n tesseract-langpack-jpn
Summary:       Tesseract language files for Japanese
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-jpn
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Japanese language.

%files -n tesseract-langpack-jpn
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/jpn.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-kannada
Summary:       Tesseract language files for Kannada
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-kannada
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Kannada language.

%files -n tesseract-ocr-traineddata-kannada
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/kan.*
%else
%package -n tesseract-langpack-kan
Summary:       Tesseract language files for Kannada
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-kan
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Kannada language.

%files -n tesseract-langpack-kan
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/kan.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-korean
Summary:       Tesseract language files for Korean
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-korean
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Korean language.

%files -n tesseract-ocr-traineddata-korean
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/kor.*
%else
%package -n tesseract-langpack-kor
Summary:       Tesseract language files for Korean
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-kor
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Korean language.

%files -n tesseract-langpack-kor
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/kor.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-malayalam
Summary:       Tesseract language files for Malayalam
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-malayalam
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Malayalam language.

%files -n tesseract-ocr-traineddata-malayalam
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/mal.*
%else
%package -n tesseract-langpack-mal
Summary:       Tesseract language files for Malayalam
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-mal
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Malayalam language.

%files -n tesseract-langpack-mal
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/mal.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-macedonian
Summary:       Tesseract language files for Macedonian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-macedonian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Macedonian language.

%files -n tesseract-ocr-traineddata-macedonian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/mkd.*
%else
%package -n tesseract-langpack-mkd
Summary:       Tesseract language files for Macedonian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-mkd
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Macedonian language.

%files -n tesseract-langpack-mkd
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/mkd.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-maltese
Summary:       Tesseract language files for Maltese
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-maltese
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Maltese language.

%files -n tesseract-ocr-traineddata-maltese
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/mlt.*
%else
%package -n tesseract-langpack-mlt
Summary:       Tesseract language files for Maltese
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-mlt
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Maltese language.

%files -n tesseract-langpack-mlt
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/mlt.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-malay
Summary:       Tesseract language files for Malay
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-malay
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Malay language.

%files -n tesseract-ocr-traineddata-malay
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/msa.*
%else
%package -n tesseract-langpack-msa
Summary:       Tesseract language files for Malay
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-msa
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Malay language.

%files -n tesseract-langpack-msa
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/msa.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-spanish_old
Summary:       Tesseract language files for Spanish, Castilian - Old
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-spanish_old
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Spanish, Castilian - Old language.

%files -n tesseract-ocr-traineddata-spanish_old
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/spa_old.*
%else
%package -n tesseract-langpack-spa-old
Summary:       Tesseract language files for Spanish, Castilian - Old
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-spa-old
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Spanish, Castilian - Old language.

%files -n tesseract-langpack-spa-old
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/spa_old.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-albanian
Summary:       Tesseract language files for Albanian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-albanian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Albanian language.

%files -n tesseract-ocr-traineddata-albanian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/sqi.*
%else
%package -n tesseract-langpack-sqi
Summary:       Tesseract language files for Albanian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-sqi
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Albanian language.

%files -n tesseract-langpack-sqi
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/sqi.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-swahili
Summary:       Tesseract language files for Swahili
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-swahili
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Swahili language.

%files -n tesseract-ocr-traineddata-swahili
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/swa.*
%else
%package -n tesseract-langpack-swa
Summary:       Tesseract language files for Swahili
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-swa
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Swahili language.

%files -n tesseract-langpack-swa
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/swa.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-tamil
Summary:       Tesseract language files for Tamil
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-tamil
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Tamil language.

%files -n tesseract-ocr-traineddata-tamil
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/tam.*
%else
%package -n tesseract-langpack-tam
Summary:       Tesseract language files for Tamil
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-tam
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Tamil language.

%files -n tesseract-langpack-tam
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/tam.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-telugu
Summary:       Tesseract language files for Telugu
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-telugu
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Telugu language.

%files -n tesseract-ocr-traineddata-telugu
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/tel.*
%else
%package -n tesseract-langpack-tel
Summary:       Tesseract language files for Telugu
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-tel
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Telugu language.

%files -n tesseract-langpack-tel
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/tel.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-thai
Summary:       Tesseract language files for Thai
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-thai
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Thai language.

%files -n tesseract-ocr-traineddata-thai
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/tha.*
%else
%package -n tesseract-langpack-tha
Summary:       Tesseract language files for Thai
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-tha
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Thai language.

%files -n tesseract-langpack-tha
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/tha.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-breton
Summary:       Tesseract language files for Breton
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-breton
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Breton language.

%files -n tesseract-ocr-traineddata-breton
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/bre.*
%else
%package -n tesseract-langpack-bre
Summary:       Tesseract language files for Breton
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-bre
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Breton language.

%files -n tesseract-langpack-bre
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/bre.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-chinese_simplified_vert
Summary:       Tesseract language files for Chinese - Simplified (vertical)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-chinese_simplified_vert
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Chinese - Simplified (vertical) language.

%files -n tesseract-ocr-traineddata-chinese_simplified_vert
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/chi_sim_vert.*
%else
%package -n tesseract-langpack-chi-sim-vert
Summary:       Tesseract language files for Chinese - Simplified (vertical)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-chi-sim-vert
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Chinese - Simplified (vertical) language.

%files -n tesseract-langpack-chi-sim-vert
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/chi_sim_vert.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-chinese_traditional_vert
Summary:       Tesseract language files for Chinese - Traditional (vertical)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-chinese_traditional_vert
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Chinese - Traditional (vertical) language.

%files -n tesseract-ocr-traineddata-chinese_traditional_vert
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/chi_tra_vert.*
%else
%package -n tesseract-langpack-chi-tra-vert
Summary:       Tesseract language files for Chinese - Traditional (vertical)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-chi-tra-vert
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Chinese - Traditional (vertical) language.

%files -n tesseract-langpack-chi-tra-vert
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/chi_tra_vert.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-corsican
Summary:       Tesseract language files for Corsican
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-corsican
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Corsican language.

%files -n tesseract-ocr-traineddata-corsican
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/cos.*
%else
%package -n tesseract-langpack-cos
Summary:       Tesseract language files for Corsican
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-cos
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Corsican language.

%files -n tesseract-langpack-cos
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/cos.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-divehi
Summary:       Tesseract language files for Divehi
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-divehi
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Divehi language.

%files -n tesseract-ocr-traineddata-divehi
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/div.*
%else
%package -n tesseract-langpack-div
Summary:       Tesseract language files for Divehi
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-div
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Divehi language.

%files -n tesseract-langpack-div
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/div.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-faroese
Summary:       Tesseract language files for Faroese
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-faroese
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Faroese language.

%files -n tesseract-ocr-traineddata-faroese
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/fao.*
%else
%package -n tesseract-langpack-fao
Summary:       Tesseract language files for Faroese
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-fao
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Faroese language.

%files -n tesseract-langpack-fao
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/fao.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-filipino
Summary:       Tesseract language files for Filipino
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-filipino
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Filipino language.

%files -n tesseract-ocr-traineddata-filipino
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/fil.*
%else
%package -n tesseract-langpack-fil
Summary:       Tesseract language files for Filipino
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-fil
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Filipino language.

%files -n tesseract-langpack-fil
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/fil.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-frisian_western
Summary:       Tesseract language files for Frisian (Western)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-frisian_western
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Frisian (Western) language.

%files -n tesseract-ocr-traineddata-frisian_western
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/fry.*
%else
%package -n tesseract-langpack-fry
Summary:       Tesseract language files for Frisian (Western)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-fry
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Frisian (Western) language.

%files -n tesseract-langpack-fry
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/fry.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-gaelic_scots
Summary:       Tesseract language files for Gaelic (Scots)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-gaelic_scots
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Gaelic (Scots) language.

%files -n tesseract-ocr-traineddata-gaelic_scots
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/gla.*
%else
%package -n tesseract-langpack-gla
Summary:       Tesseract language files for Gaelic (Scots)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-gla
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Gaelic (Scots) language.

%files -n tesseract-langpack-gla
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/gla.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-armenian
Summary:       Tesseract language files for Armenian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-armenian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Armenian language.

%files -n tesseract-ocr-traineddata-armenian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/hye.*
%else
%package -n tesseract-langpack-hye
Summary:       Tesseract language files for Armenian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-hye
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Armenian language.

%files -n tesseract-langpack-hye
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/hye.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-japanese_vert
Summary:       Tesseract language files for Japanese (vertical)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-japanese_vert
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Japanese (vertical) language.

%files -n tesseract-ocr-traineddata-japanese_vert
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/jpn_vert.*
%else
%package -n tesseract-langpack-jpn-vert
Summary:       Tesseract language files for Japanese (vertical)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-jpn-vert
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Japanese (vertical) language.

%files -n tesseract-langpack-jpn-vert
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/jpn_vert.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-korean_vert
Summary:       Tesseract language files for Korean (vertical)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-korean_vert
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Korean (vertical) language.

%files -n tesseract-ocr-traineddata-korean_vert
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/kor_vert.*
%else
%package -n tesseract-langpack-kor-vert
Summary:       Tesseract language files for Korean (vertical)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-kor-vert
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Korean (vertical) language.

%files -n tesseract-langpack-kor-vert
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/kor_vert.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-kurmanji_latin
Summary:       Tesseract language files for Kurmanji (Latin)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-kurmanji_latin
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Kurmanji (Latin) language.

%files -n tesseract-ocr-traineddata-kurmanji_latin
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/kmr.*
%else
%package -n tesseract-langpack-kmr
Summary:       Tesseract language files for Kurmanji (Latin)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-kmr
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Kurmanji (Latin) language.

%files -n tesseract-langpack-kmr
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/kmr.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-luxembourgish
Summary:       Tesseract language files for Luxembourgish
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-luxembourgish
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Luxembourgish language.

%files -n tesseract-ocr-traineddata-luxembourgish
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ltz.*
%else
%package -n tesseract-langpack-ltz
Summary:       Tesseract language files for Luxembourgish
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-ltz
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Luxembourgish language.

%files -n tesseract-langpack-ltz
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ltz.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-mongolian
Summary:       Tesseract language files for Mongolian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-mongolian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Mongolian language.

%files -n tesseract-ocr-traineddata-mongolian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/mon.*
%else
%package -n tesseract-langpack-mon
Summary:       Tesseract language files for Mongolian
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-mon
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Mongolian language.

%files -n tesseract-langpack-mon
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/mon.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-maori
Summary:       Tesseract language files for Maori
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-maori
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Maori language.

%files -n tesseract-ocr-traineddata-maori
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/mri.*
%else
%package -n tesseract-langpack-mri
Summary:       Tesseract language files for Maori
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-mri
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Maori language.

%files -n tesseract-langpack-mri
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/mri.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-occitan
Summary:       Tesseract language files for Occitan (post 1500)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-occitan
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Occitan (post 1500) language.

%files -n tesseract-ocr-traineddata-occitan
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/oci.*
%else
%package -n tesseract-langpack-oci
Summary:       Tesseract language files for Occitan (post 1500)
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-oci
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Occitan (post 1500) language.

%files -n tesseract-langpack-oci
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/oci.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-quechua
Summary:       Tesseract language files for Quechua
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-quechua
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Quechua language.

%files -n tesseract-ocr-traineddata-quechua
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/que.*
%else
%package -n tesseract-langpack-que
Summary:       Tesseract language files for Quechua
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-que
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Quechua language.

%files -n tesseract-langpack-que
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/que.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-sindhi
Summary:       Tesseract language files for Sindhi
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-sindhi
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Sindhi language.

%files -n tesseract-ocr-traineddata-sindhi
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/snd.*
%else
%package -n tesseract-langpack-snd
Summary:       Tesseract language files for Sindhi
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-snd
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Sindhi language.

%files -n tesseract-langpack-snd
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/snd.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-sundanese
Summary:       Tesseract language files for Sundanese
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-sundanese
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Sundanese language.

%files -n tesseract-ocr-traineddata-sundanese
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/sun.*
%else
%package -n tesseract-langpack-sun
Summary:       Tesseract language files for Sundanese
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-sun
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Sundanese language.

%files -n tesseract-langpack-sun
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/sun.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-tatar
Summary:       Tesseract language files for Tatar
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-tatar
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Tatar language.

%files -n tesseract-ocr-traineddata-tatar
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/tat.*
%else
%package -n tesseract-langpack-tat
Summary:       Tesseract language files for Tatar
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-tat
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Tatar language.

%files -n tesseract-langpack-tat
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/tat.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-tonga
Summary:       Tesseract language files for Tonga
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-tonga
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Tonga language.

%files -n tesseract-ocr-traineddata-tonga
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ton.*
%else
%package -n tesseract-langpack-ton
Summary:       Tesseract language files for Tonga
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-ton
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Tonga language.

%files -n tesseract-langpack-ton
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/ton.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-yoruba
Summary:       Tesseract language files for Yoruba
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-ocr-traineddata-yoruba
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Yoruba language.

%files -n tesseract-ocr-traineddata-yoruba
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/yor.*
%else
%package -n tesseract-langpack-yor
Summary:       Tesseract language files for Yoruba
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99


%description -n tesseract-langpack-yor
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Yoruba language.

%files -n tesseract-langpack-yor
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/yor.*
%endif


%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-orientation_and_script_detection
Summary:       Tesseract language files for script and orientation
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-orientation_and_script_detection
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for identifying script and orientation.

%files -n tesseract-ocr-traineddata-orientation_and_script_detection
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/osd.*
%else
%package -n tesseract-langpack-osd
Summary:       Tesseract language files for script and orientation
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-langpack-osd
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for identifying script and orientation.

%files -n tesseract-langpack-osd
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/osd.*
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-arabic
Summary:       Tesseract data for Arabic script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-arabic
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Arabic script.

%files -n tesseract-ocr-traineddata-script-arabic
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Arabic.traineddata
%else
%package -n tesseract-script-arab
Summary:       Tesseract data for Arabic script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-arab
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Arabic script.

%files -n tesseract-script-arab
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Arabic.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-armenian
Summary:       Tesseract data for Armenian script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-armenian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Armenian script.

%files -n tesseract-ocr-traineddata-script-armenian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Armenian.traineddata
%else
%package -n tesseract-script-armn
Summary:       Tesseract data for Armenian script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-armn
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Armenian script.

%files -n tesseract-script-armn
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Armenian.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-bengali
Summary:       Tesseract data for Bengali script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-bengali
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Bengali script.

%files -n tesseract-ocr-traineddata-script-bengali
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Bengali.traineddata
%else
%package -n tesseract-script-beng
Summary:       Tesseract data for Bengali script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-beng
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Bengali script.

%files -n tesseract-script-beng
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Bengali.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-canadian_aboriginal
Summary:       Tesseract data for Canadian Aboriginal script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-canadian_aboriginal
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Canadian Aboriginal script.

%files -n tesseract-ocr-traineddata-script-canadian_aboriginal
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Canadian_Aboriginal.traineddata
%else
%package -n tesseract-script-cans
Summary:       Tesseract data for Canadian Aboriginal script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-cans
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Canadian Aboriginal script.

%files -n tesseract-script-cans
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Canadian_Aboriginal.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-cherokee
Summary:       Tesseract data for Cherokee script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-cherokee
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Cherokee script.

%files -n tesseract-ocr-traineddata-script-cherokee
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Cherokee.traineddata
%else
%package -n tesseract-script-cher
Summary:       Tesseract data for Cherokee script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-cher
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Cherokee script.

%files -n tesseract-script-cher
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Cherokee.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-cyrillic
Summary:       Tesseract data for Cyrillic script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-cyrillic
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Cyrillic script.

%files -n tesseract-ocr-traineddata-script-cyrillic
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Cyrillic.traineddata
%else
%package -n tesseract-script-cyrl
Summary:       Tesseract data for Cyrillic script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-cyrl
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Cyrillic script.

%files -n tesseract-script-cyrl
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Cyrillic.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-devanagari
Summary:       Tesseract data for Devanagari script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-devanagari
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Devanagari script.

%files -n tesseract-ocr-traineddata-script-devanagari
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Devanagari.traineddata
%else
%package -n tesseract-script-deva
Summary:       Tesseract data for Devanagari script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-deva
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Devanagari script.

%files -n tesseract-script-deva
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Devanagari.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-ethiopic
Summary:       Tesseract data for Ethiopic script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-ethiopic
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Ethiopic script.

%files -n tesseract-ocr-traineddata-script-ethiopic
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Ethiopic.traineddata
%else
%package -n tesseract-script-ethi
Summary:       Tesseract data for Ethiopic script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-ethi
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Ethiopic script.

%files -n tesseract-script-ethi
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Ethiopic.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-fraktur
Summary:       Tesseract data for Fraktur script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-fraktur
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Fraktur script.

%files -n tesseract-ocr-traineddata-script-fraktur
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Fraktur.traineddata
%else
%package -n tesseract-script-frak
Summary:       Tesseract data for Fraktur script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-frak
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Fraktur script.

%files -n tesseract-script-frak
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Fraktur.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-georgian
Summary:       Tesseract data for Georgian script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-georgian
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Georgian script.

%files -n tesseract-ocr-traineddata-script-georgian
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Georgian.traineddata
%else
%package -n tesseract-script-geor
Summary:       Tesseract data for Georgian script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-geor
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Georgian script.

%files -n tesseract-script-geor
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Georgian.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-greek
Summary:       Tesseract data for Greek script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-greek
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Greek script.

%files -n tesseract-ocr-traineddata-script-greek
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Greek.traineddata
%else
%package -n tesseract-script-grek
Summary:       Tesseract data for Greek script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-grek
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Greek script.

%files -n tesseract-script-grek
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Greek.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-gujarati
Summary:       Tesseract data for Gujarati script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-gujarati
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Gujarati script.

%files -n tesseract-ocr-traineddata-script-gujarati
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Gujarati.traineddata
%else
%package -n tesseract-script-gujr
Summary:       Tesseract data for Gujarati script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-gujr
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Gujarati script.

%files -n tesseract-script-gujr
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Gujarati.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-gurmukhi
Summary:       Tesseract data for Gurmukhi script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-gurmukhi
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Gurmukhi script.

%files -n tesseract-ocr-traineddata-script-gurmukhi
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Gurmukhi.traineddata
%else
%package -n tesseract-script-guru
Summary:       Tesseract data for Gurmukhi script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-guru
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Gurmukhi script.

%files -n tesseract-script-guru
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Gurmukhi.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-han_simplified
Summary:       Tesseract data for Han - Simplified script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-han_simplified
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Han - Simplified script.

%files -n tesseract-ocr-traineddata-script-han_simplified
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/HanS.traineddata
%else
%package -n tesseract-script-hans
Summary:       Tesseract data for Han - Simplified script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-hans
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Han - Simplified script.

%files -n tesseract-script-hans
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/HanS.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-han_simplified_vert
Summary:       Tesseract data for Han - Simplified (vertical) script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-han_simplified_vert
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Han - Simplified (vertical) script.

%files -n tesseract-ocr-traineddata-script-han_simplified_vert
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/HanS_vert.traineddata
%else
%package -n tesseract-script-hans-vert
Summary:       Tesseract data for Han - Simplified (vertical) script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-hans-vert
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Han - Simplified (vertical) script.

%files -n tesseract-script-hans-vert
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/HanS_vert.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-han_traditional
Summary:       Tesseract data for Han - Traditional script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-han_traditional
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Han - Traditional script.

%files -n tesseract-ocr-traineddata-script-han_traditional
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/HanT.traineddata
%else
%package -n tesseract-script-hant
Summary:       Tesseract data for Han - Traditional script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-hant
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Han - Traditional script.

%files -n tesseract-script-hant
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/HanT.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-han_traditional_vert
Summary:       Tesseract data for Han - Traditional (vertical) script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-han_traditional_vert
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Han - Traditional (vertical) script.

%files -n tesseract-ocr-traineddata-script-han_traditional_vert
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/HanT_vert.traineddata
%else
%package -n tesseract-script-hant-vert
Summary:       Tesseract data for Han - Traditional (vertical) script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-hant-vert
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Han - Traditional (vertical) script.

%files -n tesseract-script-hant-vert
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/HanT_vert.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-hangul
Summary:       Tesseract data for Hangul script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-hangul
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Hangul script.

%files -n tesseract-ocr-traineddata-script-hangul
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Hangul.traineddata
%else
%package -n tesseract-script-hang
Summary:       Tesseract data for Hangul script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-hang
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Hangul script.

%files -n tesseract-script-hang
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Hangul.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-hangul_vert
Summary:       Tesseract data for Hangul (vertical) script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-hangul_vert
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Hangul (vertical) script.

%files -n tesseract-ocr-traineddata-script-hangul_vert
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Hangul_vert.traineddata
%else
%package -n tesseract-script-hang-vert
Summary:       Tesseract data for Hangul (vertical) script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-hang-vert
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Hangul (vertical) script.

%files -n tesseract-script-hang-vert
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Hangul_vert.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-hebrew
Summary:       Tesseract data for Hebrew script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-hebrew
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Hebrew script.

%files -n tesseract-ocr-traineddata-script-hebrew
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Hebrew.traineddata
%else
%package -n tesseract-script-hebr
Summary:       Tesseract data for Hebrew script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-hebr
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Hebrew script.

%files -n tesseract-script-hebr
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Hebrew.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-japanese
Summary:       Tesseract data for Japanese script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-japanese
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Japanese script.

%files -n tesseract-ocr-traineddata-script-japanese
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Japanese.traineddata
%else
%package -n tesseract-script-jpan
Summary:       Tesseract data for Japanese script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-jpan
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Japanese script.

%files -n tesseract-script-jpan
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Japanese.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-japanese_vert
Summary:       Tesseract data for Japanese (vertical) script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-japanese_vert
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Japanese (vertical) script.

%files -n tesseract-ocr-traineddata-script-japanese_vert
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Japanese_vert.traineddata
%else
%package -n tesseract-script-jpan-vert
Summary:       Tesseract data for Japanese (vertical) script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-jpan-vert
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Japanese (vertical) script.

%files -n tesseract-script-jpan-vert
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Japanese_vert.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-kannada
Summary:       Tesseract data for Kannada script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-kannada
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Kannada script.

%files -n tesseract-ocr-traineddata-script-kannada
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Kannada.traineddata
%else
%package -n tesseract-script-knda
Summary:       Tesseract data for Kannada script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-knda
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Kannada script.

%files -n tesseract-script-knda
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Kannada.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-khmer
Summary:       Tesseract data for Khmer script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-khmer
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Khmer script.

%files -n tesseract-ocr-traineddata-script-khmer
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Khmer.traineddata
%else
%package -n tesseract-script-khmr
Summary:       Tesseract data for Khmer script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-khmr
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Khmer script.

%files -n tesseract-script-khmr
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Khmer.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-lao
Summary:       Tesseract data for Lao script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-lao
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Lao script.

%files -n tesseract-ocr-traineddata-script-lao
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Lao.traineddata
%else
%package -n tesseract-script-laoo
Summary:       Tesseract data for Lao script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-laoo
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Lao script.

%files -n tesseract-script-laoo
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Lao.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-latin
Summary:       Tesseract data for Latin script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-latin
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Latin script.

%files -n tesseract-ocr-traineddata-script-latin
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Latin.traineddata
%else
%package -n tesseract-script-latn
Summary:       Tesseract data for Latin script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-latn
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Latin script.

%files -n tesseract-script-latn
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Latin.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-malayalam
Summary:       Tesseract data for Malayalam script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-malayalam
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Malayalam script.

%files -n tesseract-ocr-traineddata-script-malayalam
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Malayalam.traineddata
%else
%package -n tesseract-script-mlym
Summary:       Tesseract data for Malayalam script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-mlym
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Malayalam script.

%files -n tesseract-script-mlym
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Malayalam.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-myanmar
Summary:       Tesseract data for Myanmar script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-myanmar
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Myanmar script.

%files -n tesseract-ocr-traineddata-script-myanmar
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Myanmar.traineddata
%else
%package -n tesseract-script-mymr
Summary:       Tesseract data for Myanmar script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-mymr
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Myanmar script.

%files -n tesseract-script-mymr
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Myanmar.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-oriya
Summary:       Tesseract data for Oriya (Odia) script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-oriya
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Oriya (Odia) script.

%files -n tesseract-ocr-traineddata-script-oriya
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Oriya.traineddata
%else
%package -n tesseract-script-orya
Summary:       Tesseract data for Oriya (Odia) script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-orya
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Oriya (Odia) script.

%files -n tesseract-script-orya
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Oriya.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-sinhala
Summary:       Tesseract data for Sinhala script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-sinhala
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Sinhala script.

%files -n tesseract-ocr-traineddata-script-sinhala
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Sinhala.traineddata
%else
%package -n tesseract-script-sinh
Summary:       Tesseract data for Sinhala script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-sinh
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Sinhala script.

%files -n tesseract-script-sinh
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Sinhala.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-syriac
Summary:       Tesseract data for Syriac script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-syriac
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Syriac script.

%files -n tesseract-ocr-traineddata-script-syriac
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Syriac.traineddata
%else
%package -n tesseract-script-syrc
Summary:       Tesseract data for Syriac script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-syrc
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Syriac script.

%files -n tesseract-script-syrc
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Syriac.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-tamil
Summary:       Tesseract data for Tamil script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-tamil
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Tamil script.

%files -n tesseract-ocr-traineddata-script-tamil
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Tamil.traineddata
%else
%package -n tesseract-script-taml
Summary:       Tesseract data for Tamil script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-taml
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Tamil script.

%files -n tesseract-script-taml
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Tamil.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-telugu
Summary:       Tesseract data for Telugu script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-telugu
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Telugu script.

%files -n tesseract-ocr-traineddata-script-telugu
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Telugu.traineddata
%else
%package -n tesseract-script-telu
Summary:       Tesseract data for Telugu script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-telu
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Telugu script.

%files -n tesseract-script-telu
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Telugu.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-thaana
Summary:       Tesseract data for Thaana script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-thaana
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Thaana script.

%files -n tesseract-ocr-traineddata-script-thaana
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Thaana.traineddata
%else
%package -n tesseract-script-thaa
Summary:       Tesseract data for Thaana script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-thaa
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Thaana script.

%files -n tesseract-script-thaa
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Thaana.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-thai
Summary:       Tesseract data for Thai script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-thai
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Thai script.

%files -n tesseract-ocr-traineddata-script-thai
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Thai.traineddata
%else
%package -n tesseract-script-thai
Summary:       Tesseract data for Thai script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-thai
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Thai script.

%files -n tesseract-script-thai
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Thai.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-tibetan
Summary:       Tesseract data for Tibetan script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-tibetan
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Tibetan script.

%files -n tesseract-ocr-traineddata-script-tibetan
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Tibetan.traineddata
%else
%package -n tesseract-script-tibt
Summary:       Tesseract data for Tibetan script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-tibt
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Tibetan script.

%files -n tesseract-script-tibt
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Tibetan.traineddata
%endif

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-vietnamese
Summary:       Tesseract data for Vietnamese script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-ocr-traineddata-script-vietnamese
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Vietnamese script.

%files -n tesseract-ocr-traineddata-script-vietnamese
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Vietnamese.traineddata
%else
%package -n tesseract-script-viet
Summary:       Tesseract data for Vietnamese script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata} >= 3.99

%description -n tesseract-script-viet
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in Vietnamese script.

%files -n tesseract-script-viet
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/Vietnamese.traineddata
%endif

%changelog
* Wed May 02 2018 Alexander Pozdnyakov <almipo@mail.ru> - 4.00~git30-1
- Compile
- URL: https://github.com/tesseract-ocr/tessdata_fast.git
- Commit: 7274cfad453d770f36b53ec5a2294ddd6d905703
- Date: 1524677480
* Sat Apr 07 2018 Alexander Pozdnyakov <almipo@mail.ru> - 4.00~git28-1
- Compile
- URL: https://github.com/tesseract-ocr/tessdata_fast.git
- Commit: f7a4c123725ea3fdbe4717d3ee376038717b5b06
- Date: 1521525456
* Thu Mar 15 2018 Alexander Pozdnyakov <almipo@mail.ru>  - 4.00~git26-1
- Compile
- URL: https://github.com/tesseract-ocr/tessdata_fast.git
- Branch: master
- Commit: f102e00ba31f4374c56cf3f16a67c3eb5f73058b
- Date: 1520711596
- git changelog:
-  f102e00 - Merge pull request #12 from stweil/script
-  9f875fb - Move trained data for scripts to new subdirectory
* Thu Mar 08 2018 Alexander Pozdnyakov <almipo@mail.ru>  - 4.00~git24-1
- Compile
- URL: https://github.com/tesseract-ocr/tessdata_fast.git
- Branch: master
- Commit: 0e00fe67ae71ead6155ea03ef13f1a9e77dd7093
- Date: 1519659145
- git changelog:
-  0e00fe6 - Merge pull request #10 from Shreeshrii/master
-  4e7c9ce - Add config files to fix auto PSM issue 1273
-  b2832c5 - Merge pull request #9 from Shreeshrii/patch-2
-  86db1f4 - Update README.md
-  c5aa3ac - Add sections, better formatting
-  8203e55 - Merge pull request #6 from Shreeshrii/patch-1
-  c526125 - Merge pull request #8 from Shreeshrii/Shreeshrii-
-   extraspaces_chi_tra
-  719cfd4 - Fix extra spaces in words for chi_tra
-  80d92b7 - Fix extra intra-word spaces by adding config file
-  066ce2d - Formatting Changes
-  cd93ef7 - update with info re jpn and Japanese
-  c9e5053 - Update README.md
-  139ff12 - Use legacy Orientation Script Detector (OSD) because that
-   is the only thing that currently works.
-  7588b03 - Merge pull request #2 from stweil/master
-  4888b72 - README: Improve description and add link to Tesseract wiki
-  f7218f8 - Merge pull request #1 from stweil/master
-  56fa301 - README: Add text from former COPYRIGHT and add links
-  7a05840 - Use the full Apache License text
-  25cb87d - add license info
-  923915d - Initial import to github (on behalf of Ray)
-  0415860 - Testing permissions
-  f7ec066 - Initial commit
