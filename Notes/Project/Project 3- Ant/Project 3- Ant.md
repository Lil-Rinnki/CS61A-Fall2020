# Project 3: Ant

![](image/1678117841378_dfrbwlpTA0.png)

![](image/image_76rjzhKHZ0.png)

![](image/1678119428204_9lYe_21Gof.png)

![](image/1678119606978_2RlbgmqgbG.png)

![](image/1678119864787_NX8ZNT_6a3.png)

![](image/1678119927430_z025Bq_8BC.png)

![](image/1678120527102_ln2LCSy0mN.png)

✅

![](image/1678121451485_Jh3HiscBxx.png)

![](image/1678154108951_NkO0_aPEUz.png)

![](image/1678154237613_PHQ3z31sl3.png)

✅

![](image/1678155945246_GefihfeaD2.png)

![](image/1678157054135_oUvNRx3qh5.png)

![](image/1678157241436_c_mJoCSto_.png)

✅

![](image/1678158136534_2yTfuNYcDQ.png)

![](image/1678158226098_lJbwZhev3-.png)

近距离攻击和远距离攻击

![](image/image_61EZps_g6O.png)

![](image/1678163165041_mzGiK29nAc.png)

![](image/1678163291257_Iuq_SCWjQs.png)

✅注意使用min\_range和max\_range作为ThrowerAnt的属性，并在ShortThrower与LongThrower中做出相应改变。

![](image/1678166420228_00sXPzd-Av.png)

![](image/1678166601625_V1SU06CdRV.png)

![](image/1678167192758_ArMO2K7Agl.png)

![](image/1678167217628_kNtLwqjizY.png)

![](image/1678167275977_Gim4QQkbYw.png)

✅注意在使用上级Method使，object对象要确定好；同时注意使用哪一级的类方法

![](image/1678169119424_Y1BsjK1cBP.png)

![](image/1678169360247_BvL7K4XPKv.png)

-   [ ] 有类特征time\_to\_digest=3和例特征digesting记录该饿蚁消化时间，默认为0
-   [ ] 该饿蚁随机将自身格中的任意一只蜜蜂吃进消化（armor降为0），并改变digesting为time\_to\_digest
-   [ ] 每一轮游戏进行都对其状态进行判断，如果digesting=0则表示可以吃蜜蜂；如果digesting≠0，则digesting减一

![](image/1678170827204_UI0U02ALKy.png)

✅注意随机rANTdom\_else\_none返回值可能为None的特殊情况判断

![](image/1678171497749_O7NqZt2DEp.png)

✅创建一个Ant的子类WallAnt，它不做任何事情（肉盾）

![](image/1678171951600_nd0kwtlOi8.png)

![](image/1678172148702_H6_JjkkAUH.png)

✅

![](image/1678172702644_T06pch6asw.png)

✅

![](image/image_DDnX1FABCe.png)

![](image/1678173980752_Se92qhgQM6.png)

![](image/1678174111254_9c9cyenyqm.png)

✅注意：1.真假蚁皇——涉及判断参数、决定输赢、是否能被移走；2.蚁皇BUFF——是否被加强过判断

![](image/image_cehV9ufRBZ.png)

-   [ ] 在ant类中创建一个blocks\_path参数，默认为True；而忍者蚁blocks\_path的值为False;
-   [ ] 在Bee类方法blocked中，若当前所在place没有蚂蚁或该蚂蚁blocks\_path属性为False，则返还False——有蚂蚁且其blocks\_path属性为True返回True;
-   [ ] 忍者蚁对每一个路过蜜蜂都会造成伤害。

✅

![](image/1678180779919_TvTT59nkDS.png)

![](image/1678189302735_C0Jb6lMaGm.png)

![](image/1678189408427_PA5OGqRgv3.png)

✅注意判定当前格内是否能放下第二只蚂蚁的逻辑判定：两只必须有一个是容器蚁，一个非容器蚁；先将非容器蚁放在容器蚁中，再将容器蚁放在当前格内

![](image/image_dSAi3NtSyE.png)

✅tank自己攻击之外，还有其中的ant攻击

![](image/image_82ETrHtQ2g.png)

![](image/1678192436967_CGoJmuZsJY.png)

![](image/1678192594343_qOrD3nvtot.png)

❎学问很多，多看

![](image/1678196919304_dNZ4iPFYDl.png)

![](image/1678197142302_NHVFDZfUrd.png)

✅重点在如何创造字典，即如何将蚂蚁和蜜蜂的信息放入其中，条件怎么判断即如何遍历
