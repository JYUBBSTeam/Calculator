/*
 *创建人：Huang
 *创建日期：2019.4.19
 *修改日期：2019.4.19
 *类：CACLInteger
 *功能：绝对值函数absoluteValue()
 */

#include "CACLInteger.h"

// 求number的绝对值
CACLInteger CACLInteger::absoluteValue() {
    if (symbol) {
        CACLInteger tmp;
        tmp = *this;
        tmp.symbol = false;
        return tmp;
    } else {
        return *this;
    }
}