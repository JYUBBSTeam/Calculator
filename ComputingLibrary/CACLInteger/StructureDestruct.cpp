/*
 *类：CACLInteger
 *功能：构造方法CACLInteger()；析构方法~CALInteger()；拷贝构造方法CACLInteger(const CACLInteger *obj)
 */


#include "CACLInteger.h"

CACLInteger::CACLInteger() {
    symbol = false;
    bit = 1;
    num[0] = 0;
}


CACLInteger::~CACLInteger() {
}