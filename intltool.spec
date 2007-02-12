%include	/usr/lib/rpm/macros.perl
Summary:	Utility scripts for internationalizing various kinds of data files
Summary(pl.UTF-8):   Skrypty do internacjonalizacji róznych typów plików z danymi
Name:		intltool
Version:	0.29
%define		_snap	20040114
Release:	0.%{_snap}.1
License:	GPL
Group:		Development/Tools
#Source0:	http://ftp.gnome.org/pub/GNOME/sources/intltool/0.28/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}-%{_snap}.tar.bz2
# Source0-md5:	2da2421f474b8a7d4a07c09dadd74512
Patch0:		%{name}-am18.patch
URL:		http://www.gnome.org/
BuildRequires:	automake
Requires:	patch
# not detected automaticaly
Requires:	perl-XML-Parser
Provides:	xml-i18n-tools
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
%setup -q -n %{name}-%{version}
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
%doc AUTHORS ChangeLog NEWS README TODO doc/I18N-HOWTO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/intltool
%attr(755,root,root) %{_datadir}/intltool/*
%{_aclocaldir}/*.m4
%{_mandir}/man8/*.8*
