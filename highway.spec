%define debug_package %{nil}
%define devname %mklibname -d -s hwy

Summary:	C++ library for SIMD
Name:		highway
Version:	0.11.1
Release:	1
Source0:	https://github.com/google/highway/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake ninja
BuildRequires:	pkgconfig(gtest)
License:	Apache 2.0

%description
C++ library for SIMD

%package -n %{devname}
Summary:	Development files for the Highway SIMD library

%description -n %{devname}
Development files for the Highway SIMD library

%prep
%autosetup -p1
%cmake \
	-DHWY_SYSTEM_GTEST:BOOL=ON \
	-G Ninja

%build
export LD_LIBRARY_PATH=`pwd`/build/lib:$LD_LIBRARY_PATH
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{devname}
%{_includedir}/hwy
%{_includedir}/contrib
%{_libdir}/libhwy.a
%{_libdir}/pkgconfig/*.pc
