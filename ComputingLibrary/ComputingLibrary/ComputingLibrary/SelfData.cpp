#include "CACLInteger.h"

//��ʼ������
void CACLInteger::initialize() {
    for (int i = 0; i < MAX_OF_BIT; ++i) {
        this->num[i] = 0;
    }

    this->bit = 0;
    this->symbol = 0;
}


//��������
CACLInteger CACLInteger::copy(const CACLInteger number) {
    this->initialize;

    for (int i = 0; i < number.bit; ++i) {
        this->num[i] = number.num[i];
    }

    this->bit = number.bit;
    this->symbol = number.symbol;

    return *this;
}


//ת��long longΪCACLInteger
CACLInteger CACLInteger::translate(const long long number) {
    
}