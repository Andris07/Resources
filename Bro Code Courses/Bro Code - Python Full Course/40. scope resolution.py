# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    a = 1
    print(a) # print(b) -> error

def func2():
    b = 2
    print(b) # print(a) -> error

func1()
func2()

def func3():
    x = 1
    print(x) # print(a) -> error

def func4():
    x = 2
    print(x) # print(b) -> error

func1()
func2()

def func5():
    x = 1
    print(x) # print(x) -> 1

    def func6():
        x = 2 # if this line wouldn't exist, x would still have a value '1' because of declaration inside func5()
        print(x) # print(x) -> 2

    func6()

func5()

x = 13

def func7():
    x = 6
    print(x) 

def func8():
    x = 7
    print(x) 

func7()     # 6
func8()     # 7
print(x)    # 13

from math import e
print(e)

e = 67
def func9():
    print(e)

func9()     # 67