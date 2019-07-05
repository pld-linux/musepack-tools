#
# Conditional build:
%bcond_without  static_libs     # static library
#
%define		rev	475
Summary:	Musepack SV8 tools
Summary(pl.UTF-8):	Narzędzia Musepack SV8
Name:		musepack-tools
Version:	0.0.1.r%{rev}
Release:	4
License:	GPL v2+
Group:		Libraries
#Source0Download: https://www.musepack.net/index.php?pg=src
Source0:	http://files.musepack.net/source/musepack_src_r%{rev}.tar.gz
# Source0-md5:	754d67be67f713e54baf70fcfdb2817e
Patch0:		%{name}-libs.patch
URL:		http://www.musepack.net/
BuildRequires:	cmake >= 2.4
BuildRequires:	libcuefile-devel
BuildRequires:	libreplaygain-devel
Requires:	musepack-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Musepack SV8 (StreamVersion8) tools.

%description -l pl.UTF-8
Narzędzia Musepack SV8 (StreamVersion8).

%package -n musepack-libs
Summary:	Musepack SV8 library
Summary(pl.UTF-8):	Biblioteka Musepack SV8
Group:		Development/Libraries

%description -n musepack-libs
Musepack SV8 (StreamVersion8) library.

%description -n musepack-libs -l pl.UTF-8
Biblioteka Musepack SV8 (StreamVersion8).

%package -n musepack-devel
Summary:	Header files for Musepack SV8 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Musepack SV8
Group:		Development/Libraries
Requires:	musepack-libs = %{version}-%{release}

%description -n musepack-devel
Header files for Musepack SV8 library.

%description -n musepack-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Musepack SV8.

%package -n musepack-static
Summary:	Static version of Musepack SV8 library
Summary(pl.UTF-8):	Statyczna wersja biblioteki Musepack SV8
Group:		Development/Libraries
Requires:	musepack-devel = %{version}-%{release}

%description -n musepack-static
Static version of Musepack SV8 library.

%description -n musepack-static -l pl.UTF-8
Statyczna wersja biblioteki Musepack SV8.

%prep
%setup -q -n musepack_src_r%{rev}
%patch0 -p0

%build
%cmake

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n musepack-libs -p /sbin/ldconfig
%postun	-n musepack-libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mpcdec
%attr(755,root,root) %{_bindir}/mpcenc
%attr(755,root,root) %{_bindir}/mpc2sv8
%attr(755,root,root) %{_bindir}/mpcchap
%attr(755,root,root) %{_bindir}/mpccut
%attr(755,root,root) %{_bindir}/mpcgain
%attr(755,root,root) %{_bindir}/wavcmp

%files -n musepack-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpcdecsv8.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpcdecsv8.so.7

%files -n musepack-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpcdecsv8.so
%{_includedir}/mpc

%if %{with static_libs}
%files -n musepack-static
%defattr(644,root,root,755)
%{_libdir}/libmpcdecsv8.a
%endif
