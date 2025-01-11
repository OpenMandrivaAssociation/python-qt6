%define _disable_lto 1
%define _disable_ld_no_undefined 1
%define major %(echo %{version} |cut -d. -f1-2)
%define _debugsource_packages 0
%global _debugsource_template %{nil}

Summary:	Set of Python bindings for Trolltech's Qt application framework
Name:		python-qt6
Version:	6.8.0
Release:	1
License:	GPLv2+
Group:		Development/KDE and Qt
Url:		https://www.riverbankcomputing.co.uk/software/pyqt/intro
Source0:	https://files.pythonhosted.org/packages/source/P/PyQt6/PyQt6-%{version}.tar.gz
Patch1:		pyqt6-workaround-qttest-detection.patch

BuildRequires:	python-sip >= 5.1.0
BuildRequires:	python-sip-qt6
BuildRequires:	python-qt-builder
BuildRequires:	qmake-qt6
BuildRequires:	qt6-cmake
BuildRequires:	glibc-devel
BuildRequires:	sed
BuildRequires:	pkgconfig(dbus-python)
BuildRequires:	pkgconfig(python3)
BuildRequires:	cmake(Qt6Bluetooth)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Nfc)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Designer)
BuildRequires:	cmake(Qt6UiPlugin)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Location)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6MultimediaWidgets)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6Pdf)
BuildRequires:	cmake(Qt6PdfWidgets)
BuildRequires:	cmake(Qt6Positioning)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6RemoteObjects)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6QmlModels)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Quick3D)
BuildRequires:	cmake(Qt6Quick3DParticleEffects)
BuildRequires:	cmake(Qt6Quick3DEffects)
BuildRequires:	cmake(Qt6Quick3DHelpers)
BuildRequires:	cmake(Qt6Quick3DParticles)
BuildRequires:	cmake(Qt6Quick3DAssetUtils)
BuildRequires:	cmake(Qt6Quick3DAssetImport)
BuildRequires:	cmake(Qt6Quick3DGlslParserPrivate)
BuildRequires:	cmake(Qt6Quick3DIblBaker)
BuildRequires:	cmake(Qt6Quick3DRuntimeRender)
BuildRequires:	cmake(Qt6Quick3DUtils)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Help)
BuildRequires:	cmake(Qt6SerialPort)
BuildRequires:	cmake(Qt6SpatialAudio)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6SvgWidgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6TextToSpeech)
BuildRequires:	cmake(Qt6WebChannel)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qt6WebSockets)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Sensors)
BuildRequires:	cmake(Qt6ShaderTools)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(dri)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(libpcre2-16)
BuildRequires:	pkgconfig(libzstd)
BuildRequires:	cmake(double-conversion)
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-dbus = %{EVRD}
Requires:	%{name}-bluetooth = %{EVRD}
Requires:	%{name}-designer = %{EVRD}
Requires:	%{name}-gui = %{EVRD}
Requires:	%{name}-multimedia = %{EVRD}
Requires:	%{name}-multimediawidgets = %{EVRD}
Requires:	%{name}-network = %{EVRD}
Requires:	%{name}-opengl = %{EVRD}
Requires:	%{name}-positioning = %{EVRD}
Requires:	%{name}-printsupport = %{EVRD}
Requires:	%{name}-remoteobjects = %{EVRD}
Requires:	%{name}-qml = %{EVRD}
Requires:	%{name}-quick = %{EVRD}
Requires:	%{name}-quickwidgets = %{EVRD}
Requires:	%{name}-sensors = %{EVRD}
Requires:	%{name}-serialport = %{EVRD}
Requires:	%{name}-sql = %{EVRD}
Requires:	%{name}-svg = %{EVRD}
Requires:	%{name}-test = %{EVRD}
Requires:	%{name}-webchannel = %{version}
Requires:	%{name}-websockets = %{EVRD}
Requires:	%{name}-widgets = %{EVRD}
Requires:	%{name}-xml = %{EVRD}
Provides:	PyQt6 = %{EVRD}

%description
PyQt is a set of Python bindings for Trolltech's Qt application framework.

%files

#------------------------------------------------------------

%package core
Summary:	PyQt 6 core
Group:		Development/KDE and Qt
Requires:	python-sip-qt6

%description core
PyQt 6 core.

%files core
%dir %{py_platsitedir}/PyQt6
%{py_platsitedir}/PyQt6/QtCore.abi3.so
%{py_platsitedir}/PyQt6/__init__.py
%{py_platsitedir}/PyQt6/bindings/QtCore/pyqt-gpl.sip5
%{py_platsitedir}/PyQt6-*.dist-info

#------------------------------------------------------------

%package dbus
Summary:	PyQt 6 dbus
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}
Requires:	python3dist(dbus-python)

%description dbus
PyQt 6 dbus.

%files dbus
%{py_platsitedir}/PyQt6/QtDBus.abi3.so
%{py_platsitedir}/dbus/mainloop/pyqt6.abi3.so

#------------------------------------------------------------

%package designer
Summary:	PyQt 6 designer
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description designer
PyQt 6 designer.

%files designer
%{py_platsitedir}/PyQt6/QtDesigner.abi3.so

#------------------------------------------------------------

%package bluetooth
Summary:	PyQt 6 bluetooth
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description bluetooth
PyQt 6 bluetooth.

%files bluetooth
%{py_platsitedir}/PyQt6/QtBluetooth.abi3.so

#------------------------------------------------------------

%package gui
Summary:	PyQt 6 gui
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description gui
PyQt 6 gui.

%files gui
%{py_platsitedir}/PyQt6/QtGui.abi3.so

#------------------------------------------------------------

%package network
Summary:	PyQt 6 network
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description network
PyQt 6 network.

%files network
%{py_platsitedir}/PyQt6/QtNetwork.abi3.so

#------------------------------------------------------------

%package multimedia
Summary:	PyQt 6 multimedia
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description multimedia
PyQt 6 multimedia.

%files multimedia
%{py_platsitedir}/PyQt6/QtMultimedia.abi3.so

#------------------------------------------------------------

%package opengl
Summary:	PyQt 6 opengl
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description opengl
PyQt 6 opengl.

%files opengl
%{py_platsitedir}/PyQt6/QtOpenGL.abi3.so
%{py_platsitedir}/PyQt6/QtOpenGLWidgets.abi3.so

#------------------------------------------------------------

%package positioning
Summary:	PyQt 6 positioning
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description positioning
PyQt 6 positioning.

%files positioning
%{py_platsitedir}/PyQt6/QtPositioning.abi3.so

#------------------------------------------------------------

%package printsupport
Summary:	PyQt 6 printsupport
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description printsupport
PyQt 6 printsupport

%files printsupport
%{py_platsitedir}/PyQt6/QtPrintSupport.abi3.so

#------------------------------------------------------------

%package qml
Summary:	PyQt 6 qml
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description qml
PyQt 6 qml.

%files qml
%{py_platsitedir}/PyQt6/QtQml.abi3.so

#------------------------------------------------------------

%package quick
Summary:	PyQt 6 quick
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description quick
PyQt 6 quick.

%files quick
%{py_platsitedir}/PyQt6/QtQuick.abi3.so
%{py_platsitedir}/PyQt6/QtQuick3D.abi3.so

#------------------------------------------------------------

%package quickwidgets
Summary:	PyQt 6 quickwidgets
Group:		Development/KDE and Qt
Requires:	%{name}-quick = %{EVRD}

%description quickwidgets
PyQt 6 quickwidgets.

%files quickwidgets
%{py_platsitedir}/PyQt6/QtQuickWidgets.abi3.so

#------------------------------------------------------------

%package serialport
Summary:	PyQt 6 serialport
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description serialport
PyQt 6 serialport.

%files serialport
%{py_platsitedir}/PyQt6/QtSerialPort.abi3.so

#------------------------------------------------------------
%package spatialaudio
Summary:	PyQt 6 Spatial Audio module
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description spatialaudio
PyQt 6 Spatial Audio module

%files spatialaudio
%{py_platsitedir}/PyQt6/QtSpatialAudio.abi3.so

#------------------------------------------------------------

%package sql
Summary:	PyQt 6 sql
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description sql
PyQt 6 sql.

%files sql
%{py_platsitedir}/PyQt6/QtSql.abi3.so

#------------------------------------------------------------

%package svg
Summary:	PyQt 6 svg
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description svg
PyQt 6 svg.

%files svg
%{py_platsitedir}/PyQt6/QtSvg.abi3.so

#------------------------------------------------------------

%package svg-widgets
Summary:	PyQt 6 SVG widgets
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description svg-widgets
PyQt 6 SVG widgets

%files svg-widgets
%{py_platsitedir}/PyQt6/QtSvgWidgets.abi3.so

#------------------------------------------------------------

%package test
Summary:	PyQt 6 test
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description test
PyQt 6 test.

%files test
%{py_platsitedir}/PyQt6/QtTest.abi3.so

#------------------------------------------------------------
%package texttospeech
Summary:	PyQt 6 Text-to-Speech module
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description texttospeech
PyQt 6 Text-to-Speech module

%files texttospeech
%{py_platsitedir}/PyQt6/QtTextToSpeech.abi3.so

#------------------------------------------------------------

%package webchannel
Summary:	PyQt 6 webchannel
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description   webchannel
PyQt 6 webchannel.

%files webchannel
%{py_platsitedir}/PyQt6/QtWebChannel.abi3.so

#------------------------------------------------------------

%package websockets
Summary:	PyQt 6 WebSockets
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description websockets
PyQt 6 websockets.

%files websockets
%{py_platsitedir}/PyQt6/QtWebSockets.abi3.so


#------------------------------------------------------------

%package widgets
Summary:	PyQt 6 widgets
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description widgets
PyQt 6 widgets.

%files widgets
%{py_platsitedir}/PyQt6/QtWidgets.abi3.so

#------------------------------------------------------------

%package xml
Summary:	PyQt 6 xml
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description xml
PyQt 6 xml.

%files xml
%{py_platsitedir}/PyQt6/QtXml.abi3.so

#------------------------------------------------------------

%package devel
Summary:	PyQt 6 devel
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}
Suggests:	qt6-qttools-designer

%description devel
PyQt 6 devel utilities.

%files devel
%{_bindir}/pyuic6
%{_bindir}/pylupdate6
%{py_platsitedir}/PyQt6/lupdate
%{py_platsitedir}/PyQt6/bindings/*/*.sip
%{py_platsitedir}/PyQt6/bindings/*/*.toml
%{py_platsitedir}/PyQt6/uic
%{_libdir}/qt6/plugins/PyQt6/libpyqt6qmlplugin.so
%{_libdir}/qt6/plugins/designer/libpyqt6.so
%{_datadir}/sip/PyQt6

#------------------------------------------------------------

%package help
Summary:	PyQt 6 Help module
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description help
PyQt 6 Help module

%files help
%{py_platsitedir}/PyQt6/QtHelp.abi3.so

#------------------------------------------------------------

%package multimediawidgets
Summary:	PyQt 6 multimedia widgets
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-multimedia = %{EVRD}

%description multimediawidgets
PyQt 6 multimedia widgets

%files multimediawidgets
%{py_platsitedir}/PyQt6/QtMultimediaWidgets.abi3.so

#------------------------------------------------------------

%package nfc
Summary:	PyQt 6 NFC
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description nfc
PyQt 6 NFC

%files nfc
%{py_platsitedir}/PyQt6/QtNfc.abi3.so

#------------------------------------------------------------

%package pdf
Summary:	PyQt 6 PDF
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description pdf
PyQt 6 PDF

%files pdf
%{py_platsitedir}/PyQt6/QtPdf.abi3.so
%{py_platsitedir}/PyQt6/QtPdfWidgets.abi3.so

#------------------------------------------------------------

%package remoteobjects
Summary:	PyQt 6 Remote Objects
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description remoteobjects
PyQt 6 Remote Objects

%files remoteobjects
%{py_platsitedir}/PyQt6/QtRemoteObjects.abi3.so

#------------------------------------------------------------

%package sensors
Summary:	PyQt 6 sensor interfaces
Group:		Development/KDE and Qt
Requires:	%{name}-core = %{EVRD}

%description sensors
PyQt 6 sensor interfaces

%files sensors
%{py_platsitedir}/PyQt6/QtSensors.abi3.so

%prep
%autosetup -n PyQt6-%{version} -p1

export QTDIR=%{_qtdir}
export PATH=%{_qtdir}/bin:$PATH
sip-build \
	--no-make \
	--confirm-license \
	--verbose \
	--dbus %{_includedir}/dbus-1.0 \
	--qmake-setting 'QMAKE_CFLAGS_RELEASE="%{optflags}"' \
	--qmake-setting 'QMAKE_CXXFLAGS_RELEASE="%{optflags} -DQT_NO_INT128"' \
	--qmake-setting 'QMAKE_LFLAGS_RELEASE="%{ldflags}"'

find . -name Makefile |xargs sed -i -e 's,-L/usr/lib64 , ,g;s,-L/usr/lib , ,g'

%build
%make_build -C build

%install
%make_install -C build INSTALL_ROOT=%{buildroot}

rm -rf %{buildroot}%{python_sitearch}/PyQt6/uic/port_v2

# ensure .so modules are executable for proper -debuginfo extraction
for i in %{buildroot}%{python_sitearch}/PyQt6/*.so ; do
    chmod a+rx $i
done

# Compatibility with sip 4.x
mkdir -p %{buildroot}%{_datadir}/sip
ln -s %{python_sitearch}/PyQt6/bindings %{buildroot}%{_datadir}/sip/PyQt6
