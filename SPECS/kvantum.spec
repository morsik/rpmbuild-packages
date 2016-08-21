Name:		kvantum
Version:	0.10.1
Release:	1%{?dist}
Summary:	SVG-based theme engine for Qt4/Qt5 and KDE

Group:		User Interface/Desktops
License:	GPLv3
URL:		https://github.com/tsujan/Kvantum
Source0:	https://github.com/tsujan/Kvantum/archive/V%{version}.tar.gz

# BuildRequires:	
# Requires:	

%description
Kvantum is an SVG-based theme engine for Qt4/Qt5, KDE and LXQT,
with an emphasis on elegance, usability and practicality.

%prep
%setup -q -n Kvantum-%{version}/Kvantum

%package qt4
Summary: SVG-based theme engine for Qt4

%description qt4
Kvantum for Qt5. This package contains Qt4 style.

%package qt5
Summary: SVG-based theme engine for Qt5

%description qt5
Kvantum for Qt5. This package contains Qt5 style.

%package kde4
Summary: SVG-based theme engine for Qt5
BuildRequires: qt5-qtsvg-devel
Requires: qt5-qtsvg

%description kde4
Kvantum support for KDE4. This package contains KDE4 specific files
(color schemes)

%build
mkdir build-qt{4,5}

cd build-qt4
%{qmake_qt4} ..
make %{?_smp_mflags}

cd ../build-qt5
%{qmake_qt5} ..
make %{?_smp_mflags}

%install
cd build-qt4
make install INSTALL_ROOT=%{buildroot}

cd ../build-qt5
make install INSTALL_ROOT=%{buildroot}

%files qt4
/usr/lib64/qt4/plugins/styles/libkvantum.so

%files qt5
/usr/lib64/qt5/plugins/styles/libkvantum.so

%files kde4
/usr/share/kde4

%files
/usr/share/Kvantum
/usr/share/applications
/usr/share/color-schemes
/usr/share/icons
/usr/share/themes
/usr/bin



%changelog

