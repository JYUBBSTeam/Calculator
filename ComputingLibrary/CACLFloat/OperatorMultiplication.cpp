
#include "CACLFloat.hpp"

cacl::CACLFloat cacl::CACLFloat::operator*(cacl::CACLFloat number) {
    CACLFloat ans;
    ans.initialize();

    ans.integer = this->integer * number.integer;
    // 利用无符号小数乘法
    unsignedMultiplication(&ans, *this, number);

    return ans;
}

cacl::CACLFloat cacl::CACLFloat::operator*(double number) {
    CACLFloat translatedNumber = translate(number);
    CACLFloat ans;

    ans = *this * translatedNumber;

    return ans;
}

void cacl::CACLFloat::unsignedMultiplication(cacl::CACLFloat *ans, cacl::CACLFloat number1, cacl::CACLFloat number2) {
    CACLFloat longer, shorter;

    if (number1.decimalBit > number2.decimalBit) {
        longer = number1;
        shorter = number2;
    } else {
        longer = number2;
        shorter = number1;
    }

    // 短位小数补位
    for (int i = shorter.decimalBit; i < longer.decimalBit; ++i) {
        shorter.decimalNum[i] = 1;
    }
    
}