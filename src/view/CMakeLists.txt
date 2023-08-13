add_subdirectory(settings)

target_sources(${PROJECT_NAME} PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/CentralWidget.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/CraneTab.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/LeftSide.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/RightSide.cpp)