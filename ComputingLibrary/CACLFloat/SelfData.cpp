

#include "CACLFloat.hpp"

// 初始化对象
void CACLFloat::initialize() {
    integer.initialize();

    decimalBit = 0;
    for (auto &i : decimalNum) {
        i = 0;
    }
}


// 拷贝对象
void CACLFloat::copy(const CACLFloat number) {
    integer.copy(number.integer);

    for (int i = 0; i < number.decimalBit; ++i) {
        decimalNum[i] = number.decimalNum[i];
    }

    decimalBit = number.decimalBit;
}

// 将double转换为CACLFloat对象
CACLFloat CACLFloat::translate(double number) {
    CACLFloat ans;

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
bool CACLFloat::isZero() {
    return integer.isZero() && decimalBit == 0;
}

// 判断是不是负数
bool CACLFloat::isNegative() {
    return integer.isNegative();
}

// 判断是不是正数
bool CACLFloat::isPositive() {
    return integer.isPositive();
}

// 转换符号
void CACLFloat::exchangeSymbol() {
    integer.exchangeSymbol();
}