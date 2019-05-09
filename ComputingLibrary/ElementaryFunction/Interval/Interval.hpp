/*
 * 创建人：黄子涵
 * 创建时间：2019.5.9
 * 修改时间：2019.5.9
 * 类：CACLInterval
 * 创建目的：实现区间的表示
 * 私有数据：
 * 公有数据：
 * 私有方法：
 * 公有方法：
 */

#ifndef ELEMENTARYFUNCTION_INTERVAL_HPP
#define ELEMENTARYFUNCTION_INTERVAL_HPP

#include "../../CACLFloat/CACLFloat.hpp"
#include <vector>

namespace cacl {

    // 记录区间的左右端点的数据
    class CACLEndPoint {
        friend class CACLInterval;

    public:
        CACLEndPoint() {
            left = right = false;
        }

        CACLEndPoint(bool l,CACLFloat lP, bool r, CACLFloat rP){
            left = l;
            right = r;

            leftPoint= lP;
            rightPoint = rP;
        }

        ~CACLEndPoint() = default;

    private:
        // false为开，true为闭
        bool left;
        bool right;


        CACLFloat leftPoint;
        CACLFloat rightPoint;
    };

    // 区间类
    class CACLInterval {
    public:
        CACLInterval() {
            intervalPrecision = 0.01;
        }

        ~CACLInterval() = default;

        // 设置取值精度
        void setIntervalPrecision(CACLFloat number);

        // 放入区间
        void push(bool l , CACLFloat lP, bool r, CACLFloat rP);



    private:
        // 区间取值精度
        CACLFloat intervalPrecision;

        // 存放各个区间
        std::vector<CACLEndPoint>  segment;
    };
}

#endif //ELEMENTARYFUNCTION_INTERVAL_HPP
