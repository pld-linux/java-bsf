Summary:	Bean Scripting Framework
Summary(pl.UTF-8):	Bean Scripting Framework - środowisko skryptowe
Name:		bsf
Version:	2.3.0
Release:	5
License:	Apache v1.1
Group:		Development/Languages/Java
Source0:	http://cvs.apache.org/dist/jakarta/bsf/v2.3.0rc1/src/%{name}-src-%{version}.tar.gz
# Source0-md5:	78bae3747ca5734bb7554eed6868b7da
URL:		http://jakarta.apache.org/bsf/
BuildRequires:	ant
BuildRequires:	jacl
BuildRequires:	jpackage-utils
BuildRequires:	netrexx
#BuildRequires:	rhino < 1.5R4
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	sed >= 4.0
BuildRequires:	xalan-j
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bean Scripting Framework.

%description -l pl.UTF-8
Bean Scripting Framework - środowisko skryptowe.

%package javadoc
Summary:	Bean Scripting Framework documentation
Summary(pl.UTF-8):	Dokumentacja do Bean Scripting Framework
Group:		Development/Languages/Java
Requires:	jpackage-utils
Obsoletes:	bsf-doc

%description javadoc
Bean Scripting Framework documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do Bean Scripting Framework.

%prep
%setup -q

# hack to disable rhino engine (not ready for new rhino debugger API)
sed -i -e 's/available property="rhino.present/available property="rhino.blah/' \
	src/bsf/build.xml

# jython obsoleted jpython long time ago - don't try to build
sed -i -e 's/available property="jpython.present/available property="jpython.blah/' \
	src/bsf/build.xml

%build
export CLASSPATH="`build-classpath jacl jython NetRexxC NetRexxR xalan xsltc`"
export JAVA_HOME="%{java_home}"
cd src
%ant compile javadocs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}/%{name}-%{version}}

install src/build/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

cp -R src/build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license.txt src/{AUTHORS,CHANGES,README,TODO}
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%doc %{_javadocdir}/%{name}-%{version}
