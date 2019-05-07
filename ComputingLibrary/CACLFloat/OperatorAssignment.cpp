

#include "CACLFloat.hpp"

void cacl::CACLFloat::operator=(cacl::CACLFloat number) {
    this->integer = number.integer;

    for (int i = 0; i < number.decimalBit; ++i) {
        this->decimalNum[i] = number.decimalNum[i];
    }

    this->decimalBit = number.decimalBit;
}

void cacl::CACLFloat::operator=(double number) {
    CACLFloat translatedNumber = translate(number);

    *this = translatedNumber;
}