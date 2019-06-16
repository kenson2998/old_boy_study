class C:
    def __init__(self):
        self.name = "NONO"

    def __str__(self):  # 可以在打印 物件的時候,修改成你想顯示的內容(<lib_0609.aa.C object at 0x1061f0550> 變成<obj:NONO>)
        return "<obj:%s>" % self.name
