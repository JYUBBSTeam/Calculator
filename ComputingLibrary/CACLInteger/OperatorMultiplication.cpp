/*
 *创建人：Huang
 *创建日期：2019.4.19
 *修改日期：2019.4.20
 *类：CACLInteger
 *功能：重载运算符：+；-;>;<;=
 */


#include "CACLInteger.h"


//无符号两个CACLInteger相加
CACLInteger CACLInteger::unsignedAdd(CACLInteger number1, CACLInteger number2) {
    CACLInteger ans;
    CACLInteger longer, shorter;

    ans.initialize();

    //比较number1和number2的大小
    if (number1.absoluteValue() > number2.absoluteValue()) {
        longer = number1;
        shorter = number2;
    } else {
        longer = number2;
        shorter = number1;
    }

    for (int i = 0; i < shorter.bit; i++) {
        ans.num[i] = longer.num[i] + shorter.num[i];
    }

    for (int j = shorter.bit; j < longer.bit; ++j) {
        ans.num[j] = longer.num[j];
    }

    //加法运算结果最多位max(number1.bit,number2.bit) + 1位，将最高位先初始化位零
    ans.num[longer.bit] = 0;

    //统一进位
    for (int i = 0; i < longer.bit; ++i) {
        ans.num[i + 1] += ans.num[i] / 10;
        ans.num[i] %= 10;
    }

    //判断ans位数
    if (ans.num[longer.bit] == 0) {
        ans.bit = longer.bit;
    } else {
        ans.bit = longer.bit + 1;
    }

    return ans;
}


//重载减法
CACLInteger CACLInteger::operator-(CACLInteger number) {
    CACLInteger ans;
    ans.initialize();

    if (this->symbol == false && number.symbol == false) {
        ans = unsignedSubtract(*this, number);
        ans.symbol = (this->absoluteValue() > number.absoluteValue()) ? false : true;
    } else if (this->symbol == false && number.symbol == true) {
        ans = unsignedAdd(*this, number);
        ans.symbol = false;
    } else if (this->symbol == true && number.symbol == false) {
        ans = unsignedAdd(*this, number);
        ans.symbol = true;
    } else if (this->symbol == true && number.symbol == true) {
        ans = unsignedSubtract(*this, number);
        ans.symbol = (this->absoluteValue() > number.absoluteValue()) ? true : false;
    }

    return ans;
}


CACLInteger CACLInteger::operator-(const long long number) {
    CACLInteger translatedNumber = translate(number);
    CACLInteger ans;

    ans = *this - translatedNumber;

    return ans;
}


//无符号两个CACLInteger相减
CACLInteger CACLInteger::unsignedSubtract(CACLInteger number1, CACLInteger number2) {
    CACLInteger ans;
    CACLInteger longer, shorter;

    ans.initialize();

    //比较number1和number2的大小
    if (number1.absoluteValue() > number2.absoluteValue()) {
        longer = number1;
        shorter = number2;
    } else {
        longer = number2;
        shorter = number1;
    }

    for (int i = 0; i < shorter.bit; ++i) {
        ans.num[i] = longer.num[i] - shorter.num[i];
    }
    for (int i = shorter.bit; i < longer.bit; ++i) {
        ans.num[i] = longer.num[i];
    }

    //统一借位
    for (int i = 0; i < longer.bit; ++i) {
        if (ans.num[i] < 0) {
            ans.num[i + 1]--;
            ans.num[i] += 10;
        }
    }

    //判断ans位数
    int i;
    for (i = longer.bit; i > 0; --i) {
        if (ans.num[i] != 0) {
            ans.bit = i + 1;
            break;
        }
    }

    ans.bit = i + 1;

    return ans;
}


//重载乘法，参照《计算机程序设计艺术，卷二》4.3.3算法T
#include <stack>
#include <vector>
#include <cmath>

CACLInteger CACLInteger::operator*(CACLInteger number) {
    // *this 记为u， number记为v
    CACLInteger ans;
    // tmpThis->U, tmpNumber->V, numberController->C, ansStack->W
    // U和V作为临时存储，C存储用来做乘法的数和控制代码
    stack<CACLInteger> tmpThis, tmpNumber, numberController, ansStack;
    // 创建q、r两个数据表
    vector<int> q, r;
    // 数据表节点位置代码:k
    int k;
    int Q, R;

    void T3(int *k, CACLInteger *ans, );

    // 初始化控制代码code_1, code_2, code_3
    CACLInteger code_1, code_2, code_3;
    code_1.num[0] = 1;
    code_2.num[0] = 2;
    code_3.num[0] = 3;

    ans.symbol = symbol != number.symbol;
    int maxBit = max(this->bit, number.bit);

    // T1 初始化线性表q， r，使k为1， Q为4， R为2
    k = 1;
    q.push_back(16), q.push_back(16);
    r.push_back(4), r.push_back(4);
    Q = 4;
    R = 2;

    // 循环建立q，r
    while (q.at(k - 1) + q.at(k) < maxBit) {
        k++;
        Q += R;
        if ((R + 1) * (R + 1) <= Q) {
            R++;
        }
        q.push_back((int) pow(2, Q));
        r.push_back((int) pow(2, R));
    }

    // T2 在栈C中放入code_1, 然后将u和v都作为qk-1 + qk位数放入栈C
    numberController.push(code_1);
    numberController.push(*this);
    numberController.push(number);

    T3();

    return ans;
}

// T3 检查递归进度  将k减1， 如果k=0， 则栈C顶部应包含两个32位数u和v。
// 将它们从栈中释放，然后调用内建的32位数乘法程序，完成赋值ans<-uv，再转向T10
// 如果k>0， 则令r<-rk, q<-qk, p<- qk-1 + qk, 然后转向T4
void T3(){

}

CACLInteger CACLInteger::operator*(const long long number) {
    CACLInteger translatedNumber = translate(number);
    CACLInteger ans;

    ans = *this * translatedNumber;

    return ans;
}


//重载大于号
bool CACLInteger::operator>(const CACLInteger &number) {
    if (symbol != number.symbol) {
        return symbol == false ? true : false;
    }

    //从找到this和number中位数最高的，然后最高位开始比较
    if (symbol == false) {
        if (bit > number.bit) {
            return true;
        } else if (bit < number.bit) {
            return false;
        } else {
            for (int i = bit - 1; i >= 0; --i) {
                if (num[i] < number.num[i]) {
                    return false;
                }
            }
        }
    }


//类似上一个代码块
    if (symbol == true) {
        if (bit < number.bit) {
            return true;
        } else if (bit > number.bit) {
            return false;
        } else {
            for (int i = bit - 1; i >= 0; --i) {
                if (num[i] > number.num[i]) {
                    return false;
                }
            }
        }
    }

    return true;
}


bool CACLInteger::operator>(const long long number) {
    CACLInteger translatedNumber = translate(number);

    return *this > translatedNumber;
}


//重载小于号
bool CACLInteger::operator<(CACLInteger number) {
    if (symbol != number.symbol) {
        return symbol == false ? false : true;
    }

    //从找到this和number中位数最高的，然后最高位开始比较
    if (symbol == false) {
        if (bit > number.bit) {
            return false;
        } else if (bit < number.bit) {
            return true;
        } else {
            for (int i = bit - 1; i >= 0; --i) {
                if (num[i] > number.num[i]) {
                    return false;
                }
            }
        }
    }

    //类似上一个代码块
    if (this->symbol == true) {
        if (bit > number.bit) {
            return true;
        } else if (bit < number.bit) {
            return false;
        } else {
            for (int i = bit - 1; i >= 0; --i) {
                if (this->num[i] < number.num[i]) {
                    return false;
                }
            }
        }
    }

    return true;
}


bool CACLInteger::operator<(const long long number) {
    CACLInteger translatedNumber = translate(number);

    return *this < translatedNumber;
}


//重载等于
bool CACLInteger::operator==(CACLInteger number) {
    if (symbol != number.symbol) {
        return false;
    }

    if (bit != number.bit) {
        return false;
    }

    for (int i = bit - 1; i >= 0; --i) {
        if (num[i] != number.num[i])
            return false;
    }

    return true;
}

bool CACLInteger::operator==(const long long number) {
    CACLInteger translatedNumber = translate(number);

    return *this == translatedNumber;
}


//重载不等于
bool CACLInteger::operator!=(CACLInteger number) {
    return !(*this == number);
}

bool CACLInteger::operator!=(const long long number) {
    CACLInteger translatedNumber = translate(number);

    return !(*this == translatedNumber);
}


//重载大于或等于
bool CACLInteger::operator>=(CACLInteger number) {
    return *this > number || *this == number;
}


bool CACLInteger::operator>=(const long long number) {
    CACLInteger translatedNumber = translate(number);

    return *this >= translatedNumber;
}


//重载小于或等于
bool CACLInteger::operator<=(CACLInteger number) {
    return *this < number || *this == number;
}


bool CACLInteger::operator<=(const long long number) {
    CACLInteger translatedNumber = translate(number);

    return *this <= translatedNumber;
}


//重载赋值
void CACLInteger::operator=(const CACLInteger &number) {
    for (int i = 0; i < number.bit; ++i) {
        num[i] = number.num[i];
    }

    bit = number.bit;
    symbol = number.symbol;
}


void CACLInteger::operator=(const long long number) {
    const CACLInteger translatedNumber = translate(number);

    *this = translatedNumber;
}


//重载加赋值
void CACLInteger::operator+=(const CACLInteger &number) {
    *this = *this + number;
}

void CACLInteger::operator+=(const long long number) {
    const CACLInteger translatedNumber = translate(number);

    *this += translatedNumber;
}


//重载减赋值
void CACLInteger::operator-=(const CACLInteger &number) {
    *this = *this - number;
}

void CACLInteger::operator-=(const long long number) {
    const CACLInteger translatedNumber = translate(number);

    *this -= translatedNumber;
}