/*
 *�ࣺCACLInteger
 *���ܣ�����ֵ����absoluteValue()
 */

#include "CACLInteger.h"

CACLInteger CACLInteger::absoluteValue(const CACLInteger number) {
    CACLInteger tmp = number;

    if (tmp.symbol) {
        tmp.symbol = false;
    }

    return tmp;
}