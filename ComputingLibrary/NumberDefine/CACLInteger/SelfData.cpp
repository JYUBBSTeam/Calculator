/*
 *创建人：Huang
 *创建日期：2019.4.19
 *修改日期：2019.7.19
 *类：CACLInteger
 *功能：初始化函数initialize()；拷贝函数copy()；转换数字为CACLInteger对象函数translate()
 */


#include "CACLInteger.hpp"


// 初始化对象
void CACLInteger::initialize() {
    for (int i = 0; i < MAX_OF_BIT; ++i) {
        this->num[i] = 0;
    }
    bit = 1;
    symbol = false;
}


// 拷贝对象
void CACLInteger::copy(const CACLInteger number) {
    for (int i = 0; i < MAX_OF_BIT; ++i) {
        num[i] = number.num[i];
    }

    bit = number.bit;
    symbol = number.symbol;
}


// 转换string为CACLInteger
CACLInteger CACLInteger::translate(std::string number) {
    CACLInteger ans;
    ans.initialize();

    int symbolLocation = 0;
    if (number.at(0) == '-') {
        ans.symbol = true;
        symbolLocation = 1;
    } else if (number.at(0) == '+') {
        ans.symbol = false;
        symbolLocation = 1;
    } else {
        ans.symbol = false;
    }

    ans.bit = number.length() - symbolLocation;

    // number对ans进行逐位对应赋值
    for (int i = 0 + symbolLocation; i < number.length(); ++i) {
        ans.num[i] = (u_int8_t) (number.at(i) - '0');
    }

    return ans;
}


// 判断是不是零
bool CACLInteger::isZero() {
    return this->bit == 1 && this->num[0] == 0;
}


// 判断是不是负数
bool CACLInteger::isNegative() {
    return symbol;
}


// 判断是不是正数
bool CACLInteger::isPositive() {
    return !symbol;
}


// 获取位数
const int CACLInteger::getBit() {
    return bit;
}

// 转换符号
void CACLInteger::exchangeSymbol() {
    symbol = !symbol;
}

// 获取正负值
bool CACLInteger::getSymbol() {
    return this->symbol;
}

// 设置符号
void CACLInteger::setSymbol(bool target) {
    symbol = target;
}