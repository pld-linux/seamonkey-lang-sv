Summary:	sv-SE resources for SeaMonkey
Summary(pl):	sv-SE pliki j�zykowe dla SeaMonkeya
Name:		seamonkey-lang-sv
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.sv-SE.langpack.xpi
# Source0-md5:	163d0b0fafbdeaa816eb664fce766b04
Source1:	gen-installed-chrome.sh
URL:		http://www.mozilla.org/projects/seamonkey/
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
sv-SE resources for SeaMonkey.

%description -l pl
sv-SE pliki j�zykowe dla SeaMonkeya.

%prep
%setup -q -c -T
unzip %{SOURCE0}
install %{SOURCE1} .
./gen-installed-chrome.sh locale chrome/{SE,sv-SE,sv-unix}.jar > lang-sv-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install chrome/{SE,sv-SE,sv-unix}.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-sv-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r defaults $RPM_BUILD_ROOT%{_datadir}/seamonkey

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/sv-SE.jar
%{_chromedir}/sv-unix.jar
%{_chromedir}/SE.jar
%{_chromedir}/lang-sv-installed-chrome.txt
%{_datadir}/seamonkey/defaults/messenger/SE
%{_datadir}/seamonkey/defaults/profile/SE
