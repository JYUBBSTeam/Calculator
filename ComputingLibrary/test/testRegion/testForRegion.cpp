#include "../../ElementaryFunction/Region.hpp"

int main(int argc, char **argv) {
    CACLDefineInterval test;
    CACLFloat testleft, testright;
    CACLFloat lineLeft, lineRight;
    lineLeft = 15;
    lineRight = 20;
    testleft = 12.6;
    testright = 13.1;
    test.push(testleft);
    test.push(true, lineLeft, false, lineRight);

    return 0;
}