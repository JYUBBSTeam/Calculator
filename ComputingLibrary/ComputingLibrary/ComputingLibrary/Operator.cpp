#include "CACLInteger.h"

//重载加法
CACLInteger CACLInteger::operator+(const CACLInteger& number) {
    CACLInteger ans;
    ans.initialize();

    if((this->symbol ^ number.symbol) == false){
        ans = unsignedAdd(*this, number);
    }

    if ((this->symbol ^ number.symbol) == true) {

    }

    return ans;
}


CACLInteger CACLInteger::operator+(const long long number) {

}


//无符号两个CACLInteger相加
CACLInteger CACLInteger::unsignedAdd(const CACLInteger number1, const CACLInteger number2) {

}


//重载减法
CACLInteger CACLInteger::operator-(const CACLInteger& number) {

}


CACLInteger CACLInteger::operator-(const long long number) {

}


//无符号两个CACLInteger相减
CACLInteger CACLInteger::unsignedSubtract(const CACLInteger number1, const CACLInteger number2) {

}