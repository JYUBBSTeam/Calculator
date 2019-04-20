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
    CACLInteger translate(long long number);

    //���ؼӷ�
    CACLInteger operator+(CACLInteger number);
    CACLInteger operator+(const long long number);
    //�޷�������CACLInteger���
    CACLInteger unsignedAdd(CACLInteger number1, CACLInteger number2);

    //���ؼ���
    CACLInteger operator-(CACLInteger number);
    CACLInteger operator-(const long long number);
    //�޷�������CACLInteger���
    CACLInteger unsignedSubtract(CACLInteger number1, CACLInteger number2);

    //���ش��ں�
    bool operator>(const CACLInteger& number);
    bool operator>(const long long number);

    //����С�ں�
    bool operator<(CACLInteger number);
    bool operator<(const long long number);

    //���ظ�ֵ
    void operator=(const CACLInteger& number);
    void operator=(const long long number);

    //����������Ϊ����
    friend istream& operator>>(istream& _cin, CACLInteger& integer);

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
