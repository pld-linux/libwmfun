Summary:	Library that provides function textures for WindowMaker
Summary(pl):	Biblioteka dostarczaj±ca funkcje tekstur dla WindowMakera
Name:		libwmfun
Version:	0.0.1
Release:	2
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Copyright:	GPL
Source:		ftp://ftp.windowmaker.org/pub/beta/srcs/%{name}-%{version}.tar.gz
BuildPrereq:	XFree86-devel
BuildPrereq:	WindowMaker-devel
Requires:	WindowMaker
BuildRoot:   	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6

%description
libwmfun is a library that provides function textures for WindowMaker.
For more info see %{_defaultdocdir}/%{name}-%{version}/README after 
installing this package.

%description -l pl
libwmfun jest bibliotek± dla WindowMakera, która wyposa¿a go w funkcje
tworzenia tekstur. Wiêcej informacji znajdziesz po zainstalowaniu tego
pakietu w %{_defaultdocdir}/%{name}-%{version}/README.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--disable-static
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
%attr(755,root,root) %{_libdir}/lib*.so*
%{_libdir}/libwmfun.la

%changelog
* Tue Jul 6 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [0.1.1-2]
- rewritten for PLD use,
- based on spec file by Ryan Weaver <ryanw@infohwy.com>.
