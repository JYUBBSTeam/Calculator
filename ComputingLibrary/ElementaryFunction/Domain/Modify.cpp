
#include "Interval.hpp"

void cacl::CACLDefineInterval::setIntervalPrecision(cacl::CACLFloat number) {
    intervalPrecision = number;
}

void cacl::CACLDefineInterval::push(bool l, cacl::CACLFloat lP, bool r, cacl::CACLFloat rP) {
    CACLEndPoint newInterval(l, lP, r, rP);

    // 其实是补全缺少的那一部分区间，可能需要一个search方法来查找哪些是存在的，
    // 方便用来补全缺少的那些部分
}

