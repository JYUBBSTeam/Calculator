#include "CACLInteger.hpp"

// 重载求余数
CACLInteger CACLInteger::operator%(CACLInteger number) {
    CACLInteger ans;

    ans = *this - (*this / number) * number;

    return ans;
}


CACLInteger CACLInteger::operator%(const long long number) {
    CACLInteger translatedNumber = translate(number);
    CACLInteger ans;

    ans = *this % translatedNumber;

    return ans;
}
