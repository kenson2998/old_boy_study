'''
類
    屬性
        實例變量
        類變量
        私有屬性 __var
    方法
        構造方法
        析構函數
        私有方法


對象
    實例化一個類之後得到的對象

封裝
    把一些功能的實現細節不對外暴露


繼承
    代碼的重用
    單繼承
    多繼承
        2.7 經典類 是深度優先 新式類是廣度優先
        3.x 全都是廣度優先
    經典類 : class Foo:
    新式類 : class Foo(object):

    class Foo(Foo_father):
        def __init__(self,name,age,sex,salary):
            #因為Foo有inin構造函數了,會以Foo的為主,但是又想繼承Foo_father的某些功能 就會用到super
            super(Foo,self).__init__(name,age,sex)
            self.salary = salary


多態
    接口重用 ,一種接口,多種實現


靜態方法 @staticmethod
    只是名義上歸類管理,實際上在靜態方法裡訪問不了類或實例中的任何屬性

類方法 @classmethod
    只能訪問類變量,不能訪問實例變量

屬性方法 @property
    把一個方法變成靜態屬性去調用
    屬性賦值 @方法.setter
    刪除需要配置  @方法.deleter

反射
    hasattr(object,name_str) , 判斷一個對象object是否有對應的name_str方法
    getattr(object,name_str) , 根據字符串去獲取object裡的對應的方法的內存地址
    setattr(object,'y',z) , 相當於 object.y = z
    delattr(object,

異常
    try:
        code
    except (e1,e2) as e:

    except Exception as e: 抓所有錯誤,建議放最後使用



'''