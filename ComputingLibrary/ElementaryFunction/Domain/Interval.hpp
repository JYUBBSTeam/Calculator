/*
 * 创建人：黄子涵
 * 创建时间：2019.5.9
 * 修改时间：2019.5.9
 * 类：CACLDefineInterval
 * 创建目的：实现定义域的表示
 * 私有数据：
 * 公有数据：
 * 私有方法：
 * 公有方法：
 */

#ifndef ELEMENTARYFUNCTION_INTERVAL_HPP
#define ELEMENTARYFUNCTION_INTERVAL_HPP

#include "../../CACLFloat/CACLFloat.hpp"
#include <vector>


// 记录区间的左右端点的数据
class CACLDomainEndPoint {
    friend class CACLDefineInterval;

public:
    CACLDomainEndPoint() {
        left = right = false;
    }

    CACLDomainEndPoint(bool l, CACLFloat lP, bool r, CACLFloat rP) {
        left = l;
        right = r;

        leftPoint = lP;
        rightPoint = rP;
    }

    ~CACLDomainEndPoint() = default;

private:
    // false为开，true为闭
    bool left;
    bool right;


    CACLFloat leftPoint;
    CACLFloat rightPoint;


};

// 区间类
class CACLDefineInterval {
public:
    CACLDefineInterval() = default;

    ~CACLDefineInterval() = default;

    // 放入区间
    void push(bool l, CACLFloat lP, bool r, CACLFloat rP);

private:
    // 存放各个区间
    std::vector<CACLDomainEndPoint> segment;
};


#endif //ELEMENTARYFUNCTION_INTERVAL_HPP
