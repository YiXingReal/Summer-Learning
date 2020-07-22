#广播机制
    \两个数组的形状并不相同的时候，我们可以通过扩展数组的方法来实现相加、相减、相乘等操作，这种机制叫做广播
    广播的原则：如果两个数组的后缘维度（trailing dimension，即从末尾开始算起的维度）的轴长度相符，
    或其中的一方的长度为1，则认为它们是广播兼容的。广播会在缺失和（或）长度为1的维度上进行。
    #https://www.cnblogs.com/jiaxin359/p/9021726.html

#遍历数组
    numpy.nditer
        #格式：
        a = np.arange(0,60,5)
        a = a.reshape(3,4)
        for x in np.nditer(a):
            print(x)
        #迭代顺序选择为匹配数组的内存布局,即使转置，顺序不变
        b = a.T#进行转置
        for x in np.nditer(b):
            print(x)#输出和上面的一样

        #改变遍历顺序
            #在数组创建的时候指定order格式
            c = b.copy(order='C')#按行依次输出
            c = b.copy(order='F')#按列依次输出
            #使用nditer时指定格式
            for x in np.nditer(a, order = 'C'):#按行依次输出
            for x in np.nditer(a, order = 'F'):#按列依次输出
        #遍历是修改元素的值
            for x in np.nditer(a, op_flags=['readwrite']):#修改为可写模式，这样元素就可以修改了
        #构造函数的参数flags
            for x in np.nditer(a, flags = ['external_loop'], order = 'F'):#迭代的结果每列用一个一维数组包装
        c_index
        f_index
        multi-index
        #广播迭代
            for x,y in np.nditer([a,b]):


#NumPy数组操作   
    改变形状
    转置操作
    更改尺寸
    加入数组
    拆分数组
    添加/删除元素


#二元运算符
np.bitwise_and(13, 17)#按位与操作
np.bitwise_or(13, 17)#按位或操作
np.invert(np.array([13], dtype = np.uint8))#按位NOT
np.left_shift(10,2)#将二进制表示的位向左移2位
np.right_shift(10,2)#将二进制表示的位向右移2位


#NumPy字符串函数
    #三角函数
        np.sin(a*np.pi/180)
        np.cos(a*np.pi/180)
        np.tan(a*np.pi/180)
        np.arcsin(sin)
        np.arcsin(sin)#arcsin，arcos 和 arctan 函数返回给定角度的sin，cos和tan的三角函数的倒数
        np.arcos(sin)
        np.arctan(sin)
    #四舍五入
        numpy.around(10)#默认值为0.
        np.around(a, decimals = 1)#小数点后一位
        np.around(a, decimals = -1)#小数点前一位
    numpy.floor()#该函数返回不大于输入参数的最大整数
    
NumPy算术运算
    \用于执行诸如add（），subtract（），multiply（）和divide（）等算术运算的输入数组必须是相同的形状，
    \或者应符合数组广播 规则。
    #其他运算
        numpy.reciprocal()#求倒数
        np.power(a,2)#a中的每个元素都取2次方
        np.power(a,b)#a中的元素的次方数为b中对应位置上的值
        np.mod(a,b)#返回输入数组中相应元素的除法余数
        numpy.remainder()#返回输入数组中相应元素的除法余数
    #复数的数组操作
        numpy.real（） - 返回复杂数据类型参数的实部。
        numpy.imag（） - 返回复数数据类型参数的虚部。
        numpy.conj（） - 返回通过改变虚部符号得到的复共轭。
        numpy.angle（） - 返回复杂参数的角度。 该功能具有度数参数。如果为true，则返回角度，否则角度以弧度表示。


#统计函数
    np.amin(a,1)#按行求最小值
    np.amax(a)#求整个数组的最小值
    np.amax(a,0)#按列求最小值
    numpy.ptp()#计算最大值与最小值差的函数
        np.ptp(a, axis = 1)#依照行计算
        np.ptp(a, axis = 0)#依照列计算
    numpy.percentile()#将一组数据从大到小排序，