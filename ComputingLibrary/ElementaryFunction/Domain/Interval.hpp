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
#include "../Range/Interval.hpp"
#include <vector>


// 记录区间的左右端点的数据
class CACLDomainEndPoint {
    friend class CACLDefineInterval;

public:
    CACLDomainEndPoint() {
        left = right = false;
        linkToRange = nullptr;
        dotMode = false;
    }

    CACLDomainEndPoint(CACLFloat d) {
        dot = d;
        dotMode = true;
    }

    CACLDomainEndPoint(bool l, CACLFloat lP, bool r, CACLFloat rP) {
        left = l;
        right = r;

        leftPoint = lP;
        rightPoint = rP;

        linkToRange = nullptr;

        dotMode = false;
    }

    ~CACLDomainEndPoint() = default;

public:
    // 链接对应值域
    CACLRangeEndPoint *linkToRange;

private:
    // false为开，true为闭
    bool left;
    bool right;

    // 左右端点
    CACLFloat leftPoint;
    CACLFloat rightPoint;

    // 使用点模式, false是不用，true是用
    bool dotMode;
    // 点
    CACLFloat dot;
};

// 区间类
class CACLDefineInterval {
public:
    CACLDefineInterval() {
        controlCode = 0;
    }

    ~CACLDefineInterval() {
        for(auto &i : segment){
            delete(i);
        }
    };

    // 放入区间
    void push(bool l, CACLFloat lP, bool r, CACLFloat rP);

    // 放入点
    void push(CACLFloat number);

    // 连接值域
    void link(CACLDomainEndPoint &domain, CACLRangeEndPoint *range);

private:
    void sortSegment();

private:
    // 存放各个区间
    std::vector<CACLDomainEndPoint *> segment;

    // 链接操作代码，0初始，1可直接插入，2需要重建值域
    int controlCode;
};


#endif //ELEMENTARYFUNCTION_INTERVAL_HPP
