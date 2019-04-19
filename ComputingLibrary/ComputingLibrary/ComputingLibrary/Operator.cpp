/*
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

}


//重载大于号
bool CACLInteger::operator>(const CACLInteger number) {
    if ((this->symbol ^ number.symbol) == false) {
        return this->symbol == false ? true : false;
    }


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