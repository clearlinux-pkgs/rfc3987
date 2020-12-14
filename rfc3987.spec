#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rfc3987
Version  : 1.3.8
Release  : 11
URL      : https://files.pythonhosted.org/packages/14/bb/f1395c4b62f251a1cb503ff884500ebd248eed593f41b469f89caa3547bd/rfc3987-1.3.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/14/bb/f1395c4b62f251a1cb503ff884500ebd248eed593f41b469f89caa3547bd/rfc3987-1.3.8.tar.gz
Summary  : Parsing and validation of URIs (RFC 3986) and IRIs (RFC 3987)
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: rfc3987-license = %{version}-%{release}
Requires: rfc3987-python = %{version}-%{release}
Requires: rfc3987-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
See http://pypi.python.org/pypi/rfc3987 or the docstrings in rfc3987.py.

%package license
Summary: license components for the rfc3987 package.
Group: Default

%description license
license components for the rfc3987 package.


%package python
Summary: python components for the rfc3987 package.
Group: Default
Requires: rfc3987-python3 = %{version}-%{release}

%description python
python components for the rfc3987 package.


%package python3
Summary: python3 components for the rfc3987 package.
Group: Default
Requires: python3-core
Provides: pypi(rfc3987)

%description python3
python3 components for the rfc3987 package.


%prep
%setup -q -n rfc3987-1.3.8
cd %{_builddir}/rfc3987-1.3.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603403636
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rfc3987
cp %{_builddir}/rfc3987-1.3.8/COPYING.txt %{buildroot}/usr/share/package-licenses/rfc3987/8624bcdae55baeef00cd11d5dfcfa60f68710a02
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rfc3987/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
