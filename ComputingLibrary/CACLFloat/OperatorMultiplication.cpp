
#include "CACLFloat.hpp"

//重载乘法
cacl::CACLFloat cacl::CACLFloat::operator*(cacl::CACLFloat number) {
    CACLFloat ans;
    ans.initialize();

    if (this->isZero() || number.isZero()) {
        return ans;
    } else {
        ans.integer = this->integer * number.integer;
        // 利用无符号小数乘法
        unsignedMultiplication(&ans, *this, number);

        // 设置ans符号
        ans.integer.setSymbol(this->integer.getSymbol() != number.integer.getSymbol());
    }

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

    CACLFloat temp = unsignedIntegerFloatMultiplication(longer.integer, shorter);
    temp.integer.setSymbol(ans->integer.getSymbol());
    *ans += temp;
    temp = unsignedIntegerFloatMultiplication(shorter.integer, longer);
    temp.integer.setSymbol(ans->integer.getSymbol());
    *ans += temp;
}

// 将number2转换成乘以10的number2.decimalBit次方的CACLInteger类型对象，以两个CACLInteger的方式相乘
cacl::CACLFloat
cacl::CACLFloat::unsignedIntegerFloatMultiplication(cacl::CACLInteger number1, cacl::CACLFloat number2) {
    CACLInteger tempNumber;

    // 把number2的小数转换成整数
    for (int i = 0; i < number2.decimalBit; ++i) {
        tempNumber += number2.decimalNum[i] * pow(10, number2.decimalBit - 1 - i);
    }

    CACLFloat ans;
    ans = tempNumber * number1;
    // 将ans向后移动ans.decimalBit位
    for (int j = 0, i = number2.decimalBit - 1; i >= 0; ++j, --i) {
        ans.decimalNum[i] = *ans.integer.at(j);
    }

    // 设置小数部分位数
    ans.decimalBit = number2.decimalBit;
    for (int k = 0; k < ans.integer.getBit() - ans.decimalBit; ++k) {
        *ans.integer.at(k) = *ans.integer.at(k + ans.decimalBit);
    }
    for (int l = ans.integer.getBit() - 1; l >= ans.integer.getBit() - number2.decimalBit; --l) {
        *ans.integer.at(l) = 0;
    }

    // 设置整数的位数
    if (number1.getBit() - ans.decimalBit < 0) {
        ans.integer.setBit(1);
        *ans.integer.at(0) = 0;
    } else {
        if (*ans.integer.at(number1.getBit() - ans.decimalBit) > 0) {
            ans.integer.setBit(number1.getBit() - ans.decimalBit + 1);
        } else {
            ans.integer.setBit(number1.getBit() - ans.decimalBit);
        }
    }

    return ans;
}