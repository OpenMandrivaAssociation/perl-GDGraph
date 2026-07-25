%define modname	GDGraph
%define modver	1.56

Summary:	Graph Plotting Module for Perl 5
Name:		perl-%{modname}
Version:	%{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/bestpractical/gdgraph
Source0:	https://cpan.metacpan.org/authors/id/B/BP/BPS/GDGraph-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	gd-devel
BuildRequires:	perl-devel
BuildRequires:	perl-GD >= 1.20
BuildRequires:	perl-GDTextUtil >= 0.83
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test)
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
