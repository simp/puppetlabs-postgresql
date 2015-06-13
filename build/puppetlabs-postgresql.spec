Summary: PuppetLabs PostgreSQL Module
Name: puppetlabs-postgresql
Version: 4.1.0
Release: 1.SIMP
License: Apache License, 2.0
Group: Applications/System
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: pupmod-concat
Requires: puppet >= 3.3.2
Buildarch: noarch
Requires: simp-bootstrap >= 4.2.0
Obsoletes: puppetlabs-postgresql-test

Prefix: %{prefix}

%description
This is the puppetlabs postgresql module as hosted at
https://github.com/puppetlabs/puppetlabs-postgresql.

Modifications have been made to work properly within a SIMP environment.

%prep
%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/postgresql

dirs='files lib manifests templates'
for dir in $dirs; do
  test -d $dir && cp -r $dir %{buildroot}/%{prefix}/postgresql
done

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/postgresql

%files
%defattr(0640,root,puppet,0750)
%{prefix}/postgresql

%post
#!/bin/sh

if [ -d %{prefix}/postgresql/plugins ]; then
  /bin/mv %{prefix}/postgresql/plugins %{prefix}/postgresql/plugins.bak
fi

%postun
# Post uninstall stuff

%changelog
* Thu Apr 02 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 4.1.0-1.SIMP
- Spot fix for postgres
- The cut over to using our Concat was not correct and is corrected here

* Mon Feb 02 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 4.1.0-0.SIMP
- First integration into SIMP for PuppetDB
