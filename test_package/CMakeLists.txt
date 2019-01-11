project(PackageTest LANGUAGES CXX)
cmake_minimum_required(VERSION 3.10.0)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(KEEP_RPATHS)

find_package(graylog-logger REQUIRED)

find_library(GRAYLOG-LOGGER_LIB graylog-logger)

add_executable(example example.cpp)
target_link_libraries(example ${GRAYLOG-LOGGER_LIB})
