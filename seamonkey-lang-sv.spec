Summary:	Swedish resources for SeaMonkey
Summary(pl):	Szwedzkie pliki jêzykowe dla SeaMonkeya
Name:		seamonkey-lang-sv
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.sv-SE.langpack.xpi
# Source0-md5:	163d0b0fafbdeaa816eb664fce766b04
Source1:	http://www.mozilla-enigmail.org/downloads/lang/0.9x/enigmail-sv-SE-0.9x.xpi
# Source1-md5:	8850c1eab91e441d30a2e536b3b31a3b
Source2:	gen-installed-chrome.sh
URL:		http://www.mozilla.org/projects/seamonkey/
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
Swedish resources for SeaMonkey.

%description -l pl
Szwedzkie pliki jêzykowe dla SeaMonkeya.

%prep
%setup -q -c
unzip -o %{SOURCE1}
install %{SOURCE2} .
./gen-installed-chrome.sh locale chrome/{SE,sv-SE,sv-unix,enigmail-sv-SE}.jar \
	> lang-sv-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install chrome/{SE,sv-SE,sv-unix,enigmail-sv-SE}.jar $RPM_BUILD_ROOT%{_chromedir}
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
%{_chromedir}/SE.jar
%{_chromedir}/sv-SE.jar
%{_chromedir}/sv-unix.jar
%{_chromedir}/enigmail-sv-SE.jar
%{_chromedir}/lang-sv-installed-chrome.txt
%{_datadir}/seamonkey/defaults/messenger/SE
%{_datadir}/seamonkey/defaults/profile/SE
