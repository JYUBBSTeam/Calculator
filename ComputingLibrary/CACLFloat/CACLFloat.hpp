/*
 * 创建人：Huang
 * 创建日期：2019.5.3
 * 修改日期：2019.5.3
 * 类：CACLFloat
 * 数据成员（私有）：
 *      // 符号，如果false是正数，true是负数
        bool symbol;
        // 整数位数
        int integerBit;
        // 小数位数
        int decimalBit;
        // 整数部分的数字
        short integerNum[MAX_OF_INTEGER_BIT];
        // 小数部分的数字
        short decimalNum[MAX_OF_DECIMAL_BIT];
 * 重载的运算符：+加法；-减法；*乘法；/除法；%求余； =赋值；>大于；<小于
 * 方法(公有）：构造方法CACLFloat()；析构方法～CACLFloat();
 *      初始化方法initialize()；拷贝方法copy()；
 *      数字转换成CACLInteger对象方法translate()；求绝对值方法absoluteValue();
 * 方法（私有）：
 */

#ifndef CACLFLOAT_CACLFLOAT_H
#define CACLFLOAT_CACLFLOAT_H

#include <iostream>
#include "../CACLInteger/CACLInteger.hpp"

// 小数最小位数
constexpr int MAX_OF_DECIMAL_BIT = 320;
// double转换为CACLFloat精度
constexpr double MIN_OF_TRANSLATE_DECIMAL_BIT = 10e-18;
// 输出精度
static int precision = 5;

// 设置精度
void setPrecision();

// 初始化进度为0.00001
void initPrecision();

namespace cacl {

    class CACLFloat {
    public:
        // 构造CACLFloat
        CACLFloat() {
            for (auto &i : decimalNum) {
                i = 0;
            }
            decimalBit = 0;
        };

        // 析构CACLFloat
        ~CACLFloat() = default;

        // 初始化对象
        void initialize();

        // 拷贝对象
        void copy(const CACLFloat number);

        // 将double转换为CACLFloat对象
        CACLFloat translate(double number);

        // 判断是不是零
        bool isZero();

        // 判断是不是负数
        bool isNegative();

        // 判断是不是正数
        bool isPositive();

        // 转换符号
        void exchangeSymbol();

        // 重载加法
        CACLFloat operator+(CACLFloat number);

        CACLFloat operator+(double number);

        // 重载减法
        CACLFloat operator-(CACLFloat number);

        CACLFloat operator-(double number);

        // 重载乘法
        CACLFloat operator*(CACLFloat number);

        CACLFloat operator*(double number);

        // 重载除法
        CACLFloat operator/(CACLFloat number);

        CACLFloat operator/(double number);

        // 重载大于号
        bool operator>(CACLFloat number);

        bool operator>(double number);

        // 重载小于号
        bool operator<(CACLFloat number);

        bool operator<(double number);

        // 重载大于或等于号
        bool operator>=(CACLFloat number);

        bool operator>=(double number);

        // 重载小于或等于号
        bool operator<=(CACLFloat number);

        bool operator<=(double number);

        // 重载等于号
        bool operator==(CACLFloat number);

        bool operator==(double number);

        // 重载赋值
        CACLFloat operator=(CACLFloat number);

        CACLFloat operator=(CACLInteger number);

        CACLFloat operator=(double number);

        //重载加赋值
        CACLFloat operator+=(CACLFloat number);

        CACLFloat operator+=(double number);

        //重载减赋值
        CACLFloat operator-=(CACLFloat number);

        CACLFloat operator-=(double number);

        //重载乘赋值
        CACLFloat operator*=(CACLFloat number);

        CACLFloat operator*=(double number);

        //重载除赋值
        CACLFloat operator/=(CACLFloat number);

        CACLFloat operator/=(double number);

        // 重载右移动作为输入
        friend std::istream &operator>>(std::istream &_cin, CACLFloat &myFloat);

        // 重载左移作为输出
        friend std::ostream &operator<<(std::ostream &_cout, CACLFloat &myFloat);

        // 求绝对值
        CACLFloat absoluteValue();

    private:

        // 无符号小数相加
        void unsignedAddition(CACLFloat *ans, CACLFloat number1, CACLFloat number2);

        // 无符号小数相减
        void unsignedSubtraction(CACLFloat *ans, CACLFloat number1, CACLFloat number2);

        // 无符号小数乘法
        void unsignedMultiplication(CACLFloat *ans, CACLFloat number1, CACLFloat number2);

        // 无符号整数和小数相乘
        CACLFloat unsignedIntegerFloatMultiplication(CACLInteger number1, CACLFloat number2);

        // 无符号CACLFloat相除
        void unsignedDivision(CACLFloat *ans, CACLFloat number1, CACLFloat number2);

    private:
        // 小数位数
        int decimalBit;

        // 小数部分的数字
        short decimalNum[MAX_OF_DECIMAL_BIT]{};

        // 整数部分
        CACLInteger integer;
    };
}

// 找出两个参数的最大值
template<class T>
T max(T value1, T value2) {
    return value1 > value2 ? value1 : value2;
}

// 找出两个参数的最小值
template<class T>
T min(T value1, T value2) {
    return value1 < value2 ? value1 : value2;
}

// 整数pow
template<class T>
T pow(T x, T n) {
    T one, zero;
    one = 1;
    if (n == zero) {
        return one;
    } else if (n == one) {
        return x;
    }

    if (n % 2 == 0) {
        return pow(x * x, n / 2);
    } else {
        return pow(x * x, n / 2) * x;
    }
}

// 交换两个数
template<class T>
void swap(T *a, T *b) {
    T *temp = a;
    a = b;
    b = temp;
}

#endif //CACLFLOAT_CACLFLOAT_H
