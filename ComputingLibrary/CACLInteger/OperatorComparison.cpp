


#include "CACLInteger.h"

//重载大于号
bool cacl::CACLInteger::operator>(const CACLInteger &number) {
    if (symbol != number.symbol) {
        return symbol == false ? true : false;
    }

    //从找到this和number中位数最高的，然后最高位开始比较
    if (symbol == false) {
        if (bit > number.bit) {
            return true;
        } else if (bit < number.bit) {
            return false;
        } else {
            for (int i = bit - 1; i >= 0; --i) {
                if (num[i] < number.num[i]) {
                    return false;
                }
            }
        }
    }


//类似上一个代码块
    if (symbol == true) {
        if (bit < number.bit) {
            return true;
        } else if (bit > number.bit) {
            return false;
        } else {
            for (int i = bit - 1; i >= 0; --i) {
                if (num[i] > number.num[i]) {
                    return false;
                }
            }
        }
    }

    return true;
}


bool cacl::CACLInteger::operator>(const long long number) {
    CACLInteger translatedNumber = translate(number);

    return *this > translatedNumber;
}


//重载小于号
bool cacl::CACLInteger::operator<(CACLInteger number) {
    if (symbol != number.symbol) {
        return symbol == false ? false : true;
    }

    //从找到this和number中位数最高的，然后最高位开始比较
    if (symbol == false) {
        if (bit > number.bit) {
            return false;
        } else if (bit < number.bit) {
            return true;
        } else {
            for (int i = bit - 1; i >= 0; --i) {
                if (num[i] > number.num[i]) {
                    return false;
                }
            }
        }
    }

    //类似上一个代码块
    if (this->symbol == true) {
        if (bit > number.bit) {
            return true;
        } else if (bit < number.bit) {
            return false;
        } else {
            for (int i = bit - 1; i >= 0; --i) {
                if (this->num[i] < number.num[i]) {
                    return false;
                }
            }
        }
    }

    return true;
}


bool cacl::CACLInteger::operator<(const long long number) {
    CACLInteger translatedNumber = translate(number);

    return *this < translatedNumber;
}


//重载等于
bool cacl::CACLInteger::operator==(CACLInteger number) {
    if (symbol != number.symbol) {
        return false;
    }

    if (bit != number.bit) {
        return false;
    }

    for (int i = bit - 1; i >= 0; --i) {
        if (num[i] != number.num[i])
            return false;
    }

    return true;
}

bool cacl::CACLInteger::operator==(const long long number) {
    CACLInteger translatedNumber = translate(number);

    return *this == translatedNumber;
}


//重载不等于
bool cacl::CACLInteger::operator!=(CACLInteger number) {
    return !(*this == number);
}

bool cacl::CACLInteger::operator!=(const long long number) {
    CACLInteger translatedNumber = translate(number);

    return !(*this == translatedNumber);
}


//重载大于或等于
bool cacl::CACLInteger::operator>=(CACLInteger number) {
    return *this > number || *this == number;
}


bool cacl::CACLInteger::operator>=(const long long number) {
    CACLInteger translatedNumber = translate(number);

    return *this >= translatedNumber;
}


//重载小于或等于
bool cacl::CACLInteger::operator<=(CACLInteger number) {
    return *this < number || *this == number;
}


bool cacl::CACLInteger::operator<=(const long long number) {
    CACLInteger translatedNumber = translate(number);

    return *this <= translatedNumber;
}