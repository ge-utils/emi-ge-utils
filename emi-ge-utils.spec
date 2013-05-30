Summary: Metapackage for the installation of CREAM Grid Engine Utils
Name: emi-ge-utils
Version: 2.0.2
Release: 1
License: Apache Software License
Group: System/Information
Vendor: CREAM GE utils <ge-support@listas.cesga.es>
Packager: CREAM GE utils <ge-support@listas.cesga.es>
BuildArch: noarch
Requires: emi-version  
Requires: glite-info-dynamic-ge
Requires: glite-yaim-ge-utils
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: yes

%description
Metapackage for the installation of CREAM Grid Engine Utils

%prep
# Nothing, this is a metapackage!

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%changelog
* Thu May 30 2013 GE Utils <ge-support@listas.cesga.es> - 2.0.2
- New metapackage.

* Fri Aug 31 2012 CREAM group <cream-support@lists.infn.it> - 2.0.1-1.sl5
- New major release.
