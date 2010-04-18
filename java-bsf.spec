%include	/usr/lib/rpm/macros.java
#
%define		pkgname	bsf
#
Summary:	Bean Scripting Framework
Summary(pl.UTF-8):	Bean Scripting Framework - środowisko skryptowe
Name:		java-%{pkgname}
Version:	2.3.0
Release:	1
License:	Apache v1.1
Group:		Development/Languages/Java
Source0:	http://cvs.apache.org/dist/jakarta/bsf/v2.3.0rc1/src/%{pkgname}-src-%{version}.tar.gz
# Source0-md5:	78bae3747ca5734bb7554eed6868b7da
URL:		http://jakarta.apache.org/bsf/
BuildRequires:	ant
BuildRequires:	jacl
BuildRequires:	jpackage-utils
BuildRequires:	java-netrexx
#BuildRequires:	java-rhino < 1.5R4
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	sed >= 4.0
BuildRequires:	java-xalan
Requires:	jpackage-utils
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

# hack to disable rhino engine (not ready for new rhino debugger API)
sed -i -e 's/available property="rhino.present/available property="rhino.blah/' \
	src/bsf/build.xml

# jython obsoleted jpython long time ago - don't try to build
sed -i -e 's/available property="jpython.present/available property="jpython.blah/' \
	src/bsf/build.xml

%build
required_jars="jacl jython NetRexxC NetRexxR xalan xsltc"
export CLASSPATH=$(build-classpath $required_jars)
%ant -f src/build.xml compile javadocs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install src/build/lib/%{pkgname}.jar $RPM_BUILD_ROOT%{_javadir}/%{pkgname}-%{version}.jar
ln -s %{pkgname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{pkgname}.jar

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{pkgname}-%{version}
cp -a src/build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{pkgname}-%{version}
ln -s %{pkgname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{pkgname} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{pkgname}-%{version} %{_javadocdir}/%{pkgname}

%files
%defattr(644,root,root,755)
%doc license.txt src/{AUTHORS,CHANGES,README,TODO}
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{pkgname}-%{version}
%ghost %{_javadocdir}/%{pkgname}
