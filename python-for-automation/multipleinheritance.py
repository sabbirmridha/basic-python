# Multiple inheritance-


class A :
    def show(self):
        print("I am in A ")


class B :
    def show(self):
        print("I am in B")


class C(A,B): # parameter will be choosed as per priority as A is at first it will show A
    pass


ob1 = C()
ob1.show()
