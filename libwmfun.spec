Summary:	Library that provides function textures for WindowMaker
Summary(pl.UTF-8):	Biblioteka dostarczająca funkcje tekstur dla WindowMakera
Name:		libwmfun
Version:	0.0.4
Release:	4
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.windowmaker.org/pub/libs/%{name}-%{version}.tar.gz
# Source0-md5:	af1ad49bada4b8f0df9377a133f109c4
Patch0:		%{name}-fix.patch
BuildRequires:	WindowMaker-devel >= 0.63.1
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libwmfun is a library that provides function textures for WindowMaker.
For more info see %{_docdir}/%{name}-%{version}/README* after
installing this package.

%description -l pl.UTF-8
libwmfun jest biblioteką dla WindowMakera, która wyposaża go w funkcje
tworzenia tekstur. Więcej informacji można znaleźć po zainstalowaniu
tego pakietu w %{_docdir}/%{name}-%{version}/README*.

%package devel
Summary:	Header files etc to develop libwmfun applications
Summary(pl.UTF-8):	Pliki nagłówkowe i inne do libwmfun
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	WindowMaker-devel >= 0.63.1
Requires:	freetype-devel >= 2.0.0

%description devel
Header files etc to develop libwmfun applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe i inne do libwmfun.

%package static
Summary:	Static libwmfun library
Summary(pl.UTF-8):	Biblioteka statyczna libwmfun
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libwmfun library.

%description static -l pl.UTF-8
Biblioteka statyczna libwmfun.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -I/usr/include/freetype2"
%configure \
	--enable-static
%{__make} \
	LXLIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS NEWS WMFun-demo.style
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
