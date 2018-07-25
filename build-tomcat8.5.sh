#!/bin/bash
# This script is supposed to run as the user "ulyaoth".

# Clean repository because AMI could have old data.
if type dnf 2>/dev/null
then
  sudo dnf clean all
elif type yum 2>/dev/null
then
  sudo yum clean all
fi

# Create build environment.
rpmdev-setuptree

# Download spec file.
wget https://raw.githubusercontent.com/dalitun/tomcatspec/master/SPECS/tomcat8.5-admin.spec -O ~/rpmbuild/SPECS/tomcat8.5-admin.spec
wget https://raw.githubusercontent.com/dalitun/tomcatspec/master/SPECS/tomcat8.5-docs.spec -O ~/rpmbuild/SPECS/tomcat8.5-docs.spec
wget https://raw.githubusercontent.com/dalitun/tomcatspec/master/SPECS/tomcat8.5-examples.spec -O ~/rpmbuild/SPECS/tomcat8.5-examples.spec
wget https://raw.githubusercontent.com/dalitun/tomcatspec/master/SPECS/tomcat8.5.spec -O ~/rpmbuild/SPECS/tomcat8.5.spec

# Install all requirements
if type dnf 2>/dev/null
then
  sudo dnf builddep -y ~/rpmbuild/SPECS/tomcat8.5.spec
elif type yum 2>/dev/null
then
  sudo yum-builddep -y ~/rpmbuild/SPECS/tomcat8.5.spec
fi

# Download additional files specified in spec file.
spectool ~/rpmbuild/SPECS/tomcat8.5.spec -g -R

# Build the rpm.
rpmbuild -ba ~/rpmbuild/SPECS/tomcat8.5.spec
rpmbuild -ba ~/rpmbuild/SPECS/tomcat8.5-admin.spec
rpmbuild -ba ~/rpmbuild/SPECS/tomcat8.5-docs.spec
rpmbuild -ba ~/rpmbuild/SPECS/tomcat8.5-examples.spec
