Name:		dummy
Version:	1
Release:	1%{?dist}
Summary:	Nothing here

License:	WTF
URL:	 	https://github.com/xsuchy/Dummy
Source0: 	something.py

Requires:	python

%description
Really nothing here. Move on.

%prep
%setup -q


%build


%install
mkdir -p %{buildroot}%{_bindir}
cp -a something.py %{_bindir}/

%files
%{_bindir}/something.py



%changelog

