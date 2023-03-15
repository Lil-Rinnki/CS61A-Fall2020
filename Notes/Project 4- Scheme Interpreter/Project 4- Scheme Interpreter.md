# Project 4: Scheme Interpreter

![](image/1678692741650_U8oeBMlcQ5.png)

![](image/1678695017588_Xua1eMAlW2.png)

![](image/1678695185827_fkBqDhLxX8.png)

![](image/1678695307604_eBb7nlFCKD.png)

![](image/1678695674463_etWpNxRhOg.png)

![](image/1678695870641_JydVxsaTN3.png)

![](image/image_3UrtOxgUOx.png)

![](image/1678696228976_Rq9vhCLOyr.png)

![](image/1678696473074_IskNRmt3Qj.png)

![](image/1678696526571_xsSehCazHV.png)

![](image/1678707122715_6c4Qx0o1CO.png)

![](image/1678696643140_KfFi9Jd7cT.png)

![](image/image_hXASo8AOF1.png)

![](image/1678697083118_fa4qcDz7il.png)

![](image/1678697250027_K_2HKjnnPQ.png)

![](image/1678781816214_kbMtu0x3jg.png)

✅与Lecture29中的部分有重合，可再次观看理解

![](image/1678775554061_1tF8yjGYtr.png)

![](image/1678707273801_Eg8SLH2Qtf.png)

![](image/1678775784363_B7i9Kx2y3D.png)

![](image/1678776284887_oGmR6P6117.png)

![](image/1678781797706_qB5IFxCVSG.png)

✅测试问题思考了很久不知道怎么写…结果是***True***

![](image/CX}A93]6RLP]G\$\~8JQ0E7AG_ZygMrkQ0aV.jpg)

![](image/1678780152155_Vpvd0pQ4xK.png)

✅主要在于如何将Scheme的list转换成Python的list

![](image/1678781762451_P4J5bHb4T7.png)

![](image/1678781881050_ybmlSA5r5_.png)

The ***validate\_procedure*** function 用于检查operator是否合法;The ***map*** method of Pair 用于获得代表operands的Scheme list;The ***scheme\_apply*** function 用于向operands调用operator.

✅

![](image/1678782633217_MQgH9B636i.png)

![](image/1678782843811_F_H79VInsD.png)

![](image/1678782930978_X6T9goK0kd.png)

![](image/1678783002348_lEJSUFITb-.png)

![](image/1678783079636_YxwFOhubna.png)

完善***do\_define\_form***函数的第一部分，简要思路就是用之前实现的Frame的类方法define.所以需要symbol和value.expressions.first就是symbol即target. 而value由于可能是表达式形式,第5问解决的是符号定义问题。特别注意在赋值时，由于链表形式的结束为nil，故对expressions.rest.first调用scheme\_eval函数。

✅

![](image/1678784189925_B5LaV8FlIZ.png)

![](image/1678784268289_ffAXsJhwIs.png)

![](image/1678784439859_1I9_QcEnEW.png)

✅

完成以上内容，则可实现以下功能：

![](image/1678786281767_HJFwxfrlLI.png)

![](image/1678789888751_3-MCexwSb1.png)

![](image/1678790135138_0XaaVwuJfq.png)

依次执行语句，返回值为最后一个表达式的结果。

✅简单的迭代，但要注意更替方法

![](image/1678792500982_MpPAeLrD88.png)

✅定义***LambdaProcedure***返回，对应输入formals形参列表, body函数体, env定义时的环境。

![](image/image_B7sIjXs9XF.png)

✅得到函数的name, formals, body后通过前面实现的***do\_lambda\_form***即可将lambda函数绑定到全局环境env中.

![](image/1678803789368_13gqTcNXwP.png)

✅创建子环境，其中用来储存用户自定义函数的变量名与数字

![](image/1678804714546_J4wU0d6dST.png)

✅完成lambda函数的搭建，注意在创建lambda函数的框架下进行该函数新环境的创建——即使用self.env而不是env去make\_child\_frame

![](image/1678805851137_nwROPYoGOb.png)

![](image/1678843370069_GwZ2aBksTv.png)

Scheme中只有False(#f)对应非值，其他所有的值（包括0和nil）都是True。可以使用***is\_true\_primitive***和***is\_false\_primitive***在编程中协助完成Schemez中是非值的判断。

![](image/image_5drBkR5yBU.png)

✅

![](image/1678846655435_2Z6a_ylKMr.png)

&#x20;✅

![](image/image_BWBZ1sXiY2.png)

要求在let语句环境下创建一个子空间，同时在子空间中完成各变量名的赋值，这要求bindings语句中满足语法条件，每个语段都是由一个变量名与一个值对应的(***validate\_form(bindings.first, 2, 2)***)，且不能出现重复变量名(***validate\_formals(names)***)

&#x20;✅特别注意在内部变量赋值时，对Pair格式的理解，它永远带有一个nil，故需要对***bindings.first.rest***\*\* *.first*\*\*进行scheme\_eval

![](image/image_JzvZlZvd7y.png)

![](image/1678859773912_yFw8mifyH_.png)

![](image/1678859843245_SSyehJQws8.png)

注意使用***python3 editor***指令调出网页版Scheme编辑器，同时打开另一个终端使用***python3 ok —local***文件以检查编写是否正确，这样做是为了保证网页版Scheme编辑器持续工作！

![](image/1678859880629_glqGCP4pmJ.png)

✅

![](image/image__5d2ZJGKsv.png)

-   [ ] 递归最终的情况怎么写：再细分情况两者等长/两者不等长
-   [ ] 比较中有相等的情况怎么解决，提示中说可以任意选择，那么可以理解为合并数字列表中可存在重复的

✅

![](image/1678862926133_lvzqxwoJ9O.png)

-   [ ] 当出现前项＞后项时，“截断”功能如何实现？使用begin语句
-   [ ] 如何创建子列表

✅

![](image/1678865036251_RBRrzpEMGx.png)

![](image/1678865118130_Uszii4im5Y.png)

![](image/1678865202694__-eWNKfD_k.png)

![](image/image_bMCIBQhf2t.png)

![](image/1678875585615_RWT6iuTNPg.png)

思路：(***let-to-lambda*** '(let (定义赋值式) (表达式) )) → ((lambda (定义变量) (表达式)）(变量赋值)）
