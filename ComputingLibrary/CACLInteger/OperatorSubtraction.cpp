

#include "CACLInteger.h"

using namespace caclInt;

//重载减法
CACLInteger CACLInteger::operator-(CACLInteger number) {
    CACLInteger ans;

    if (this->symbol == false && number.symbol == false) {
        ans = unsignedSubtract(*this, number);
        ans.symbol = (this->absoluteValue() > number.absoluteValue()) ? false : true;
    } else if (this->symbol == false && number.symbol == true) {
        ans = unsignedAdd(*this, number);
        ans.symbol = false;
    } else if (this->symbol == true && number.symbol == false) {
        ans = unsignedAdd(*this, number);
        ans.symbol = true;
    } else if (this->symbol == true && number.symbol == true) {
        ans = unsignedSubtract(*this, number);
        ans.symbol = (this->absoluteValue() > number.absoluteValue()) ? true : false;
    }

    return ans;
}


CACLInteger CACLInteger::operator-(const long long number) {
    CACLInteger translatedNumber = translate(number);
    CACLInteger ans;

    ans = *this - translatedNumber;

    return ans;
}


//无符号两个CACLInteger相减
CACLInteger CACLInteger::unsignedSubtract(CACLInteger number1, CACLInteger number2) {
    CACLInteger ans;
    CACLInteger longer, shorter;
    ans.initialize();

    //比较number1和number2的大小
    if (number1.absoluteValue() > number2.absoluteValue()) {
        longer = number1;
        shorter = number2;
    } else {
        longer = number2;
        shorter = number1;
    }

    for (int i = 0; i < shorter.bit; ++i) {
        ans.num[i] = longer.num[i] - shorter.num[i];
    }
    for (int i = shorter.bit; i < longer.bit; ++i) {
        ans.num[i] = longer.num[i];
    }

    //统一借位
    for (int i = 0; i < longer.bit; ++i) {
        if (ans.num[i] < 0) {
            ans.num[i + 1]--;
            ans.num[i] += 10;
        }
    }

    //判断ans位数
    int i;
    for (i = longer.bit; i > 0; --i) {
        if (ans.num[i] != 0) {
            ans.bit = i + 1;
            break;
        }
    }

    ans.bit = i + 1;

    return ans;
}