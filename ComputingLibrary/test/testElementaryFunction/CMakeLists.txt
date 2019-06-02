cmake_minimum_required(VERSION 3.6)
project(testElementaryFunction)

set(CMAKE_CXX_STANDARD 11)

add_executable(testElementaryFunction testForRegion.cpp
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
        ../../CACLFloat/Math.cpp
        ../../CACLFloat/Precision.cpp
        ../../CACLFloat/OperatorDivision.cpp
        ../../CACLFloat/OperatorSubtraction.cpp


        # Interval类
        ../../ElementaryFunction/Domain/Interval.hpp
        ../../ElementaryFunction/Domain/BasicallyModify.cpp
        ../../ElementaryFunction/Region.hpp
        ../../ElementaryFunction/Range/Interval.hpp ../../ElementaryFunction/Domain/Others.cpp)