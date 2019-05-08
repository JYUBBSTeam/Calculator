

#include "CACLFloat.hpp"

cacl::CACLFloat cacl::CACLFloat::operator+(cacl::CACLFloat number) {
    CACLFloat ans;

    // 通过两数的不同正负值来区分不同的算法
    if (this->integer.getSymbol() == number.integer.getSymbol()) {
        unsignedAddition(&ans, *this, number);
    } else {
        unsignedSubtraction(&ans, *this, number);
    }

    return ans;
}


cacl::CACLFloat cacl::CACLFloat::operator+(double number) {
    CACLFloat translatedNumber = translate(number);
    CACLFloat ans;

    ans = *this + translatedNumber;

    return ans;
}

void
cacl::CACLFloat::unsignedAddition(cacl::CACLFloat *ans, cacl::CACLFloat number1, cacl::CACLFloat number2) {
    ans->integer = number1.integer + number2.integer;


}