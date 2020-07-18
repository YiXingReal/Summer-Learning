# 基本语句
    if语句的关键字为：if – elif – else
        if condition_1:
            statement_block_1
        elif condition_2:
            statement_block_2
        else:
            statement_block_3


    在Python中没有switch – case语句


    while 判断条件：
        statements


    for <variable> in <sequence>:
    <statements>
    else:# 循环结束后无条件执行
    <statements>
    \for else:当for语句中有break时才执行else。



    #range()的应用
    for i in range(0, 10, 3) :#从0到10，一次跳3
        print(i)

    pass 占位符 避免空函数的出现

# 迭代器
    list=[1,2,3,4]
    it = iter(list)    # 创建迭代器对象，it本身就列表中元素的标签
    print (next(it))   # 输出迭代器的下一个元素
    输出：1
    print (next(it))
    输出：2
    \迭代器被创建时，指向的是序列第一个元素的前面


    list=[1,2,3,4]
    it = iter(list)    # 创建迭代器对象
    for x in it:
        print (x, end=" ")# 直接输出

# 生成器
    \yield 的函数被称为生成器（generator）
    def foo():
        print("starting...")
        while True:
            res = yield 4
            print("res:",res)
    g = foo()#这里可以看成生成了一个对象
    print(next(g)) #用了next才开始执行这个函数，执行到yield时返回4
    print("*"*20)
    print(next(g))# 在这里继续接着退出点执行，执行到yield时退出
    print(g.send(7))# 把7值赋给 res

    #用法
        def foo(num):
        print("starting...")
        while num<10:
            num=num+1
            yield num
        for n in foo(0):#for自带迭代属性
            print(n)
   # https://blog.csdn.net/mieleizhi0522/article/details/82142856/ 最强解析

#函数
    def  函数名（参数列表）：
        函数体 

    #关键字参数
        def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
        调用时必须为voltage赋值，注意赋值的位置
    #可变参数列表
        def arithmetic_mean(*args):
            sum = 0
            for x in args:
                sum += x
            return sum
        arithmetic_mean(8989.8,78787.78,3453,78778.73)
        

# 数据结构
    # 堆栈——列表
        append()：在末尾添加一个元素
        pop() ：弹出末尾的一个元素 
    # 队列——列表
        from collections import deque
        queue = deque(["Eric", "John", "Michael"])
        queue.append("Terry") #末尾添加元素
        queue.popleft()       #弹出首元素
    # 列表推导式
        list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
        扩展如下：
        T = []
        for x in range(10):
            for y in range(10):
                if (x%2==0) and (y%2!=0):
                    T.append((x,y))#注意这里的写法！
    # 嵌套列表——矩阵
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
        ]
        # 将此矩阵转置
            [[row[i] for row in matrix] for i in range(4)]
    
    # del
        del a[0]   #删除指定元素
        del a[2:4] #删除切片
        del a[:]   #清空列表
        del a      #直接删除变量

    # 集合
        \集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。


    # 遍历技巧

       #  字典的items()方法，可同时读出关键字和值
            knights = {'gallahad': 'the pure', 'robin': 'the brave'}
            for k, v in knights.items():
            print(k, v)

        # 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
            for i, v in enumerate(['tic', 'tac', 'toe']):
                print(i, v)

        # 同时遍历两个或更多的序列，可以使用 zip() 组合：
            questions = ['name', 'quest', 'favorite color']
            answers = ['lancelot', 'the holy grail', 'blue']
            for q, a in zip(questions, answers):
                print('What is your {0}?  It is {1}.'.format(q, a))


        # 反向遍历
            for i in reversed(range(1, 10, 2)):
                print(i)
        
        # 使用 sorted() 函数返回一个已排序的序列
            basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
            for f in sorted(set(basket)):
                print(f)



# 模块导入
    from fibo import fib, fib2
    from fibo import *