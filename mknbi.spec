%include        /usr/lib/rpm/macros.perl     
Summary:	Utility for creating network bootable images
Summary(pl):	Narzêdzia umo¿liwiaj±ce tworzenie startowalnych przez sieæ obrazów
Name:		mknbi
Version:	1.2
Release:	2
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://etherboot.sourceforge.net/%{name}-%{version}.tar.gz
Patch0:		%{name}-oformat.patch
URL:		http://etherboot.sourceforge.net/
BuildRequires:	perl >= 5.6
ExcludeArch:	alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility that accompanies Etherboot for making tagged images from ROM
images, Linux kernels, FreeDOS and DOS bootable floppy images.

%description -l pl
Narzêdzia korzystaj±ce z obrazów Etherboot do tworzenia startowalnych
obrazów z obrazów ROM, kerneli Linuksa, obrazów FreeDOS oraz DOS.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	PREFIX=%{_prefix} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BUILD_ROOT="$RPM_BUILD_ROOT" \
	PREFIX=%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf LOG README RELNOTES spec.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/di*
%attr(755,root,root) %{_libdir}/%{name}/mknbi
%{_libdir}/%{name}/*.pm
%{_libdir}/%{name}/first*
%{_libdir}/%{name}/menu
%{_libdir}/%{name}/rm*
%attr(644,root,root) %{_mandir}/man?/*
