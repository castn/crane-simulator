cmake_minimum_required(VERSION 3.18)

project(mainwindow)

set(QT_MIN_VERSION "5.15.2")
set(KF5_MIN_VERSION "5.78.0")
# Instruct CMake to run moc and uic automatically when needed.
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)


find_package(ECM 1.0.0 REQUIRED NO_MODULE)
set(CMAKE_MODULE_PATH ${ECM_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/cmake)

include(KDEInstallDirs)
include(KDECMakeSettings)
include(KDECompilerSettings NO_POLICY_SCOPE)
include(FeatureSummary)

find_package(Qt5 ${QT_MIN_VERSION} CONFIG REQUIRED COMPONENTS
        Core    # QCommandLineParser, QStringLiteral
        Widgets # QApplication
        )

find_package(KF5 ${KF5_MIN_VERSION} REQUIRED COMPONENTS
        CoreAddons      # KAboutData
        I18n            # KLocalizedString
        XmlGui          # KXmlGuiWindow
        TextWidgets     # KTextEdit
        ConfigWidgets   # KStandardActions
        WidgetsAddons   # KMessageBox
        KIO             # KIO
        )
# vtk code taken from https://examples.vtk.org/site/Cxx/Qt/MinimalQtVTKApp/
find_package(VTK COMPONENTS
        CommonCore
        CommonDataModel
        FiltersSources
        GUISupportQt
        InteractionStyle
        RenderingContextOpenGL2
        RenderingCore
        RenderingFreeType
        RenderingGL2PSOpenGL2
        RenderingOpenGL2
        GUISupportQt
        RenderingQt
        )

if(NOT VTK_FOUND)
    message(FATAL_ERROR "MinimalQtVTKApp: Unable to find the VTK build folder.")
endif()

if(NOT(TARGET VTK::GUISupportQt))
    message(FATAL_ERROR "MinimalQtVTKApp: VTK not built with Qt support.")
endif()

if(NOT DEFINED VTK_QT_VERSION)
    set(VTK_QT_VERSION 5)
endif()

set(qt_components Core Gui Widgets)
if(${VTK_QT_VERSION} VERSION_GREATER_EQUAL 6)
    list(APPEND qt_components OpenGLWidgets)
endif()
list(SORT qt_components)
# vtk uses ui files, so this will also bring in the macro:
#   qt5_wrap_ui or qt_wrap_ui from Widgets.
find_package(Qt${VTK_QT_VERSION} QUIET
        REQUIRED COMPONENTS ${qt_components}
        )

foreach(_qt_comp IN LISTS qt_components)
    list(APPEND qt_modules "Qt${VTK_QT_VERSION}::${_qt_comp}")
endforeach()
# Print version numbers to cmake build output
message (STATUS "VTK_VERSION: ${VTK_VERSION}, Qt Version: ${Qt${VTK_QT_VERSION}Widgets_VERSION}")


feature_summary(WHAT ALL INCLUDE_QUIET_PACKAGES FATAL_ON_MISSING_REQUIRED_PACKAGES)

# Tell cmake where to find the source and header files from this file
set(mainwindow_SRCS src/main.cpp src/mainwindow.cpp src/view/CentralWidget.cpp src/view/CentralWidget.h src/view/CraneTab.cpp src/view/CraneTab.h)

add_executable(mainwindow ${mainwindow_SRCS})

if (Qt${VTK_QT_VERSION}Widgets_VERSION VERSION_LESS "5.11.0")
    qt5_use_modules(mainwindow ${qt_components})
else()
    target_link_libraries(mainwindow ${qt_modules})
endif()
target_link_libraries(mainwindow ${VTK_LIBRARIES})

target_link_libraries(mainwindow
        Qt5::Widgets
        KF5::CoreAddons
        KF5::I18n
        KF5::XmlGui
        KF5::TextWidgets
        KF5::ConfigWidgets
        KF5::WidgetsAddons
        KF5::KIOCore
        )

# vtk_module_autoinit is needed
vtk_module_autoinit(
        TARGETS mainwindow
        MODULES ${VTK_LIBRARIES}
)

install(TARGETS mainwindow ${KDE_INSTALL_TARGETS_DEFAULT_ARGS})
install(FILES mainwindowui.rc DESTINATION ${KDE_INSTALL_KXMLGUI5DIR}/mainwindow)