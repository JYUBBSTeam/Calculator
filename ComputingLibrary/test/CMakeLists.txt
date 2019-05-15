cmake_minimum_required(VERSION 3.14)
project(test)

set(CMAKE_CXX_STANDARD 14)

include_directories(testCACLFloat)
include_directories(testCACLInteger)

add_executable(test
        testCACLFloat/cmake-build-debug/cmake_install.cmake
        testCACLFloat/cmake-build-debug/CMakeCache.txt
        testCACLFloat/cmake-build-debug/Makefile
        testCACLFloat/cmake-build-debug/testCACLFloat
        testCACLFloat/cmake-build-debug/testCACLFloat.cbp
        testCACLFloat/cmake-build-debug/testCACLFloat.exe
        testCACLFloat/CMakeLists.txt
        testCACLFloat/test.cpp
        testCACLInteger/cmake-build-debug/cmake_install.cmake
        testCACLInteger/cmake-build-debug/CMakeCache.txt
        testCACLInteger/cmake-build-debug/Makefile
        testCACLInteger/cmake-build-debug/testCACLInteger.cbp
        testCACLInteger/cmake-build-debug/testCACLInterger.exe
        testCACLInteger/CMakeLists.txt
        testCACLInteger/test.cpp)
