Summary:	Bean Scripting Framework
Summary(pl):	Bean Scripting Framework - ¶rodowisko skryptowe
Name:		bsf
Version:	2.3.0
Release:	0.rc1.1
License:	Apache v1.1
Group:		Development/Languages/Java
Source0:	http://cvs.apache.org/dist/jakarta/bsf/v2.3.0rc1/src/%{name}-src-%{version}.tar.gz
# Source0-md5:	78bae3747ca5734bb7554eed6868b7da
URL:		http://jakarta.apache.org/bsf/
BuildRequires:	jacl
BuildRequires:	ant
BuildRequires:	jython
BuildRequires:	netrexx
#BuildRequires:	rhino < 1.5R4
BuildRequires:	sed >= 4.0
BuildRequires:	xalan-j
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bean Scripting Framework.

%description -l pl
Bean Scripting Framework - ¶rodowisko skryptowe.

%package doc
Summary:	Bean Scripting Framework documentation
Summary(pl):	Dokumentacja do Bean Scripting Framework
Group:		Development/Languages/Java

%description doc
Bean Scripting Framework documentation.

%description doc -l pl
Dokumentacja do Bean Scripting Framework.

%prep
%setup -q
# cleanup
rmdir ../bsf

# hack to disable rhino engine (not ready for new rhino debugger API)
sed -i -e 's/available property="rhino.present/available property="rhino.blah/' \
	src/bsf/build.xml

# jython obsoleted jpython long time ago - don't try to build
sed -i -e 's/available property="jpython.present/available property="jpython.blah/' \
	src/bsf/build.xml

%build
cd src
ant compile javadocs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install src/build/lib/bsf.jar $RPM_BUILD_ROOT%{_javadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license.txt src/{AUTHORS,CHANGES,README,TODO}
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc src/build/javadocs/*
