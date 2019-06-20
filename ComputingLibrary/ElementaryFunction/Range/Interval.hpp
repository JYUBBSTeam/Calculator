

#ifndef TESTELEMENTARYFUNCTION_INTERVAL_HPP
#define TESTELEMENTARYFUNCTION_INTERVAL_HPP

#include <vector>
#include "../../NumberDefine/Number.hpp"
#include "../Domain/Interval.hpp"

class CACLDomainEndPoint;

class CACLRangeEndPoint {
    friend class CACLValueInterval;

public:
    CACLRangeEndPoint() {
        linkToDomain = nullptr;
    }

    ~CACLRangeEndPoint() = default;

public:
    // 链接到定义域
    CACLDomainEndPoint *linkToDomain;

private:
    // 存放元素的集合
    std::vector<CACLFloat> point;
};

class CACLValueInterval {
public:
    CACLValueInterval() = default;

    ~CACLValueInterval() {
        for (auto i : segment) {
            delete (i);
        }
    }

private:
    // 存放定义域
    std::vector<CACLRangeEndPoint *> segment;
};

#endif //TESTELEMENTARYFUNCTION_INTERVAL_HPP
