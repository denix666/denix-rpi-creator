Name:		denix-rpi-creator
Version:	3.0
Release:	3%{?dist}
Summary:	Raspberry Pi sd image creator
Group:		Scripts
License:	GPL
URL:		http://os.vc
Requires:	yum rpm denix-colors
Source0:        %{name}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch

%description
Set of scripts to make sd image for Raspberry Pi

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{buildroot}
cp -r %{_builddir}/%{name} %{buildroot}

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/%{name}

%files
%defattr(-,root,root,-)
%attr(0755,root,root) /usr/share/denix-rpi-creator/denix-rpi-creator
%attr(0755,root,root) /usr/bin/denix-rpi-creator
%attr(0644,root,root) /etc/pam.d/denix-rpi-creator
%attr(0644,root,root) /etc/security/console.apps/denix-rpi-creator
