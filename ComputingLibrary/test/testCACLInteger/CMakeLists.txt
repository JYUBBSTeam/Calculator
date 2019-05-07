cmake_minimum_required(VERSION 3.6.2)
project(testCACLInteger)

set(CMAKE_CXX_STANDARD 11)

# link_directories("/usr/local/lib") #库文件目录
# link_libraries(libgmp.a libgmpxx.a libmpfr.a) # 库名

add_executable(testCACLInterger test.cpp

        ../../CACLInteger/CACLInteger.hpp
        ../../CACLInteger/IO.cpp
        ../../CACLInteger/Math.cpp
        ../../CACLInteger/OperatorAddition.cpp
        ../../CACLInteger/OperatorAssignment.cpp
        ../../CACLInteger/OperatorComparison.cpp
        ../../CACLInteger/OperatorDivision.cpp
        ../../CACLInteger/OperatorMultiplication.cpp
        ../../CACLInteger/OperatorRemainder.cpp
        ../../CACLInteger/OperatorSubtraction.cpp
        ../../CACLInteger/SelfData.cpp)