%include        /usr/lib/rpm/macros.perl
Summary:	Utility for creating network bootable images
Summary(pl):	Narzêdzia umo¿liwiaj±ce tworzenie startowalnych przez sieæ obrazów
Summary(pt_BR):	Utilitário para criação de imagens para inicialização via rede.
Name:		mknbi
Version:	1.2
Release:	4
License:	GPL v2
Group:		Applications/System
Source0:	http://etherboot.sourceforge.net/%{name}-%{version}.tar.gz
Patch0:		%{name}-oformat.patch
URL:		http://etherboot.sourceforge.net/
BuildRequires:	perl >= 5.6
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility that accompanies Etherboot for making tagged images from ROM
images, Linux kernels, FreeDOS and DOS bootable floppy images.

%description -l es
Paquete de soporte para permitir a un PC la inicalización con
etherboot.

%description -l pl
Narzêdzia korzystaj±ce z obrazów Etherboot do tworzenia startowalnych
obrazów z obrazów ROM, kerneli Linuksa, obrazów FreeDOS oraz DOS.

%description -l pt_BR
Pacote responsável por modificar imagens para permitir que PCs
inicializem via rede.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html LOG README RELNOTES spec.txt 
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/di*
%attr(755,root,root) %{_libdir}/%{name}/mknbi
%{_libdir}/%{name}/*.pm
%{_libdir}/%{name}/first*
%{_libdir}/%{name}/menu
%{_libdir}/%{name}/rm*
%attr(644,root,root) %{_mandir}/man?/*
