# Lecture 4. Higher-Order Functions

1.Iteration Example 迭代示例

设计循环时最重要的是思考什么信息是**需要一直记录**以完成迭代的

![](image/1675856995804_RTxFg8-zKT.png)

![](image/1675857379605_EqENDnanEN.png)

2.Designing Functions 设计函数

——知道函数的定义域和值域，函数的作用是创造两者之间的关系

![](image/1675857593180_q_NSRTtWnX.png)

对设计函数的建议

![](image/1675857728417_Y8pCanJkyh.png)

3.Higher-Order Functions

（1）通过参数概括

![](image/1675857877554_J99loyo3lH.png)

提取统一求解的内容，化繁为简并不重复代码工作！

![](image/image_zS5kzlXLEp.png)

![](image/1675858280756_7lmFHy6IUL.png)

（2）通过计算过程归纳

![](image/1675858471792_k99baD2agH.png)

![](image/1675858724031_xjTv5ymt-7.png)

![](image/1675859064268_RjC2ej8ppu.png)

![](image/1675859169326_wzSEdMEZOF.png)

(3)Functions as Return Values

一类输出为函数的特殊函数，即内部再定义新的函数

![](image/1675859692782_1YcYZ6NF22.png)

![](image/1675859859258_tD7pMy1lOu.png)

![](image/1675859981280_7JijUMiPkL.png)

![](image/1675860155856_ZshGgH0h1m.png)

4.Lambda Expressions

![](image/1675860402455_w1Ao9cVWmu.png)

![](image/image_OCWOYVFZAM.png)

![](image/1675860954632_J7X6n3V1KJ.png)

λ函数直接写其计算表达式，不能出现while、return等语句。由于其没有定义函数名的特殊性，它无法单独成行，往往需要搭配函数定义“f=lambda x:……”或函数调用“f(lambda x:……)”使用。

总结而言，λ函数的定义能使代码更加简洁，但同时也使代码更难理解。通常在**函数的输入也为函数时**，若作为输入函数是较为简单的计算，会使用λ函数来定义。

![](image/1676255996491_S9J2auEpou.png)

5.Return

Return代表着函数调用的结束，并决定着调用表达的输出值。

![](image/1675861228537_RZ2XD0bV9B.png)

![](image/1675861652322_Vjev9EMygA.png)

![](image/image_M3ZIc8hEyZ.png)

6.Control

控制语句的重要性，理解为它用于**选择执行**！

区别于调用函数时所有语句都要先执行得出相应值（这是由Python对于调用语句用法规定造成的，属于语法）。

![](image/image_z-HpT_ofe8.png)

![](image/1675862627272_HZ5SeIzUoj.png)

![](image/1675862846705_sTmIcPPOPw.png)

例子：

![](image/1675863141624_tWxtq9iT3I.png)

![](image/image_SujrxNd8ib.png)

![](image/1675863431271_Kp6i_QZ2yp.png)
