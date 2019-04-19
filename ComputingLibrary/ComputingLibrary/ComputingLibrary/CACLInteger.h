/*
 *创建人:Huang
 *日期:2019.4.19
 *类:CACLInteger
 *重载的运算符：+加法；-减法；*乘法；/除法；%求余； =赋值；>大于；<小于
 *方法：构造方法CACLInteger()；析构方法~CALInteger()；拷贝构造方法CACLInteger(const CACLInteger *obj)；
 *      初始化方法initialize()；拷贝方法copy()；数字转换成CACLInteger对象方法translate()；求绝对值方法Ab
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
    void copy(const CACLInteger number);

    //转换long long为CACLInteger
    CACLInteger translate(const long long number);

    //重载加法
    CACLInteger operator+(const CACLInteger number);
    CACLInteger operator+(const long long number);
    //无符号两个CACLInteger相加
    CACLInteger unsignedAdd(const CACLInteger number1, const CACLInteger number2);

    //重载减法
    CACLInteger operator-(const CACLInteger number);
    CACLInteger operator-(const long long number);
    //无符号两个CACLInteger相减
    CACLInteger unsignedSubtract(const CACLInteger number1, const CACLInteger number2);

    //重载大于号
    bool operator>(const CACLInteger number);
    bool operator>(const long long number);

    //重载小于号
    bool operator<(const CACLInteger number);
    bool operator<(const long long number);

    //重载赋值
    void operator=(const CACLInteger number);
    void operator=(const long long number);

    //求CACLInteger的绝对值
    CACLInteger absoluteValue(const CACLInteger number);



private:
    //数字的符号,true时是负数，false时是正数
    bool symbol;
    //数字的位数
    int bit;
    //各个位的数字
    short num[MAX_OF_BIT];

};

#endif // !_CACLINEGER_H_
