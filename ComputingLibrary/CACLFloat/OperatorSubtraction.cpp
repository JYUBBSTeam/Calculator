
#include "CACLFloat.hpp"

cacl::CACLFloat cacl::CACLFloat::operator-(cacl::CACLFloat number) {
    CACLFloat ans;

    if (this->integer.getSymbol() == false && number.integer.getSymbol() == false) {
        unsignedSubtraction(&ans, *this, number);
        ans.integer.setSymbol(!(this->absoluteValue()> number.absoluteValue());
    } else if (this->integer.getSymbol() == false && number.integer.getSymbol() == true) {
        unsignedAddition(&ans, *this, number);
    } else if (this->integer.getSymbol() == true && number.integer.getSymbol() == false) {
        unsignedAddition(&ans, *this, number);
    } else if (this->integer.getSymbol() == true && number.integer.getSymbol() == true) {
        unsignedSubtraction(&ans, *this, number);
    }

    return ans;
}


cacl::CACLFloat cacl::CACLFloat::operator-(double number) {
    CACLFloat translatedNumber = translate(number);
    CACLFloat ans;

    ans = *this - translatedNumber;

    return ans;
}

void cacl::CACLFloat::unsignedSubtraction(cacl::CACLFloat *ans, cacl::CACLFloat number1, cacl::CACLFloat number2) {

}