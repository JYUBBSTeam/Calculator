cmake_minimum_required(VERSION 3.14)
project(test)

set(CMAKE_CXX_STANDARD 11)

add_executable(test ComputingLibrary/test/test/test.cpp
        ComputingLibrary/ComputingLibrary/ComputingLibrary/CACLInteger.h
        ComputingLibrary/ComputingLibrary/ComputingLibrary/Operator.cpp
        ComputingLibrary/ComputingLibrary/ComputingLibrary/IO.cpp
        ComputingLibrary/ComputingLibrary/ComputingLibrary/SelfData.cpp
        ComputingLibrary/ComputingLibrary/ComputingLibrary/Math.cpp
        ComputingLibrary/ComputingLibrary/ComputingLibrary/StructureDestruct.cpp
        )