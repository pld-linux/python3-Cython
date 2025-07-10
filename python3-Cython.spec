#
# Conditional build:
%bcond_without	apidocs		# Sphinx documentation
%bcond_with	tests		# test suite (SLOOOOW)

%define		module	Cython
Summary:	Language for writing Python Extension Modules (Python 2.x version)
Summary(pl.UTF-8):	Język służący do pisania modułów rozszerzających Pythona (wersja dla Pythona 2.x)
Name:		python3-%{module}
Version:	3.1.2
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/cython/
Source0:	https://files.pythonhosted.org/packages/source/c/cython/cython-%{version}.tar.gz
# Source0-md5:	6fb2dc869f4d00b4a13e130ec1197bfd
URL:		https://cython.org/
BuildRequires:	python3 >= 1:3.8
BuildRequires:	python3-devel >= 1:3.8
BuildRequires:	python3-setuptools
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with apidocs}
BuildRequires:	python3-sphinx_issues
BuildRequires:	python3-sphinx_tabs
BuildRequires:	sphinx-pdg-3 >= 1.8
%endif
Requires:	python3-devel >= 1:3.8
Conflicts:	python-Cython < 3.0.11-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautocompressdoc	*.c

%description
Cython lets you write code that mixes Python and C data types any way
you want, and compiles it into a C extension for Python. Cython is
based on Pyrex.

This package contains Cython module for Python 3.x.

%description -l pl.UTF-8
Cython pozwala pisać kod zawierający dane Pythona i języka C połączone
w jakikolwiek sposób i kompiluje to jako rozszerzenie C dla Pythona.
Cython jest oparty na Pyreksie.

Ten pakiet zawiera moduł Cython dla Pythona 3.x.

%package apidocs
Summary:	API documentation for Cython module
Summary(pl.UTF-8):	Dokumentacja API modułu Cython
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Cython module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Cython.

%package examples
Summary:	Examples for Cython language
Summary(pl.UTF-8):	Przykłady programów w języku Cython
Group:		Libraries/Python
BuildArch:	noarch

%description examples
This package contains example programs for Cython language.

%description examples -l pl.UTF-8
Pakiet zawierający przykładowe programy napisane w języku Cython.

%prep
%setup -q -n cython-%{version}

%{__sed} -i -e '1s,/usr/bin/env python$,%{__python3},' Demos/benchmarks/bm_unpack_sequence.py

%build
%py3_build

%if %{with tests}
%{__python3} runtests.py \
	SPHINXBUILD=sphinx-build-3
%endif

%if %{with apidocs}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/cython{,3}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/cythonize{,3}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/cygdb{,3}

%{__ln_s} cython3 $RPM_BUILD_ROOT%{_bindir}/cython
%{__ln_s} cythonize3 $RPM_BUILD_ROOT%{_bindir}/cythonize
%{__ln_s} cygdb3 $RPM_BUILD_ROOT%{_bindir}/cygdb

cp -a Demos/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYING.txt README.rst ToDo.txt USAGE.txt
%attr(755,root,root) %{_bindir}/cython
%attr(755,root,root) %{_bindir}/cython3
%attr(755,root,root) %{_bindir}/cythonize
%attr(755,root,root) %{_bindir}/cythonize3
%attr(755,root,root) %{_bindir}/cygdb
%attr(755,root,root) %{_bindir}/cygdb3
%{py3_sitedir}/cython.py
%{py3_sitedir}/__pycache__/cython.*
%{py3_sitedir}/Cython
%{py3_sitedir}/pyximport
%{py3_sitedir}/Cython-%{version}-py*.egg-info

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_images,_static,src,*.html,*.js}
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
