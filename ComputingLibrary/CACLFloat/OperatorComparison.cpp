

#include "CACLFloat.hpp"

bool cacl::CACLFloat::operator>(cacl::CACLFloat number) {
    if (*this == number) {
        return false;
    }

    if (this->integer > number.integer) {
        return true;
    } else if (this->integer == number.integer) {
        if (this->decimalBit > number.decimalBit) {
            return true;
        } else if (this->decimalBit == number.decimalBit) {
            for (auto i = 0; i < this->decimalBit; ++i) {
                if (this->decimalNum[i] < number.decimalNum[i]) {
                    return false;
                }
            }
            return true;
        }
    }

    return false;
}


bool cacl::CACLFloat::operator>(double number) {
    CACLFloat translatedNumber;

    translatedNumber = translate(number);

    return *this > translatedNumber;
}


bool cacl::CACLFloat::operator<(cacl::CACLFloat number) {
    return !(*this > number);
}

bool cacl::CACLFloat::operator<(double number) {
    CACLFloat translatedNumber;

    translatedNumber = translate(number);

    return *this < translatedNumber;
}

bool cacl::CACLFloat::operator>=(cacl::CACLFloat number) {
    return *this > number or *this == number;
}

bool cacl::CACLFloat::operator>=(double number) {
    CACLFloat translatedNumber;

    translatedNumber = translate(number);

    return *this >= translatedNumber;
}

bool cacl::CACLFloat::operator<=(cacl::CACLFloat number) {
    return *this < number or *this == number;
}


bool cacl::CACLFloat::operator<=(double number) {
    CACLFloat translatedNumber;

    translatedNumber = translate(number);

    return *this <= translatedNumber;
}

bool cacl::CACLFloat::operator==(cacl::CACLFloat number) {
    if (this->integer == number.integer) {
        return true;
    }

    if (this->decimalBit == number.decimalBit) {
        int i;
        for (i = 0; i < this->decimalBit; ++i) {
            if (this->decimalNum[i] != number.decimalNum[i]) {
                return false;
            }
        }
        if (i == this->decimalBit) {
            return true;
        }
    }

    return false;
}

bool cacl::CACLFloat::operator==(double number) {
    CACLFloat translatedNumber;

    translatedNumber = translate(number);

    return *this == translatedNumber;
}