
#include "CACLFloat.hpp"

//重载除法
CACLFloat CACLFloat::operator/(CACLFloat number) {
    CACLFloat ans;
    ans.initialize();

    // 利用无符号CACLFloat相除函数
    unsignedDivision(&ans, *this, number);

    // 设置ans的符号
    ans.integer.setSymbol(this->integer.getSymbol() != number.integer.getSymbol());

    return ans;
}

CACLFloat CACLFloat::operator/(double number) {
    CACLFloat translatedNumber = translate(number);
    CACLFloat ans;

    ans = *this / translatedNumber;
    return ans;
}

void
CACLFloat::unsignedDivision(CACLFloat *ans, CACLFloat number1, CACLFloat number2) {
    CACLInteger tempNumber1, tempNumber2;
    int tempPrecision = precision + 1;

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
    tempNumber1 = tempTranslate(number1, 2 * tempPrecision);
    tempNumber2 = tempTranslate(number2, tempPrecision);

    // 计算值
    ans->integer = tempNumber1 / tempNumber2;

    // 临时记录ans->integer的bit
    int tempAnsIntBit = (number1.integer / number2.integer).getBit();

    // 将ans向后移动precision位
    for (int j = 0, i = ans->integer.getBit() - tempAnsIntBit - 1; i >= 0; ++j, --i) {
        ans->decimalNum[i] = *ans->integer.at(j);
    }
    ans->decimalBit = precision;
    for (int k = ans->integer.getBit() - 1, j = tempAnsIntBit - 1; j >= 0; --k, --j) {
        *ans->integer.at(j) = *ans->integer.at(k);
    }
    for (int l = ans->integer.getBit() - 1; l > tempAnsIntBit - 1; --l) {
        *ans->integer.at(l) = 0;
    }

    // 设置整数部分的位数
    ans->integer.setBit(tempAnsIntBit);
}