%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global drv_vendor Arista
%global srcname networking_arista
%global pkgname networking-arista
%global docpath doc/build/html

Name:           python-%{pkgname}
Version:        2018.1.16
Release:        1%{?dist}
Summary:        %{drv_vendor} OpenStack Neutron driver
Provides:       python-%{srcname} = %{version}-%{release}
Obsoletes:      python-%{srcname}

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://tarballs.opendev.org/x/%{pkgname}/%{srcname}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-mock
BuildRequires:  python-neutron-tests
BuildRequires:  python2-oslo-sphinx
#BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools
BuildRequires:  python2-sphinx
BuildRequires:  python2-testrepository
BuildRequires:  python2-testtools

Requires:       python2-alembic >= 0.8.10
Requires:       python-neutron-lib >= 1.13.0
Requires:       python2-oslo-config >= 2:5.1.0
Requires:       python2-oslo-i18n >= 3.15.3
Requires:       python2-oslo-log >= 3.36.0
Requires:       python2-oslo-service >= 1.24.0
Requires:       python2-oslo-utils >= 3.33.0
Requires:       python2-pbr
Requires:       python2-six >= 1.10.0
Requires:       python2-sqlalchemy >= 1.0.10
Requires:       python2-requests >= 2.14.2


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
* Thu Jul 09 2020 Mark McClain <mark@mcclain.xyz> 2018.1.16-1
- Update to 2018.1.16

* Thu Sep 19 2019 Mark McClain <mark@mcclain.xyz> 2018.1.9-1
- Update to 2018.1.9

* Tue Sep 10 2019 Mark McClain <mark@mcclain.xyz> 2018.1.7-1
- Update to 2018.1.7
