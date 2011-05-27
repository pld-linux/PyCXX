# TODO: Find out authors idea behind installing it properly and try implement it
# Propably it shoud be library thus not marked as noarch.

Summary:	Set of classes to help create extensions of Python in the C++ language
Summary(pl.UTF-8):	Klasy C++ pomocne przy tworzeniu modułów Pythona
Name:		PyCXX
Version:	6.2.3
Release:	1
License:	BSD
Group:		Development/Libraries
# http://prdownloads.sourceforge.net/cxx/pycxx-6.2.3.tar.gz
Source0:	http://downloads.sourceforge.net/cxx/pycxx-%{version}.tar.gz
# Source0-md5:	4e545ad225df9c14a3b344b1e6224661
URL:		http://cxx.sourceforge.net/
BuildRequires:	python-modules
Requires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyCXX is a set of classes to help create extensions of Python in the
C++ language. The first part encapsulates the Python C API taking care
of exceptions and ref counting. The second part supports the building
of Python extension modules in C++.

%description -l pl.UTF-8
PyCXX jest zbiorem klas pomagających tworzorzyć moduły rozszerzeń
Pythona w języku C++. Pierwsza część hermetyzuje interfejs C Pythona
dbając o wyjątki i zliczanie refrencji. Druga wspiera budowanie
modułów rozszerzeń Pythona.

%prep
%setup -q -n pycxx-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_includedir}/
cp -r CXX $RPM_BUILD_ROOT%{_includedir}/
install -d $RPM_BUILD_ROOT%{_includedir}/CXX/Src
install Src/IndirectPythonInterface.cxx  $RPM_BUILD_ROOT%{_includedir}/CXX/Src
install Src/Python2/*  $RPM_BUILD_ROOT%{_includedir}/CXX/Src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%defattr(644,root,root,755)
%{_includedir}/CXX
