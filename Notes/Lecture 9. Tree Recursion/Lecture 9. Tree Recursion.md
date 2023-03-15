# Lecture 9. Tree Recursion

1.Order of Recursive Calls 递归函数调用的顺序

“瀑布函数”，函数调用只有在其值得出后，才会运行进行之后的代码

![](image/1676809574101_yytFZY6-sP.png)

有一些“嵌套”的感觉

![](image/1676809793364_8aH1eIivMM.png)

![](image/1676810091653_YkqG_cfmTt.png)

![](image/1676809987970_6o7IyqZ98z.png)

例：反瀑布函数

![](image/image_wQ0GXmuetd.png)

2.Tree Recursion 一个函数进行不止一个递归调用

最典型的示例：斐波那契数列fib(n)=fib(**n-1**)+fib(**n-2**)

![](image/1676811057363_ZF_kT0Z4Y8.png)

![](image/1676811268679_LjwMoHXhvm.png)

![](image/1676811436602_YnbPmyp-DK.png)

![](image/1676811518484_AAlXNTcZps.png)

![](image/1676823183098_Snw5F9fabp.png)

3.Tower of *Hanoi*与递归函数——只需要完成最底下那层的移动+递归

![](image/1676824000333_7HD3Y6fuNp.png)

![](image/1676824319265_vNjmk3kHeb.png)

4.Example: Counting Partitions整数划分

![](image/1676824708227_kq08PInnq7.png)

![](image/1676824963429_ZzZcWoSWxQ.png)

![](image/1676825101525_cyVcr8zYo2.png)
