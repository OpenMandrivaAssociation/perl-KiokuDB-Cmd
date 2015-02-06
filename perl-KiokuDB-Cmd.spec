%define upstream_name    KiokuDB-Cmd
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

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
BuildRequires:	perl(namespace::autoclean)
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
