
#include "CACLInteger.hpp"
#include <string>

namespace cacl {
    std::istream &operator>>(std::istream &_cin, CACLInteger number) {
        std::string tmpNumber;

        _cin >> tmpNumber;
        char *translatedNumber = new char[tmpNumber.size() + 1];
        for (int i = 0; i < tmpNumber.size(); ++i) {
            translatedNumber[i] = tmpNumber[i];
        }
        translatedNumber[tmpNumber.size()] = 0;

        mpz_init_set_str(number.integer, translatedNumber, 10);

        delete[](translatedNumber);

        return _cin;
    }

    std::ostream &operator<<(std::ostream &_cout, const CACLInteger number) {
        gmp_printf("%Zd", number.integer);
        return _cout;
    }
}