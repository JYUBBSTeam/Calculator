#include "CACLInteger.h"

using namespace caclInt;

// 重载除法
CACLInteger CACLInteger::operator/(CACLInteger number) {
    CACLInteger ans;

    ans.normalDivision(*this, number);

    return ans;
}


CACLInteger CACLInteger::operator/(const long long number) {
    CACLInteger translatedNumber = translate(number);
    CACLInteger ans;

    ans = *this / translatedNumber;

    return ans;
}


// 小数据除法
void CACLInteger::normalDivision(CACLInteger number1, CACLInteger number2) {
    CACLInteger tmpNumber1, tmpNumber2;
    CACLInteger tryNumber;

    if (number2.isZero()) {
        cout << "The denominator cannot be zero!\n";
        exit(1);
    }

    if (number1.isZero() || number1.absoluteValue() < number2.absoluteValue()) {
        return;
    } else {
        tmpNumber1 = number1;

        // 除数末尾添零使其与被除数等长
        int i;
        for (i = 0; i < number1.bit - number2.bit; ++i) {
            tmpNumber2.num[i] = 0;
        }
        for (; i < number1.bit; ++i) {
            tmpNumber2.num[i] = number2.num[i - (number1.bit - number2.bit)];
        }
        tmpNumber2.bit = number1.bit;
        tmpNumber2.symbol = number2.symbol;

        // 做出发，最多进行number1.bit - number2.bit + 1次
        for (int j = number1.bit - number2.bit; j >= 0; --j) {
            if (tmpNumber1.isZero()) {
                this->num[j] = 0;
            } else {
                // 试商
                for (int k = 9; k >= 0; --k) {
                    tryNumber = tmpNumber2 * k;
                    if (tmpNumber1 >= tryNumber) {
                        tmpNumber1 -= tryNumber;
                        this->num[j] = k;

                        // 右移一位， 最后一次不用右移
                        for (int l = 0; l < tmpNumber2.bit - 1 && i > 0; ++l) {
                            tmpNumber2.num[l] = tmpNumber2.num[l + 1];
                        }
                        tmpNumber2.bit--;
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
        int tmpBit;
        CACLInteger tmpNumber;

        while (number1 >= number2) {
            tmpNumber.initialize();
            tmpNumber.bit = number1.bit - number2.bit;
            for (int i = number1.bit - 1, j = i; i > tmpNumber.bit; --i, --j) {
                tmpNumber.num[j] = number1.num[i];
            }

            long long tryNumber = 0;
            while (number2 * tryNumber <= tmpNumber) {
                tryNumber++;
            }
            tryNumber--;
            if (tryNumber != 0 && !noteFirstInput) {
                noteFirstInput = true;
                tmpBit = bit = number1.bit - number2.bit + 1;
                tmpBit--;
                num[tmpBit] = tryNumber;
            }
            if (noteFirstInput) {
                num[tmpBit] = tryNumber;
            }

            number1 -= number2 * tryNumber * 10 * (number1.bit - number2.bit);
        }
        return noteNumber1 - *this * number2;
    }
}
 */