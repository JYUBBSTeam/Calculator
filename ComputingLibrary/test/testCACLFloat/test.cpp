#include <iostream>
#include "../../NumberDefine/Number.hpp"

int main(int argc, char **argv) {
    CACLFloat test, test1, test2;

    std::cin >> test1 >> test2;
    test = test1 / test2;
    std::cout << test;

    return 0;
}