#include "CACLInteger.hpp"

// 重载赋值
void cacl::CACLInteger::operator=(const CACLInteger &number) {
    for (int i = 0; i < number.bit; ++i) {
        num[i] = number.num[i];
    }

    bit = number.bit;
    symbol = number.symbol;
}


void cacl::CACLInteger::operator=(const long long number) {
    const CACLInteger translatedNumber = translate(number);

    *this = translatedNumber;
}


// 重载加赋值
void cacl::CACLInteger::operator+=(const CACLInteger &number) {
    *this = *this + number;
}

void cacl::CACLInteger::operator+=(const long long number) {
    const CACLInteger translatedNumber = translate(number);

    *this += translatedNumber;
}


// 重载减赋值
void cacl::CACLInteger::operator-=(const CACLInteger &number) {
    *this = *this - number;
}

void cacl::CACLInteger::operator-=(const long long number) {
    const CACLInteger translatedNumber = translate(number);

    *this -= translatedNumber;
}


// 重载乘赋值
void cacl::CACLInteger::operator*=(const CACLInteger &number) {
    *this = *this * number;
}

void cacl::CACLInteger::operator*=(const long long number) {
    const CACLInteger translatedNumber = translate(number);

    *this *= translatedNumber;
}


// 重载除赋值
void cacl::CACLInteger::operator/=(const CACLInteger &number) {
    *this = *this / number;
}

void cacl::CACLInteger::operator/=(const long long number) {
    const CACLInteger translatedNumber = translate(number);

    *this /= translatedNumber;
}


// 重载求余赋值
void cacl::CACLInteger::operator%=(const cacl::CACLInteger &number) {
    *this = *this % number;
}

void cacl::CACLInteger::operator%=(const long long number) {
    const CACLInteger translatedNumber = translate(number);

    *this %= translatedNumber;
}