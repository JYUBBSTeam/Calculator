/*
 * 创建人：黄子涵
 * 修改时间：2019.7.19
 */

#include "CACLInteger.hpp"

// 重载除法
CACLInteger CACLInteger::operator/(CACLInteger number) {
    CACLInteger ans;

    ans.normalDivision(*this, number);

    return ans;
}


CACLInteger CACLInteger::operator/(std::string number) {
    CACLInteger translatedNumber = translate(number);
    CACLInteger ans;

    ans = *this / translatedNumber;

    return ans;
}


// 小数据除法
void CACLInteger::normalDivision(CACLInteger number1, CACLInteger number2) {
    CACLInteger tempNumber1, tempNumber2;
    CACLInteger tryNumber;

    if (number2.isZero()) {
        std::cout << "The denominator cannot be zero!\n";
        exit(1);
    }

    if (number1.isZero() || number1.absoluteValue() < number2.absoluteValue()) {
        return;
    } else {
        tempNumber1 = number1;

        // 除数末尾添零使其与被除数等长
        int i;
        for (i = 0; i < number1.bit - number2.bit; ++i) {
            tempNumber2.num[i] = 0;
        }
        for (; i < number1.bit; ++i) {
            tempNumber2.num[i] = number2.num[i - (number1.bit - number2.bit)];
        }
        tempNumber2.bit = number1.bit;
        tempNumber2.symbol = number2.symbol;

        // 做出发，最多进行number1.bit - number2.bit + 1次
        for (int j = number1.bit - number2.bit; j >= 0; --j) {
            if (tempNumber1.isZero()) {
                this->num[j] = 0;
            } else {
                // 试商
                for (CACLInteger k = (const CACLInteger &) "9"; k >= "0"; k -= "1") { // 这里的const CACLInteger &是测试型写法
                    tryNumber = tempNumber2 * k;
                    if (tempNumber1 >= tryNumber) {
                        tempNumber1 -= tryNumber;
                        this->num[j] = k.num[0];

                        // 右移一位， 最后一次不用右移
                        for (int l = 0; l < tempNumber2.bit - 1 && i > 0; ++l) {
                            tempNumber2.num[l] = tempNumber2.num[l + 1];
                        }
                        tempNumber2.bit--;
                        break;
                    }
                }
            }
        }

        // 确定运算结果的位数
        if (this->num[number1.bit - number2.bit] == 0) {
            this->bit = number1.bit - number2.bit;
        } else {
            this->bit = number1.bit - number2.bit + 1;
        }

        // 确定运算结果的符号
        this->symbol = number1.symbol != number2.symbol;
    }
}



/* 原本是小数据除法，但是bug太多，故而换重新写了函数
CACLInteger CACLInteger::normalDivision(CACLInteger number1, CACLInteger number2) {
    if (number2.isZero()) {
        cout << "The denominator cannot be zero!\n";
        exit(1);
    }

    if (number1.isZero()) {
        return number1;
    }

    if (number1 < number2) {
        return number1;
    } else {
        CACLInteger noteNumber1 = number1;

        symbol = number1.symbol != number2.symbol;
        number1.symbol = false;
        number2.symbol = false;

        bool noteFirstInput = false;
        int tempBit;
        CACLInteger tempNumber;

        while (number1 >= number2) {
            tempNumber.initialize();
            tempNumber.bit = number1.bit - number2.bit;
            for (int i = number1.bit - 1, j = i; i > tempNumber.bit; --i, --j) {
                tempNumber.num[j] = number1.num[i];
            }

            long long tryNumber = 0;
            while (number2 * tryNumber <= tempNumber) {
                tryNumber++;
            }
            tryNumber--;
            if (tryNumber != 0 && !noteFirstInput) {
                noteFirstInput = true;
                tempBit = bit = number1.bit - number2.bit + 1;
                tempBit--;
                num[tempBit] = tryNumber;
            }
            if (noteFirstInput) {
                num[tempBit] = tryNumber;
            }

            number1 -= number2 * tryNumber * 10 * (number1.bit - number2.bit);
        }
        return noteNumber1 - *this * number2;
    }
}
 */