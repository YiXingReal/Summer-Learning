#统计函数
    np.amin(a,1)#按行求最小值
    np.amax(a)#求整个数组的最小值
    np.amax(a,0)#按列求最大值
    numpy.ptp()#计算最大值与最小值差的函数
        np.ptp(a, axis = 1)#依照行计算
        np.ptp(a, axis = 0)#依照列计算
    numpy.percentile(a, q, axis)#将一组数据从大到小排序，以q这个百分数为 依据取数
    numpy.median(a, axis) #求中位数
    numpy.mean(a, axis = 0)#返回数组中元素的算术平均值
    numpy.average(a,axis)#平均值
    numpy.std([1,2,3,4])#标准偏差
    numpy.var([1,2,3,4])#方差

#排序 搜索 计数  
    numpy.sort(a, axis, kind, order)
    numpy.argsort()#间接排序——返回排序后的索引，这个索引可以构造排序后的数组
    numpy.lexsort()#使用键值进行间接排序
    numpy.argmax()#返回最大元素的索引
    numpy.argmin()#返回最小元素的索引
    numpy.nonzero()#返回非零元素的索引
    numpy.where()#返回满足给定条件的输入数组中元素的索引
    numpy.extract()#返回返回满足任何条件的元素

#改变大端对齐和小端对齐的方式
    numpy.ndarray.byteswap(true)



#浅拷贝和深拷贝
    ndarray.view()#浅拷贝
    ndarray.copy()#深拷贝

#矩阵
    numpy.matlib.empty(shape, dtype, order) 
    numpy.matlib.zeros(shape, dtype, order) 
    numpy.matlib.ones(shape, dtype, order) 
    numpy.matlib.eye(n, M,k, dtype)#这个函数返回一个矩阵，其中对角线元素为1，其他地方为0 n为行数 m为列数 k为对角线索引
        np.matlib.eye(n = 3, M = 4, k = 0, dtype = float)
    numpy.matlib.identity(5, dtype = float)#返回单位矩阵
    numpy.matlib.rand()#函数返回填充有随机值的给定大小的矩阵。

#线性代数
    dot #两个阵列的点积
    vdot #两个向量的点积
    inner #两个阵列的内积
    matmul #两个阵列的矩阵乘积
    determinant #计算数组的行列式
    solve #求解线性矩阵方程
    inv #找出矩阵的乘法逆

