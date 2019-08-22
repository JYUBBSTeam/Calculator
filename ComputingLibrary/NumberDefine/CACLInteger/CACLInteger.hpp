/*
 *创建人:Huang
 *创建日期:2019.4.19
 *修改日期：2019.7.19 重构到字符串转换
 *类:CACLInteger
 * 数据成员（私有）：
 *      // 数字的符号,true时是负数，false时是正数
        bool symbol;
        // 数字的位数
        int bit;
        // 各个位的数字
        short num[MAX_OF_BIT];
 *重载的运算符：+加法；-减法；*乘法；/除法；%求余； =赋值；>大于；<小于
 *方法（公有）：构造方法CACLInteger()；析构方法~CALInteger()；
 *      初始化方法initialize()；拷贝方法copy()；
 *      数字转换成CACLInteger对象方法translate()；求绝对值方法absoluteValue();
 * 方法（私有）：
 */


#ifndef _CACLINEGER_H_
#define _CACLINEGER_H_

#include <iostream>
#include <string>

//定义的CACLInteger的最大位数
constexpr int MAX_OF_BIT = 100;

class CACLInteger {

public:
    // 构造方法
    CACLInteger() {
        for (auto &i : num) {
            i = 0;
        }
        symbol = false;
        bit = 1;
    };

    // string构造方法
    CACLInteger(std::string &stingNum) {
        this->translate(stingNum);
    }

    // 析构方法
    ~CACLInteger() = default;

private:
    // 初始化对象
    void initialize();

    // 拷贝对象
    void copy(const CACLInteger number);

    // 转换std::string为CACLInteger
    static CACLInteger translate(std::string &number);

public:
    // 判断是不是零
    bool isZero();

    //判断是不是负数
    bool isNegative();

    // 判断是不是正数
    bool isPositive();

    // 获取位数
    int getBit();

    std::string toString();

    // 重载加法
    CACLInteger operator+(CACLInteger number);

    CACLInteger operator+(std::string number);

    // 重载减法
    CACLInteger operator-(CACLInteger number);

    CACLInteger operator-(std::string number);

    //重载乘法
    CACLInteger operator*(CACLInteger number);

    CACLInteger operator*(std::string number);


    // 重载除法
    CACLInteger operator/(CACLInteger number);

    CACLInteger operator/(std::string number);

    // 重载求余
    CACLInteger operator%(CACLInteger number);

    CACLInteger operator%(std::string number);

    // 重载大于号
    bool operator>(CACLInteger number);

    bool operator>(std::string number);

    // 重载小于号
    bool operator<(CACLInteger number);

    bool operator<(std::string number);

    //重载等于
    bool operator==(CACLInteger number);

    bool operator==(std::string number);

    //重载不等于
    bool operator!=(CACLInteger number);

    bool operator!=(std::string number);

    //重载大于或等于
    bool operator>=(CACLInteger number);

    bool operator>=(std::string number);


    //重载小于或等于
    bool operator<=(CACLInteger number);

    bool operator<=(std::string number);

    // 重载赋值
    CACLInteger operator=(CACLInteger number);

    CACLInteger operator=(std::string number);


    //重载加赋值
    void operator+=(CACLInteger number);

    void operator+=(std::string number);

    //重载减赋值
    void operator-=(CACLInteger number);

    void operator-=(std::string number);

    // 重载乘赋值
    void operator*=(CACLInteger number);

    void operator*=(std::string number);

    // 重载除赋值
    void operator/=(CACLInteger number);

    void operator/=(std::string number);

    // 重载余赋值
    void operator%=(CACLInteger number);

    void operator%=(std::string number);


    // 重载右移作为输入
    friend std::istream &operator>>(std::istream &_cin, CACLInteger &integer);

    // 重载左移作为输出
    friend std::ostream &operator<<(std::ostream &_cout, const CACLInteger &integer);

    // 求CACLInteger的绝对值
    CACLInteger absoluteValue();

    // 转换符号
    void exchangeSymbol();

    // 获取符号
    bool getSymbol();

    // 设置符号
    void setSymbol(bool target);

private:
    // 小数据除法
    void normalDivision(CACLInteger number1, CACLInteger number2);

    // 小数据乘法
    void normalMultiplication(CACLInteger number1, CACLInteger number2);

    // 无符号两个CACLInteger相加
    CACLInteger unsignedAdd(CACLInteger number1, CACLInteger number2);

    // 无符号两个CACLInteger相减
    CACLInteger unsignedSubtract(CACLInteger number1, CACLInteger number2);

protected:
    // 数字的符号,true时是负数，false时是正数
    bool symbol;

    // 各个位的数字
    short num[MAX_OF_BIT];

private:
    // 数字的位数
    int bit;
};


#endif // !_CACLINEGER_H_
