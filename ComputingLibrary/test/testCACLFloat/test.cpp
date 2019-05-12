#include <iostream>
#include "../../CACLFloat/CACLFloat.hpp"

int main(int argc, char **argv) {
    cacl::CACLFloat test, test1, test2;
    double num;

    std::cin >> test1 >> test2;
    // test = num;
    test = test1 * test2;
    std::cout << test;

    return 0;
}