%define upstream_name    GDGraph
%define upstream_version 1.44

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	Graph Plotting Module for Perl 5
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://search.cpan.org/CPAN/authors/id/M/MV/MVERB/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.440.0-4mdv2012.0
+ Revision: 765280
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.440.0-3
+ Revision: 763773
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.440.0-2
+ Revision: 667164
- mass rebuild

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.440.0-1mdv2010.1
+ Revision: 403186
- rebuild using %%perl_convert_version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.44-4mdv2009.0
+ Revision: 223765
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.44-3mdv2008.1
+ Revision: 180402
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 22 2007 Thierry Vignaud <tv@mandriva.org> 1.44-2mdv2008.0
+ Revision: 68987
- fix upgrade

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.44-1mdv2008.0
+ Revision: 20096
- 1.44


* Sun Apr 02 2006 Oden Eriksson <oeriksson@mandriva.com> 1.43-2mdk
- fix deps

* Sat Jun 04 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.43-1mdk 
- new release
- change name to match distribution
- make test
- rpmbuilupdate aware
- better URL

* Fri Oct 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.35-8mdk
- fix deps

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.35-7mdk
- rebuild for new perl
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.35-6mdk
- rebuild for new auto{prov,req}

* Fri Apr 25 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.35-5mdk
- fix buildrequires, thanks to Stefan van der Eijks robot

