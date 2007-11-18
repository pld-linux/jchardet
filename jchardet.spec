%include	/usr/lib/rpm/macros.java
Summary:	Java port of Mozilla's automatic charset detection algorithm
Name:		jchardet
Version:	1.0
Release:	0.1
License:	MPL 1.1
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/jchardet/chardet.zip
# Source0-md5:	4091d24451ee9a840933bce34b9e3a55
URL:		http://jchardet.sourceforge.net/
BuildRequires:	ant
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
chardet is a Java port of the source from Mozilla's automatic charset
detection algorithm. The original author is Frank Tang. What is
available here is the Java port of that code.

The original source in C++ can be found from
<http://lxr.mozilla.org/mozilla/source/intl/chardet/>.

More information can be found at
<http://www.mozilla.org/projects/intl/chardet.html>.

%prep
%setup -qc

%build
cd mozilla/intl/chardet/java
%ant

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
# install jar
cp -a mozilla/intl/chardet/java/dist/lib/chardet.jar $RPM_BUILD_ROOT%{_javadir}/chardet-%{version}.jar
ln -s chardet-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/chardet.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar