add_subdirectory(components)

target_sources(${PROJECT_NAME} PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/counterjib.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/jib.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/tower.cpp)