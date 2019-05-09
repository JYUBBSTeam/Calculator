

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

void cacl::CACLFloat::unsignedAddition(cacl::CACLFloat *ans, cacl::CACLFloat number1, cacl::CACLFloat number2) {
    ans->initialize();
    ans->integer = number1.integer + number2.integer;

    // 将number1、2的小数位中多余的数设置为零
    for (auto i = number1.decimalBit; i < MAX_OF_DECIMAL_BIT; ++i) {
        number1.decimalNum[i] = 0;
    }
    for (auto i = number2.decimalBit; i < MAX_OF_DECIMAL_BIT; ++i) {
        number2.decimalNum[i] = 0;
    }

    // 逐位相加
    int maxDecimalBit = max(number1.decimalBit, number2.decimalBit);
    for (auto j = maxDecimalBit - 1; j >= 0; --j) {
        ans->decimalNum[j] = number1.decimalNum[j] + number2.decimalNum[j];
    }

    // 统一进位，但零位不操作
    for (auto j = maxDecimalBit - 1; j > 0; --j) {
        ans->decimalNum[j - 1] += ans->decimalNum[j] / 10;
        ans->decimalNum[j] %= 10;
    }

    // 处理零位
    short tmpInteger = ans->decimalNum[0] / 10;
    ans->integer += tmpInteger;
    ans->decimalNum[0] %= 10;
    ans->decimalBit = maxDecimalBit;
}