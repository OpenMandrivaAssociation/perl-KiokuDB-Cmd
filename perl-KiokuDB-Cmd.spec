%define upstream_name    KiokuDB-Cmd
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A role for command line tools which accept entry IDs as options
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/KiokuDB/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(App::Cmd)
BuildRequires: perl(KiokuDB)
BuildRequires: perl(MooseX::App::Cmd)
BuildRequires: perl(MooseX::Getopt)
BuildRequires: perl(MooseX::Types::Path::Class)
BuildRequires: perl(Proc::InvokeEditor)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is an the App::Cmd manpage based, pluggable suite of commands for the
KiokuDB manpage.

Some commands such as the KiokuDB::Cmd::Command::Dump manpage are part of
the core distributions, but backends can provide their own subcommands as
well.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


