/*
 *创建人：Huang
 *创建日期：2019.4.19
 *修改日期：2019.4.20
 *类：CACLInteger
 *功能：重载运算符：+；-;>;<;=
 */


#include "CACLInteger.hpp"

/* 暂时实现不了算法T
//重载乘法，参照《计算机程序设计艺术，卷二》4.3.3算法T
#include <stack>
#include <vector>
#include <cmath>

// 创建控制代码
CACLInteger code_1, code_2, code_3;
// *this 记为u， number记为v
// ans 记为w
CACLInteger ans;
// tempThis->U, tempNumber->V, numberController->C, ansStack->W
// U和V作为临时存储，C存储用来做乘法的数和控制代码
stack<CACLInteger> numberController, ansStack;
stack<short> tempThis, tempNumber;

// 创建qVector、rVector两个数据表
vector<int> qVector, rVector;
// 数据表节点位置代码:k
int k;
int Q, R;
int r, q, p;

CACLInteger cacl::CACLInteger::operator*(CACLInteger number) {
    void T3();

    // 初始化控制代码code_1, code_2, code_3
    code_1.num[0] = 1;
    code_2.num[0] = 2;
    code_3.num[0] = 3;

    ans.symbol = symbol != number.symbol;
    int maxBit = max(this->bit, number.bit);

    // T1 初始化线性表qVector， r，使k为1， qVector为4， R为2
    k = 1;
    qVector.push_back(16), qVector.push_back(16);
    rVector.push_back(4), rVector.push_back(4);
    Q = 4;
    R = 2;

    // 循环建立qVector，r
    while (qVector.at(k - 1) + qVector.at(k) < maxBit) {
        k++;
        Q += R;
        if ((R + 1) * (R + 1) <= Q) {
            R++;
        }
        qVector.push_back((int) pow(2, Q));
        rVector.push_back((int) pow(2, R));
    }

    // T2 在栈C中放入code_1, 然后将u和v都作为qVectork-1 + qVectork位数放入栈C
    numberController.push(code_1);
    numberController.push(*this);
    numberController.push(number);

    T3();

    return ans;
}

// T3 检查递归进度  将k减1， 如果k=0， 则栈C顶部应包含两个32位数u和v。
// 将它们从栈中释放，然后调用内建的32位数乘法程序(在这里，我写了一个简单的小数据乘法函数normalMultiplication），完成赋值ans<-uv，再转向T10
// 如果k>0， 则令r<-rk, qVector<-qVectork, p<- qVectork-1 + qVectork, 然后转向T4
void T3() {
    void T10();
    void T4();

    k--;
    if (k == 0) {
        CACLInteger number1 = numberController.top();
        numberController.pop();
        CACLInteger number2 = numberController.top();
        numberController.pop();
        ans.normalMultiplication(number1, number2);
        T10();
    }

    if (k > 0) {
        r = rVector.at(k);
        q = qVector.at(k);
        p = qVector.at(k - 1) + qVector.at(k);
        T4();
    }
}


// 拆分r + 1块
void T4() {
    // 将栈C顶部的数看做r+1个 q位 数的序列（ Ur ... U1 U0）2q
    // （栈C的顶部现在应该是一个（r+1）q = （qk + qk+1）位数）
    // 对j = 0,1， 2， ... 2r
    // 计算p位数

}


// （此时乘法算法已将w赋值为诸乘积 W(j) = U(j) V(j)之一了）
// 将w放入栈W（w是 2 (qk + qk-1)为数）转回到T3
void T6() {

}


//
void T7() {

}


// T10 令k<-k + 1  释放栈C顶部的数据。
// 如果该数据为code_3， 则转到T6
// 如果该数据为code_2, 则将w放入栈W并转向T7.
// 如果该数据为code_1, 则结束算法（此时w就是计算结果）
void T10() {
    void T6();
    void T7();

    k++;
    CACLInteger tempTop = numberController.top();
    numberController.pop();
    if (tempTop == code_3) {
        T6();
    } else if (tempTop == code_2) {
        ansStack.push(ans);
        T7();
    }
}
 */

void cacl::CACLInteger::normalMultiplication(CACLInteger number1, CACLInteger number2) {
    // 判断两个乘数是不是零，直接return this是因为任何CACLInteger的初始值为0
    if (number1.isZero() || number2.isZero()) {
        this->bit = 1;
        this->num[0] = 0;
        this->symbol = false;
        return;
    }

    int maxBit = number1.bit + number2.bit;
    // 初始化要可能要使用的位
    for (int i = 0; i < maxBit; ++i) {
        this->num[i] = 0;
    }

    // 累加
    for (int i = 0; i < number1.bit; ++i) {
        if (number1.num[i] > 0) {
            for (int j = 0; j < number2.bit; ++j) {
                this->num[i + j] += number1.num[i] * number2.num[j];
            }
        }
    }

    // 统一进位
    for (int l = 0; l < maxBit; ++l) {
        this->num[l + 1] += this->num[l] / 10;
        this->num[l] %= 10;
    }

    this->symbol = number1.symbol != number2.symbol;

    // 判断相乘后的位数
    if (this->num[maxBit - 1] > 0) {
        this->bit = maxBit;
    } else {
        this->bit = maxBit - 1;
    }
}

cacl::CACLInteger cacl::CACLInteger::operator*(CACLInteger number) {
    CACLInteger ans;

    ans.normalMultiplication(*this, number);

    return ans;
}

cacl::CACLInteger cacl::CACLInteger::operator*(const long long number) {
    CACLInteger translatedNumber = translate(number);
    CACLInteger ans;

    ans = *this * translatedNumber;

    return ans;
}