#!/bin/bash

LANG="grc bul cat ces  dan deu  ell eng fin fra hun ind ita lav lit nld nor pol por ron rus slk slv spa srp swe tur ukr vie chi-sim chi-tra amh asm aze-cyrl bod bos ceb cym dzo fas gle guj hat iku jav kat kat-old kaz khm kir lao lat mar mya nep ori pan pus san sin srp-latn syr tgk tir uig urd uzb uzb-cyrl yid afr ara aze bel ben chr enm epo est eus frk frm glg heb hin hrv isl ita-old jpn kan kor mal mkd mlt msa spa-old sqi swa tam tel tha"
LANG_NEW="bre chi-sim-vert chi-tra-vert cos div fao fil fry gla hye jpn-vert kor-vert kmr ltz mon mri oci que snd sun tat ton yor"
SCRIPT="arab armn beng cans cher cyrl deva ethi frak geor grek gujr guru hans hans-vert hant hant-vert hang hang-vert hebr jpan jpan-vert knda khmr laoo latn mlym mymr orya sinh syrc taml telu thaa thai tibt viet"

CONTROL="tesseract-lang.spec"
rm -f ${CONTROL}
cp -f tesseract-lang.spec.in ${CONTROL}


# See https://github.com/tesseract-ocr/tessdata_best/pull/17
dependencies() {
  case "$1" in
    aze)
      DEPS="%if 0%{?suse_version} > 1130
Requires:      tesseract-ocr-traineddata-azerbaijani_cyrillic >= 3.99
%else
Requires:      tesseract-langpack-aze-cyrl >= 3.99
%endif"
      ;;
    uzb)
      DEPS="%if 0%{?suse_version} > 1130
Requires:      tesseract-ocr-traineddata-uzbek_cyrillic >= 3.99
%else
Requires:      tesseract-langpack-uzb-cyrl >= 3.99
%endif"
      ;;
    aze-cyrl)
      DEPS='%if 0%{?centos_version} == 700 || 0%{?scientificlinux_version} == 700 || 0%{?rhel_version} == 700
Requires:      tesseract-langpack-aze >= 3.99
%else
%if 0%{?suse_version} > 1130
Suggests:      tesseract-ocr-traineddata-azerbaijani >= 3.99
%else
Suggests:      tesseract-langpack-aze >= 3.99
%endif
%endif'
      ;;
    uzb-cyrl)
      DEPS='%if 0%{?centos_version} == 700 || 0%{?scientificlinux_version} == 700 || 0%{?rhel_version} == 700
Requires:      tesseract-langpack-uzb >= 3.99
%else
%if 0%{?suse_version} > 1130
Suggests:      tesseract-ocr-traineddata-uzbek >= 3.99
%else
Suggests:      tesseract-langpack-uzb >= 3.99
%endif
%endif'
      ;;
    srp-latn)
      DEPS="%if 0%{?suse_version} > 1130
Requires:      tesseract-ocr-traineddata-serbian >= 3.99
%else
Requires:      tesseract-langpack-srp >= 3.99
%endif"
      ;;
  esac
}


for i in ${LANG} ${LANG_NEW}; do
dependencies $i
j=$(cat lang.txt | grep "^${i}__" | awk -F '__' '{print $2}')
h=$(cat lang.txt | grep "^${i}__" | awk -F '__' '{print $3}')
cat >> ${CONTROL} << EOF

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-${h}
Summary:       Tesseract language files for ${j}
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata}
$(echo "${DEPS}")

%description -n tesseract-ocr-traineddata-${h}
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in ${j} language.

%files -n tesseract-ocr-traineddata-${h}
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/$(echo ${i} | sed 's/-/_/g').*
%else
%package -n tesseract-langpack-${i}
Summary:       Tesseract language files for ${j}
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata}
$(echo "${DEPS}")

%description -n tesseract-langpack-${i}
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in ${j} language.

%files -n tesseract-langpack-${i}
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/$(echo ${i} | sed 's/-/_/g').*
%endif

EOF
unset DEPS
done

cat >> ${CONTROL} << EOF

%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-orientation_and_script_detection
Summary:       Tesseract language files for script and orientation
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata}

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
%{_datadir}/%{tessdata}/4/tessdata/$(echo osd | sed 's/-/_/g').*
%else
%package -n tesseract-langpack-osd
Summary:       Tesseract language files for script and orientation
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata}

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
%{_datadir}/%{tessdata}/4/tessdata/$(echo osd | sed 's/-/_/g').*
%endif

EOF

for i in ${SCRIPT}; do
j=$(cat script.txt | grep "^${i}__" | awk -F '__' '{print $3}')
h=$(cat script.txt | grep "^${i}__" | awk -F '__' '{print $4}')
cat >> ${CONTROL} << EOF
%if 0%{?suse_version} > 1130
%package -n tesseract-ocr-traineddata-script-${h}
Summary:       Tesseract data for ${j} script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata}

%description -n tesseract-ocr-traineddata-script-${h}
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in ${j} script.

%files -n tesseract-ocr-traineddata-script-${h}
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/$(cat script.txt | grep "${i}__" | awk -F '__' '{print $2}')
%else
%package -n tesseract-script-${i}
Summary:       Tesseract data for ${j} script
Group:         Productivity/Graphics/Other
BuildArch:     noarch
Requires:      %{tessdata}

%description -n tesseract-script-${i}
Tesseract is an open source Optical Character Recognition (OCR)
Engine. It can be used directly, or (for programmers) using an API to
extract printed text from images. This package contains the data
needed for processing images in ${j} script.

%files -n tesseract-script-${i}
%defattr(-,root,root)
%dir %{_datadir}/%{tessdata}/
%dir %{_datadir}/%{tessdata}/4/
%dir %{_datadir}/%{tessdata}/4/tessdata/
%{_datadir}/%{tessdata}/4/tessdata/$(cat script.txt | grep "${i}__" | awk -F '__' '{print $2}')
%endif

EOF
done

cat changelog.in >> ${CONTROL}
