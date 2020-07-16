# 基础语法：自然字符串， 通过在字符串前加r或R。 如 r"this is a line with \n" 则\n会显示，并不是换行。
\同时赋值：a, b = 1, 2
\单引号和双引号没有区别



# Numbers（数字）

# String（字符串）
    # Python中的字符串有两种索引方式，第一种是从左往右，从0开始依次增加；第二种是从右往左，从-1开始依次减少
    # 字符串用 + 拼接 用 * 运算符重复 :a = 'hello'*2
    # 切片:格式→变量名[头下标:尾下标]
    # Python字符串不能被改变,不能向字符串的某一个下标赋值
    # 反斜杠 \ 续行符  
    # len(str)输出字符串长度


    #基本方法
        #改变大小写
        str1.capitalize()使第一个字符大写
        str1.casefold()把整个字符串的所有字符改为小写
        str1.lower()转换字符串中所有大写字符为小写
        str1.upper()转换字符串中所有小写字符为大写
        str1.swapcase()翻转大小写

        #统计次数
        str1.count(sub,[start],[end])

        #检测末尾的字符
        str1.endswith(sub,[start],[end])
        #检测开头的字符
        str1.startswith(sub,[start],[end])

        #\t变成空格
        str1.expandtabs()

        #找到指定字符的索引值
        str1.find(sub,[start],[end]) 没有指定字符返回-1
        str1.index(sub,[start],[end])返回异常
        str1.rfind(sub,[start],[end]) 从右边
        str1.rindex(sub,[start],[end])从右边

        #检测字符串的成分
        str1.isalnum()至少存在一个字符且为字母或数字
        str1.isalpha()至少存在一个字符且为字母
        str1.islower()检测是不是有字母且全为小写
        str1.isupper()检测是不是有字母且全为大写
        str1.isnumeric()字符串只包含数字
        str1.isdigit()字符串只包含数字
        str1.isdecimal()只包含十进制数字
        str1.isspace()是否全为空格
        str1.istitle()是否标题化（所有单词以大写开头）

        #插入字符串
        str1.join(sub) 将str1插入sub的间隙里

        #对齐
        str1.center(居中长度) 居中
        str1.ljust(width) 返回一个左对齐的字符串width为总长度 
        str1.rjust(width)返回长度为 width 的字符串，原字符串右对齐，前边用空格填充
        str1.zfill(width)返回长度为 width 的字符串，原字符串右对齐，前边用 0 填充。

        #去掉空格
        str1.lstrip()去掉左边的空格
        str1.rstrip()去掉右边的空格
        str1.strip([chars])去掉前后的空格，也可指定删除chars

        #分割成元组
        str1.partition(sub)
        str1.rpartition(sub)从右边开始

        #分割成列表
        str1.split([以什么为分割符,这个分割符会被吃掉],[分割成几个])
        str1.splitlines(([keepends]))以\n 为分隔符分割为列表，没有则返回一个列表,(keepends=True)时保留\n

        #替换
        str1.replace(old,new,[count])将old用new 替换count个
        str1.translate(str.maketrans('a','b'))用b替换a


        #返回标题化字符串
        str1.title()

    #字符串的格式化：
        format
        位置参数
        '{} {} {}'.format('I','Love','You')按位置依次赋值
        关键字参数
        '{a} {b} {c}'.format(a='I',b='Love',c='You')
        两者可以混合使用，但是位置参数必须在前面
        '{{}}'.format("a")
        '{:.1f}'.format(24.54)

#List（列表）
    #列表可以容纳任何东西，不限类型
    #创键列表：
        创建一个普通列表：
        T = ['','','','','','']
        创建一个混合列表：
        T = ['欧文',123,3.12,[1,1,1,],]
        创建一个空列表：
        T = []

    #基本方法
        #list.append(1)
        向T列表中加入一个整型1元素（一次只能添加一个），添加在末尾
        #list.extend([1,2])
        用一个列表扩张现在列表
        #list.insert(1,牡丹)
        在指定位置插入牡丹这个字符串
        #list.remove(1)
        删除list列表中1这个元素：在知道要删除那个元素的情况下使用
        #del
        del list[0]删除第零个元素
        del list 删除整个列表
        #list.pop()
        移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
        x = list.pop(1)
        将列表中的第一个元素赋值给x
        #list.reverse()
        将列表逆转
        #获取长度：
        len([1, 2, 3])
        #list.sort()(只针对同类型的)
        从小到大排队
        T.sort(reverse=True)
        排序+逆转：相当于从大到小排队
        # max(list)
        返回列表元素最大值
        # min(list)
        返回列表元素最小值
        # list(seq)
        将元组转换为列表
        dir(list)
        # list.count(1):
        统计1在T中出现的次数
        # T.index(1,[起始位置]，[终止位置])
        返回指定范围内1所在的位置即索引（下标）
        没有指定位置默认最前面

    #获取列表元素
        T[0]：第一个元素
        T[0][:]对第一个元素进行切片

    #列表切片
        T[i:j]
        将从i到（j-1）的元素切出来，原来的列表不发生改变
        T[:j]
        从0到（j-1）
        T[i:]
        T[:]
        P=T[:]获得拷贝
        T[1:9:5]
        从1到8 每5个值取出

    #操作符
        #T<P
        类似字符串的比较，第一个元素大即整个列表大
        #T=T1+T2
        整个加法只能用于两个列表
        #T*=3
        将T复制三遍再赋值给T
        #成员关系操作符——in 的用法
        1 in T
        1 not in T
        返还布尔数

    # 两种赋值方法的区别
        T1 = T[:]
        T2 = T 
        当T改变时T1不变T2变

    #迭代：
    for x in [1, 2, 3]:
            print x,     


    '''
    operator.[不同的功能](list1, list2)
    比较两个列表的元素
    '''

    # 细节
        #请问 list1[0] 和 list1[0:1] 一样吗？
        不一样，list1[0] 返回第0个元素的值，list1[0:1] 返回一个只含有第0个元素的列表。

        #如果你每次想从列表的末尾取出一个元素，并将这个元素插入到列表的最前边，你会怎么做？
        T.insert(0, T.pop())

        #对标签深层次的理解
        >>> old = [1, 2, 3, 4, 5]
        >>> new = old
        >>> old = [6]
        >>> print(new)
        首先将标签old贴到了一个列表上
        接着也将new贴到了这个列表上
        最后又将old贴到了另一个列表上
        
    #列表推导式/列表解析
        [有关A的表达式 for A in B]：
        list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
        扩展如下：
        T = []
        for x in range(10):
            for y in range(10):
                if (x%2==0) and (y%2!=0):
                    T.append((x,y))#注意这里的写法！
        list1 = [x for x in range(10) if x%2==0 ] 同理！！！！

    给出一道列表解析的练习：
    list1 = ['1.Jost do It','2.一切皆有可能','3.让编程改变世界','4.Impossible is Nothing']
    list2 = ['4.阿迪达斯','2.李宁','3.鱼C工作室','1.耐克']
    list2.sort()
    list3 = [ x+':'+y[2:] for x in list2 for y in list1 if x[:1] == y[:1]]
    #涉及到字符串的拼接、列表逆转、对列表元素的切片。

#Tuple（元组）
    #和列表类似，唯一的区别：一旦创建就无法修改元素

    #创建
        T = （1,2,3,4,5,6,7）
        T = tup1 = (50,)#元组中只包含一个元素时，需要在元素后面添加逗号

        # 从类型来看创建
        T1=(1)
        type(T1) T1的类型为int

        T2=(1,)
        type(T2) T2的类型为 tuple

        T3=1,2,3
        type(T3) T3的类型为 tuple

        T4=()
        type(T4) T4的类型为 tuple

        T5=1,
        type(T5) T5的类型为 tuple

        8*(8,)
        (8,8,8,8,8,8,8,8,8)

    #间接修改元祖
        切片间接更改元素：
        通过创建一个新的元组进行更改
        T=(1,2,4,5)
        T=T[:2]+('3',)+T[2:]

    #三种拷贝方式
        T=T1    只有这个是两个标签使用一个列表
        T=T1[:]
        T=T.copy()

\string、list和tuple都属于sequence（序列)。

#Sets（集合）

    \集合（set）是一个无序不重复元素的集。
    \基本功能是进行成员关系测试和消除重复元素。
    \可以使用大括号 或者 set()函数创建set集合，注意：创建一个空集合必须用 set() 而不是 { }，因为{ }是用来创建一个空字典。

    # set可以进行集合运算
    a = set('abracadabra')
    b = set('alacazam')
    a
    {'a', 'b', 'c', 'd', 'r'}
    a - b     # a和b的差集
    {'b', 'd', 'r'}
    a | b     # a和b的并集
    {'l', 'm', 'a', 'b', 'c', 'd', 'z', 'r'}
    a & b     # a和b的交集
    {'a', 'c'}
    a ^ b     # a和b中不同时存在的元素
    {'l', 'm', 'b', 'd', 'z', 'r'}




# Dictionaries（字典）
    \字典是一种映射类型（mapping type），它是一个 键:值 的集合
    \关键字必须使用不可变类型，也就是说list和包含可变类型的tuple不能做关键字
    \在同一个字典中，关键字还必须互不相同
    \不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
    \键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行

    # 创建空字典
    dic = {} # 空字典
    tel = {'Jack':1557, 'Tom':1320, 'Rose':1886}#可以通过key进行查询，类似下标

    # 删除
    del dict['Name'] # 删除键 'Name'
    dict.clear()     # 删除字典
    del dict         # 删除字典

    # 添加一个键值对或修改键对应的值
    tel['Mary'] = 4127  


    #构造函数 dict() ：对sequence中构建字典
        dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) \构造
        {'jack': 4098, 'sape': 4139, 'guido': 4127}

        {x: x**2 for x in (2, 4, 6)}
        {2: 4, 4: 16, 6: 36}

        dict(sape=4139, guido=4127, jack=4098)
        {'jack': 4098, 'sape': 4139, 'guido': 4127}


    #内置函数
    len(dict)计算字典元素个数，即键的总数
    str(dict)输出字典以可打印的字符串表示
    type(variable)返回输入的变量类型，如果变量是字典就返回字典类型

    #内置方法
        radiansdict.clear() 删除字典内所有元素
        radiansdict.copy() 返回一个字典的浅复制
        radiansdict.fromkeys() 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
        radiansdict.get(key, default=None) 返回指定键的值，如果值不在字典中返回default值
        key in dict 如果键在字典dict里返回true，否则返回false
        radiansdict.items()以列表返回可遍历的(键, 值) 元组数组
        radiansdict.keys()以列表返回一个字典所有的键
        radiansdict.values()以列表返回字典中的所有值
        radiansdict.setdefault(key, default=None)和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
        radiansdict.update(dict2)把字典dict2的键/值对更新到dict里

    
