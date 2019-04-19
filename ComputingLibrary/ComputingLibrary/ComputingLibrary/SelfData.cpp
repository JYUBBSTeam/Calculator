/*
 *类：CACLInteger
 *功能：初始化函数initialize()；拷贝函数copy()；转换数字为CACLInteger对象函数translate()
 */


#include "CACLInteger.h"

 //初始化对象
void CACLInteger::initialize() {
    for (int i = 0; i < MAX_OF_BIT; ++i) {
        this->num[i] = 0;
    }

    this->bit = 0;
    this->symbol = false;
}


//拷贝对象
void CACLInteger::copy(const CACLInteger number) {
    for (int i = 0; i < number.bit; ++i) {
        this->num[i] = number.num[i];
    }

    this->bit = number.bit;
    this->symbol = number.symbol;
}


//转换long long为CACLInteger
CACLInteger CACLInteger::translate(const long long number) {
    long long pow(long long x, int n);

    CACLInteger ans;
    int tmpBit = 0;
    short tmpNum[MAX_OF_BIT]{};

    ans.initialize();
    if (number > 0) {
        ans.symbol = false;
    }
    else {
        ans.symbol = true;
        number = -number;
    }

    //用tmpBit记录位数,先用tmpNum逆序存储number的各个位的数字
    for (int i = 1; number > 0; ++i, tmpBit++) {
        tmpNum[i - 1] = (short)(number % pow(10, i));
        number -= tmpNum[i - 1];
    }
    ans.bit = tmpBit;

    //将tmpNum逆序存储进ans的num成员
    for (int j = ans.bit - 1, i = 0; j >= 0; --j, i++) {
        ans.num[j] = tmpNum[i];
    }

    return ans;
}


long long pow(long long x, int n) {
    if (n == 0) {
        return 1;
    }
    if (n == 1) {
        return x;
    }

    if (n % 2 == 0) {
        return pow(x * x, n / 2);
    }
    else {
        return pow(x * x, n / 2) * x;
    }
}