%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define rc_version 0

%if 0%{?rc_version}
%define release_prefix 0.rc%{rc_version}.
%endif

Name:       sd-mux-ctrl
Summary:    Control software for sd-mux devices.
Version:    0.0.1
Release:    %{?release_prefix}%{?opensuse_bs:<CI_CNT>.<B_CNT>}%{!?opensuse_bs:0}
Group:      Development/Tools
License:    Apache-2.0
URL:        http://www.tizen.org
Source0:    %{name}_%{version}.tar.gz
Requires:   libftdi >= 1.2
Requires:   popt

BuildRoot:  %{_tmppath}/%{name}_%{version}-build

%description
sd-mux-ctrl is a tool for controlling multiple sd-mux devices. This tool allows:
- to connect SD card to DUT (Device under test) or to TS (Test Server)
- to connect one USB port to DUT or TS
- to power off or on DUT
- to reset DUT through power disconnecting and reconnecting after specified timeout

%prep
%setup -q -n %{name}-%{version}

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
make

%install
rm -rf %{buildroot}
cd build
make install DESTDIR="%{buildroot}"

%files
%{_bindir}/%{name}