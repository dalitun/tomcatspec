
%define __jar_repack %{nil}
%define debug_package %{nil}
%define tomcat_home /opt/tomcat
%define tomcat_group tomcat
%define tomcat_user tomcat

Summary:    Apache Servlet/JSP Engine
Name:       tomcat9-docs
Version:    9.0.10
Release:    1%{?dist}
BuildArch: x86_64
License:    Apache License version 2
Group:      Applications/Internet
URL:        http://tomcat.apache.org/
Vendor:     Apache Software Foundation
Packager:   your name <you email>
Source0:    http://www.us.apache.org/dist/tomcat/tomcat-9/v%{version}/bin/apache-tomcat-%{version}.tar.gz
BuildRoot:  %{_tmppath}/tomcat-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: tomcat9

Provides: tomcat-docs
Provides: apache-tomcat-docs
Provides: tomcat-docs
Provides: tomcat9-docs

%description
The package contains the official Apache Tomcat "webapps/docs" directory.

%prep
%setup -q -n apache-tomcat-%{version}

%build

%install
install -d -m 755 %{buildroot}/%{tomcat_home}/
cp -R * %{buildroot}/%{tomcat_home}/

# Delete all files except webapp docs
%{__rm} -rf %{buildroot}/%{tomcat_home}/bin
%{__rm} -rf %{buildroot}/%{tomcat_home}/conf
%{__rm} -rf %{buildroot}/%{tomcat_home}/lib
%{__rm} -rf %{buildroot}/%{tomcat_home}/LICENSE
%{__rm} -rf %{buildroot}/%{tomcat_home}/NOTICE
%{__rm} -rf %{buildroot}/%{tomcat_home}/RELEASE-NOTES
%{__rm} -rf %{buildroot}/%{tomcat_home}/RUNNING.txt
%{__rm} -rf %{buildroot}/%{tomcat_home}/temp
%{__rm} -rf %{buildroot}/%{tomcat_home}/work
%{__rm} -rf %{buildroot}/%{tomcat_home}/logs
%{__rm} -rf %{buildroot}/%{tomcat_home}/webapps/examples
%{__rm} -rf %{buildroot}/%{tomcat_home}/webapps/ROOT
%{__rm} -rf %{buildroot}/%{tomcat_home}/webapps/host-manager
%{__rm} -rf %{buildroot}/%{tomcat_home}/webapps/manager

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,%{tomcat_user},%{tomcat_group})
%dir %{tomcat_home}/webapps/docs
%{tomcat_home}/webapps/docs/*

%post
cat <<BANNER
----------------------------------------------------------------------

Thank you for using tomcat9-docs!

Please find the official documentation for tomcat here:
* http://tomcat.apache.org/

----------------------------------------------------------------------
BANNER

%changelog
* Wed May 23 2018 your name <your email> 9.0.10-1
- Create Tomcat 9.0.10.
