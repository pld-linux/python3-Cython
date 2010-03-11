
%define		module	Cython

Summary:	Language for writing Python Extension Modules
Summary(pl.UTF-8):	Język służący do pisania modułów rozszerzających Pythona
Name:		python3-%{module}
Version:	0.12.1
Release:	1
License:	PSF
Group:		Libraries/Python
Source0:	http://www.cython.org/release/%{module}-%{version}.tar.gz
# Source0-md5:	cf9f98e982258f8516620277975016f3
URL:		http://www.cython.org/
BuildRequires:	python3
BuildRequires:	python3-2to3
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python3-libs
%pyrequires_eq	python3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautocompressdoc	*.c

%description
Cython lets you write code that mixes Python and C data types any way
you want, and compiles it into a C extension for Python. Cython is
based on Pyrex.

%description -l pl.UTF-8
Pyrex pozwala pisać kod zawierający dane Pythona i języka C połączone
w jakikolwiek sposób i kompiluje to jako rozszerzenie C dla Pythona.
Cython jest oparty na Pyreksie.

%package examples
Summary:	Examples for Pyrex language
Summary(pl.UTF-8):	Przykłady programów w języku Pyrex
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Pyrex language.

%description examples -l pl.UTF-8
Pakiet zawierający przykładowe programy napisane w języku Pyrex.

%prep
%setup -q -n %{module}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__python3} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-purelib=%{py3_sitescriptdir} \
	-O2

find $RPM_BUILD_ROOT%{py3_sitescriptdir} -name "*.py" -a ! -name 'Lexicon.py' -exec rm -f {} \;

cp -a Demos/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

mv $RPM_BUILD_ROOT%{_bindir}/cython{,3}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt ToDo.txt USAGE.txt Doc/*.html Doc/*.c
%attr(755,root,root) %{_bindir}/cython3
%{py3_sitescriptdir}/cython.py[co]
%{py3_sitescriptdir}/Cython
%{py3_sitescriptdir}/pyximport
%{py3_sitescriptdir}/Cython-*.egg-info

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
