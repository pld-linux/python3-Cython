
%define		module	Cython

Summary:	Language for writing Python Extension Modules (Python 3.x version)
Summary(pl.UTF-8):	Język służący do pisania modułów rozszerzających Pythona (wersja dla Pythona 3.x)
Name:		python3-%{module}
Version:	0.17.4
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	http://www.cython.org/release/%{module}-%{version}.tar.gz
# Source0-md5:	cb11463e3a0c8d063e578db64ff61dde
URL:		http://www.cython.org/
BuildRequires:	python3
BuildRequires:	python3-2to3
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python3-libs
%pyrequires_eq	python3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautocompressdoc	*.c

%description
Cython lets you write code that mixes Python and C data types any way
you want, and compiles it into a C extension for Python. Cython is
based on Pyrex.

This package contains Cython module for Python 3.x.

%description -l pl.UTF-8
Pyrex pozwala pisać kod zawierający dane Pythona i języka C połączone
w jakikolwiek sposób i kompiluje to jako rozszerzenie C dla Pythona.
Cython jest oparty na Pyreksie.

Ten pakiet zawiera moduł Cython dla Pythona 3.x.

%package examples
Summary:	Examples for Cython language
Summary(pl.UTF-8):	Przykłady programów w języku Cython
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Cython language.

%description examples -l pl.UTF-8
Pakiet zawierający przykładowe programy napisane w języku Cython.

%prep
%setup -q -n %{module}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__python3} setup.py install \
	--root=$RPM_BUILD_ROOT \
	-O2

cp -a Demos/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

mv $RPM_BUILD_ROOT%{_bindir}/cython{,3}
mv $RPM_BUILD_ROOT%{_bindir}/cygdb{,3}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING.txt README.txt ToDo.txt USAGE.txt Doc/*.html Doc/*.c
%attr(755,root,root) %{_bindir}/cython3
%attr(755,root,root) %{_bindir}/cygdb3
%{py3_sitedir}/cython.py
%{py3_sitedir}/__pycache__/cython.*
%{py3_sitedir}/Cython
%{py3_sitedir}/pyximport
%{py3_sitedir}/Cython-*.egg-info

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
