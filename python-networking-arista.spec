%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global drv_vendor Arista
%global srcname networking_arista
%global pkgname networking-arista
%global docpath doc/build/html

Name:           python-%{pkgname}
Version:        2017.2.6
Release:        1%{?dist}
Summary:        %{drv_vendor} OpenStack Neutron driver
Provides:       python-%{srcname} = %{version}-%{release}
Obsoletes:      python-%{srcname}

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://tarballs.openstack.org/%{pkgname}/%{srcname}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-mock
BuildRequires:  python-neutron-tests
BuildRequires:  python-oslo-sphinx
#BuildRequires:  python-oslotest
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx
BuildRequires:  python-testrepository
BuildRequires:  python-testtools

Requires:       python-alembic >= 0.8.10
Requires:       python-babel
Requires:       python-jsonrpclib
Requires:       python-neutron-lib >= 1.9.0
Requires:       python-oslo-config >= 2:4.6.0
Requires:       python-oslo-i18n >= 3.15.3
Requires:       python-oslo-log >= 3.30.0
Requires:       python-oslo-service >= 1.24.0
Requires:       python-oslo-utils >= 3.28.0
Requires:       python-pbr
Requires:       python-six >= 1.9.0
Requires:       python-sqlalchemy >= 1.0.10


%description
This package contains %{drv_vendor} networking driver for OpenStack Neutron.


%prep
%setup -q -n %{srcname}-%{upstream_version}


%build
rm requirements.txt test-requirements.txt
%{__python2} setup.py build
%{__python2} setup.py build_sphinx
rm %{docpath}/.buildinfo


#%check
#%{__python2} setup.py testr


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%doc %{docpath}
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}*.egg-info
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/ml2/*.ini

%changelog
* Sat Sep 16 2017 Haikel Guemar <hguemar@fedoraproject.org> 2017.2.0-1
- Update to 2017.2.0

