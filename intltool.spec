%include	/usr/lib/rpm/macros.perl
Summary:	Utility scripts for internationalizing various kinds of data files
Summary(pl.UTF-8):	Skrypty do internacjonalizacji różnych typów plików z danymi
Name:		intltool
Version:	0.50.2
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	https://launchpad.net/intltool/trunk/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	23fbd879118253cb99aeac067da5f591
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	perl-XML-Parser
BuildRequires:	rpm-perlprov
Requires:	patch
# not detected automaticaly
Requires:	perl-XML-Parser
Obsoletes:	xml-i18n-tools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Automatically extracts translatable strings from oaf, glade, bonobo
ui, nautilus theme and other files into the po files.

Automatically merges translations from po files back into .oaf files
(encoding to be 7-bit clean). I can also extend this merging mechanism
to support other types of files.

%description -l pl.UTF-8
Program automatycznie wyciąga możliwe do przetłumaczenia ciągi znaków
z plików interfejsów oaf, glade, bonobo, tematów nautilusa i innych
plików do plików po.

Także automatycznie włącza tłumaczenia z plików po z powrotem do
plików oaf (kodując, by były 7-bitowe). Mechanizm ten może być
rozszerzony o inne rodzaje plików.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aclocaldir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO doc/I18N-HOWTO
%attr(755,root,root) %{_bindir}/intltool-extract
%attr(755,root,root) %{_bindir}/intltool-merge
%attr(755,root,root) %{_bindir}/intltool-prepare
%attr(755,root,root) %{_bindir}/intltool-update
%attr(755,root,root) %{_bindir}/intltoolize
%dir %{_datadir}/intltool
%attr(755,root,root) %{_datadir}/intltool/*
%{_aclocaldir}/intltool.m4
%{_mandir}/man8/intltool-extract.8*
%{_mandir}/man8/intltool-merge.8*
%{_mandir}/man8/intltool-prepare.8*
%{_mandir}/man8/intltool-update.8*
%{_mandir}/man8/intltoolize.8*
