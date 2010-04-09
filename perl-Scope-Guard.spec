#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Scope
%define	pnam	Guard
Summary:	Scope::Guard - lexically scoped resource management
Summary(pl.UTF-8):	Scope::Guard - zarządzanie zasobami o zakresie leksykalnym
Name:		perl-Scope-Guard
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/C/CH/CHOCOLATE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	74a5c78230e219defb86954cb2ceec85
URL:		http://search.cpan.org/dist/Scope-Guard/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a convenient way to perform cleanup or other
forms of resource management at the end of a scope.

%description -l pl.UTF-8
Ten moduł udostępnia wygodny sposób wykonywania czyszczenia i innych
form zarządzania zasobami poza zakresem ich widoczności.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Scope
%{perl_vendorlib}/Scope/*.pm
%{_mandir}/man3/*
