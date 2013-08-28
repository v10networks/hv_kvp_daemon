Name:           hv_userspace_daemons
Version:        0.1
Release:        1%{?dist}
Summary:        Hyper-V userspace daemons for interacting with the parent partition

Group:          System Environment 
License:        GPL
URL:            http://github.v10networks.com
Source0:	hv_userspace_daemons-0.1.tar.gz 

BuildRequires:  kernel
Requires:       kernel

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/init.d
cp init/rhel/hv_*_daemon $RPM_BUILD_ROOT/etc/init.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_sbindir}/*
%{_sysconfdir}/init.d/*
%doc

%post
/sbin/chkconfig --add hv_kvp_daemon
/sbin/chkconfig --add hv_vss_daemon

/sbin/chkconfig hv_kvp_daemon on
/sbin/chkconfig hv_vss_daemon off

%preun
/sbin/chkconfig --del hv_kvp_daemon
/sbin/chkconfig --del hv_vss_daemon

%changelog
