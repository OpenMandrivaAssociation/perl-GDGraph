%define modname	GDGraph
%define modver	1.44

Summary:	Graph Plotting Module for Perl 5
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	15
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MV/MVERB/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	gd-devel
BuildRequires:	perl-devel
BuildRequires:	perl-GD >= 1.20
BuildRequires:	perl-GDTextUtil >= 0.83
Provides:	perl-GD-Graph

%description
This is GDGraph, a package to generate charts, using Lincoln
Stein's GD.pm. See the documentation for some history and more
information.

%prep
%autosetup -p1 -n %{modname}-%{modver}

# perl path hack
#find . -type f | xargs perl -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make_build

%install
%make_install

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/GD/*
%doc %{_mandir}/man3/*

