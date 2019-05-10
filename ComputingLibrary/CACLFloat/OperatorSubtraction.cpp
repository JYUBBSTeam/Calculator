
#include "CACLFloat.hpp"

cacl::CACLFloat cacl::CACLFloat::operator-(cacl::CACLFloat number) {
    CACLFloat ans;

    if (this->integer.getSymbol() == false && number.integer.getSymbol() == false) {
        unsignedSubtraction(&ans, *this, number);
    } else if (this->integer.getSymbol() == false && number.integer.getSymbol() == true) {
        unsignedAddition(&ans, *this, number);
    } else if (this->integer.getSymbol() == true && number.integer.getSymbol() == false) {
        unsignedAddition(&ans, *this, number);
    } else if (this->integer.getSymbol() == true && number.integer.getSymbol() == true) {
        unsignedSubtraction(&ans, *this, number);
    }

    return ans;
}


cacl::CACLFloat cacl::CACLFloat::operator-(double number) {
    CACLFloat translatedNumber = translate(number);
    CACLFloat ans;

    ans = *this - translatedNumber;

    return ans;
}

void cacl::CACLFloat::unsignedSubtraction(cacl::CACLFloat *ans, cacl::CACLFloat number1, cacl::CACLFloat number2) {
    CACLFloat longer, shorter;
    ans->initialize();

    ans->integer = number1.integer - number2.integer;

    // 比较number1和number2的绝对值大小
    // 并且将大的赋值给longer，小的赋值给shorter
    if (number1.absoluteValue() > number2.absoluteValue()) {
        longer = number1;
        shorter = number2;
    } else {
        longer = number2;
        shorter = number1;
    }

    for (int i = 0; i < shorter.decimalBit; ++i) {
        ans->decimalNum[i] = longer.decimalNum[i] - shorter.decimalNum[i];
    }
    for (int j = shorter.decimalBit; j < longer.decimalBit; ++j) {
        ans->decimalNum[j] = longer.decimalNum[j];
    }

    // 统一借位,零位不处理
    for (int k = longer.decimalBit - 1; k > 0; --k) {
        if (ans->decimalNum[k] < 0) {
            ans->decimalNum[k - 1]--;
            ans->decimalNum[k] += 10;
        }
    }

    // 处理零位的借位问题
    if (ans->decimalNum[0] < 0) {
        if (ans->integer.isPositive()) {
            ans->integer -= 1;
        } else {
            ans->integer += 1;
        }
        ans->decimalNum[0] += 10;
    }

    // 判断小数位
    int i;
    for (i = longer.decimalBit; i > 0; --i) {
        if (ans->decimalNum[i] != 0) {
            ans->decimalBit = i + 1;
            break;
        }
    }
    ans->decimalBit = i + 1;
}