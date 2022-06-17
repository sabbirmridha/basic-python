# Multilevel inheritance

class A :
    def show1(self):
        print("I am in A ")


class B(A):
    def show2(self):
        print("I am in B")


class C(B):
    def show3(self):
        super().show1()
        super().show2()
        print("I am in C")
ob1 = C()
ob1.show3()
