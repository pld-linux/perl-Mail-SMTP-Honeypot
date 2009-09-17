#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	SMTP-Honeypot
Summary:	Mail::SMTP::Honeypot - Dummy mail server
Summary(pl.UTF-8):	Mail::SMTP::Honeypot - fałszywy serwer poczty
Name:		perl-Mail-SMTP-Honeypot
Version:	0.09
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	87b75c5d669f2b8ff356e3e114d9a490
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Net-DNS-Codes >= 0.09
BuildRequires:	perl-Net-DNS-ToolKit >= 0.41
BuildRequires:	perl-Net-NBsocket >= 0.15
BuildRequires:	perl-Proc-PidUtil >= 0.07
BuildRequires:	perl-Sys-Hostname-FQDN >= 0.07
BuildRequires:	perl-Unix-Syslog >= 0.97
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail::SMTP::Honeypot is a Perl module that appears to provide all the
functionality of a standard SMTP server except that when the targeted
command state is detected (default DATA), it terminates the connection
with a temporary failure.

The purpose of this module is to provide a spam sink on a tertiary MX
host.

%description -l pl.UTF-8
Mail::SMTP::Honeypot to moduł Perla udający, że jest w pełni
funkcjonalnym standardowym serwerem SMTP z wyjątkiem tego, że po
wykryciu określonego stanu polecenia (domyślnie DATA) przerywa
połączenie z tymczasowym niepowodzeniem.

Celem tego modułu jest udostępnienie kanału dla spamu na trzecim
hoście MX.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Mail/SMTP/Honeypot/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Mail/SMTP
%{perl_vendorlib}/Mail/SMTP/*.pm
%{_mandir}/man3/*
