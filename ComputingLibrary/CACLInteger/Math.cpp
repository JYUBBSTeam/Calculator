/*
 *创建人：Huang
 *创建日期：2019.4.19
 *修改日期：2019.4.19
 *类：CACLInteger
 *功能：绝对值函数absoluteValue()
 */

#include "CACLInteger.hpp"

// 求number的绝对值
CACLInteger CACLInteger::absoluteValue() {
    if (symbol) {
        CACLInteger temp;
        temp = *this;
        temp.symbol = false;
        return temp;
    } else {
        return *this;
    }
}