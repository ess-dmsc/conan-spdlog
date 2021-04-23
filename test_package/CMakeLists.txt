project(PackageTest LANGUAGES CXX)
cmake_minimum_required(VERSION 3.10.0)

set(CMAKE_CXX_STANDARD 14)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(KEEP_RPATHS)

add_executable(example example.cpp)
message(STATUS "Libraries: ${CONAN_LIBS}")
target_link_libraries(example ${CONAN_LIBS})
