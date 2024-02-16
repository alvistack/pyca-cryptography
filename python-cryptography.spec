# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-cryptography
Epoch: 100
Version: 42.0.1
Release: 1%{?dist}
Summary: Python library which exposes cryptographic recipes and primitives
License: Apache-2.0
URL: https://github.com/pyca/cryptography/tags
Source0: %{name}_%{version}.orig.tar.gz
%if 0%{?rhel} == 7
BuildRequires: openssl11
BuildRequires: openssl11-devel
%else
BuildRequires: openssl
BuildRequires: openssl-devel
%endif
BuildRequires: cargo
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: libffi-devel
BuildRequires: pkgconfig
BuildRequires: python-rpm-macros
BuildRequires: python3-cffi >= 1.12
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-pycparser
BuildRequires: python3-setuptools >= 61.0.0
BuildRequires: python3-setuptools-rust >= 1.7.0
BuildRequires: python3-wheel
BuildRequires: rust

%description
cryptography is a package designed to expose cryptographic primitives
and recipes to Python developers.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
set -ex && \
%if 0%{?rhel} == 7
    export LDFLAGS="-L%{_libdir}/openssl11" && \
    export CFLAGS="-I%{_includedir}/openssl11" && \
    export OPENSSL_DIR="%{_libdir}/openssl11" && \
    export OPENSSL_LIB_DIR="%{_libdir}/openssl11" && \
    export OPENSSL_INCLUDE_DIR="%{_includedir}/openssl11" && \
%endif
    %py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-cryptography
Summary: Python library which exposes cryptographic recipes and primitives
Requires: libssl.so.1.1()(64bit)
Requires: python3
Requires: python3-cffi >= 1.12
Provides: python3-cryptography = %{epoch}:%{version}-%{release}
Provides: python3dist(cryptography) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cryptography = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cryptography) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cryptography = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cryptography) = %{epoch}:%{version}-%{release}
Conflicts: python3-pyOpenSSL < 22.0.0

%description -n python%{python3_version_nodots}-cryptography
cryptography is a package designed to expose cryptographic primitives
and recipes to Python developers.

%files -n python%{python3_version_nodots}-cryptography
%license LICENSE
%{python3_sitearch}/*
%endif

%if 0%{?rhel} == 7
%package -n python%{python3_version_nodots}-cryptography
Summary: Python library which exposes cryptographic recipes and primitives
Requires: libssl.so.1.1()(64bit)
Requires: python3
Requires: python3-cffi >= 1.12
Provides: python3-cryptography = %{epoch}:%{version}-%{release}
Provides: python3dist(cryptography) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cryptography = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cryptography) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cryptography = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cryptography) = %{epoch}:%{version}-%{release}
Conflicts: python3-pyOpenSSL < 22.0.0

%description -n python%{python3_version_nodots}-cryptography
cryptography is a package designed to expose cryptographic primitives
and recipes to Python developers.

%files -n python%{python3_version_nodots}-cryptography
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?rhel} == 7)
%package -n python3-cryptography
Summary: Python library which exposes cryptographic recipes and primitives
Requires: libssl.so.1.1()(64bit)
Requires: python3
Requires: python3-cffi >= 1.12
Provides: python3-cryptography = %{epoch}:%{version}-%{release}
Provides: python3dist(cryptography) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cryptography = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cryptography) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cryptography = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cryptography) = %{epoch}:%{version}-%{release}
Conflicts: python3-pyOpenSSL < 22.0.0

%description -n python3-cryptography
cryptography is a package designed to expose cryptographic primitives
and recipes to Python developers.

%files -n python3-cryptography
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
