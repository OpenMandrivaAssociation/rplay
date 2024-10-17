%define libname %{_lib}%{name}
%define libnamedevel %{_lib}%{name}-devel

Summary: A flexible network audio system
Name:    rplay
Version: 3.3.2
Release: 8
Source0: %{name}-%{version}.tar.bz2
Patch0: rplay-3.3.2-use-gnu.patch
License: GPL
Group: Sound
Url: https://rplay.doit.org/
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires(pre): rpm-helper
Requires(preun): rpm-helper

%description
rplay is a flexible network audio system that allows sounds to be
played to and from local and remote Unix systems.  Sounds can be
played with or without sending audio data over the network using
either UDP or TCP.  rplay audio servers can be configured to share
sound files with each other.

Support for rplay is included in several applications.  These include
xpilot, xlockmore, xboing, fvwm, and ctwm.

%package -n %{libname}
Group: Sound
Summary: The rplay libraries

%description -n %{libname}
rplay is a flexible network audio system that allows sounds to be
played to and from local and remote Unix systems.  Sounds can be
played with or without sending audio data over the network using
either UDP or TCP.  rplay audio servers can be configured to share
sound files with each other.

Support for rplay is included in several applications.  These include
xpilot, xlockmore, xboing, fvwm, and ctwm.

%package -n %{libnamedevel}
Group: Sound
Summary: The rplay libraries
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{libnamedevel}
rplay is a flexible network audio system that allows sounds to be
played to and from local and remote Unix systems.  Sounds can be
played with or without sending audio data over the network using
either UDP or TCP.  rplay audio servers can be configured to share
sound files with each other.

Support for rplay is included in several applications.  These include
xpilot, xlockmore, xboing, fvwm, and ctwm.

%prep
%setup -q
%patch0 -p0 -b .usegnu

%build
%configure

%make

%install
%makeinstall


%files
%doc ChangeLog NEWS PORTING README README.linux TODO
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/*

%files -n %{libname}
%doc ChangeLog NEWS PORTING README README.linux TODO
%{_libdir}/*.so

%files -n %{libnamedevel}
%doc ChangeLog NEWS PORTING README README.linux TODO
%{_includedir}/*
%{_libdir}/*.a



%changelog
* Tue Sep 15 2009 Thierry Vignaud <tvignaud@mandriva.com> 3.3.2-6mdv2010.0
+ Revision: 442757
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.3.2-5mdv2009.0
+ Revision: 260318
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.3.2-4mdv2009.0
+ Revision: 251470
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 3.3.2-2mdv2008.1
+ Revision: 140747
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Aug 13 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/13/06 21:36:07 (55853)
- rebuild

* Sun Aug 13 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/13/06 21:34:25 (55852)
Import rplay

* Tue Nov 15 2005 Olivier Thauvin <nanardon@mandriva.org> 3.3.2-1mdk
- Initial contrib

