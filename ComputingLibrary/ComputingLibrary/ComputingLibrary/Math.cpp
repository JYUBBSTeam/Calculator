/*
 *�ࣺCACLInteger
 *���ܣ�����ֵ����absoluteValue()
 */

#include "CACLInteger.h"

CACLInteger CACLInteger::absoluteValue() {
    CACLInteger tmp = *this;

    if (tmp.symbol) {
        tmp.symbol = false;
    }

    return tmp;
}