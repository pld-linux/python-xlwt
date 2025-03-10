#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

%define		module		xlwt
Summary:	Library to create spreadsheets compatible with MS Excel 97/2000/XP/2003 XLS
Name:		python-%{module}
Version:	1.3.0
Release:	5
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/xlwt/
Source0:	https://files.pythonhosted.org/packages/source/x/xlwt/%{module}-%{version}.tar.gz
# Source0-md5:	4b1ca8a3cef3261f4b4dc3f138e383a8
URL:		http://www.python-excel.org/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a library for developers to use to generate spreadsheet files
compatible with Microsoft Excel versions 95 to 2003.

The package itself is pure Python with no dependencies on modules or
packages outside the standard Python distribution.

%package -n python3-%{module}
Summary:	Library to create spreadsheets compatible with MS Excel 97/2000/XP/2003 XLS
Requires:	python3-modules >= 1:3.5

%description -n python3-%{module}
This is a library for developers to use to generate spreadsheet files
compatible with Microsoft Excel versions 95 to 2003.

The package itself is pure Python with no dependencies on modules or
packages outside the standard Python distribution.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
