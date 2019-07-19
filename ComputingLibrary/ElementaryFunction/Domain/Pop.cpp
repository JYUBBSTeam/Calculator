/* 创建人：黄子涵
 * 创建时间：2019.7.10
 * 修改时间：
 * 类：CACLDefineInterval
 * 功能：删除区间函数pop
 */


#include "Interval.hpp"

// 以段区间为单位进行删除
void CACLDefineInterval::pop(bool l, CACLFloat lP, bool r, CACLFloat rP) {
    for (auto i = segment.begin(); i <= segment.end(); i++) {
        if ((*i)->dotMode) {
            // 点区间，就查找是否在要删段里面
            if ((*i)->dot >= lP or (*i)->dot <= rP) {
                CACLDomainEndPoint *temp = (*i);
                segment.erase(i);
                delete (temp);
            }
        } else {
            
        }
    }
}


void CACLDefineInterval::pop(CACLFloat) {

}
