Summary: Dependencies for wallaroo
Name: blah-deps
Version: 0.1
Release: 0
License: distributable


%if %{?_vendor} == suse
Requires:  libopenssl1_1
Requires:  liblz4-1
Requires:  libsnappy1
%else
Requires:  openssl-libs
Requires:  snappy
%if 0%{?el7}
Requires:  lz4
%else
Requires:  lz4-libs
%endif
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
