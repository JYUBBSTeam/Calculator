/*
 *������:Huang
 *����:2019.4.19
 *��:CACLInteger
 *���ص��������+�ӷ���-������*�˷���/������%���ࣻ =��ֵ��>���ڣ�<С��
 *���������췽��CACLInteger()����������~CALInteger()���������췽��CACLInteger(const CACLInteger *obj)��
 *      ��ʼ������initialize()����������copy()������ת����CACLInteger���󷽷�translate()�������ֵ����Ab
 */


#ifndef _CACLINEGER_H_
#define _CACLINEGER_H_

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
    CACLInteger operator+(const CACLInteger number);
    CACLInteger operator+(const long long number);
    //�޷�������CACLInteger���
    CACLInteger unsignedAdd(const CACLInteger number1, const CACLInteger number2);

    //���ؼ���
    CACLInteger operator-(const CACLInteger number);
    CACLInteger operator-(const long long number);
    //�޷�������CACLInteger���
    CACLInteger unsignedSubtract(const CACLInteger number1, const CACLInteger number2);

    //���ش��ں�
    bool operator>(const CACLInteger number);
    bool operator>(const long long number);

    //����С�ں�
    bool operator<(const CACLInteger number);
    bool operator<(const long long number);

    //���ظ�ֵ
    void operator=(const CACLInteger number);
    void operator=(const long long number);

    //��CACLInteger�ľ���ֵ
    CACLInteger absoluteValue(const CACLInteger number);



private:
    //���ֵķ���,trueʱ�Ǹ�����falseʱ������
    bool symbol;
    //���ֵ�λ��
    int bit;
    //����λ������
    short num[MAX_OF_BIT];

};

#endif // !_CACLINEGER_H_
