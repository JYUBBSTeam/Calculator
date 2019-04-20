/*
 *创建人：Huang
 *创建日期：2019.4.19
 *修改日期：2019.4.20
 *类：CACLInteger
 *功能：重载运算符：+；-;>;<;=
 */


#include "CACLInteger.h"

 //重载加法
CACLInteger CACLInteger::operator+(const CACLInteger number) {
    CACLInteger ans;
    ans.initialize();

    if ((this->symbol ^ number.symbol) == false) {
        ans = unsignedAdd(*this, number);
        ans.symbol = this->symbol;
    }

    if ((this->symbol ^ number.symbol) == true) {
        ans = unsignedSubtract(*this, number);
        ans.symbol = (this->absoluteValue > number.absoluteValue) ? this->symbol : number.symbol;
    }

    return ans;
}


CACLInteger CACLInteger::operator+(const long long number) {
    CACLInteger translatedNumber = translate(number);
    CACLInteger ans;

    ans.initialize();
    ans = translatedNumber + *this;

    return ans;
}


//无符号两个CACLInteger相加
CACLInteger CACLInteger::unsignedAdd(const CACLInteger number1, const CACLInteger number2) {
    CACLInteger ans;
    CACLInteger longer, shorter;

    ans.initialize;

    //比较number1和number2的大小
    if (number1.absoluteValue > number2.absoluteValue) {
        longer = number1;
        shorter = number2;
    }
    else {
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
    }
    else {
        ans.bit = longer.bit + 1;
    }

    return ans;
}


//重载减法
CACLInteger CACLInteger::operator-(const CACLInteger number) {
    CACLInteger ans;
    ans.initialize();

    if (this->symbol == false && number.symbol == false) {
        ans = unsignedSubtract(*this, number);
        ans.symbol = (this->absoluteValue > number.absoluteValue) ? false : true;
    }
    else if (this->symbol == false && number.symbol == true) {
        ans = unsignedAdd(*this, number);
        ans.symbol = false;
    }
    else if (this->symbol == true && number.symbol == false) {
        ans = unsignedAdd(*this, number);
        ans.symbol = true;
    }
    else if (this->symbol == true && number.symbol == true) {
        ans = unsignedSubtract(*this, number);
        ans.symbol = (this->absoluteValue > number.absoluteValue) ? true : false;
    }

    return ans;
}


CACLInteger CACLInteger::operator-(const long long number) {
    CACLInteger translatedNumber = translate(number);
    CACLInteger ans;

    ans.initialize();
    ans = *this - translatedNumber;

    return ans;
}


//无符号两个CACLInteger相减
CACLInteger CACLInteger::unsignedSubtract(const CACLInteger number1, const CACLInteger number2) {
    CACLInteger ans;
    CACLInteger longer, shorter;

    ans.initialize;

    //比较number1和number2的大小
    if (number1.absoluteValue > number2.absoluteValue) {
        longer = number1;
        shorter = number2;
    }
    else {
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


//重载大于号
bool CACLInteger::operator>(const CACLInteger number) {
    int max(int a, int b);

    if ((this->symbol ^ number.symbol) == false) {
        return this->symbol == false ? true : false;
    }

    //记录this和number的绝对值
    CACLInteger absThis = this->absoluteValue;
    CACLInteger absNumber = number.absoluteValue;

    //从找到this和number中位数最高的，然后最高位开始比较
    if (this->symbol == false) {
        int tmpBit = max(this->symbol, number.symbol);
        for (int i = tmpBit - 1; i >= 0; --i) {
            if (this->num[i] < number.num[i]) {
                return false;
            }
        }
    }

    //类似上一个代码块
    if (this->symbol == true) {
        int tmpBit = max(this->symbol, number.symbol);
        for (int i = tmpBit - 1; i >= 0; --i) {
            if (this->num[i] > number.num[i]) {
                return false;
            }
        }
    }

    return true;
}


int max(int a, int b) {
    return a > b ? a : b;
}


bool CACLInteger::operator>(const long long number) {
    CACLInteger translatedNumber = translate(number);

    return *this > translatedNumber;
}


//重载小于号
bool CACLInteger::operator<(const CACLInteger number) {
    if ((this->symbol ^ number.symbol) == false) {
        return this->symbol == false ? false : true;
    }

    //记录this和number的绝对值
    CACLInteger absThis = this->absoluteValue;
    CACLInteger absNumber = number.absoluteValue;

    //从找到this和number中位数最高的，然后最高位开始比较
    if (this->symbol == false) {
        int tmpBit = max(this->symbol, number.symbol);
        for (int i = tmpBit - 1; i >= 0; --i) {
            if (this->num[i] > number.num[i]) {
                return false;
            }
        }
    }

    //类似上一个代码块
    if (this->symbol == true) {
        int tmpBit = max(this->symbol, number.symbol);
        for (int i = tmpBit - 1; i >= 0; --i) {
            if (this->num[i] < number.num[i]) {
                return false;
            }
        }
    }

    return true;
}


bool CACLInteger::operator<(const long long number) {
    CACLInteger translatedNumber = translate(number);

    return *this > translatedNumber;
}


//重载赋值
void CACLInteger::operator=(const CACLInteger number) {
    this->copy(number);
}


void CACLInteger::operator=(const long long number) {
    CACLInteger translatedNumber = translate(number);

    this->copy(translatedNumber);
}