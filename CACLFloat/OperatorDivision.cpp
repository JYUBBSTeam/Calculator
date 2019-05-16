
#include "CACLFloat.hpp"

//重载除法
cacl::CACLFloat cacl::CACLFloat::operator/(cacl::CACLFloat number) {

}

cacl::CACLFloat cacl::CACLFloat::operator/(double number) {
    CACLFloat translatedNumber = translate(number);
    CACLFloat ans;

    ans = *this / translatedNumber;
    return ans;
}