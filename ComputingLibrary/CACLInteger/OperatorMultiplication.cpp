/*
 *创建人：Huang
 *创建日期：2019.4.19
 *修改日期：2019.4.20
 *类：CACLInteger
 *功能：重载运算符：+；-;>;<;=
 */


#include "CACLInteger.h"

//重载乘法，参照《计算机程序设计艺术，卷二》4.3.3算法T
#include <stack>
#include <vector>
#include <cmath>

// 创建控制代码
CACLInteger code_1, code_2, code_3;
// *this 记为u， number记为v
// ans 记为w
CACLInteger ans;
// tmpThis->U, tmpNumber->V, numberController->C, ansStack->W
// U和V作为临时存储，C存储用来做乘法的数和控制代码
stack<CACLInteger> numberController, ansStack;
stack<short> tmpThis, tmpNumber;

// 创建qVector、rVector两个数据表
vector<int> qVector, rVector;
// 数据表节点位置代码:k
int k;
int Q, R;
int r, q, p;

CACLInteger CACLInteger::operator*(CACLInteger number) {
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
// 将它们从栈中释放，然后调用内建的32位数乘法程序，完成赋值ans<-uv，再转向T10
// 如果k>0， 则令r<-rk, qVector<-qVectork, p<- qVectork-1 + qVectork, 然后转向T4
void T3() {
    CACLInteger normalMultiplication(CACLInteger number1, CACLInteger number2);
    void T10();
    void T4();

    k--;
    if (k == 0) {
        CACLInteger number1 = numberController.top();
        numberController.pop();
        CACLInteger number2 = numberController.top();
        numberController.pop();
        ans = normalMultiplication(number1, number2);
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

}


void T6() {

}


// T10 令k<-k + 1  释放栈C顶部的数据。
// 如果该数据为code_3， 则转到T6
// 如果该数据为code_2, 则将w放入栈W并转向T7.
// 如果该数据为code_1, 则结束算法（此时w就是计算结果）
void T10() {
    void T6();

    k++;
    CACLInteger tmpTop = numberController.top();
    numberController.pop();
    if (tmpTop == code_3) {
        T6();
    } else if (tmpTop == code_2) {
        ansStack.push(ans);
    }
}

CACLInteger normalMultiplication(CACLInteger number1, CACLInteger number2) {
    CACLInteger ans;

    return ans;
}

CACLInteger CACLInteger::operator*(const long long number) {
    CACLInteger translatedNumber = translate(number);
    CACLInteger ans;

    ans = *this * translatedNumber;

    return ans;
}