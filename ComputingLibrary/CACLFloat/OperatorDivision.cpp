
#include "CACLFloat.hpp"

cacl::CACLFloat cacl::CACLFloat::operator/(cacl::CACLFloat number) {

}

cacl::CACLFloat cacl::CACLFloat::operator/(double number) {
    CACLFloat translatedNumber = translate(number);
    CACLFloat ans;

    ans = *this / translatedNumber;
    return ans;
}