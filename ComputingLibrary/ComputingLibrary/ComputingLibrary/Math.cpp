/*
 *创建人：Huang
 *创建日期：2019.4.19
 *修改日期：2019.4.19
 *类：CACLInteger
 *功能：绝对值函数absoluteValue()
 */

#include "CACLInteger.h"

CACLInteger CACLInteger::absoluteValue() {
    CACLInteger tmp = *this;

    if (tmp.symbol) {
        tmp.symbol = false;
    }

    return tmp;
}