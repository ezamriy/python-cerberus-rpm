Name:           python-cerberus
Version:        1.1
Release:        1%{?dist}
Summary:        Lightweight, extensible data validation library for Python.

Group:          Development/Languages
License:        ISC
URL:            https://github.com/pyeve/cerberus
Source0:        https://github.com/pyeve/cerberus/archive/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-setuptools


%description
Cerberus provides type checking and other base functionality out of the box
and is designed to be non-blocking and easily extensible, allowing for
custom validation. It has no dependencies and is thoroughly tested under
Python 2.6, Python 2.7, Python 3.3, Python 3.4, Python 3.5, Python 3.6,
PyPy and PyPy3.


%prep
%setup -q -n cerberus-%{version}


%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


# pytest-runner is required to run tests on EL7
#%check
#%{__python} setup.py test


%clean
%{__rm} -rf %{buildroot}
 

%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGES CONTRIBUTING.rst LICENSE README.rst UPGRADING.rst
%{python_sitelib}/*


%changelog
* Tue Oct 10 2017 Eugene Zamriy <eugene@zamriy.info> - 1.1-1
- Update to 1.1 version
- Update summary and description
- Disable tests because there is pytest-runner available for EL7

* Sun Jan 24 2016 Eugene Zamriy <eugene@zamriy.info> - 0.9.2-1
- Update to 0.9.2 version

* Sun Aug 24 2014 Eugene G. Zamriy <eugene@zamriy.info> - 0.7.2-1
- Initial release: 0.7.2 version
