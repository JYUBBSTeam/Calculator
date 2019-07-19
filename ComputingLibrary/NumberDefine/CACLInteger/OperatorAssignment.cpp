/*
 * 创建人：黄子涵
 * 修改时间:2019.7.19
 */

#include "CACLInteger.hpp"

// 重载赋值
CACLInteger CACLInteger::operator=(CACLInteger number) {
    for (int i = 0; i < number.bit; ++i) {
        num[i] = number.num[i];
    }

    bit = number.bit;
    symbol = number.symbol;
}


CACLInteger CACLInteger::operator=(std::string number) {
    CACLInteger translatedNumber = translate(number);

    *this = translatedNumber;
}


// 重载加赋值
void CACLInteger::operator+=(CACLInteger number) {
    *this = *this + number;
}

void CACLInteger::operator+=(std::string number) {
    CACLInteger translatedNumber = translate(number);

    *this += translatedNumber;
}


// 重载减赋值
void CACLInteger::operator-=(CACLInteger number) {
    *this = *this - number;
}

void CACLInteger::operator-=(std::string number) {
    CACLInteger translatedNumber = translate(number);

    *this -= translatedNumber;
}


// 重载乘赋值
void CACLInteger::operator*=(CACLInteger number) {
    *this = *this * number;
}

void CACLInteger::operator*=(std::string number) {
    CACLInteger translatedNumber = translate(number);

    *this *= translatedNumber;
}


// 重载除赋值
void CACLInteger::operator/=(CACLInteger number) {
    *this = *this / number;
}

void CACLInteger::operator/=(std::string number) {
    CACLInteger translatedNumber = translate(number);

    *this /= translatedNumber;
}


// 重载求余赋值
void CACLInteger::operator%=(CACLInteger number) {
    *this = *this % number;
}

void CACLInteger::operator%=(std::string number) {
    CACLInteger translatedNumber = translate(number);

    *this %= translatedNumber;
}