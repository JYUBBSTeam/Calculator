cmake_minimum_required(VERSION 3.6.2)
project(testCACLFloat)

set(CMAKE_CXX_STANDARD 11)

add_executable(testCACLFloat test.cpp
        # CACLInteger类
        ../../NumberDefine/CACLInteger/CACLInteger.hpp
        ../../NumberDefine/CACLInteger/OperatorMultiplication.cpp
        ../../NumberDefine/CACLInteger/IO.cpp
        ../../NumberDefine/CACLInteger/SelfData.cpp
        ../../NumberDefine/CACLInteger/Math.cpp
        ../../NumberDefine/CACLInteger/OperatorAddition.cpp
        ../../NumberDefine/CACLInteger/OperatorSubtraction.cpp
        ../../NumberDefine/CACLInteger/OperatorComparison.cpp
        ../../NumberDefine/CACLInteger/OperatorAssignment.cpp
        ../../NumberDefine/CACLInteger/OperatorDivision.cpp
        ../../NumberDefine/CACLInteger/OperatorRemainder.cpp


        # CACLFloat类
        ../../NumberDefine/CACLFloat/CACLFloat.hpp
        ../../NumberDefine/CACLFloat/IO.cpp
        ../../NumberDefine/CACLFloat/SelfData.cpp
        ../../NumberDefine/CACLFloat/OperatorAddition.cpp
        ../../NumberDefine/CACLFloat/OperatorAssignment.cpp
        ../../NumberDefine/CACLFloat/Math.cpp
        ../../NumberDefine/CACLFloat/Precision.cpp
        ../../NumberDefine/CACLFloat/OperatorSubtraction.cpp
        ../../NumberDefine/CACLFloat/OperatorComparison.cpp
        ../../NumberDefine/CACLFloat/OperatorDivision.cpp
        ../../NumberDefine/CACLFloat/OperatorMultiplication.cpp)