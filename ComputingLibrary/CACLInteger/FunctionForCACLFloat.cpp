

#include "CACLInteger.h"

bool *cacl::CACLInteger::symbolPointer(){
    return &this->symbol;
}

int *cacl::CACLInteger::bitPointer() {
    return &this->bit;
}

short *cacl::CACLInteger::numPointer() {
    return this->num;
}
