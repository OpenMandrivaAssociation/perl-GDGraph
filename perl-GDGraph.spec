%define module  GDGraph
%define name	perl-%{module}
%define version 1.44
%define release %mkrel 4

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary:	Graph Plotting Module for Perl 5
License:	GPL or Artistic
Group:		Development/Perl
Source:	http://search.cpan.org/CPAN/authors/id/M/MV/MVERB/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-GD >= 1.20
BuildRequires:	perl-GDTextUtil >= 0.83
BuildRequires:	gd-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}
Provides:	perl-GD-Graph
Obsoletes:	perl-GD-Graph

%description
This is GDGraph, a package to generate charts, using Lincoln
Stein's GD.pm. See the documentation for some history and more
information.

%prep
%setup -q -n %{module}-%{version} 

# perl path hack
#find . -type f | xargs perl -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%install
rm -rf %{buildroot} 
%makeinstall_std

%check
make test

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/GD/*
%{_mandir}/*/*

