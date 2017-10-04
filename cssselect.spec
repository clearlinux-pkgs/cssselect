#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cssselect
Version  : 1.0.1
Release  : 22
URL      : http://pypi.debian.net/cssselect/cssselect-1.0.1.tar.gz
Source0  : http://pypi.debian.net/cssselect/cssselect-1.0.1.tar.gz
Summary  : cssselect parses CSS3 Selectors and translates them to XPath 1.0
Group    : Development/Tools
License  : BSD-3-Clause
Requires: cssselect-legacypython
Requires: cssselect-python3
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

%package legacypython
Summary: legacypython components for the cssselect package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the cssselect package.


%package python
Summary: python components for the cssselect package.
Group: Default
Requires: cssselect-legacypython
Requires: cssselect-python3

%description python
python components for the cssselect package.


%package python3
Summary: python3 components for the cssselect package.
Group: Default
Requires: python3-core

%description python3
python3 components for the cssselect package.


%prep
%setup -q -n cssselect-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507152867
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1507152867
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
