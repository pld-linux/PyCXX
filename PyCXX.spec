Summary:	Set of classes to help create extensions of Python in the C++ language
Summary(pl.UTF-8):	Klasy C++ pomocne przy tworzeniu modułów Pythona
Name:		PyCXX
Version:	7.1.7
Release:	1
License:	BSD
Group:		Development/Libraries
# http://prdownloads.sourceforge.net/cxx/pycxx-6.2.3.tar.gz
Source0:	http://downloads.sourceforge.net/cxx/pycxx-%{version}.tar.gz
# Source0-md5:	b145c3444f66e129fc2fac9924855439
URL:		http://cxx.sourceforge.net/
BuildRequires:	python-modules
Requires:	libstdc++-devel
BuildArch:	noarch
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

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py3_incdir}/CXX
%{py3_prefix}/share/python%{py3_ver}/CXX
%{py3_sitescriptdir}/CXX-%{version}-py*.egg-info
%{py3_sitescriptdir}/CXX
