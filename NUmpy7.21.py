import numpy as np #模块导入


#ndarray对象
    numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)#通过这个函数创建一个ndarray实例
    a = np.array([1, 2, 3,4,5], ndmin = 2)#ndmin指定最小维度，这是一个二维矩阵，一行五列
    a = np.array([1, 2, 3], dtype = complex)#dtype指定期望数据类型，输出的数据类型格式为虚数

#数据类型dtype对象
    numpy.dtype(object, align, copy)#构建一个对象
    #简单的使用
    dt = np.dtype(np.int32)
    a = np.array([1, 2, 3], dtype = dt)
    #结构化数据类型
    student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])#定义了结构化的数据对象
    a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)#和每一列对应起来

#数组的属性
    np.shape
        a = np.array([[1,2,3],[4,5,6]])
        print(a.shape) #输出数组行数和列数
        a.shape = (3,2)#调整数组
    np.reshape
        a = np.array([[1,2,3],[4,5,6]])
        b = a.reshape(3,2)#和上面不同的是，这里新生成了一个数组

    np.ndim#查看维度

    ny.itemsize#输出array元素的字节数
        a=np.array([[1,2,3,4,5],[1,2,3,4,5]])
        print(a.itemsize)#输出为4
        a=np.array([[1,2,3,4,5],[1.0,2,3,4,5]])
        print(a.itemsize)#输出为8

    np.flags#输出标志
        \每一种标志对应一种状态

#数组的创建
    numpy.empty(shape, dtype = float, order = 'C')#order为风格
    x = np.empty([3,2], dtype = int) #数组中的元素显示随机值，因为它们未被初始化。

    numpy.zeros(shape, dtype = float, order = 'C')
    a = np.zeros((3,4))# 定义一个全部为0的 三行四列的数组


    numpy.ones(shape, dtype = None, order = 'C')
    a = np.ones((3,4))# 数组的元素全为1


    #从数值范围创建一个数组
    numpy.arange(start, stop, step, dtype)
    a = np.arange(10,20,2)# 生成矩阵 从10到20 每隔2输出
    a = np.arange(12).reshape((3,4))# 生成一个三行四列的从1到12的矩阵

    numpy.linspace(start, stop, num, endpoint, retstep, dtype)
    #可指定间隔之间的均匀间隔值的数量，即均匀生成的
    #num要生成的均匀间隔样本的数量。默认值是50
    #endpoint默认情况下为真，因此停止值包含在序列中。如果错误，则不包括在内
    a = np.linspace(1,10,4)# 从1到10之间依次挑选四个数，生成数列
    a = np.llnspace(1,10,4).reshape((2,3))# 生成矩阵


    numpy.logspace
    #该函数返回一个 ndarray 对象，该对象包含在对数刻度上均匀间隔的数字。规模的起止点是基数的指数，通常为10
    

#来自现有数据的ndarray
    numpy.asarray()
        \将Python序列转换为ndarray
        numpy.asarray(a, dtype = None, order = None)
            a = [1,2,3]
            x = np.asarray(x)


    numpy.frombuffer()
        \将缓冲区解释为一维数组
        numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)


    numpy.fromiter
        \从任何可迭代对象构建一个 ndarray 对象,这个函数返回一个新的一维数组
        list = range(5)
        it = iter(list) 
        x = np.fromiter(it, dtype = float)
        print x


#索引——切片
    #简单索引
        a = np.arange(10)#定义数组
        s = slice(2,7,2)#定义切片对象
        a[s] #数组使用切片对象
        a[2:7:2] #可以实现相同的效果

        #多维
        abs = np.array([[1,2,3],[3,4,5],[4,5,6]])
        print(A[2])#输出第二行
        print(A[2][1])#输出第二行第一个元素
        print(A[2,1])#这样写就相当于上面的两个中括号
        print(A[1:])#输出第2 3行
        print(A[1,:])#输出第2行，注意与上面的区别
        print(A[2,...])#输出第2行，与上面的类似  
        print(A[...,2])#输出第2列
        print(A[1,1:2])#第一行从第一列到第二列

    for row in A:#默认迭代每一行
        print(row)

    for column in A.T:#迭代每一列
        print(column)

    print(A.flatten())#把矩阵变成只有一行的数列
    for item in A.flat:#迭代每一个元素
        print(item)


#高级索引
    \高级索引始终返回数据的副本
    \高级索引是复制
    #整数索引
        x = np.array([[1, 2], [3, 4], [5, 6]])
        y = x[[0,1,2], [0,1,0]] #内中括号的数量是x的维度数，选择包括x数组中的（0,0），（1,1）和（2,0）元素
        输出:[1  4  5]

        x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])
        y = x[[[0,0],[3,3]],[[0,2],[0,2]]]
        #输出的格式[  [  [0,0]对应的元素和[0,2]对应的元素 ]  ， [  [0,2]对应的元素和[0,2]对应的元素 ]      ]
        z = x[1:4,1:3]#第一行到第四行，第一列到第三列的重叠
        y = x[1:4,[1,2]]#第一行到第四行，第一列和第二列的重叠

        print(arr[[1, 5, 7, 2]] [:, [0, 3, 1, 2]])  # 1572行的0312列


    #布尔索引
        x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])
        print(x[x > 5])  
        输出：[ 6  7  8  9 10 11]
        print(x<3) # 输出ture和false的列表
        print(x==3) # 输出ture和false的列表





#基础的运算
a = np.array([10,20,30,40])
b = np.arange(4)
c = a+b
c = a-b
c = a*b# 各位置上的元素相乘
c = b**2# b的二次方

c = 10*np.sin(a) # 求a中元素的sin值再乘10





a = np.array([1,2,],[3,4])
b = np.arange(4).reshape((2,2))

c_dot = np.dot(a,b)# 矩阵相乘
c_dot = a.dot(b)# 第二种形式


a = np.random.random((2,4))#生成随机的二行四列的矩阵
np.sum(a,axis=1)#求每一列的最小值
np.max(a,axis=0)# 在每一行求最小值
np.min(a)

A = np.arange(2,14).reshape((3,4))
print(np.argmin(A))# 求最小值的索引
print(np.argmax(A))# 求最大值的索引
#求平均值
    print(np.mean(A,axis=0))
    print(A.mean())

np.median(A)#求中位值

np.cumsum(A) #逐步累加

np.diff(A) #逐步累差

np.nonzero(A)#输出非零值的行数和列数

np.sort(A)#对每一个行排序

np.transpose(A)#矩阵转置
print(A.T)
print((A.T).dot(T))#矩阵和矩阵的转置相乘

np.clip(A,5,9)#矩阵A中所有小于5的数都等于5，所有大于9的数都等于9






#合并
A = np.array([1,1,1])
B = np.array([2,2,2])
np.vstack((A,B))#上下合并  可以进行多个合并，即括号里可以有多个矩阵
np.hstack((A,B))#左右合并

#将一个横向的序列变成一维行向量或一维列向量，变完之后才是矩阵，现在的A不是矩阵
A.T #直接这样是不行的，没法将一个横向序列变成一个矩阵
A[np.newaxis,:]#给定一个行维度，变成行向量
A[:,np.newaxis]#给定一个列维度，变成列向量

np.concatenate((A,B,B,A),axis=0) #纵向合并
np.concatenate((A,B,B,A),axis=1) #横向合并