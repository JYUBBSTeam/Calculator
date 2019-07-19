/*
 * 创建人：黄子涵
 * 修改时间：2019.7.19
 */


#include "CACLInteger.hpp"

// 重载求余数
CACLInteger CACLInteger::operator%(CACLInteger number) {
    CACLInteger ans;

    ans = *this - (*this / number) * number;

    return ans;
}


CACLInteger CACLInteger::operator%(std::string number) {
    CACLInteger translatedNumber = translate(number);
    CACLInteger ans;

    ans = *this % translatedNumber;

    return ans;
}
