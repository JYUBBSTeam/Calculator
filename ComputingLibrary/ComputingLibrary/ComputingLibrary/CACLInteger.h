/*
 *������:Huang
 *����:2019.4.19
 *��:CACLInteger
 *���ص��������+�ӷ���-������*�˷���/������%����
 *���������췽��CACLInteger()����������~CALInteger()���������췽��CACLInteger(const CACLInteger *obj)��
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
    CACLInteger copy(const CACLInteger number);

    //���ؼӷ�
    CACLInteger operator+(const CACLInteger& number);
    CACLInteger operator+(const int number);


private:
    //���ֵķ���,trueʱ�Ǹ�����falseʱ������
    bool symbol;
    //���ֵ�λ��
    int bit;
    //����λ������
    short num[MAX_OF_BIT];

};

#endif // !_CACLINEGER_H_
