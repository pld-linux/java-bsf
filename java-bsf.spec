Summary:	Bean Scripting Framework
Summary(pl):	Bean Scripting Framework - ¶rodowisko skryptowe
Name:		bsf
Version:	2.3.0
Release:	0.rc1.1
License:	IBM Public License
Group:		Development/Languages/Java
Source0:	http://cvs.apache.org/dist/jakarta/bsf/v2.3.0rc1/src/%{name}-src-%{version}.tar.gz
# Source0-md5:	78bae3747ca5734bb7554eed6868b7da
URL:		http://jakarta.apache.org/bsf/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

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
