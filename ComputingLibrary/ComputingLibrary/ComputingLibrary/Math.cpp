/*
 *�����ˣ�Huang
 *�������ڣ�2019.4.19
 *�޸����ڣ�2019.4.19
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