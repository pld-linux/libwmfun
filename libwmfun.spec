Summary:	Library that provides function textures for WindowMaker
Summary(pl):	Biblioteka dostarczaj±ca funkcje tekstur dla WindowMakera
Name:		libwmfun
Version:	0.0.2
Release:	1
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Copyright:	GPL
Source:		ftp://ftp.windowmaker.org/pub/beta/srcs/%{name}-%{version}.tar.gz
BuildRequires:	XFree86-devel
BuildRequires:	WindowMaker-devel
Requires:	WindowMaker
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix 	/usr/X11R6

%description
libwmfun is a library that provides function textures for WindowMaker.
For more info see %{_defaultdocdir}/%{name}-%{version}/README after 
installing this package.

%description -l pl
libwmfun jest bibliotek± dla WindowMakera, która wyposa¿a go w funkcje
tworzenia tekstur. Wiêcej informacji znajdziesz po zainstalowaniu tego
pakietu w %{_defaultdocdir}/%{name}-%{version}/README.

%package devel
Summary:	Header files etc to develop libwmfun applications
Summary(pl):	Pliki nag³ówkowe i inne do libwmfun
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files etc to develop libwmfun applications.

%description -l pl devel
Pliki nag³ówkowe i inne do libwmfun.

%package static
Summary:	Static libwmfun library
Summary(pl):	Biblioteka statyczna libwmfun
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libwmfun library.

%description -l pl static
Biblioteka statyczna libwmfun.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include"; export CFLAGS
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf README ChangeLog AUTHORS NEWS

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog,AUTHORS,NEWS}.gz WMFun-demo.style
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%files static
%attr(644,root,root) %{_libdir}/lib*.a
