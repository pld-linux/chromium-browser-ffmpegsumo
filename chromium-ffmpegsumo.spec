# TODO
# - Document how to make the source for this beast from the chromium checkout
Summary:	Media playback library for chromium
Name:		chromium-ffmpegsumo
Version:	17.0.963.46
Release:	1
License:	LGPL v2+
Group:		Libraries
URL:		http://www.chromium.org/
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	05fc44a7be5bd2e4edc2ee1247c55f80
BuildRequires:	libvpx-devel
BuildRequires:	yasm
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A media playback library for chromium-browser. This is a fork of
ffmpeg.

Because Google doesn't understand open source community involvement.
It only supports unencumbered codecs.

%package devel
Summary:	Development headers and libraries for ffmpegsumo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development headers and libraries for ffmpegsumo.

%prep
%setup -q

%build
%{__make} \
%ifarch %{ix86}
	ARCH=ia32 \
%endif
%ifarch %{x8664}
	ARCH=x64 \
%endif
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags} %{rpmcppflags}" \
	libdir=%{_libdir} \
	includedir=%{_includedir}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
%ifarch %{ix86}
	ARCH=ia32 \
%endif
%ifarch %{x8664}
	ARCH=x64 \
%endif
	libdir=%{_libdir} \
	includedir=%{_includedir} \
	DESTDIR=$RPM_BUILD_ROOT

/sbin/ldconfig -n $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE COPYING.LGPLv2.1
%attr(755,root,root) %{_libdir}/libffmpegsumo.so.*.*.*
%ghost %{_libdir}/libffmpegsumo.so.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/ffmpegsumo
