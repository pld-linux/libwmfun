Summary:	Library that provides function textures for WindowMaker
Summary(pl):	Biblioteka dostarczaj±ca funkcje tekstur dla WindowMakera
Name:		libwmfun
Version:	0.0.4
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.windowmaker.org/pub/libs/%{name}-%{version}.tar.gz
BuildRequires:	XFree86-devel
BuildRequires:	WindowMaker-devel >= 0.63.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	libtool
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
Requires:	%{name} = %{version}

%description devel
Header files etc to develop libwmfun applications.

%description devel -l pl
Pliki nag³ówkowe i inne do libwmfun.

%package static
Summary:	Static libwmfun library
Summary(pl):	Biblioteka statyczna libwmfun
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libwmfun library.

%description static -l pl
Biblioteka statyczna libwmfun.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -I%{_includedir} -I/usr/include/freetype2"
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog AUTHORS NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz WMFun-demo.style
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
