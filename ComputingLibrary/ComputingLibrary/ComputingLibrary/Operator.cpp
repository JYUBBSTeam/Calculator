#include "CACLInteger.h"

//���ؼӷ�
CACLInteger CACLInteger::operator+(const CACLInteger& number) {
    CACLInteger ans;
    ans.initialize();

    if((this->symbol ^ number.symbol) == false){
        ans = unsignedAdd(*this, number);
    }

    if ((this->symbol ^ number.symbol) == true) {

    }

    return ans;
}


CACLInteger CACLInteger::operator+(const long long number) {

}


//�޷�������CACLInteger���
CACLInteger CACLInteger::unsignedAdd(const CACLInteger number1, const CACLInteger number2) {

}


//���ؼ���
CACLInteger CACLInteger::operator-(const CACLInteger& number) {

}


CACLInteger CACLInteger::operator-(const long long number) {

}


//�޷�������CACLInteger���
CACLInteger CACLInteger::unsignedSubtract(const CACLInteger number1, const CACLInteger number2) {

}