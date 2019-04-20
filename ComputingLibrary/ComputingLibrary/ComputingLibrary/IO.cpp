/*
 *创建人：Huang
 *创建日期：2019.4.20
 *修改日期：2019.4.20
 *类：CACLInteger
 *功能：控制输入和输出
 */

#include "CACLInteger.h"
#include <string>

using namespace std;

 //重载右移作为输入
CACLInteger::istream& operator>>(istream& _cin, CACLInteger& integer) {
	string tmpNumber;
	
	//检查tmpNumber的符号
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


//重载左移作为输出
CACLInteger::ostream& operator<<(ostream& _cout, CACLInteger& integer) {
	if (integer.symbol == false) {
		_cout << '-';
	}

	for (int i = integer.bit - 1; i >= 0; --i) {
		_cout << integer.num[i];
	}

	return _cout;
}