
#include "CACLFloat.hpp"

cacl::CACLFloat cacl::CACLFloat::absoluteValue() {
    CACLFloat ans;
    ans = *this;
    ans.integer.absoluteValue();

    return ans;
}
