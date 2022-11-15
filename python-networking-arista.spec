%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global drv_vendor Arista
%global srcname networking_arista
%global pkgname networking-arista
%global docpath doc/build/html

Name:           python-%{pkgname}
Version:        XXX
Release:        XXX
Summary:        %{drv_vendor} OpenStack Neutron driver
Provides:       python-%{srcname} = %{version}-%{release}
Obsoletes:      python-%{srcname}

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://tarballs.opendev.org/x/%{pkgname}/%{srcname}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.opendev.org/x/%{pkgname}/%{srcname}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-neutron-tests
BuildRequires:  python3-oslo-sphinx
#BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-testrepository
BuildRequires:  python3-testtools

%description
This package contains %{drv_vendor} networking driver for OpenStack Neutron.

%package -n python3-%{pkgname}
Summary: Arista OpenStack Neutron driver
%{?python_provide:%python_provide python3-%{pkgname}}

Requires:       python3-alembic >= 1.6.5
Requires:       python3-neutron-lib >= 2.20.0
Requires:       python3-oslo-config >= 2:8.0.0
Requires:       python3-oslo-i18n >= 3.20.0
Requires:       python3-oslo-log >= 4.5.0
Requires:       python3-oslo-service >= 1.31.0
Requires:       python3-oslo-utils >= 4.5.0
Requires:       python3-pbr >= 4.0.0
Requires:       python3-six >= 1.10.0
Requires:       python3-sqlalchemy >= 1.4.23
Requires:       python3-requests >= 2.18.0


%description -n python3-%{pkgname}
This package contains %{drv_vendor} networking driver for OpenStack Neutron.


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%setup -q -n %{srcname}-%{upstream_version}


%build
rm requirements.txt test-requirements.txt
%{py3_build}
# oslosphinx do not work with sphinx > 2
# python3 setup.py build_sphinx
#rm %{docpath}/.buildinfo


#%check
#python3 setup.py testr


%install
export PBR_VERSION=%{version}
%{py3_install}

%files -n python3-%{pkgname}
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}*.egg-info
%config(noreplace) %attr(0640, root, neutron) %{_sysconfdir}/neutron/plugins/ml2/*.ini

%changelog
