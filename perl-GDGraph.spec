%define upstream_name    GDGraph
%define upstream_version 1.44

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Graph Plotting Module for Perl 5
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://search.cpan.org/CPAN/authors/id/M/MV/MVERB/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-GD >= 1.20
BuildRequires:	perl-GDTextUtil >= 0.83
BuildRequires:	gd-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
Provides:	perl-GD-Graph
Obsoletes:	perl-GD-Graph

%description
This is GDGraph, a package to generate charts, using Lincoln
Stein's GD.pm. See the documentation for some history and more
information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
