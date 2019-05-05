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
#include "../CACLInteger/CACLInteger.h"

// 小数最小位数
constexpr int MAX_OF_DECIMAL_BIT = 320;
constexpr double MIN_OF_TRANSLATE_DECIMAL_BIT = 10e-18;

namespace cacl {

    class CACLFloat {
    public:
        // 构造CACLFloat
        CACLFloat() {
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

        // 重载右移动作为输入
        friend std::istream &operator>>(std::istream &_cin, CACLFloat &myFloat);

        // 重载左移作为输出
        friend std::ostream &operator<<(std::ostream &_cout, CACLFloat &myFloat);

    private:

        // 小数位数
        int decimalBit;

        // 小数部分的数字
        short decimalNum[MAX_OF_DECIMAL_BIT]{};

        // 整数部分
        cacl::CACLInteger integer;
    };
}

#endif //CACLFLOAT_CACLFLOAT_H
