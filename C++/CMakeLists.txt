cmake_minimum_required(VERSION 3.0.0)
project(Cpp_python VERSION 0.1.0)
set(CMAKE_CXX_STANDARD 17)

include(CTest)
enable_testing()

set(SOURCE_FILES main.cpp)

# add_executable(${PROJECT_NAME} ${SOURCE_FILES})

add_library(${PROJECT_NAME} SHARED ${SOURCE_FILES})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
