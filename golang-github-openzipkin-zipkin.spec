# Run tests in check section
# Tests need Internet access, disabled.
%bcond_with check

%global goipath         github.com/openzipkin/zipkin-go
Version:                0.1.0

%global common_description %{expand:
Zipkin tracer library for go.}

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        Zipkin tracer library for go
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/gorilla/mux)
BuildRequires: golang(github.com/Shopify/sarama)
BuildRequires: golang(google.golang.org/grpc/metadata)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1
- First package for Fedora

