
#include "Interval.hpp"
#include <algorithm>

void CACLDefineInterval::push(bool l, CACLFloat lP, bool r, CACLFloat rP) {
    // 插入方式
    bool judge = false;

    auto rules = [&](CACLDomainEndPoint *theInterval) {
        // theInterval是点区间
        if (theInterval->dotMode) {
            if (theInterval->dot >= lP && theInterval->dot <= rP) {
                if (theInterval->dot == lP && !l) {
                    l = true;
                } else if (theInterval->dot == rP & !r) {
                    r = true;
                }
                int nowDomainLocation;
                for (nowDomainLocation = 0; nowDomainLocation < this->segment.size(); ++nowDomainLocation) {
                    if (this->segment.at(nowDomainLocation) == theInterval) {
                        break;
                    }
                }
                this->segment.erase(this->segment.begin() + nowDomainLocation);
                delete (theInterval);
                this->controlCode = 2;
            }
            return;
        }


        // 新左端点在区间中,而新右端点不在
        if ((theInterval->leftPoint <= lP && lP <= theInterval->rightPoint)
            && theInterval->rightPoint < rP) {
            if (theInterval->leftPoint == lP && l != theInterval->left) {
                theInterval->left = true;
            }
            theInterval->right = true;
            lP = theInterval->rightPoint;
            l = false;
            this->controlCode = 2;
        }
        // 新右端点在区间中，而新左端点不在
        if ((theInterval->leftPoint <= rP && rP <= theInterval->rightPoint)
            && theInterval->leftPoint < lP) {
            if (theInterval->rightPoint == rP && r != theInterval->right) {
                theInterval->right = true;
            }
            theInterval->left = true;
            rP = theInterval->leftPoint;
            r = false;
            this->controlCode = 2;
        }

        // 都不在区间中
        if (theInterval->leftPoint > lP && theInterval->rightPoint < rP) {
            judge = true;
        }
    };

    // 遍历segment， 查找出已经存在的范围，并插入不存在的范围
    for (auto i : this->segment) {
        rules(i);
        if (judge) {
            break;
        }
    }

    // judge判断是否插入新的区间
    if (judge) {
        auto *newDomain = new CACLDomainEndPoint(l, lP, r, rP);
        this->segment.push_back(newDomain);
        sortSegment();
        if (this->controlCode != 2) {
            this->controlCode = 1;
        }
    }
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
        this->sortSegment();
        this->controlCode = 1;
    }
}