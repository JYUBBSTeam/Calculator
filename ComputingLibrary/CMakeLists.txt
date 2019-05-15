cmake_minimum_required(VERSION 3.14)
project(ComputingLibrary)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)
include_directories(CACLFloat)
include_directories(CACLInteger)
include_directories(test)

add_executable(ComputingLibrary
        CACLFloat/CACLFloat.hpp
        CACLFloat/IO.cpp
        CACLFloat/Math.cpp
        CACLFloat/OperatorAddition.cpp
        CACLFloat/OperatorAssignment.cpp
        CACLFloat/OperatorComparison.cpp
        CACLFloat/OperatorDivision.cpp
        CACLFloat/OperatorMultiplication.cpp
        CACLFloat/OperatorSubtraction.cpp
        CACLFloat/Precision.cpp
        CACLFloat/SelfData.cpp
        CACLInteger/CACLInteger.hpp
        CACLInteger/IO.cpp
        CACLInteger/Math.cpp
        CACLInteger/OperatorAddition.cpp
        CACLInteger/OperatorAssignment.cpp
        CACLInteger/OperatorComparison.cpp
        CACLInteger/OperatorDivision.cpp
        CACLInteger/OperatorMultiplication.cpp
        CACLInteger/OperatorRemainder.cpp
        CACLInteger/OperatorSubtraction.cpp
        CACLInteger/SelfData.cpp
        test/testCACLFloat/test.cpp)
