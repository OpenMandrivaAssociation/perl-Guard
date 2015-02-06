%define upstream_name    Guard
%define upstream_version 1.022

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:    Safe cleanup blocks
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This module implements so-called "guards". A guard is something (usually an
object) that "guards" a resource, ensuring that it is cleaned up when
expected.

Specifically, this module supports two different types of guards: guard
objects, which execute a given code block when destroyed, and scoped
guards, which are tied to the scope exit.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*



%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.22.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Fri Jul 22 2011 Götz Waschk <waschk@mandriva.org> 1.22.0-1
+ Revision: 691050
- update to new version 1.022

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.21.0-2mdv2011.0
+ Revision: 555932
- rebuild for perl 5.12

* Fri Jul 24 2009 Jérôme Quelin <jquelin@mandriva.org> 1.21.0-1mdv2010.0
+ Revision: 399301
- update to 1.021
- fixed license field

  + Götz Waschk <waschk@mandriva.org>
    - remove the macro definition again

* Fri May 08 2009 Götz Waschk <waschk@mandriva.org> 1.20.0-1mdv2010.0
+ Revision: 373390
- add perl_convert_version macro
- new version
- use perl convert version macro

* Sun Dec 28 2008 Götz Waschk <waschk@mandriva.org> 1.0-1mdv2009.1
+ Revision: 320309
- import perl-Guard


* Sun Dec 28 2008 cpan2dist 1.0-1mdv
- initial mdv release, generated with cpan2dist

