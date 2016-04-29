#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cssselect
Version  : 0.9.1
Release  : 8
URL      : https://pypi.python.org/packages/source/c/cssselect/cssselect-0.9.1.tar.gz
Source0  : https://pypi.python.org/packages/source/c/cssselect/cssselect-0.9.1.tar.gz
Summary  : cssselect parses CSS3 Selectors and translates them to XPath 1.0
Group    : Development/Tools
License  : BSD-3-Clause
Requires: cssselect-python
BuildRequires : cssselect
BuildRequires : lxml
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : testrepository
BuildRequires : testresources
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : unittest2

%description
===================================
cssselect: CSS Selectors for Python
===================================

%package python
Summary: python components for the cssselect package.
Group: Default

%description python
python components for the cssselect package.


%prep
%setup -q -n cssselect-0.9.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
python cssselect/tests.py
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
