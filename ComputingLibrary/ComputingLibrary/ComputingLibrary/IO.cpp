/*
 *�����ˣ�Huang
 *�������ڣ�2019.4.20
 *�޸����ڣ�2019.4.20
 *�ࣺCACLInteger
 *���ܣ�������������
 */

#include "CACLInteger.h"
#include <string>

using namespace std;

//����������Ϊ����
istream &operator>>(istream &_cin, CACLInteger &integer) {
    string tmpNumber;

    cin >> tmpNumber;

    //���tmpNumber�ķ���
    if (tmpNumber[0] == '+') {
        integer.symbol = false;
        tmpNumber.erase(0, 1);
    } else if (tmpNumber[0] >= 48 && tmpNumber[0] <= 57) {
        integer.symbol = false;
    } else {
        integer.symbol = true;
        tmpNumber.erase(0, 1);
    }

    for (int i = tmpNumber.size() - 1, j = 0; i >= 0; --i, ++j) {
        integer.num[i] = (short) (tmpNumber[j] - 48);
    }

    integer.bit = tmpNumber.size();

    return _cin;
}


//����������Ϊ���
ostream &operator<<(ostream &_cout, const CACLInteger &integer) {
    if (integer.symbol == true) {
        _cout << '-';
    }

    for (int i = integer.bit - 1; i >= 0; --i) {
        _cout << integer.num[i];
    }

    return _cout;
}