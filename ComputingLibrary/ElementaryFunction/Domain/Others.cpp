#include "Interval.hpp"
#include <algorithm>

void CACLDefineInterval::sortSegment() {
    // 给区间排序
    auto sortRules = [](CACLDomainEndPoint *a, CACLDomainEndPoint *b) {
        //  a是点区间，b是线区间
        if (a->dotMode && !b->dotMode) {
            return a->dot < b->leftPoint;
        }
            // a是线区间，b是点区间
        else if (!a->dotMode && b->dotMode) {
            return a->rightPoint < b->dot;
        }
            // a和b都是点区间
        else if (a->dotMode && b->dotMode) {
            return a->dot < b->dot;
        }
            // a和b都是线区间
        else {
            return a->rightPoint < b->leftPoint;
        }
    };
    std::sort(this->segment.begin(), this->segment.end(), sortRules);
}