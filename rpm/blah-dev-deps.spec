Summary: Development dependencies for wallaroo
Name: blah-dev-deps
Version: 0.1
Release: 0
License: distributable

Requires:  ponyc
Requires:  pony-stable
Requires:  make
Requires:  gcc-c++
Requires:  snappy-devel

%if %{?_vendor} == suse
Requires:  libopenssl-devel
Requires:  liblz4-devel
%else
Requires:  openssl-devel
Requires:  lz4-devel
%endif


%description
A virtual package which installs dependencies for a Wallaroo application

%prep

%build

%clean 

%install

%post

%files 


%changelog
* Sat Jun 9 2018 Dipin Hora <dipin@wallaroolabs.com>
- initial release
