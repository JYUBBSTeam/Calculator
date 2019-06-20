/*
 * 创建人：Huang
 * 修改人：Liang
 * 修改时间：2019.5.13
 */

#include "CACLFloat.hpp"

//重载赋值
CACLFloat CACLFloat::operator=(CACLFloat number) {
    this->integer = number.integer;

    for (int i = 0; i < number.decimalBit; ++i) {
        this->decimalNum[i] = number.decimalNum[i];
    }

    this->decimalBit = number.decimalBit;
    return *this;
}

CACLFloat CACLFloat::operator=(CACLInteger number) {
    integer = number;

    return *this;
}

CACLFloat CACLFloat::operator=(double number) {
    CACLFloat translatedNumber = translate(number);

    *this = translatedNumber;
    return *this;
}


// 重载加赋值
CACLFloat CACLFloat::operator+=(CACLFloat number) {
    *this = *this + number;
}

CACLFloat CACLFloat::operator+=(double number) {
    CACLFloat translatedNumber = translate(number);

    *this += translatedNumber;
}


// 重载减赋值
CACLFloat CACLFloat::operator-=(CACLFloat number) {
    *this = *this - number;
}

CACLFloat CACLFloat::operator-=(double number) {
    CACLFloat translatedNumber = translate(number);

    *this -= translatedNumber;
}


//重载乘赋值
CACLFloat CACLFloat::operator*=(CACLFloat number) {
    *this = *this * number;
}

CACLFloat CACLFloat::operator*=(double number) {
    CACLFloat translatedNumber = translate(number);

    *this *= translatedNumber;
}


//重载除赋值
CACLFloat CACLFloat::operator/=(CACLFloat number) {
    *this = *this / number;
}

CACLFloat CACLFloat::operator/=(double number) {
    CACLFloat translatedNumber = translate(number);

    *this /= translatedNumber;
}

