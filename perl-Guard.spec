
%define realname   Guard
%define ver    1.02
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %perl_convert_version %ver
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Safe cleanup blocks
Source:     http://www.cpan.org/modules/by-module//%{realname}-%{ver}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel




%description
This module implements so-called "guards". A guard is something (usually an
object) that "guards" a resource, ensuring that it is cleaned up when
expected.

Specifically, this module supports two different types of guards: guard
objects, which execute a given code block when destroyed, and scoped
guards, which are tied to the scope exit.



%prep
%setup -q -n %{realname}-%{ver} 

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


