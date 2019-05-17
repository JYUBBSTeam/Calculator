
#include "CACLFloat.hpp"

//重载除法
cacl::CACLFloat cacl::CACLFloat::operator/(cacl::CACLFloat number) {
    CACLFloat ans;
    ans.initialize();

    // 利用无符号CACLFloat相除函数
    unsignedDivision(&ans, *this, number);

    // 设置ans的符号
    ans.integer.setSymbol(this->integer.getSymbol() != number.integer.getSymbol());

    return ans;
}

cacl::CACLFloat cacl::CACLFloat::operator/(double number) {
    CACLFloat translatedNumber = translate(number);
    CACLFloat ans;

    ans = *this / translatedNumber;
    return ans;
}

void
cacl::CACLFloat::unsignedDivision(cacl::CACLFloat *ans, cacl::CACLFloat number1, cacl::CACLFloat number2) {
    CACLInteger tempNumber1, tempNumber2;

    // (lambda) 转换CACLFloat到CACLInteger（根据precision）
    auto tempTranslate = [](CACLFloat number, int tempPrecision) {
        CACLInteger translatedNumber;
        CACLInteger ten;
        CACLInteger bigPrecision;
        bigPrecision = tempPrecision;
        ten = 10;

        // 腾出位置
        translatedNumber = number.integer * pow(ten, bigPrecision);

        // 进行位移
        for (int i = 0; i <= tempPrecision; ++i) {
            translatedNumber += pow(ten, bigPrecision - 1 - i) * number.decimalNum[i];
        }

        return translatedNumber;
    };

    // 将number1和number2根据precision转换成CACLInteger
    tempNumber1 = tempTranslate(number1, 2 * precision);
    tempNumber2 = tempTranslate(number2, precision);

    // 计算值
    ans->integer += tempNumber1 / tempNumber2;

    // 将ans向后移动precision位
    for (int j = 0, i = precision - 1; i >= 0; ++j, --i) {
        ans->decimalNum[i] = *ans->integer.at(j);
    }
    ans->decimalBit = precision;
    for (int l = ans->integer.getBit() - 1; l >= ans->integer.getBit() - precision; --l) {
        *ans->integer.at(l) = 0;
    }

    // 设置整数的位数
    if (ans->integer.getBit() - ans->decimalBit < 0) {
        ans->integer.setBit(1);
        *ans->integer.at(0) = 0;
    } else {
        if (*ans->integer.at(ans->integer.getBit() - ans->decimalBit) > 0) {
            ans->integer.setBit(ans->integer.getBit() - ans->decimalBit + 1);
        } else {
            ans->integer.setBit(ans->integer.getBit() - ans->decimalBit);
        }
    }
}