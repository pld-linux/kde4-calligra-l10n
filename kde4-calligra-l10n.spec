# NOTE
# - easy way to update all sources with new/old locales:
#   lynx -dump ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n | awk '/.tar.xz$/{printf("Source%d: %s\n", i++, $2)}' | tee out
#   and then ':r out' in vim and ./builder -a5 the spec
#   and ':%s#calligra-1.6.3#calligra-%{version}#g'
# - ISO 639-1 language codes maybe be looked up from http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
#

%define		orgname		calligra-l10n
%define		kdever		4.10.0

Summary:	Calligra suite - international support
Summary(pl.UTF-8):	Calligra - wsparcie dla wielu języków
Name:		kde4-calligra-l10n
Version:	2.8.7
Release:	2
License:	GPL
Group:		I18n
Source0:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-bs-%{version}.tar.xz
# Source0-md5:	d40b53e9266d0381fd6951daae0fbc69
Source1:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-ca-%{version}.tar.xz
# Source1-md5:	42dc9dd95b709ebfcb1f00cf69cf094f
Source2:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-cs-%{version}.tar.xz
# Source2-md5:	96232bbe66f1ee60a86bcf023670ced8
Source3:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-da-%{version}.tar.xz
# Source3-md5:	a8dcfa38b9c3e8ca0eb8fbc68a7b21b8
Source4:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-de-%{version}.tar.xz
# Source4-md5:	d17be021229e6ccc84582da889abedb8
Source5:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-el-%{version}.tar.xz
# Source5-md5:	aa141334488455d590b01fc6104e7ea8
Source6:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-es-%{version}.tar.xz
# Source6-md5:	743d02e730421d2caa802276f6917a6a
Source7:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-et-%{version}.tar.xz
# Source7-md5:	d275542a37bf6e696123ff52e2c70345
Source8:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-fi-%{version}.tar.xz
# Source8-md5:	a135128f4afe4125f4e82c166fa9b17d
Source9:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-fr-%{version}.tar.xz
# Source9-md5:	de076e3e38ccc698288420dc719c9357
Source10:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-gl-%{version}.tar.xz
# Source10-md5:	d8139eb50b743144852e328278d39164
Source11:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-hu-%{version}.tar.xz
# Source11-md5:	46e06d980692bdd86f114d16ff71187d
Source12:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-it-%{version}.tar.xz
# Source12-md5:	e1ec962ac680cd9dce72e48dd9c754e6
Source13:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-kk-%{version}.tar.xz
# Source13-md5:	719acbca3e86c5ddc88ab0232d3e973b
Source14:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-nb-%{version}.tar.xz
# Source14-md5:	2400e204e613a9710a09d57a08eb2631
Source15:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-nds-%{version}.tar.xz
# Source15-md5:	a8d94ba46a914a9b6d63fa71a89ecf8a
Source16:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-nl-%{version}.tar.xz
# Source16-md5:	dfe2b5d1ee93ad60c361cfd01b4f2057
Source17:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-pl-%{version}.tar.xz
# Source17-md5:	ca3546b5449ac81334b9228c88f4172f
Source18:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-pt-%{version}.tar.xz
# Source18-md5:	5c5f0499d26545e26cdd9a8aa21a5928
Source19:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-pt_BR-%{version}.tar.xz
# Source19-md5:	70e9b04b66aa74e836a23c1c606d5280
Source20:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-ru-%{version}.tar.xz
# Source20-md5:	4cb22f814b8c00040246b7d3e16fea29
Source21:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-sk-%{version}.tar.xz
# Source21-md5:	0a50e809722ad150dba660bd43b75db7
Source22:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-sv-%{version}.tar.xz
# Source22-md5:	10e5faad6c7ad0b9084978840cc75603
Source23:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-uk-%{version}.tar.xz
# Source23-md5:	09011b1829c1eafddb1987080b1e627d
Source24:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-zh_CN-%{version}.tar.xz
# Source24-md5:	ed20dba78078a127feb206afaa0490cc
Source25:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-zh_TW-%{version}.tar.xz
# Source25-md5:	20357723a567fddf2fcf12dd399b88a8
Source26:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-ca@valencia-%{version}.tar.xz
# Source26-md5:	867aa2c3351bd67acecad6a0b4642a4c
Source27:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-ja-%{version}.tar.xz
# Source27-md5:	50a3272af6c6a62bf4f5978832b96181
Source28:	ftp://ftp.kde.org/pub/kde/stable/calligra-%{version}/calligra-l10n/%{orgname}-en_GB-%{version}.tar.xz
# Source28-md5:	7b02333d666f7edfcb00ebf5a34a671b
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
%setup -q -c -T %(seq -f '-a %g' 0 28 | xargs)

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
