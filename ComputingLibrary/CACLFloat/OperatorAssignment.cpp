

#include "CACLFloat.hpp"

cacl::CACLFloat &cacl::CACLFloat::operator=(cacl::CACLFloat number) {
    this->integer = number.integer;

    for (int i = 0; i < number.decimalBit; ++i) {
        this->decimalNum[i] = number.decimalNum[i];
    }

    this->decimalBit = number.decimalBit;
    return *this;
}

cacl::CACLFloat &cacl::CACLFloat::operator=(double number) {
    CACLFloat translatedNumber = translate(number);

    *this = translatedNumber;
    return *this;
}