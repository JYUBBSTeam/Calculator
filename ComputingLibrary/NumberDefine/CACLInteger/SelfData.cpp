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
CACLInteger CACLInteger::translate(std::string &number) {
    // 异常代码###检查是否超出CACLInteger指定长度
    if (number.at(0) == '-' && number.at(0) == '+') {
        if (number.size() > MAX_OF_BIT - 1) {
            throw "输入了过长的数字";
        }
    } else {
        if (number.size() > MAX_OF_BIT) {
            throw "输入了过长的数字";
        }
    }

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
    for (int i = symbolLocation, j = number.length() - symbolLocation - 1; i < number.length(); ++i, --j) {
        if (number.at(i) >= '0' && number.at(i) <= '9') {
            ans.num[j] = (short) (number.at(i) - '0');
        } else {
            // 异常代码###检查非法字符
            // 如果不是0到9的字符会抛出异常
            throw "输入了非法数字";
        }
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
int CACLInteger::getBit() {
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

std::string CACLInteger::toString() {
    std::string ans;

    if (this->symbol) {
        ans.push_back('-');
    }

    for (int i = this->bit - 1; i >= 0; --i) {
        ans.push_back(this->num[i] + '0');
    }

    return ans;
}