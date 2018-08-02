
%define __jar_repack %{nil}
%define debug_package %{nil}

%define tomcat_user_home /var/lib/tomcat8
%define tomcat_group tomcat8
%define tomcat_user tomcat8

Summary:    Apache Servlet/JSP Engine
Name:       tomcat8.5-examples
Version:    8.5.31
Release:    1%{?dist}
BuildArch:  x86_64
License:    Apache License version 2
Group:      Applications/Internet
URL:        https://tomcat.apache.org/
Vendor:     Apache Software Foundation
Packager:   ext.malarchab@cma-cgm.com
Source0:    http://www.us.apache.org/dist/tomcat/tomcat-8/v%{version}/bin/apache-tomcat-%{version}.tar.gz
BuildRoot:  %{_tmppath}/tomcat-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: tomcat8.5

Provides: tomcat-examples
Provides: apache-tomcat-examples
Provides: tomcat-examples
Provides: tomcat8.5-examples

%description
The package contains the official Apache Tomcat "webapps/examples" and "webapps/ROOT" directories.

%prep
%setup -q -n apache-tomcat-%{version}

%build

%install
install -d -m 755 %{buildroot}/%{tomcat_user_home}/
cp -R * %{buildroot}/%{tomcat_user_home}/

# Delete all files except webapp admin
%{__rm} -rf %{buildroot}/%{tomcat_user_home}/bin
%{__rm} -rf %{buildroot}/%{tomcat_user_home}/conf
%{__rm} -rf %{buildroot}/%{tomcat_user_home}/lib
%{__rm} -rf %{buildroot}/%{tomcat_user_home}/LICENSE
%{__rm} -rf %{buildroot}/%{tomcat_user_home}/NOTICE
%{__rm} -rf %{buildroot}/%{tomcat_user_home}/RELEASE-NOTES
%{__rm} -rf %{buildroot}/%{tomcat_user_home}/RUNNING.txt
%{__rm} -rf %{buildroot}/%{tomcat_user_home}/temp
%{__rm} -rf %{buildroot}/%{tomcat_user_home}/work
%{__rm} -rf %{buildroot}/%{tomcat_user_home}/logs
%{__rm} -rf %{buildroot}/%{tomcat_user_home}/webapps/docs
%{__rm} -rf %{buildroot}/%{tomcat_user_home}/webapps/host-manager
%{__rm} -rf %{buildroot}/%{tomcat_user_home}/webapps/manager

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,%{tomcat_user},%{tomcat_group})
%dir %{tomcat_user_home}/webapps/examples
%dir %{tomcat_user_home}/webapps/ROOT
%{tomcat_user_home}/webapps/examples/*
%{tomcat_user_home}/webapps/ROOT/*

%post
cat <<BANNER
----------------------------------------------------------------------

Thank you for using tomcat8.5-docs!
* Created by CMA-CGM Indus_Devops Team
Please find the official documentation for tomcat here:
* https://tomcat.apache.org/


----------------------------------------------------------------------
BANNER

%changelog
** Wed AUG 01 2018 Mohamed-Ali Lachhab <ext.malarchab@cma-cgm.com> 8.5.31-1
- Initial release for Tomcat 8.5.31.
