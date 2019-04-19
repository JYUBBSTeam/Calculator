/*
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