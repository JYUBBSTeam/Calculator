
#include "Interval.hpp"

void CACLDefineInterval::push(bool l, CACLFloat lP, bool r, CACLFloat rP) {
    // 插入方式
    int judge = 0;
    // 遍历segment， 查找出已经存在的范围，并插入不存在的范围
    // 插入区间规则:
    auto rules = [&](CACLDomainEndPoint &theInterval) {
        // 不用点模式
        if (!theInterval.dotMode) {
            // 新的左端点在此区间中
            if (theInterval.leftPoint >= lP && theInterval.leftPoint <= rP) {
                if (theInterval.leftPoint == lP) {
                    if (theInterval.rightPoint == rP) {
                        if (theInterval.left ^ l) {
                            theInterval.left = true;
                        }
                        if (theInterval.right ^ r) {
                            theInterval.right = true;
                        }
                    } else {

                    }
                }
            } else if (theInterval.leftPoint == rP) {

            }
        } else { // 用点模式
            if ()
        }
    };
}


void CACLDefineInterval::link(CACLDomainEndPoint &domain, CACLRangeEndPoint *range) {
    domain.linkToRange = range;
}


void CACLDefineInterval::setUnit(CACLFloat number) {
    unit = number;
}