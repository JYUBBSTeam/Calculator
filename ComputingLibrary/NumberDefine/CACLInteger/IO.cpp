/*
 *创建人：Huang
 *创建日期：2019.4.20
 *修改日期：2019.4.20
 *类：CACLInteger
 *功能：控制输入和输出
 */

#include "CACLInteger.hpp"
#include <string>


// 重载右移作为输入
std::istream &operator>>(std::istream &_cin, CACLInteger &integer) {
    std::string tempNumber;

    _cin >> tempNumber;

    // 检查tempNumber的符号
    if (tempNumber[0] == '+') {
        integer.symbol = false;
        tempNumber.erase(0, 1);
    } else if (tempNumber[0] >= 48 && tempNumber[0] <= 57) {
        integer.symbol = false;
    } else {
        integer.symbol = true;
        tempNumber.erase(0, 1);
    }

    for (int i = tempNumber.size() - 1, j = 0; i >= 0; --i, ++j) {
        integer.num[i] = (short) (tempNumber[j] - 48);
    }

    integer.bit = tempNumber.size();

    return _cin;
}


// 重载左移作为输出
std::ostream &operator<<(std::ostream &_cout, const CACLInteger &integer) {
    if (integer.symbol == true) {
        _cout << '-';
    }

    for (int i = integer.bit - 1; i >= 0; --i) {
        _cout << integer.num[i];
    }

    return _cout;
}
