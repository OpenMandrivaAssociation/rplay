%define name rplay
%define version 3.3.2
%define release %mkrel 6

%define libname %{_lib}%{name}
%define libnamedevel %{_lib}%{name}-devel

Summary: A flexible network audio system
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0: rplay-3.3.2-use-gnu.patch
License: GPL
Group: Sound
Url: http://rplay.doit.org/
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

%post
%_install_info %{name}.info
%_install_info librplay.info
%_install_info RPTP.info
%_install_info RPLAY.info

%preun
%_remove_install_info %{name}.info
%_remove_install_info librplay.info
%_remove_install_info RPTP.info
%_remove_install_info RPLAY.info

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog NEWS PORTING README README.linux TODO
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/*

%files -n %{libname}
%defattr(-,root,root)
%doc ChangeLog NEWS PORTING README README.linux TODO
%{_libdir}/*.so

%files -n %{libnamedevel}
%defattr(-,root,root)
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

