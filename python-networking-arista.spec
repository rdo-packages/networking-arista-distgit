# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global drv_vendor Arista
%global srcname networking_arista
%global pkgname networking-arista
%global docpath doc/build/html

Name:           python-%{pkgname}
Version:        2019.1.0
Release:        1%{?dist}
Summary:        %{drv_vendor} OpenStack Neutron driver
Provides:       python-%{srcname} = %{version}-%{release}
Obsoletes:      python-%{srcname}

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://tarballs.openstack.org/%{pkgname}/%{srcname}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-mock
BuildRequires:  python%{pyver}-neutron-tests
BuildRequires:  python%{pyver}-oslo-sphinx
#BuildRequires:  python%{pyver}-oslotest
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-sphinx
BuildRequires:  python%{pyver}-testrepository
BuildRequires:  python%{pyver}-testtools

%description
This package contains %{drv_vendor} networking driver for OpenStack Neutron.

%package -n python%{pyver}-%{pkgname}
Summary: Arista OpenStack Neutron driver
%{?python_provide:%python_provide python%{pyver}-%{pkgname}}

Requires:       python%{pyver}-alembic >= 0.8.10
Requires:       python%{pyver}-neutron-lib >= 1.23.0
Requires:       python%{pyver}-oslo-config >= 2:5.2.0
Requires:       python%{pyver}-oslo-i18n >= 3.15.3
Requires:       python%{pyver}-oslo-log >= 3.36.0
Requires:       python%{pyver}-oslo-service > 1.28.1
Requires:       python%{pyver}-oslo-utils >= 3.33.0
Requires:       python%{pyver}-pbr >= 2.0.0
Requires:       python%{pyver}-six >= 1.10.0
Requires:       python%{pyver}-sqlalchemy >= 1.2.0
Requires:       python%{pyver}-requests >= 2.14.2


%description -n python%{pyver}-%{pkgname}
This package contains %{drv_vendor} networking driver for OpenStack Neutron.


%prep
%setup -q -n %{srcname}-%{upstream_version}


%build
rm requirements.txt test-requirements.txt
%{pyver_build}
%{pyver_bin} setup.py build_sphinx
rm %{docpath}/.buildinfo


#%check
#%{pyver_bin} setup.py testr


%install
export PBR_VERSION=%{version}
%{pyver_install}

%files -n python%{pyver}-%{pkgname}
%license LICENSE
%doc %{docpath}
%{pyver_sitelib}/%{srcname}
%{pyver_sitelib}/%{srcname}*.egg-info
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/ml2/*.ini

%changelog
* Tue Sep 10 2019 Mark McClain <mark@mcclain.xyz> 2019.1.0-1
- Update to 2019.1.0

* Thu Apr 25 2019 RDO <dev@lists.rdoproject.org> 2018.2.2-1
- Update to 2018.2.2

