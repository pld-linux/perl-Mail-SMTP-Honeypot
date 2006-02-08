#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	SMTP-Honeypot
Summary:	Mail::SMTP::Honeypot - Dummy mail server
Summary(pl):	Mail::SMTP::Honeypot - fa³szywy serwer poczty
Name:		perl-Mail-SMTP-Honeypot
Version:	0.01
Release:	0.1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2fdc03eb86f76e807805b9ced229f7c5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Net-DNS-Codes >= 0.08
BuildRequires:	perl-Net-DNS-ToolKit >= 0.24
BuildRequires:	perl-Net-NBsocket >= 0.11
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

%description -l pl
Mail::SMTP::Honeypot to modu³ Perla udaj±cy, ¿e jest w pe³ni
funkcjonalnym standardowym serwerem SMTP z wyj±tkiem tego, ¿e po
wykryciu okre¶lonego stanu polecenia (domy¶lnie DATA) przerywa
po³±czenie z tymczasowym niepowodzeniem.

Celem tego modu³u jest udostêpnienie kana³u dla spamu na trzecim
ho¶cie MX.

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
