/*
 *创建人：Huang
 *创建日期：2019.4.19
 *修改日期：2019.4.20
 *类：CACLInteger
 *功能：初始化函数initialize()；拷贝函数copy()；转换数字为CACLInteger对象函数translate()
 */


#include "CACLInteger.hpp"

// 初始化对象
void cacl::CACLInteger::initialize() {
    for (int i = 0; i < MAX_OF_BIT; ++i) {
        this->num[i] = 0;
    }
    bit = 1;
    symbol = false;
}


// 拷贝对象
void cacl::CACLInteger::copy(const CACLInteger number) {
    for (int i = 0; i < number.bit; ++i) {
        num[i] = number.num[i];
    }

    bit = number.bit;
    symbol = number.symbol;
}


// 转换long long为CACLInteger
cacl::CACLInteger cacl::CACLInteger::translate(long long number) {
    CACLInteger ans;
    int tempBit = 0;
    short tempNum[MAX_OF_BIT]{};

    ans.initialize();
    if (number > 0) {
        ans.symbol = false;
    } else {
        ans.symbol = true;
        number = -number;
    }

    //用tempBit记录位数,先用tempNum逆序存储number的各个位的数字
    for (int i = 1; number > 0; ++i, tempBit++) {
        tempNum[i - 1] = (short) (number % 10);
        number /= 10;
    }
    ans.bit = tempBit;

    //将tempNum逆序存储进ans的num成员
    for (int i = 0; i < ans.bit; i++) {
        ans.num[i] = tempNum[i];
    }

    return ans;
}


// 判断是不是零
bool cacl::CACLInteger::isZero() {
    return this->bit == 1 && this->num[0] == 0;
}


// 判断是不是负数
bool cacl::CACLInteger::isNegative() {
    return symbol;
}


// 判断是不是正数
bool cacl::CACLInteger::isPositive() {
    return !symbol;
}


// 获取位数
int cacl::CACLInteger::getBit() {
    return bit;
}

// 转换符号
void cacl::CACLInteger::exchangeSymbol() {
    symbol = !symbol;
}

// 获取正负值
bool cacl::CACLInteger::getSymbol() {
    return this->symbol;
}

// 设置符号
void cacl::CACLInteger::setSymbol(bool target){
    symbol = target;
}