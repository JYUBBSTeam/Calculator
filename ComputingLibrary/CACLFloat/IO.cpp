/*
 * 创建人：huang
 * 创建日期：2019.5.3
 * 修改
 */

#include "CACLFloat.hpp"
#include "../CACLInteger/CACLInteger.hpp"
#include <string>
#include <sstream>

namespace cacl {
    // 重载左移作为输出
    std::ostream &operator<<(std::ostream &_cout,  CACLFloat &myFloat) {
        _cout << myFloat.integer;

        // 输出小数部分
        if (myFloat.decimalBit != 0) {
            _cout << '.';
            for (int i = 0; i < myFloat.decimalBit; ++i) {
                _cout << myFloat.decimalNum[i];
            }
        }

        return _cout;
    }

    // 重载右移作为输入
    std::istream &operator>>(std::istream &_cin, CACLFloat &myFloat) {
        std::string tmpFloat;

        _cin >> tmpFloat;

        // 查找小数点
        auto decimalPointLocation = tmpFloat.find('.');

        // 没有小数点的情况
        if (decimalPointLocation == std::string::npos) {
            std::istringstream integerPart(tmpFloat);
            integerPart >> myFloat.integer;
        } else {    // 有小数点的情况
            std::string integerPart;
            // 分离整数部分, 这里依赖CACLInteger的符号控制
            for (int i = 0; i < decimalPointLocation; ++i) {
                integerPart.append(1, tmpFloat.at(i));
            }
            std::stringstream inputIntegerPart(integerPart);
            inputIntegerPart >> myFloat.integer;

            // 删除整数部分和小数点
            tmpFloat.erase(0, decimalPointLocation + 1);

            // 将剩余部分读入CACLFloat的小数部分
            for (int j = 0; j < tmpFloat.size(); ++j) {
                myFloat.decimalNum[j] = tmpFloat.at(j) - '0';
                myFloat.decimalBit++;
            }
        }

        return _cin;
    }
}
