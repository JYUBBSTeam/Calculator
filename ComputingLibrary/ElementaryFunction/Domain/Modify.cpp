
#include "Interval.hpp"

void CACLDefineInterval::push(bool l, CACLFloat lP, bool r, CACLFloat rP) {
    CACLDomainEndPoint newInterval(l, lP, r, rP);

    // 遍历segment， 查找出已经存在的的区间，并与之合并
    CACLFloat leftValue = newInterval.leftPoint;
    CACLFloat rightValue = newInterval.rightPoint;


}