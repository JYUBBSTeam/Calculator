cmake_minimum_required(VERSION 3.14)
project(testCACLFloat)

set(CMAKE_CXX_STANDARD 11)

add_executable(testCACLFloat test.cpp
        # CACLInteger类
        ../../CACLInteger/CACLInteger.h
        ../../CACLInteger/OperatorMultiplication.cpp
        ../../CACLInteger/IO.cpp
        ../../CACLInteger/SelfData.cpp
        ../../CACLInteger/Math.cpp
        ../../CACLInteger/OperatorAddition.cpp
        ../../CACLInteger/OperatorSubtraction.cpp
        ../../CACLInteger/OperatorComparison.cpp
        ../../CACLInteger/OperatorAssignment.cpp
        ../../CACLInteger/OperatorDivision.cpp
        ../../CACLInteger/OperatorRemainder.cpp


        # CACLFloat类
        ../../CACLFloat/CACLFloat.h
        ../../CACLFloat/IO.cpp
        ../../CACLFloat/SelfData.cpp)