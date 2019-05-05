

#include "CACLFloat.h"

// 初始化对象
void cacl::CACLFloat::initialize() {
    integer.initialize();

    decimalBit = 0;
}


// 拷贝对象
void cacl::CACLFloat::copy(const cacl::CACLFloat number) {
    integer.copy(number.integer);

    for (int i = 0; i < number.decimalBit; ++i) {
        decimalNum[i] = number.decimalNum[i];
    }

    decimalBit = number.decimalBit;
}

// 将double转换为CACLFloat对象
cacl::CACLFloat cacl::CACLFloat::translate(double number) {
    cacl::CACLFloat ans;

    ans.integer = integer.translate((long long) number);

    number -= (long long) number;
    for (int i = 0; number > MIN_OF_TRANSLATE_DECIMAL_BIT; ++i) {
        number *= 10;
        ans.decimalNum[i] = (long long) number;
        ans.decimalBit++;
        number -= (long long) number;
    }

    return ans;
}

// 判断是不是零
bool cacl::CACLFloat::isZero() {
    return integer.isZero() && decimalBit == 0;
}

// 判断是不是负数
bool cacl::CACLFloat::isNegative() {
    return integer.isNegative();
}

// 判断是不是正数
bool cacl::CACLFloat::isPositive() {
    return integer.isPositive();
}

// 转换符号
void cacl::CACLFloat::exchangeSymbol() {
    integer.exchangeSymbol();
}