#-*-coding: utf-8-*-

import numpy as np


def f(x, y):
    return 10*x + y


if __name__ == '__main__':

    # a = np.array(np.arange(15).reshape(3,5))
    # print(a)
    # print(a[1, :])
    # a[2,4] = 444
    # print(a)

#Basic Operations
    print("Basic Operations")
    a = np.array([20,30,40,50])
    b = np.arange(4) #取[1,2,3,4]
    c = a - b
    print(c)
    c = b ** 0.2 #平方运算
    print(c)
    d = a < 35  #返回一个bool类型的矩阵
    print(d)


'''
#The Basics
    print("The Basics:")
    my_arr = np.array([[0, 1, 2], [3, 4, 5]])
    print(my_arr)
    print(type(my_arr))   #numpy.ndarray??
    my_arr1 = np.arange(100).reshape(10, 10)
    print(my_arr1.ndim)  #n
    print(my_arr.ndim)   #矩阵的行数??貌似不对，目前解释是一个维数?
    print(my_arr.shape)  #一个元组，返回矩阵的行列((2L, 3L))
    print(my_arr.size)   #返回一个矩阵的元素个数（6个）
    print(my_arr.dtype)  #返回矩阵的元素类型（int32）
    print(my_arr.itemsize)   #返回矩阵元素类型的字节大小， int32=4字节，int64=8字节。。。
    print(my_arr.data)  #默认一般不使用的东东

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Array Create
    print("Array Create:")
    arr1 = np.array([[0, 1, 2], [3, 4, 5]])  #从list中创建
    print(type(arr1))
    arr2 = np.array(((4, 5, 6), (7, 8, 9)))  #从元组中创建
    print(type(arr2))

    arr3 = np.array([[0, 1, 2], [3, 4, 5]], dtype=np.int16)  #从list中创建，但是指定了类型为int16
    print(arr3)
    print("Tttttttttttttttt:%s" % (arr3.min()))

    arr4 = np.zeros((4,5))  #全零矩阵
    print(arr4)
    arr5 = np.ones((8, 9))   #全1矩阵
    print(arr5)
    arr6 = np.empty((4,4))  #随机矩阵, 默认类型是float
    print("aaaaahhhhhhhhhhhhhhh")
    print(arr6)

    arr7 = np.tile(arr4, 1)
    print(arr7)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Basic Operations
    print("Basic Operations")
    a = np.array([20,30,40,50])
    b = np.arange(4) #取[1,2,3,4]
    c = a - b
    print(c)
    c = b ** 2 #平方运算
    print(c)
    d = a < 35  #返回一个bool类型的矩阵
    print(d)

    a = np.array([[1, 1],
                  [0, 1]])
    b = np.array([[2, 0],
                  [3, 4]])
    print(a * b)  #这个只是矩阵元素简单的乘积，如果真的要做矩阵运算，应该使用：dot
    print(a.dot(b)) #这个才是矩阵的乘法

#Universal Functions
    print("Universal Functions")
    sin_a = np.sin(a)
    print(sin_a)
    cos_a = np.cos(a)
    print(cos_a)
    tan_a = np.tan(a)
    print(tan_a)
    self_tan_a = sin_a / cos_a
    print(self_tan_a)

    exp_a = np.exp(a)
    print(exp_a)
#Indexing, Slicing and Iterating
    print("Indexing, Slicing and Iterating:")
    a = np.arange(10) ** 3#一维数组可以被索引，切片和迭代，和python中的sequence操作很相像；
    print(a)
    print(a[2:5])



    a = np.fromfunction(f, (5,4))#多维数组的创建
    print("a=")
    print(a)
    #print(a[2,3])  #二维数组第2行第3列的元素，从0开始

    #print(a[-1])  #输出二维数组的最后一行
    print(a[1,...]) #输出第二行
    print(a[1])  #输出第二行
    for row in a :
        print("type=%s" % type(row)) #numpy.ndarray 类型
        print(row)   #列值

    for element  in a.flat: #如果想遍历每一个元素，使用flat属性
        print(element)

#shape manipulation
    print("shape manipulation:")
    print(a.reshape(2, 10))  #重新shape一个新的2*10矩阵,但是原来的a还是4*5阶矩阵
    print(a.ravel())  #返回矩阵的数组形式
    print(a)
    print(a.T) #转置矩阵4*5阶矩阵
    a.resize(2,10)
    print(a) #和reshape的区别，就是把自身给reshape了
#stacking together different arrays
    print("stacking together different arrays ")
    a = np.floor(10 * np.random.random((2, 3)))  #先随机2*3的矩阵，然后*10，之后用floor去除小数点
    print(a)
    b = np.floor(10 * np.random.random((2, 3)))
    print(b)
    print(np.vstack((a, b)))   #将两个矩阵合并，按照竖的方向合并
    print(np.hstack((a, b)))   #将两个矩阵合并，按照横的方向合并

    a = np.floor(10 * np.random.random((2, 12)))
    print(a)
    print(np.hsplit(a, 3))  #分割矩阵横着分为3个等分，返回3个矩阵，都是2*4阶矩阵

#Copy and Views
    #矩阵赋值默认只是拷贝引用
    print("Copy and Views:")
    b = a
    print(a is b) #True
    print(id(a))
    print(id(b))
    b = a.view()
    print(a is b) #False

#Linear Algebra
    a = np.array([[1.0, 2.0], [3.0, 4.0]])
    print(np.trace(a))   #矩阵的迹


#self test
    a = np.array([[1,2,4,3]])
    print(a)
    print(np.argsort(a))

'''



