cmake_minimum_required(VERSION 2.8.11)
project(cmake_wrapper)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(KEEP_RPATHS TARGETS)

add_subdirectory("source_subfolder")
