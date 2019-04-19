/*
 *�ࣺCACLInteger
 *���ܣ���ʼ������initialize()����������copy()��ת������ΪCACLInteger������translate()
 */


#include "CACLInteger.h"

 //��ʼ������
void CACLInteger::initialize() {
    for (int i = 0; i < MAX_OF_BIT; ++i) {
        this->num[i] = 0;
    }

    this->bit = 0;
    this->symbol = false;
}


//��������
void CACLInteger::copy(const CACLInteger number) {
    for (int i = 0; i < number.bit; ++i) {
        this->num[i] = number.num[i];
    }

    this->bit = number.bit;
    this->symbol = number.symbol;
}


//ת��long longΪCACLInteger
CACLInteger CACLInteger::translate(const long long number) {
    long long pow(long long x, int n);

    CACLInteger ans;
    int tmpBit = 0;
    short tmpNum[MAX_OF_BIT]{};

    ans.initialize();
    if (number > 0) {
        ans.symbol = false;
    }
    else {
        ans.symbol = true;
        number = -number;
    }

    //��tmpBit��¼λ��,����tmpNum����洢number�ĸ���λ������
    for (int i = 1; number > 0; ++i, tmpBit++) {
        tmpNum[i - 1] = (short)(number % pow(10, i));
        number -= tmpNum[i - 1];
    }
    ans.bit = tmpBit;

    //��tmpNum����洢��ans��num��Ա
    for (int j = ans.bit - 1, i = 0; j >= 0; --j, i++) {
        ans.num[j] = tmpNum[i];
    }

    return ans;
}


long long pow(long long x, int n) {
    if (n == 0) {
        return 1;
    }
    if (n == 1) {
        return x;
    }

    if (n % 2 == 0) {
        return pow(x * x, n / 2);
    }
    else {
        return pow(x * x, n / 2) * x;
    }
}