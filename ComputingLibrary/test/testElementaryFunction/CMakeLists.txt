cmake_minimum_required(VERSION 3.6)
project(testElementaryFunction)

set(CMAKE_CXX_STANDARD 11)

add_executable(testElementaryFunction testForRegion.cpp
        # 数字类的总声明头文件
        ../../NumberDefine/Number.hpp

        # CACLInteger类
        ../../NumberDefine/Number.hpp
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
        ../../NumberDefine/CACLFloat/OperatorDivision.cpp
        ../../NumberDefine/CACLFloat/OperatorSubtraction.cpp
        ../../NumberDefine/CACLFloat/OperatorComparison.cpp
        ../../NumberDefine/CACLFloat/OperatorMultiplication.cpp


        # Interval类
        ../../ElementaryFunction/Region.hpp
        # Domain
        ../../ElementaryFunction/Domain/Interval.hpp
        ../../ElementaryFunction/Domain/BasicallyModify.cpp
        ../../ElementaryFunction/Domain/Others.cpp
        # Region
        ../../ElementaryFunction/Range/Interval.hpp
        )