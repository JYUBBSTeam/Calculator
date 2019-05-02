#include "CACLInteger.h"

// 重载求余数
CACLInteger CACLInteger::operator%(CACLInteger number) {
    CACLInteger ans;

    ans = ans.normalDivision(*this, number);

    return ans;
}


CACLInteger CACLInteger::operator%(const long long number) {
    CACLInteger translatedNumber = translate(number);
    CACLInteger ans;

    ans = *this % translatedNumber;

    return ans;
}
