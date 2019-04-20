/*
 *������:Huang
 *��������:2019.4.19
 *�޸����ڣ�2019.4.20
 *��:CACLInteger
 *���ص��������+�ӷ���-������*�˷���/������%���ࣻ =��ֵ��>���ڣ�<С��
 *���������췽��CACLInteger()����������~CALInteger()���������췽��CACLInteger(const CACLInteger *obj)��
 *      ��ʼ������initialize()����������copy()������ת����CACLInteger���󷽷�translate()�������ֵ����Ab
 */


#ifndef _CACLINEGER_H_
#define _CACLINEGER_H_

#include <iostream>
/*
#include "IO.cpp"
#include "Math.cpp"
#include "Operator.cpp"
#include "SelfData.cpp"
#include "Structure_Destruce.cpp"
*/

using namespace std;

 //�����CACLInteger�����λ��
constexpr int MAX_OF_BIT = 200;

class CACLInteger {
public:
    //���췽��
    CACLInteger();
    //�������췽��
    CACLInteger(const CACLInteger& obj);
    //��������
    ~CACLInteger();

    //��ʼ������
    void initialize();

    //��������
    void copy(const CACLInteger number);

    //ת��long longΪCACLInteger
    CACLInteger translate(const long long number);

    //���ؼӷ�
    CACLInteger operator+(const CACLInteger& number) const;
    CACLInteger operator+(const long long number) const;
    //�޷�������CACLInteger���
    CACLInteger unsignedAdd(const CACLInteger number1, const CACLInteger number2);

    //���ؼ���
    CACLInteger operator-(const CACLInteger& number) const;
    CACLInteger operator-(const long long number) const;
    //�޷�������CACLInteger���
    CACLInteger unsignedSubtract(const CACLInteger number1, const CACLInteger number2);

    //���ش��ں�
    bool operator>(const CACLInteger& number) const;
    bool operator>(const long long number) const;

    //����С�ں�
    bool operator<(const CACLInteger number) const;
    bool operator<(const long long number) const;

    //���ظ�ֵ
    void operator=(const CACLInteger number) const;
    void operator=(const long long number) const;

    //����������Ϊ����
    friend istream& operator>>(istream& _cin, const CACLInteger& integer);

    //����������Ϊ���
    friend ostream& operator<<(ostream& _cout, const CACLInteger& integer);

    //��CACLInteger�ľ���ֵ
    CACLInteger absoluteValue();



private:
    //���ֵķ���,trueʱ�Ǹ�����falseʱ������
    bool symbol;
    //���ֵ�λ��
    int bit;
    //����λ������
    short num[MAX_OF_BIT];

};

#endif // !_CACLINEGER_H_
