#include "CACLInteger.h"

// 重载求余数
cacl::CACLInteger cacl::CACLInteger::operator%(CACLInteger number) {
    CACLInteger ans;

    ans = *this - (*this / number) * number;

    return ans;
}


cacl::CACLInteger cacl::CACLInteger::operator%(const long long number) {
    CACLInteger translatedNumber = translate(number);
    CACLInteger ans;

    ans = *this % translatedNumber;

    return ans;
}
