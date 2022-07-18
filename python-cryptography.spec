%global debug_package %{nil}

Name: python-cryptography
Epoch: 100
Version: 36.0.0
Release: 1%{?dist}
Summary: Python library which exposes cryptographic recipes and primitives
License: Apache-2.0
URL: https://github.com/pyca/cryptography/tags
Source0: %{name}_%{version}.orig.tar.gz
%if 0%{?centos_version} == 700
BuildRequires: openssl11-devel
%else
BuildRequires: openssl-devel
%endif
BuildRequires: cargo
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: libffi-devel
BuildRequires: python-rpm-macros
BuildRequires: python3-cffi >= 1.12
BuildRequires: python3-cython
BuildRequires: python3-devel
BuildRequires: python3-pycparser
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools-rust >= 0.11.4
BuildRequires: rust

%description
cryptography is a package designed to expose cryptographic primitives
and recipes to Python developers.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
set -ex && \
%if 0%{?centos_version} == 700
    export LDFLAGS="-L%{_libdir}/openssl11" && \
    export CFLAGS="-I%{_includedir}/openssl11" && \
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

%description -n python%{python3_version_nodots}-cryptography
cryptography is a package designed to expose cryptographic primitives
and recipes to Python developers.

%files -n python%{python3_version_nodots}-cryptography
%license LICENSE
%{python3_sitearch}/*
%endif

%if 0%{?centos_version} == 700
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

%description -n python%{python3_version_nodots}-cryptography
cryptography is a package designed to expose cryptographic primitives
and recipes to Python developers.

%files -n python%{python3_version_nodots}-cryptography
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?centos_version} == 700)
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

%description -n python3-cryptography
cryptography is a package designed to expose cryptographic primitives
and recipes to Python developers.

%files -n python3-cryptography
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
