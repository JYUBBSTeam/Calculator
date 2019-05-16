
#include "CACLFloat.hpp"

//重载乘法
cacl::CACLFloat cacl::CACLFloat::operator*(cacl::CACLFloat number) {
    CACLFloat ans;
    ans.initialize();

    ans.integer = this->integer * number.integer;
    // 利用无符号小数乘法
    unsignedMultiplication(&ans, *this, number);

    return ans;
}

cacl::CACLFloat cacl::CACLFloat::operator*(double number) {
    CACLFloat translatedNumber = translate(number);
    CACLFloat ans;

    ans = *this * translatedNumber;

    return ans;
}

void cacl::CACLFloat::unsignedMultiplication(cacl::CACLFloat *ans, cacl::CACLFloat number1, cacl::CACLFloat number2) {
    CACLFloat longer, shorter;
    // 用于记录整数部分
    CACLInteger tempNumber;

    if (number1.decimalBit > number2.decimalBit) {
        longer = number1;
        shorter = number2;
    } else {
        longer = number2;
        shorter = number1;
    }

    // 根据分配律a.b * c.d = a * c + a * 0.d + 0.b * c + 0.b * 0.d
    for (int j = shorter.decimalBit - 1; j >= 0; --j) {
        if (shorter.decimalNum[j] > 0) {
            for (int i = longer.decimalBit - 1; i >= 0; --i) {
                ans->decimalNum[i + j + 1] += longer.decimalNum[i] * shorter.decimalNum[j];
            }
        }
    }
    *ans += unsignedIntegerFloatMultiplication(longer.integer, shorter);
    *ans += unsignedIntegerFloatMultiplication(shorter.integer, longer);


    // 统一进位
    for (int k = longer.decimalBit + shorter.decimalBit - 1; k > 0; --k) {
        ans->decimalNum[k - 1] += ans->decimalNum[k] / 10;
        ans->decimalNum[k] %= 10;
    }

    // 处理零位
    tempNumber = ans->decimalNum[0] / 10;
    ans->decimalNum[0] %= 10;
    ans->integer += tempNumber;

    // 求小数位数
    ans->decimalBit = number1.decimalBit + number2.decimalBit;
}

// 将number2转换成乘以10的number2.decimalBit次方的CACLInteger类型对象，以两个CACLInteger的方式相乘
cacl::CACLFloat cacl::CACLFloat::unsignedIntegerFloatMultiplication(cacl::CACLInteger number1, cacl::CACLFloat number2) {

}