Summary:	Bean Scripting Framework
Summary(pl):	Bean Scripting Framework - środowisko skryptowe
Name:		bsf
Version:	2.2
Release:	1
License:	IBM Public License
Group:		Development/Languages/Java
Source0:	ftp://www-126.ibm.com/pub/%{name}/%{name}-src-%{version}.tar.gz
# Source0-md5:	d694cca9ab68e9acf458509fb8c97d8f
URL:		http://www-124.ibm.com/developerworks/projects/bsf/
BuildRequires:	ibm-java-sdk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
Bean Scripting Framework.

%description -l pl
Bean Scripting Framework - środowisko skryptowe.

%package doc
Summary:	Bean Scripting Framework documentation
Summary(pl):	Dokumentacja do Bean Scripting Framework
Group:		Development/Languages/Java

%description doc
Bean Scripting Framework documentation.

%description doc -l pl
Dokumentacja do Bean Scripting Framework.

%prep
%setup -q -n bsf-2_2

%build
cd $RPM_BUILD_DIR/bsf-2_2/src
mkdir -p build/javadoc

javac com/ibm/bsf/Main.java -d build
javadoc -d build/javadoc -use -splitIndex com.ibm.bsf

cd $RPM_BUILD_DIR/bsf-2_2/src/build
jar cvf bsf.jar com

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}

install src/build/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license.html
%dir %{_javalibdir}
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc src/build/javadoc/*
