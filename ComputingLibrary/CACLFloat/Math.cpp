/*
 * 创建人：Huang
 * 创建日期：2019.5.3
 * 修改日期：2019.5.3
 * 类：CACLFloat
 * 功能：类函数实现
 */
#include "CACLFloat.hpp"

// 求绝对值
cacl::CACLFloat cacl::CACLFloat::absoluteValue() {
    CACLFloat ans;
    ans = *this;
    ans.integer.absoluteValue();

    return ans;
}
