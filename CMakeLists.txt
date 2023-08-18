cmake_minimum_required(VERSION 3.23)

project(mainwindow)

set(QT_MIN_VERSION "5.15.2")
set(KF5_MIN_VERSION "5.78.0")

# Instruct CMake to run moc and uic automatically when needed.
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

# C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Create main executable
add_executable(${PROJECT_NAME} ${SRC_FILES} ${LIB_SRC})

# Collect source files
add_subdirectory(src)

# Headers are in src/
target_include_directories(${PROJECT_NAME} PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/src")

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

# library meant for numerical analysis with multi-dimensional array expressions
find_package(xtl REQUIRED)
find_package(xtensor REQUIRED)
find_package(Eigen3 REQUIRED)
if(MSVC)
    set(CMAKE_EXE_LINKER_FLAGS /MANIFEST:NO)
endif()
include_directories(${xtensor_INCLUDE_DIRS})
target_link_libraries(mainwindow ${xtensor_LIBRARIES})
include_directories(${Eigen3_INCLUDE_DIRS})
target_link_libraries(mainwindow ${Eigen3_LIBRARIES})


feature_summary(WHAT ALL INCLUDE_QUIET_PACKAGES FATAL_ON_MISSING_REQUIRED_PACKAGES)

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

#target_include_directories(mainwindow PUBLIC ${xtensor_INCLUDE_DIRS})

# vtk_module_autoinit is needed
vtk_module_autoinit(
        TARGETS mainwindow
        MODULES ${VTK_LIBRARIES}
)

install(TARGETS mainwindow ${KDE_INSTALL_TARGETS_DEFAULT_ARGS})
install(FILES mainwindowui.rc DESTINATION ${KDE_INSTALL_KXMLGUI5DIR}/mainwindow)