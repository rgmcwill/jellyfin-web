%global         debug_package %{nil}

Name:           jellyfin-web
Version:        10.8.0
Release:        1%{?dist}
Summary:        The Free Software Media System web client
License:        GPLv2
URL:            https://jellyfin.org
# Jellyfin Server tarball created by `make -f .copr/Makefile srpm`, real URL ends with `v%%{version}.tar.gz`
Source0:        jellyfin-web-%{version}.tar.gz

BuildArch:		noarch
%if 0%{?rhel} > 0 && 0%{?rhel} < 8
BuildRequires:	nodejs
%else
BuildRequires:	git
BuildRequires:	npm
%endif

# Disable Automatic Dependency Processing
AutoReqProv:    no

%description
Jellyfin is a free software media system that puts you in control of managing and streaming your media.


%prep
%autosetup -n jellyfin-web-%{version} -b 0

%build

%install
%if 0%{?rhel} > 0 && 0%{?rhel} < 8
# Required for CentOS build
chown root:root -R .
%endif
npm ci --no-audit --unsafe-perm
%{__mkdir} -p %{buildroot}%{_datadir}
mv dist %{buildroot}%{_datadir}/jellyfin-web
%{__install} -D -m 0644 LICENSE %{buildroot}%{_datadir}/licenses/jellyfin/LICENSE

%files
%defattr(644,root,root,755)
%{_datadir}/jellyfin-web
%{_datadir}/licenses/jellyfin/LICENSE

%changelog
* Fri Jun 10 2022 Jellyfin Packaging Team <packaging@jellyfin.org>
- New upstream version 10.8.0; release changelog at https://github.com/jellyfin/jellyfin-web/releases/tag/v10.8.0
