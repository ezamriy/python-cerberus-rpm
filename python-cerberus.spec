%global pkg     Cerberus

Name:           python-cerberus
Version:        0.7.2
Release:        1%{?dist}
Summary:        Extensible validation for Python dictionaries.

Group:          Development/Languages
License:        ISC
URL:            https://github.com/nicolaiarocci/cerberus
Source0:        https://pypi.python.org/packages/source/C/%{pkg}/%{pkg}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-setuptools


%description
Cerberus provides type checking and other base functionality out of the box and
is designed to be non-blocking and easily extensible, allowing for custom
validation. It has no dependancies and is thoroughly tested under Python 2.6,
Python 2.7, Python 3.3 and Python 3.4.


%prep
%setup -q -n %{pkg}-%{version}


%build
%{__python} setup.py build


%check
%{__python} setup.py test


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%clean
%{__rm} -rf %{buildroot}
 

%files
%defattr(-,root,root,-)
%doc LICENSE README.rst
%{python_sitelib}/*


%changelog
* Sun Aug 24 2014 Eugene G. Zamriy <eugene@zamriy.info> - 0.7.2-1
- Initial release: 0.7.2 version
