%define upstream_name    KiokuDB-Cmd
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A role for command line tools which accept entry IDs as options
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/KiokuDB/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(App::Cmd)
BuildRequires:	perl(KiokuDB)
BuildRequires:	perl(MooseX::App::Cmd)
BuildRequires:	perl(MooseX::Getopt)
BuildRequires:	perl(MooseX::Types::Path::Class)
BuildRequires:	perl(ok)
BuildRequires:	perl(Proc::InvokeEditor)
BuildRequires:	perl(Throwable)
BuildArch:	noarch

%description
This is an the App::Cmd manpage based, pluggable suite of commands for the
KiokuDB manpage.

Some commands such as the KiokuDB::Cmd::Command::Dump manpage are part of
the core distributions, but backends can provide their own subcommands as
well.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 656933
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 624864
- import perl-KiokuDB-Cmd

