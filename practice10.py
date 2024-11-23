class point:
    var = 10
    def method1(self):
        print("in method is point") 

class joint(point):
    var = 20
    def method2(self):
        print("In method 2 of joint")
        point.method1(self)
        super().method1()

j1 = joint()
j1.method2()
