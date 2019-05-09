cmake_minimum_required(VERSION 3.6)
project(testElementaryFunction)

set(CMAKE_CXX_STANDARD 11)

add_executable(testElementaryFunction test.cpp
        # CACLInteger类
        ../../CACLInteger/CACLInteger.hpp
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
        ../../CACLFloat/CACLFloat.hpp
        ../../CACLFloat/IO.cpp
        ../../CACLFloat/SelfData.cpp
        ../../CACLFloat/OperatorAddition.cpp
        ../../CACLFloat/OperatorAssignment.cpp
        ../../CACLFloat/Others.cpp
        ../../CACLFloat/Math.cpp
        ../../CACLFloat/Precision.cpp
        ../../CACLFloat/OperatorSubtraction.cpp


        # Interval类
        ../../ElementaryFunction/Interval/Interval.hpp
        ../../ElementaryFunction/Interval/Modify.cpp)