%global provider_tld    com
%global project sgallagher
%global repo sscg
# https://github.com/sgallagher/sscg
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          b994c9eab1d3b1ec4c2470c2955945d5f2937da1
%global shortcommit     %(c=%{commit}; echo ${c:0:7})



Name:           sscg
Version:        2.0.0
Release:        1.rc1%{?dist}
Summary:        Simple SSL certificate generator

License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libtalloc-devel
BuildRequires:  openssl-devel
BuildRequires:  popt-devel
BuildRequires:  libpath_utils-devel

%description
A utility to aid in the creation of more secure "self-signed"
certificates. The certificates created by this tool are generated in a
way so as to create a CA certificate that can be safely imported into a
client machine to trust the service certificate without needing to set
up a full PKI environment and without exposing the machine to a risk of
false signatures from the service certificate.

%prep
%setup -q -n %{name}-%{version}


%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/%{name}

%changelog
* Thu Feb 16 2017 Stephen Gallagher <sgallagh@redhat.com> - 2.0.0-1.rc1
- Update to 2.0.0

* Thu Feb 16 2017 Stephen Gallagher <sgallagh@redhat.com> - 1.1.0-6
- Exclude PPC64 from the build since it doesn't support linking to OpenSSL

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 23 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.1.0-4
- Use compat-openssl10-devel on F26+

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- https://fedoraproject.org/wiki/Changes/golang1.7

* Tue May 31 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.1.0-2
- Debundle spacelog

* Wed May 25 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.1.0-1
- Update to 1.1.0
- Add support for signing service keys with an existing CA

* Wed May 25 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.0.4-1
- Add support for exporting the CA private key
- Fix incorrect output from -version
- Add README.md

* Tue May 24 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.0.3-1
- Only sign certificates after all extensions have been added

* Mon May 23 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.0.2-1
- Generate x509v3 certificates

* Mon May 23 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.0.1-1
- Fix issue with temporary file creation

* Mon May 23 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.0.0-1
- New upstream release 1.0.0
- Rewritten in Go
- Runtime depends only on OpenSSL, no more Python
- Support for writing certificate and key in a single file

* Wed May 18 2016 Stephen Gallagher <sgallagh@redhat.com> - 0.4.1-4
- Add requirement on python-setuptools

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 30 2015 Stephen Gallagher <sgallagh@redhat.com> 0.4.1-1
- Change default CA location to match service certificate
- Improve error handling

* Tue Mar 24 2015 Stephen Gallagher <sgallagh@redhat.com> 0.4.0-1
- Spec file cleanups
- PEP8 Cleanups
- Make location arguments optional

* Mon Mar 23 2015 Stephen Gallagher <sgallagh@redhat.com> 0.3.0-1
- Rename to sscg
- Only build with default python interpreter

* Tue Mar 17 2015 Stephen Gallagher <sgallagh@redhat.com> 0.2.1-1
- Include the LICENSE file in the tarball

* Tue Mar 17 2015 Stephen Gallagher <sgallagh@redhat.com> 0.2-2
- Include the license in the build RPMs

* Tue Mar 17 2015 Stephen Gallagher <sgallagh@redhat.com> 0.2-1
- Add support for namedConstraints
- Add support for subjectAltNames
- Fix packaging issues from Fedora package review

* Mon Mar 16 2015 Stephen Gallagher <sgallagh@redhat.com> 0.1-2
- Update BuildRequires

* Mon Mar 16 2015 Stephen Gallagher <sgallagh@redhat.com> 0.1-1
- First packaging
