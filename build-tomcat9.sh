# This script is supposed to run as the user "ulyaoth".
sudo yum install -y java-1.8.0-openjdk-devel
sudo yum install -y rpmdevtools rpmlint
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
wget https://raw.githubusercontent.com/dalitun/tomcatspec/master/SPECS/tomcat9.spec -O ~/rpmbuild/SPECS/tomcat9.spec
wget https://raw.githubusercontent.com/dalitun/tomcatspec/master/SPECS//tomcat9-admin.spec -O ~/rpmbuild/SPECS/tomcat9-admin.spec
wget https://raw.githubusercontent.com/dalitun/tomcatspec/master/SPECS/tomcat9-examples.spec -O ~/rpmbuild/SPECS/tomcat9-examples.spec

# Install all requirements
if type dnf 2>/dev/null
then
  sudo dnf builddep -y ~/rpmbuild/SPECS/tomcat9.spec
elif type yum 2>/dev/null
then
  sudo yum-builddep -y ~/rpmbuild/SPECS/tomcat9.spec
fi

# Download additional files specified in spec file.
spectool ~/rpmbuild/SPECS/tomcat9.spec -g -R

# Build the rpm.
rpmbuild -ba ~/rpmbuild/SPECS/tomcat9.spec
rpmbuild -ba ~/rpmbuild/SPECS/tomcat9-admin.spec
rpmbuild -ba ~/rpmbuild/SPECS/tomcat9-docs.spec
rpmbuild -ba ~/rpmbuild/SPECS/tomcat9-examples.spec
