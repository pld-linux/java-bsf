# NOTE: there is bsf 3.1 now, bsf 2 and bsf 3 implement different specs;
#       so move 2.4 to java-bsf2.spec and upgrade this to 3.1 or the opposite
%include	/usr/lib/rpm/macros.java
#
%define		pkgname	bsf
#
Summary:	Bean Scripting Framework
Summary(pl.UTF-8):	Bean Scripting Framework - środowisko skryptowe
Name:		java-%{pkgname}
Version:	2.4.0
Release:	1
License:	Apache v1.1
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/bsf/source/%{pkgname}-src-%{version}.tar.gz
# Source0-md5:	7e58b2a009c0f70ab36bbef420b25c07
Patch0:		%{name}-buildprops.patch
URL:		http://jakarta.apache.org/bsf/
BuildRequires:	ant
BuildRequires:	jacl
BuildRequires:	jpackage-utils
BuildRequires:	java-commons-logging
BuildRequires:	java-netrexx
BuildRequires:	java-rhino
#BuildRequires:	jython < 2.5
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	sed >= 4.0
BuildRequires:	java-xalan
Requires:	jpackage-utils
Obsoletes:	bsf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bean Scripting Framework.

%description -l pl.UTF-8
Bean Scripting Framework - środowisko skryptowe.

%package javadoc
Summary:	Bean Scripting Framework documentation
Summary(pl.UTF-8):	Dokumentacja do Bean Scripting Framework
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	bsf-doc

%description javadoc
Bean Scripting Framework documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do Bean Scripting Framework.

%prep
%setup -qn %{pkgname}-%{version}
%patch0 -p1

%build
# disabled: jython (not ready for 2.5)
required_jars="commons-logging jacl tcljava js NetRexxC NetRexxR xalan xsltc"
export CLASSPATH=$(build-classpath $required_jars)
%ant compile javadocs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install lib/%{pkgname}.jar $RPM_BUILD_ROOT%{_javadir}/%{pkgname}-%{version}.jar
ln -s %{pkgname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{pkgname}.jar

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{pkgname}-%{version}
cp -a build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{pkgname}-%{version}
ln -s %{pkgname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{pkgname} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{pkgname}-%{version} %{_javadocdir}/%{pkgname}

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt CHANGES.txt LICENSE.txt NOTICE.txt README.txt RELEASE-NOTE.txt TODO.txt
%{_javadir}/bsf-%{version}.jar
%{_javadir}/bsf.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{pkgname}-%{version}
%ghost %{_javadocdir}/%{pkgname}
