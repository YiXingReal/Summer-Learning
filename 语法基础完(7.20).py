# 输出
    #repr() 或 str() 函数   
        \将输出的值转成字符串
        \str() 函数返回一个用户易读的表达形式。
        \repr() 产生一个解释器易读的表达形式。
        #  repr() 函数可以转义字符串中的特殊字符
            hello = 'hello, world\n'
            hellos = repr(hello)
            print(hellos)#输出为'hello, world\n' 而不是'hello, world'
        # repr() 的参数可以是 Python 的任何对象
            repr((x, y, ('spam', 'eggs')))

    str.format() #格式化输出
        #基本格式
        'We are the {} who say "{}!"'.format('knights', 'Ni')
        #位置参数
        '{1} and {0}'.format('spam', 'eggs')
        #关键字参数
        'This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible')
        #位置及关键字参数混合使用
        'The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg')
        #'!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr())
        'The value of PI is approximately {!r}.'.format(math.pi)
        # ':' 的使用
        'I am {0:2.3f}.'.format('man')#0位置上的参数，域宽为2，小数点保留3位，数据格式为float
        #字典的运用
        table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
        'Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table)
        #或
        table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
        'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)

    # %
        print('The value of PI is approximately %5.3f.' % math.pi)


#输入

    x=input("请输入x=")
    y=input("请输入y=")
    z=x+y
    print("x+y="+z)


#文件读写
    open()#返回一个file对象
    open(filename, mode)
    第一个参数为要打开的文件名。
    第二个参数描述文件如何使用的字符
    'r' 如果文件只读, 
    'w' 只用于写 (如果存在同名文件则将被删除),
    'a' 用于追加文件内容; 所写的任何数据都会被自动增加到末尾. 
    'r+' 同时用于读写。 mode 参数是可选的; 
    'r' 将是默认值。

    f = open('/tmp/workfile', 'w')
    f.read(size)#读写文件size大小的数据，没有写size，则为全部读出
    f.readline()#从文件中读取单独的一行。换行符为 '\n' 返回一个空字符串, 说明已经已经读取到最后一行
    f.readlines()#返回该文件中包含的所有行。
    for line in f:#迭代读取
        print(line, end='')


    f.write(string)#将 string 写入到文件中, 然后返回写入的字符数。
    #如果要写入一些不是字符串的东西, 那么将需要先进行转换
    f.tell()#返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。

    f.seek()
        #seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
        #seek(x,1) ： 表示从当前位置往后移动x个字符
        #seek(-x,2)：表示从文件的结尾往前移动x个字符 from_what 值为默认为0，即文件开头
    
    f.close()

#异常
    #格式
        try:
            f = open('myfile.txt')
        except OSError as err:
            print("OS error: {0}".format(err))
        except (RuntimeError, TypeError, NameError):#多个异常
            print("Could not convert data to an integer.")
        except:
            print("Unexpected error:", sys.exc_info()[0])
        else:#print在try子句没有发生任何异常的时候执行
            print('try中没有异常')
        finally:#如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后再次被抛出
            print("executing finally clause")
    #抛出异常
        raise NameError('HiThere')#使用raise语句
    #自定义异常类   

    #预定义清理
        with open("myfile.txt") as f:# with 语句就可以保证诸如文件之类的对象在使用完之后会执行清理方法:
        for line in f:
            print(line, end="")

#面向对象
    #格式
        class MyClass:
            i = 12345          #属性
            def __init__(self):#构造方法，self指向对象本身，相当于this
                self.data = []
            def f(self):       #方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数:
                return 'hello world'

    #继承——允许多继承
        class sample(speaker,student):#继承了两个基类
            a =''
            def __init__(self,n,a,w,g,t):
                student.__init__(self,n,a,w,g)#初始化两个基类的构造函数
                speaker.__init__(self,n,t)
    #派生类中的函数可以覆盖基类的函数

    #私有方法或变量：变量名__开头的即为私有

    #类的专有方法：
        __init__: 构造函数，在生成对象时调用
        __del__: 析构函数，释放对象时使用
        __repr__: 打印，转换
        __setitem__ : 按照索引赋值
        __getitem__: 按照索引获取值
        __len__: 获得长度
        __cmp__: 比较运算
        __call__: 函数调用
        __add__: 加运算
        __sub__: 减运算
        __mul__: 乘运算
        __div__: 除运算
        __mod__: 求余运算
        __pow__: 乘方

    #运算符重载——对专有方法进行重载
    class Vector:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __str__(self):
            return 'Vector (%d, %d)' % (self.a, self.b)

        def __add__(self,other):
            return Vector(self.a + other.a, self.b + other.b)

            v1 = Vector(2,10)
            v2 = Vector(5,-2)
            print (v1 + v2)