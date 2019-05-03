cmake_minimum_required(VERSION 3.14)
project(testCACLFloat)

set(CMAKE_CXX_STANDARD 11)

add_executable(testCACLFloat test.cpp
        ../../CACLFloat/CACLFloat.h
        ../../CACLFloat/IO.cpp
        ../../CACLFloat/StructureDestruct.cpp)