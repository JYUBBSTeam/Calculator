
#include "Interval.hpp"

void CACLDefineInterval::push(bool l, CACLFloat lP, bool r, CACLFloat rP) {
    // 插入方式
    int judge = 0;
    // 插入区间规则(judge):0左右端点未找到；1未找到左端点，但有右端点；2未找到右端点，但有左端点
    auto rules = [&](CACLDomainEndPoint *theInterval) {
        // 新左端点在区间中
        if (theInterval->leftPoint <= lP && lP <= theInterval->rightPoint) {

        }

        return 0;
    };

    // 遍历segment， 查找出已经存在的范围，并插入不存在的范围
    for (auto i : this->segment) {
        if (judge = rules(i)) {
            switch (judge) {
                case :
            }
        }
    }

    this->controlCode = 1;
}

void CACLDefineInterval::push(CACLFloat number) {
    // 判断有没有在已经存在的区间存在需要插入的点
    bool judge = false;

    for (auto &i:this->segment) {
        // 没有使用点模式
        if (!i->dotMode) {
            if (number >= i->leftPoint && number <= i->rightPoint) {
                if (number == i->leftPoint && !i->left) {
                    i->left = true;
                }
                if (number == i->rightPoint && !i->right) {
                    i->right = true;
                }
                judge = true;
                break;
            }
        } else {
            if (i->dot == number) {
                judge = true;
                break;
            }
        }
    }

    if (!judge) {
        auto *newDot = new CACLDomainEndPoint(number);
        this->segment.push_back(newDot);
    }

    this->controlCode = 1;
}


void CACLDefineInterval::link(CACLDomainEndPoint &domain, CACLRangeEndPoint *range) {
    domain.linkToRange = range;
}


void CACLDefineInterval::setUnit(CACLFloat number) {
    unit = number;
}