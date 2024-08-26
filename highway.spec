%define major 1
%define shortname hwy
%define libname %mklibname %{shortname}
%define devname %mklibname %{shortname} -d

Summary: Performance-portable, length-agnostic SIMD with runtime dispatch
Name:    highway
Version: 1.2.0
Release: 1
License: Apache 2.0
Group:   System/Libraries
URL:     https://github.com/google/highway
Source0: https://github.com/google/highway/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: ninja
BuildRequires: atomic-devel
BuildRequires: pkgconfig(gtest)

%description
Highway is a C++ library that provides portable SIMD/vector intrinsics.

%package -n %{libname}
Summary:  %{summary}
Group:    %{group}
Provides: %{name} = %{version}-%{release}

%description -n %{libname}
This package contains the %{name} runtime libraries.

%package -n %{devname}
Summary:  %{summary}
Group:    %{group}
Requires: %{libname} = %{version}-%{release}

%description -n %{devname}
This package contains the %{name} development headers and libraries.

%prep
%autosetup
%cmake -G Ninja \
       -DHWY_SYSTEM_GTEST=ON

%build
export LD_LIBRARY_PATH=`pwd`/build/lib:$LD_LIBRARY_PATH
%ninja_build -C build

%check
export LD_LIBRARY_PATH=`pwd`/build/lib:$LD_LIBRARY_PATH
%ninja_test -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/lib%{shortname}*.so.%{major}*

%files -n %{devname}
%doc README.md g3doc/* %{shortname}/examples
%license LICENSE
%{_libdir}/lib%{shortname}*.so
%{_includedir}/%{shortname}
%{_libdir}/pkgconfig/lib%{shortname}*
%{_libdir}/cmake/hwy
