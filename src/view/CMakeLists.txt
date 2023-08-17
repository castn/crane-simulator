add_subdirectory(render)
add_subdirectory(settings)

target_sources(${PROJECT_NAME} PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/maincontent.cpp
        settings/cranesettings.cpp
        render/renderer.cpp)