Name:           hv_userspace_daemons
Version:        0.2
Release:        1%{?dist}
Summary:        Hyper-V userspace daemons for interacting with the parent partition

Group:          System Environment 
License:        GPL
URL:            http://github.v10networks.com
Source0:	hv_userspace_daemons-0.2.tar.gz 

BuildRequires:  kernel
Requires:       kernel
Conflicts:	hypervkvpd
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
install -m 0755 init/rhel/hv_kvp_daemon $RPM_BUILD_ROOT/etc/init.d
install -m 0755 init/rhel/hv_vss_daemon $RPM_BUILD_ROOT/etc/init.d
install -m 0755 scripts/rhel/hv_get_dhcp_info.sh $RPM_BUILD_ROOT/usr/sbin
install -m 0755 scripts/rhel/hv_get_dns_info.sh $RPM_BUILD_ROOT/usr/sbin
install -m 0755 scripts/rhel/hv_set_ifconfig.sh $RPM_BUILD_ROOT/usr/sbin

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
/sbin/chkconfig hv_vss_daemon on

%preun
/sbin/chkconfig --del hv_kvp_daemon
/sbin/chkconfig --del hv_vss_daemon

%changelog
