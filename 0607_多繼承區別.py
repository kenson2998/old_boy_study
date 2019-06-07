class A:
    def __init__(self):
        self.A = 'aaa'
        print("A")


class B(A):
    def __init__(self):
        self.B = 'bbb'
        print("B")


class C(A):
    def __init__(self):
        self.C = 'ccc'
        print("C")


class D(B, C):
    pass
    # def __init__(self):
    #     print("D")


'''
多繼承有優先順序,
但是遇到B和C都有 __init__(構造函數) 的時候,
先有init的B就會給D繼承
B繼承A但是Ｂ有構造函數,所以沒有A屬性可以用
'''
obj = D()
# print(obj.B)




class E():
    def __init__(self):
        self.E = 'eee'
        print("E")


class F(E):
    pass


class G(E):
    def __init__(self):
        self.G = 'ggg'
        print("G")


class H(F, G):
    pass

'''
H繼承FG
F沒有構造函數, G有構造函數
F有繼承E, 可是init的繼承卻是G的
這是因為python3是廣度優先,非深度優先：
小孩(H) 繼承來自父母(F,G) > 父母繼承祖父(E)
'''
obj1 = H()
