#include "CACLInteger.h"

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