cmake_minimum_required(VERSION 3.14)
project(testCACLInteger)

set(CMAKE_CXX_STANDARD 11)

add_executable(testCACLInterger test.cpp
        ../../CACLInteger/CACLInteger.h
        ../../CACLInteger/OperatorMultiplication.cpp
        ../../CACLInteger/IO.cpp
        ../../CACLInteger/SelfData.cpp
        ../../CACLInteger/Math.cpp
        ../../CACLInteger/StructureDestruct.cpp
        ../../CACLInteger/OperatorAddition.cpp
        ../../CACLInteger/OperatorSubtraction.cpp
        ../../CACLInteger/OperatorComparison.cpp
        ../../CACLInteger/OperatorAssignment.cpp
        ../../CACLInteger/OperatorDivision.cpp)