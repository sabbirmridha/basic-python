import  sys
sys.setrecursionlimit(1991)
print(sys.getrecursionlimit())
n =0
def notify() :

    global n
    n = n+1
    print("I am practising recursion using python", n)
    notify()

notify()
