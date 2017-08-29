%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global drv_vendor Arista
%global srcname networking_arista
%global pkgname networking-arista
%global docpath doc/build/html

Name:           python-%{pkgname}
Version:        2017.1.0
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

Requires:       python-babel
Requires:       python-jsonrpclib
Requires:       python-neutron-lib >= 0.3.0
Requires:       python-oslo-log >= 0.4.0
Requires:       python-pbr


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
* Tue Mar 21 2017 Alfredo Moralejo <amoralej@redhat.com> 2017.1.0-1
- Update to 2017.1.0

