Summary:	Utility scripts for internationalizing various kinds of data files
Summary(pl):	Skrypty do internacjonalizacji róznych typów plików z danymi
Name:		intltool
Version:	0.22
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/intltool/%{name}-%{version}.tar.bz2
Patch0:		%{name}-m4.patch
URL:		http://www.gnome.org/
Provides:	xml-i18n-tools
BuildArch:	noarch
Requires:	patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	xml-i18n-tools

%description
Automatically extracts translatable strings from oaf, glade, bonobo
ui, nautilus theme and other files into the po files.

Automatically merges translations from po files back into .oaf files
(encoding to be 7-bit clean). I can also extend this merging mechanism
to support other types of files.

%description -l pl
Program automatycznie wyci±ga mo¿liwe do przet³umaczenia ci±gi znaków
z plików interfejsów oaf, glade, bonobo, tematów nautilusa i innych
plików do plików po.

Tak¿e automatycznie w³±cza t³umaczenia z plików po z powrotem do
plików oaf (koduj±c, by by³y 7-bitowe). Mechanizm ten mo¿e byæ
rozszerzony o inne rodzaje plików.

%prep
%setup -q
%patch0 -p1 

%build
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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/intltool
%attr(755,root,root) %{_datadir}/intltool/*
%{_aclocaldir}/*.m4
%{_mandir}/man8/*.8*
