
#include "Interval.hpp"

void cacl::CACLInterval::setIntervalPrecision(cacl::CACLFloat number) {
    intervalPrecision = number;
}

void cacl::CACLInterval::push(bool l, cacl::CACLFloat lP, bool r, cacl::CACLFloat rP) {
    CACLEndPoint newInterval(l, lP, r, rP);

    // ��ʵ�ǲ�ȫȱ�ٵ���һ�������䣬������Ҫһ��search������������Щ�Ǵ��ڵģ�
    // ����������ȫȱ�ٵ���Щ����
}

