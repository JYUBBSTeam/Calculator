

#ifndef TESTCACLINTEGER_CACLINTEGER_HPP
#define TESTCACLINTEGER_CACLINTEGER_HPP

#include <gmp.h>
#include <iostream>

namespace cacl {
    class CACLInteger {
        // 重载右移动作为输入
        friend std::istream &operator>>(std::istream &_cin, CACLInteger number);

        // 重载左移动作为输出
        friend std::ostream &operator<<(std::ostream &_cout, const CACLInteger number);

    public:
        CACLInteger() = default;

        ~CACLInteger() {
            mpz_clear(integer);
        }


    private:
        mpz_t integer;
    };
}
#endif //TESTCACLINTEGER_CACLINTEGER_HPP
