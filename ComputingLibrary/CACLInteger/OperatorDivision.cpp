#include "CACLInteger.h"

// 重载除法
CACLInteger CACLInteger::operator/(CACLInteger number) {
    CACLInteger ans;

    ans.normalDivision(*this, number);

    return ans;
}


CACLInteger CACLInteger::operator/(const long long number) {
    CACLInteger translatedNumber = translate(number);
    CACLInteger ans;

    ans = *this / translatedNumber;

    return ans;
}


// 小数据除法
CACLInteger CACLInteger::normalDivision(CACLInteger number1, CACLInteger number2) {
    
}