#include "CACLInteger.h"

void CACLInteger::initialize() {
    for (int i = 0; i < MAX_OF_BIT; ++i) {
        this->num[i] = 0;
    }

    this->bit = 0;
    this->symbol = 0;
}


CACLInteger CACLInteger::copy(const CACLInteger number) {
    this->initialize;


}