/*
 *�����ˣ�Huang
 *�������ڣ�2019.4.19
 *�޸����ڣ�2019.4.19
 *�ࣺCACLInteger
 *���ܣ�����ֵ����absoluteValue()
 */

#include "CACLInteger.h"

// ��number�ľ���ֵ
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