%include        /usr/lib/rpm/macros.perl
Summary:	Utility for creating network bootable images
Summary(pl):	Narzêdzia umo¿liwiaj±ce tworzenie startowalnych przez sieæ obrazów
Summary(pt_BR):	Utilitário para criação de imagens para inicialização via rede
Name:		mknbi
Version:	1.4.3
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/etherboot/%{name}-%{version}.tar.gz
# Source0-md5:	1f5ae9a4431caa70e34d2116c7f3a465
URL:		http://etherboot.sourceforge.net/
BuildRequires:	perl-base >= 1:5.6
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

%build
%{__make} \
	CC="%{__cc}" \
	PREFIX=%{_prefix}

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
%doc *.html LOG README spec.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/di*
%attr(755,root,root) %{_libdir}/%{name}/mknbi
%attr(755,root,root) %{_libdir}/%{name}/nbitoelf
%{_libdir}/%{name}/*.bin
%{_libdir}/%{name}/*.pm
%{_libdir}/%{name}/first*
%{_libdir}/%{name}/menu
%{_libdir}/%{name}/rm*
%{_libdir}/%{name}/lua
%{_libdir}/%{name}/nfl
%attr(644,root,root) %{_mandir}/man?/*
