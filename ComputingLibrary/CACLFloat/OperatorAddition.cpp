

#include "CACLFloat.hpp"

cacl::CACLFloat cacl::CACLFloat::operator+(cacl::CACLFloat number) {
    CACLFloat ans;

    ans.integer = this->integer + number.integer;

    // 处理小数点部分


    return ans;
}


cacl::CACLFloat cacl::CACLFloat::operator+(double number) {
    CACLFloat translatedNumber = translate(number);
    CACLFloat ans;

    ans = *this + translatedNumber;

    return ans;
}

