

#include "CACLInteger.h"

//重载加法
cacl::CACLInteger cacl::CACLInteger::operator+(CACLInteger number) {
    CACLInteger ans;

    if (this->symbol == number.symbol) {
        ans = unsignedAdd(*this, number);
        ans.symbol = this->symbol;
    }

    if ((this->symbol ^ number.symbol) == true) {
        ans = unsignedSubtract(*this, number);
        ans.symbol = (this->absoluteValue() > number.absoluteValue()) ? this->symbol : number.symbol;
    }

    return ans;
}


cacl::CACLInteger cacl::CACLInteger::operator+(const long long number) {
    CACLInteger translatedNumber = translate(number);
    CACLInteger ans;

    ans = translatedNumber + *this;

    return ans;
}


//无符号两个CACLInteger相加
cacl::CACLInteger cacl::CACLInteger::unsignedAdd(CACLInteger number1, CACLInteger number2) {
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

    for (int i = 0; i < shorter.bit; i++) {
        ans.num[i] = longer.num[i] + shorter.num[i];
    }

    for (int j = shorter.bit; j < longer.bit; ++j) {
        ans.num[j] = longer.num[j];
    }

    //加法运算结果最多位max(number1.bit,number2.bit) + 1位，将最高位先初始化位零
    ans.num[longer.bit] = 0;

    //统一进位
    for (int i = 0; i < longer.bit; ++i) {
        ans.num[i + 1] += ans.num[i] / 10;
        ans.num[i] %= 10;
    }

    //判断ans位数
    if (ans.num[longer.bit] == 0) {
        ans.bit = longer.bit;
    } else {
        ans.bit = longer.bit + 1;
    }

    return ans;
}
