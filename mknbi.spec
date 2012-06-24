%include        /usr/lib/rpm/macros.perl     
Summary:	Utility for creating network bootable images
Summary(pl):	Narz�dzia umo�liwiaj�ce tworzenie startowalnych przez sie� obraz�w
Summary(pt_BR):	Utilit�rio para cria��o de imagens para inicializa��o via rede.
Name:		mknbi
Version:	1.2
Release:	3
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

%description -l es
Paquete de soporte para permitir a un PC la inicalizaci�n
con etherboot.

%description -l pl
Narz�dzia korzystaj�ce z obraz�w Etherboot do tworzenia startowalnych
obraz�w z obraz�w ROM, kerneli Linuksa, obraz�w FreeDOS oraz DOS.

%description -l pt_BR
Pacote respons�vel por modificar imagens para permitir que PCs inicializem
via rede.

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
%doc *.gz *.html
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/di*
%attr(755,root,root) %{_libdir}/%{name}/mknbi
%{_libdir}/%{name}/*.pm
%{_libdir}/%{name}/first*
%{_libdir}/%{name}/menu
%{_libdir}/%{name}/rm*
%attr(644,root,root) %{_mandir}/man?/*
