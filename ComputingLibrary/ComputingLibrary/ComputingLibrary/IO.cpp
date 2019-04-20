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
CACLInteger::istream& operator>>(istream& _cin, CACLInteger& integer) {
	string tmpNumber;
	
	//���tmpNumber�ķ���
	if (tmpNumber[0] == '+') {
		integer.symbol = false;
		tmpNumber.earse(0, 1);
	}
	else if (tmpNumber[0] == '-') {
		integer.symbol = true;
		tmpNumber.earse(0, 1);
	}
	else {
		integer.symbol = false;
	}

	for (int i = tmpNumber.size() - 1, j = 0; i >= 0; --i, ++j) {
		integer.num[i] = (short)tmpNumber[j];
	}

	integer.bit = tmpNumber.size();

	return _cin;
}


//����������Ϊ���
CACLInteger::ostream& operator<<(ostream& _cout, CACLInteger& integer) {
	if (integer.symbol == false) {
		_cout << '-';
	}

	for (int i = integer.bit - 1; i >= 0; --i) {
		_cout << integer.num[i];
	}

	return _cout;
}