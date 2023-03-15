# Lecture 16. Mutable Functions

指与可变变量相关的函数

1.Mutable Functions

![](image/image_Krs6_ib2Ko.png)

![](image/1677739727789_cR1hHRxJqa.png)

![](image/1677739847347_K0kJgXmw0v.png)

![](image/1677740010790_IGnUhEP22B.png)

![](image/1677740251964_kf68On-oJx.png)

2.Non-local Assignment

![](image/1677740515662_fGfvn0vlSR.png)

![](image/image_z4MWxfwDby.png)

![](image/1677740914636_9m0g6TkWEb.png)

![](image/1677741185242_BF91GE7eWU.png)

3.Multiple Mutable Functions

![](image/1677741366950_zpZKXcWMnk.png)

![](image/1677741548582_r1NGZV52IV.png)

3.Mutation operations cause **referential transparency** lost！引用透明性

函数的返回值只依赖于其输入值，这种特性就称为**引用透明性（referential transparency）**，即“对同一输入值每次都返回相同结果”。

![](image/1677741776898_b3lKGSlKWh.png)

可变函数使这种特性失效，如下列程序在输入b(3)+b(4)和单独输入b(4)时其对应值分别是12和11，并非相同。

![](image/1677742047820_2-t7T_SauL.png)
