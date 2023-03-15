# Lecture 14. Circuits

![](image/1677139416311_dD93tmLacG.png)

![](image/1677139454432_LB4qTYi8cc.png)

Designing Circuits 四步走

**step 1**.build truth table for all possible input/output values

![](image/1677139969335_5FcaaGmrWW.png)

**step 2**.build sub-expressions with ***and/not*** for each output column

使用and逻辑表述sub-expressions的原因是，除了结果为1的情况，其余情况结果均输出为0。

![](image/image_2KHi92ap52.png)

**step 3**.combine,two at a time,sub-expressions with an ***or***

![](image/1677140561371_C7koC5V7R-.png)

**step 4**.draw circuit diagram

![](image/1677140784921_sih39lLeow.png)

如何使用线路进行逻辑计算？

**例1：** 一位数相等判断

![](image/1677140972777_e4IG7lRH4l.png)

![](image/1677141061576_dJ6YByU3vZ.png)

![](image/1677141101545_D0QYQia6_X.png)

![](image/1677141222829_eIFE0GHcWY.png)

![](image/1677141474971_QfRRIwFJ9O.png)

**例2：** 四位数相等判断

![](image/1677141628172_XcBTE2zG_X.png)

![](image/image_Qhy9P9p67q.png)

![](image/image_dA-0xr32RS.png)

![](image/1677142027488_GYsPqkGu3Y.png)

**例3：** 一位数加法器 1-Bit Adder

输入与输出都考虑进位符号，因此输入有3个（两数与进位符），输出有2两个（结果与进位符）

![](image/1677142150295_NU8G1sdhMU.png)

![](image/1677142209641_YAOquw2pqj.png)

![](image/1677142333050_iJKIDvFvY7.png)

![](image/1677142418999_Ev26XezAhA.png)

![](image/1677142470942_dyBo-eQD65.png)

![](image/1677142506173_vrcDaeFWVr.png)

**例4：** 四位数加法器——利用一位数加法器，抽象的魅力

![](image/image_Ada-sjn5Bb.png)

![](image/image_DBegHXb26n.png)

现代计算机中元件体积越来越小，助力了计算机普及化。

![](image/1677142943614_uKWqCZtod2.png)

例5：判断一个8位数是否为0 —— 优化circuit

![](image/1677147944599_FaJ_r5_Rxw.png)

只有全部都是0，最终才会判断等于0输出1

![](image/1677148066174_k7LnDGFR8M.png)

![](image/1677148114795_Fp7CNSJMH3.png)

优化circuit的核心是减少gate个数！

![](image/image__IjQTzoK2_.png)

优化的一种方法：

*Karnaugh map* 卡诺图，它重构了truth table的结构

![](image/image_8tXOnz5igo.png)

![](image/1677148931369_YTUmOqHVGM.png)
