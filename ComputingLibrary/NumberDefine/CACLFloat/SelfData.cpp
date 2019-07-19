

#include "CACLFloat.hpp"

// 初始化对象
void CACLFloat::initialize() {
    this->symbol = false;
    for (auto &i : num) {
        i = 0;
    }
}


// 拷贝对象
void CACLFloat::copy(CACLFloat number) {
    for (int i = 0; i < number.getBit(); ++i) {
        num[i] = number.num[i];
    }

    decimalBit = number.decimalBit;
}

// 将double转换为CACLFloat对象
CACLFloat CACLFloat::translate(string number) {
    CACLFloat ans;
    ans.initialize();

    for (int i = 0; number > MIN_OF_TRANSLATE_DECIMAL_BIT; ++i) {
        number *= 10;
        ans.decimalNum[i] = (long long) number;
        ans.decimalBit++;
        number -= (long long) number;
    }

    return ans;
}

// 判断是不是零
bool CACLFloat::isZero() {
    for (auto i:num) {
        if (i != 0)
            return false;
    }

    return this->decimalBit == 0;
}