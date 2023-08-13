# Add all subdirectories of src/
add_subdirectory(crane)
add_subdirectory(util)
add_subdirectory(view)

target_sources(${PROJECT_NAME} PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/main.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/mainwindow.cpp)