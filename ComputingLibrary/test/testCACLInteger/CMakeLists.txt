cmake_minimum_required(VERSION 3.6.2)
project(testCACLInteger)

set(CMAKE_CXX_STANDARD 11)

# link_directories("/usr/local/lib") #库文件目录
# link_libraries(libgmp.a libgmpxx.a libmpfr.a) # 库名

add_executable(testCACLInterger test.cpp

        ../../NumberDefine/CACLInteger/CACLInteger.hpp
        ../../NumberDefine/CACLInteger/IO.cpp
        ../../NumberDefine/CACLInteger/Math.cpp
        ../../NumberDefine/CACLInteger/OperatorAddition.cpp
        ../../NumberDefine/CACLInteger/OperatorAssignment.cpp
        ../../NumberDefine/CACLInteger/OperatorComparison.cpp
        ../../NumberDefine/CACLInteger/OperatorDivision.cpp
        ../../NumberDefine/CACLInteger/OperatorMultiplication.cpp
        ../../NumberDefine/CACLInteger/OperatorRemainder.cpp
        ../../NumberDefine/CACLInteger/OperatorSubtraction.cpp
        ../../NumberDefine/CACLInteger/SelfData.cpp)