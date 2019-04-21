/*
 *�����ˣ�Huang
 *�������ڣ�2019.4.19
 *�޸����ڣ�2019.4.20
 *�ࣺCACLInteger
 *���ܣ���ʼ������initialize()����������copy()��ת������ΪCACLInteger������translate()
 */


#include "CACLInteger.h"

// ��ʼ������
void CACLInteger::initialize() {
    for (int i = 0; i < MAX_OF_BIT; ++i) {
        num[i] = 0;
    }

    bit = 1;
    symbol = false;
}


// ��������
void CACLInteger::copy(const CACLInteger number) {
    for (int i = 0; i < number.bit; ++i) {
        num[i] = number.num[i];
    }

    bit = number.bit;
    symbol = number.symbol;
}


// ת��long longΪCACLInteger
CACLInteger CACLInteger::translate(long long number) {
    CACLInteger ans;
    int tmpBit = 0;
    short tmpNum[MAX_OF_BIT]{};

    ans.initialize();
    if (number > 0) {
        ans.symbol = false;
    } else {
        ans.symbol = true;
        number = -number;
    }

    //��tmpBit��¼λ��,����tmpNum����洢number�ĸ���λ������
    for (int i = 1; number > 0; ++i, tmpBit++) {
        tmpNum[i - 1] = (short) (number % 10);
        number /= 10;
    }
    ans.bit = tmpBit;

    //��tmpNum����洢��ans��num��Ա
    for (int i = 0; i < ans.bit; i++) {
        ans.num[i] = tmpNum[i];
    }

    return ans;
}
