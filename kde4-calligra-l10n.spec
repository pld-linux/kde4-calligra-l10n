# NOTE
# - easy way to update all sources with new/old locales:
#   lynx -dump https://download.kde.org/Attic/calligra-%{version}/calligra-l10n | awk '/.tar.xz$/{printf("Source%d: %s\n", i++, $2)}' | tee out
#   and then ':r out' in vim and ./builder -a5 the spec
#   and ':%s#calligra-1.6.3#calligra-%{version}#g'
# - ISO 639-1 language codes maybe be looked up from http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
#

%define		orgname		calligra-l10n
%define		kdever		4.10.0

Summary:	Calligra suite - international support
Summary(pl.UTF-8):	Calligra - wsparcie dla wielu języków
Name:		kde4-calligra-l10n
Version:	2.9.11
Release:	0.1
License:	GPL
Group:		I18n
Source0: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-bs-%{version}.tar.xz
# Source0-md5:	f87a80d5f9ef18e5bce4f9b546ac54f2
Source1: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-ca-%{version}.tar.xz
# Source1-md5:	a2d73c39ee84ee2f69842509da092f0b
Source2: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-cs-%{version}.tar.xz
# Source2-md5:	e644cdb5e8694b9dfd1937877d461710
Source3: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-da-%{version}.tar.xz
# Source3-md5:	02a50ae334a195845fbd9b58730c8a50
Source4: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-de-%{version}.tar.xz
# Source4-md5:	99f7c7354f593147a384850b4f365a8b
Source5: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-el-%{version}.tar.xz
# Source5-md5:	6d54da69aa0d5b79f37edae7b8edb726
Source6: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-en_GB-%{version}.tar.xz
# Source6-md5:	f3e020a8daefa5f26485e01ffa8a4520
Source7: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-es-%{version}.tar.xz
# Source7-md5:	83760e705c0dfeaa2f4f098305da3f79
Source8: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-et-%{version}.tar.xz
# Source8-md5:	20a2d9f1ceb5e1b31faee72bf5fb4d0f
Source9: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-fi-%{version}.tar.xz
# Source9-md5:	ef1fd56d9871a5235d66083bb5132968
Source10: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-fr-%{version}.tar.xz
# Source10-md5:	3042e50532305db27624be2cc4d78394
Source11: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-gl-%{version}.tar.xz
# Source11-md5:	f7f539b7a32710502176b0a157aa5057
Source12: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-hu-%{version}.tar.xz
# Source12-md5:	90ac8f87fb1f76692e19532d9e7246e6
Source13: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-it-%{version}.tar.xz
# Source13-md5:	602972907def3acfd0023fd3019a1512
Source14: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-ja-%{version}.tar.xz
# Source14-md5:	5755ce1e4d163fc07de6b4bb2abcb6e2
Source15: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-kk-%{version}.tar.xz
# Source15-md5:	89080fa5d2448f84b6c406a5c206261c
Source16: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-nb-%{version}.tar.xz
# Source16-md5:	6af6cfbae29929718e37b73f4e574b8a
Source17: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-nl-%{version}.tar.xz
# Source17-md5:	7c07d0a8e4722286cd75bd669e141ed2
Source18: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-pl-%{version}.tar.xz
# Source18-md5:	3598ca1fdcadbee772bbfbfd2e61836b
Source19: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-pt-%{version}.tar.xz
# Source19-md5:	8029eee21ad33758a9b705f1c987d83b
Source20: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-pt_BR-%{version}.tar.xz
# Source20-md5:	cf743c38b3bc4d886f3fa709df8aabb9
Source21: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-ru-%{version}.tar.xz
# Source21-md5:	23be50c6e72729526fb649a697215e69
Source22: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-sk-%{version}.tar.xz
# Source22-md5:	306843e947b62056dca378c5898fd68c
Source23: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-sv-%{version}.tar.xz
# Source23-md5:	5058af16b0a81e1087bd2a9226850ce8
Source24: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-tr-%{version}.tar.xz
# Source24-md5:	f6808a1b4f35b57b50a2050ce051fe42
Source25: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-uk-%{version}.tar.xz
# Source25-md5:	830cb6222edb3ad805ec21a9466f4e81
Source26: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-zh_CN-%{version}.tar.xz
# Source26-md5:	c3b5b8c568920fdfe9719b5da524a101
Source27: https://download.kde.org/Attic/calligra-%{version}/calligra-l10n/calligra-l10n-zh_TW-%{version}.tar.xz
# Source27-md5:	1d6acdd91f14331b465c2365272d0a2d
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.8.0
BuildRequires:	docbook-dtd42-xml
BuildRequires:	gettext-tools
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	libxml2-progs
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-calligra-l10n-Slovenian < %{version}-%{release}
Obsoletes:	kde4-calligra-l10n-Turkish < %{version}-%{release}
Obsoletes:	kde4-koffice-l10n
Obsoletes:	kde4-koffice-l10n-Frisian
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calligra suite - international support.

%description -l pl.UTF-8
Calligra - wsparcie dla wielu języków.

%package Bosnian
Summary:	Calligra suite - Bosnian language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka bośniackiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}

%description Bosnian
Calligra suite - Bosnian language support.

%description Bosnian -l pl.UTF-8
Calligra - wsparcie dla języka bośniackiego.

%package Catalan
Summary:	Calligra suite - Catalan language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka katalońskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Catalan

%description Catalan
Calligra suite - Catalan language support.

%description Catalan -l pl.UTF-8
Calligra - wsparcie dla języka katalońskiego.

%package Catalan_Valencian
Summary:	Calligra suite - Catalan Valencian language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka walenckiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}

%description Catalan_Valencian
Calligra suite - Catalan Valencian language support.

%description Catalan_Valencian -l pl.UTF-8
Calligra - wsparcie dla języka walenckiego.

%package Czech
Summary:	Calligra suite - Czech language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka czeskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}

%description Czech
Calligra suite - Czech language support.

%description Czech -l pl.UTF-8
Calligra - wsparcie dla języka czeskiego.

%package Danish
Summary:	Calligra suite - Danish language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka duńskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Danish

%description Danish
Calligra suite - Danish language support.

%description Danish -l pl.UTF-8
Calligra - wsparcie dla języka duńskiego.

%package Galician
Summary:	Calligra suite - Galician language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka galicyjskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Galician

%description Galician
Calligra suite - Galician language support.

%description Galician -l pl.UTF-8
Calligra - wsparcie dla języka galicyjskiego

%package German
Summary:	Calligra suite - German language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka niemieckiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-German

%description German
Calligra suite - German language support.

%description German -l pl.UTF-8
Calligra - wsparcie dla języka niemieckiego.

%package Greek
Summary:	Calligra suite - Greek language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka greckiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Greek

%description Greek
Calligra suite - Greek language support.

%description Greek -l pl.UTF-8
Calligra - wsparcie dla języka greckiego.

%package Kazakh
Summary:	Calligra suite - Kazakh language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka kazachskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Kazakh

%description Kazakh
Calligra suite - Kazakh language support.

%description Kazakh -l pl.UTF-8
Calligra - wsparcie dla języka kazachskiego.

%package English_UK
Summary:	Calligra suite - Calligra suite - English (UK) language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka angielskiego (odmiany brytyjskiej)
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-English_UK

%description English_UK
Calligra suite - English (UK) language support.

%description English_UK -l pl.UTF-8
Calligra - wsparcie dla języka angielskiego (odmiany brytyjskiej).

%package Spanish
Summary:	Calligra suite - Spanish language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka hiszpańskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Spanish

%description Spanish
Calligra suite - Spanish language support.

%description Spanish -l pl.UTF-8
Calligra - wsparcie dla języka hiszpańskiego.

%package Estonian
Summary:	Calligra suite - Estonian language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka estońskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Estonian

%description Estonian
Calligra suite - Estonian language support.

%description Estonian -l pl.UTF-8
Calligra - wsparcie dla języka estońskiego.

%package French
Summary:	Calligra suite - French language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka francuskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-French

%description French
Calligra suite - French language support.

%description French -l pl.UTF-8
Calligra - wsparcie dla języka francuskiego.

%package Finnish
Summary:	Calligra suite - Finnish language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka fińskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Finnish

%description Finnish
Calligra suite - Finnish language support.

%description Finnish -l pl.UTF-8
Calligra - wsparcie dla języka fińskiego.

%package Italian
Summary:	Calligra suite - Italian language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka włoskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Italian

%description Italian
Calligra suite - Italian language support.

%description Italian -l pl.UTF-8
Calligra - wsparcie dla języka włoskiego.

%package Japanese
Summary:	Calligra suite - Japanese language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka japońskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Japanese

%description Japanese
Calligra suite - Japanese language support.

%description Japanese -l pl.UTF-8
Calligra - wsparcie dla języka japońskiego.

%package Hungarian
Summary:	Calligra suite - Hungarian language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka węgierskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}

%description Hungarian
Calligra suite - Hungarian language support.

%description Hungarian -l pl.UTF-8
Calligra - wsparcie dla języka węgierskiego.

%package Low_Saxon
Summary:	Calligra suite - Low Saxon language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka dolnosaksońskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Low_Saxon

%description Low_Saxon
Calligra suite - Low Saxon language support.

%description Low_Saxon -l pl.UTF-8
Calligra - wsparcie dla języka dolnosaksońskiego.

%package Norwegian_Bokmaal
Summary:	Calligra suite - Norwegian (Bokmaal) language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka norweskiego (odmiany bokmaal)
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Norwegian_Bokmaal

%description Norwegian_Bokmaal
Calligra suite - Norwegian (Bokmaal) language support.

%description Norwegian_Bokmaal -l pl.UTF-8
Calligra - wsparcie dla języka norweskiego (odmiany bokmaal).

%package Dutch
Summary:	Calligra suite - Dutch language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka holenderskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Dutch

%description Dutch
Calligra suite - Dutch language support.

%description Dutch -l pl.UTF-8
Calligra - wsparcie dla języka holenderskiego.

%package Polish
Summary:	Calligra suite - Polish language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka polskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Polish

%description Polish
Calligra suite - Polish language support.

%description Polish -l pl.UTF-8
Calligra - wsparcie dla języka polskiego.

%package Portuguese
Summary:	Calligra suite - Portuguese language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka portugalskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Portuguese

%description Portuguese
Calligra suite - Portuguese language support.

%description Portuguese -l pl.UTF-8
Calligra - wsparcie dla języka portugalskiego.

%package Brazil_Portuguese
Summary:	Calligra suite - Portuguese (Brazil) language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka portugalskiego (odmiany brazylijskiej)
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Brazil_Portuguese

%description Brazil_Portuguese
Calligra suite - Portuguese (Brazil) language support.

%description Brazil_Portuguese -l pl.UTF-8
Calligra - wsparcie dla języka portugalskiego (odmiany brazylijskiej).

%package Slovak
Summary:	Calligra suite - Slovak language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka słowackiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}

%description Slovak
Calligra suite - Slovak language support.

%description Slovak -l pl.UTF-8
Calligra - wsparcie dla języka słowackiego.

%package Slovenian
Summary:	Calligra suite - Slovenian language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka słoweńskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}

%description Slovenian
Calligra suite - Slovenian language support.

%description Slovenian -l pl.UTF-8
Calligra - wsparcie dla języka słoweńskiego.

%package Swedish
Summary:	Calligra suite - Swedish language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka szwedzkiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Swedish

%description Swedish
Calligra suite - Swedish language support.

%description Swedish -l pl.UTF-8
Calligra - wsparcie dla języka szwedzkiego.

%package Turkish
Summary:	Calligra suite - Turkish language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka tureckiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}

%description Turkish
Calligra suite - Turkish language support.

%description Turkish -l pl.UTF-8
Calligra - wsparcie dla języka tureckiego.

%package Russian
Summary:	Calligra suite - Russian language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka rosyjskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}

%description Russian
Calligra suite - Russian language support.

%description Russian -l pl.UTF-8
Calligra - wsparcie dla języka rosyjskiego.

%package Turkish
Summary:	Calligra suite - Turkish language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka tureckiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Turkish

%description Turkish
Calligra suite - Turkish language support.

%description Turkish -l pl.UTF-8
Calligra - wsparcie dla języka tureckiego.

%package Ukrainian
Summary:	Calligra suite - Ukrainian language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka ukraińskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Ukrainian

%description Ukrainian
Calligra suite - Ukrainian language support.

%description Ukrainian -l pl.UTF-8
Calligra - wsparcie dla języka ukraińskiego.

%package Walloon
Summary:	Calligra suite - Walloon language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka walońskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Walloon

%description Walloon
Calligra suite - Walloon language support.

%description Walloon -l pl.UTF-8
Calligra - wsparcie dla języka walońskiego.

%package Simplified_Chinese
Summary:	Calligra suite - simplified Chinese language support
Summary(pl.UTF-8):	Calligra - wsparcie dla uproszczonego języka chińskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Simplified_Chinese

%description Simplified_Chinese
Calligra suite - simplified Chinese language support.

%description Simplified_Chinese -l pl.UTF-8
Calligra - wsparcie dla uproszczonego języka chińskiego.

%package Chinese
Summary:	Calligra suite - Chinese language support
Summary(pl.UTF-8):	Calligra - wsparcie dla języka chińskiego
Group:		I18n
Requires:	kde4-calligra-common = %{version}
Obsoletes:	kde4-koffice-l10n-Chinese

%description Chinese
Calligra suite - Chinese language support.

%description Chinese -l pl.UTF-8
Calligra - wsparcie dla języka chińskiego.

%prep
%setup -q -c -T %(seq -f '-a %g' 0 27 | xargs)

%build
for dir in calligra-l10n-*-%{version}; do
	cd $dir
	install -d build
	cd build
	%cmake \
		../
	%{__make}
	cd ../..
done

%install
if [ ! -f installed.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	rm -rf $RPM_BUILD_ROOT

	for dir in %{orgname}-*-%{version}; do
		%{__make} -C $dir/build install \
			DESTDIR=$RPM_BUILD_ROOT
	done
	touch installed.stamp
fi

rm -f *.lang

FindLang() {
	#    $1 - short language name
	local lang="$1"

	# share/doc/kde/HTML/(%%lang)
	if [ -d "$RPM_BUILD_ROOT%{_kdedocdir}/$lang" ]; then
		echo "%lang($lang) %{_kdedocdir}/$lang"
	fi

	# share/locale/(%%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/locale/$lang" ]; then
		echo "%lang($lang) %{_datadir}/locale/$lang/LC_MESSAGES/*.mo"
	fi

	# share/apps/calligra/autocorrect/*.xml
	if [ -f $RPM_BUILD_ROOT%{_datadir}/apps/calligra/autocorrect/$lang.xml ]; then
		echo "%lang($lang) %{_datadir}/apps/calligra/autocorrect/$lang.xml"
	fi
	if [ -f $RPM_BUILD_ROOT%{_datadir}/apps/calligra/autocorrect/${lang}_*.xml ]; then
		echo "%lang($lang) %{_datadir}/apps/calligra/autocorrect/${lang}_*.xml"
	fi

	touch $lang.ok
}

FindLang bs > Bosnian.lang
FindLang ca > Catalan.lang
FindLang ca@valencia > Catalan_Valencian.lang
FindLang cs > Czech.lang
FindLang da > Danish.lang
FindLang de > German.lang
FindLang el > Greek.lang
FindLang en_GB > English_UK.lang
FindLang es > Spanish.lang
FindLang et > Estonian.lang
FindLang fi > Finnish.lang
FindLang fr > French.lang
FindLang gl > Galician.lang
FindLang hu > Hungarian.lang
FindLang it > Italian.lang
FindLang ja > Japanese.lang
FindLang kk > Kazakh.lang
FindLang nb > Norwegian_Bokmaal.lang
FindLang nds > Low_Saxon.lang
FindLang nl > Dutch.lang
FindLang pl > Polish.lang
FindLang pt > Portuguese.lang
FindLang pt_BR > Brazil_Portuguese.lang
FindLang ru > Russian.lang
FindLang sk > Slovak.lang
FindLang sv > Swedish.lang
FindLang uk > Ukrainian.lang
FindLang zh_CN > Simplified_Chinese.lang
FindLang zh_TW > Chinese.lang

check_installed_languages() {
	err=0
	# we ignore dialects (currently sr@latin is the only case)
	for a in $(ls -1d %{orgname}-*-%{version} | %{__sed} '/@/d'); do
		l=${a#%{orgname}-}
		l=${l%%-%{version}}
		if [ ! -f $l.ok ]; then
			echo >&2 "language $l not processed"
			err=1
		fi
	done
	if [ "$err" = 1 ]; then
		exit 1
	fi
}
check_installed_languages

%clean
check_installed_files() {
	for a in *.lang; do
		lang=${a%%.lang}

		rpmfile=%{_rpmdir}/%{name}-$lang-%{version}-%{release}.%{_target_cpu}.rpm
		if [ ! -f $rpmfile ]; then
			echo >&2 "Missing %%files section for $lang"
			exit 1
		fi
	done
}
check_installed_files
%{!?debug:rm -rf $RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)

%files -f Bosnian.lang Bosnian
%defattr(644,root,root,755)

%files -f Catalan.lang Catalan
%defattr(644,root,root,755)

%files -f Catalan_Valencian.lang Catalan_Valencian
%defattr(644,root,root,755)

%files -f Czech.lang Czech
%defattr(644,root,root,755)

%files -f Danish.lang Danish
%defattr(644,root,root,755)

%files -f German.lang German
%defattr(644,root,root,755)

%files -f Greek.lang Greek
%defattr(644,root,root,755)

%files -f English_UK.lang English_UK
%defattr(644,root,root,755)

%files -f Spanish.lang Spanish
%defattr(644,root,root,755)

%files -f Estonian.lang Estonian
%defattr(644,root,root,755)

%files -f Finnish.lang Finnish
%defattr(644,root,root,755)

%files -f French.lang French
%defattr(644,root,root,755)

%files -f Galician.lang Galician
%defattr(644,root,root,755)

%files -f Hungarian.lang Hungarian
%defattr(644,root,root,755)

%files -f Italian.lang Italian
%defattr(644,root,root,755)

%files -f Japanese.lang Japanese
%defattr(644,root,root,755)

%files -f Kazakh.lang Kazakh
%defattr(644,root,root,755)

%files -f Norwegian_Bokmaal.lang Norwegian_Bokmaal
%defattr(644,root,root,755)

%files -f Low_Saxon.lang Low_Saxon
%defattr(644,root,root,755)

%files -f Dutch.lang Dutch
%defattr(644,root,root,755)

%files -f Polish.lang Polish
%defattr(644,root,root,755)

%files -f Portuguese.lang Portuguese
%defattr(644,root,root,755)

%files -f Brazil_Portuguese.lang Brazil_Portuguese
%defattr(644,root,root,755)

%files -f Russian.lang Russian
%defattr(644,root,root,755)

%files -f Slovak.lang Slovak
%defattr(644,root,root,755)

#%files -f Slovenian.lang Slovenian
#%defattr(644,root,root,755)

%files -f Swedish.lang Swedish
%defattr(644,root,root,755)

#%files -f Turkish.lang Turkish
#%defattr(644,root,root,755)

%files -f Ukrainian.lang Ukrainian
%defattr(644,root,root,755)

%files -f Simplified_Chinese.lang Simplified_Chinese
%defattr(644,root,root,755)

%files -f Chinese.lang Chinese
%defattr(644,root,root,755)
