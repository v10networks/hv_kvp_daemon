README FILE FOR RPM PACKAGING
=============================

To create a RPM package for RPM based systems, you will need to perform the following:

1. Run the bootstrap.sh script (This is only necessary if you are building from the git tree)
2. Configure the package
3. Run make dist
4. Copy over the newly generated tarball to your SOURCES directory in the rpmbuild tree
5. Run rpmbuild -bb hvuserspace.spec to generate a RPM package

Note: If you downloaded a tarball instead, you may skip the configure and make step as the tarball should contain all the necessary code to build an RPM package.
