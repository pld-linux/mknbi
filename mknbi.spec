%include        /usr/lib/rpm/macros.perl
Summary:	Utility for creating network bootable images
Summary(pl):	Narz�dzia umo�liwiaj�ce tworzenie startowalnych przez sie� obraz�w
Summary(pt_BR):	Utilit�rio para cria��o de imagens para inicializa��o via rede
Name:		mknbi
Version:	1.4.4
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/etherboot/%{name}-%{version}.tar.gz
# Source0-md5:	5ddafef0a582cfb2b3cd30951662e6e2
Patch0:		%{name}-gcc4.patch
URL:		http://etherboot.sourceforge.net/
BuildRequires:	rpm-perlprov
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility that accompanies Etherboot for making tagged images from ROM
images, Linux kernels, FreeDOS and DOS bootable floppy images.

%description -l es
Paquete de soporte para permitir a un PC la inicalizaci�n con
etherboot.

%description -l pl
Narz�dzia korzystaj�ce z obraz�w Etherboot do tworzenia startowalnych
obraz�w z obraz�w ROM, kerneli Linuksa, obraz�w FreeDOS oraz DOS.

%description -l pt_BR
Pacote respons�vel por modificar imagens para permitir que PCs
inicializem via rede.

%prep
%setup -q
%patch0 -p1

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
%{_mandir}/man?/*
