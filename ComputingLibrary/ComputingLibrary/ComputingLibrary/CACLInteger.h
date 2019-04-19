/*
 *创建人:Huang
 *日期:2019.4.19
 *类:CACLInteger
 *重载的运算符：+加法；-减法；*乘法；/除法；%求余
 *方法：构造方法CACLInteger()；析构方法~CALInteger()；拷贝构造方法CACLInteger(const CACLInteger *obj)；
 */


#ifndef _CACLINEGER_H_
#define _CACLINEGER_H_

//定义的CACLInteger的最大位数
constexpr int MAX_OF_BIT = 200;

class CACLInteger {
public:
    //构造方法
    CACLInteger();
    //拷贝构造方法
    CACLInteger(const CACLInteger& obj);
    //析构方法
    ~CACLInteger();

    //初始化对象
    void initialize();

    //拷贝对象
    CACLInteger copy(const CACLInteger number);

    //重载加法
    CACLInteger operator+(const CACLInteger& number);
    CACLInteger operator+(const int number);


private:
    //数字的符号,true时是负数，false时是正数
    bool symbol;
    //数字的位数
    int bit;
    //各个位的数字
    short num[MAX_OF_BIT];

};

#endif // !_CACLINEGER_H_
