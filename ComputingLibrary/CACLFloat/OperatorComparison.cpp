

#include "CACLFloat.hpp"

// 重载大于号
bool cacl::CACLFloat::operator>(cacl::CACLFloat number) {
    if (*this == number) {
        return false;
    }

    // 比较整数部分，如果整数部分相等，从找到this和number中位数最低的，然后从最低位开始比较
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


// 重载小于号
bool cacl::CACLFloat::operator<(cacl::CACLFloat number) {
    return !(*this > number);
}

bool cacl::CACLFloat::operator<(double number) {
    CACLFloat translatedNumber;

    translatedNumber = translate(number);

    return *this < translatedNumber;
}


//重载大于或等于
bool cacl::CACLFloat::operator>=(cacl::CACLFloat number) {
    return *this > number or *this == number;
}

bool cacl::CACLFloat::operator<=(cacl::CACLFloat number) {
    return *this < number or *this == number;
}

bool cacl::CACLFloat::operator<=(double number) {
    CACLFloat translatedNumber;

    translatedNumber = translate(number);

<<<<<<< HEAD
    return *this >= translatedNumber;
}


//重载小于或等于
bool cacl::CACLFloat::operator<=(cacl::CACLFloat number) {
    return *this < number or *this == number;
=======
    return *this <= translatedNumber;
>>>>>>> bfbed2d33976afe9fac19a1492c3416a56b1e008
}


bool cacl::CACLFloat::operator>=(double number) {
    CACLFloat translatedNumber;

    translatedNumber = translate(number);

    return *this >= translatedNumber;
}


//重载等于
bool cacl::CACLFloat::operator==(cacl::CACLFloat number) {
    if (this->integer == number.integer) {
        return true;
    }
    //从找到this和number中位数最低的，然后从最低位开始比较
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