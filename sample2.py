
# Function with out arguments and with out return type

def fun1():
    print("Function with out arguments and with out return type")
    a=10
    b=20
    c=a+b
    print("Sum = ", c)
 

# Function with  arguments and with out return type

def fun2(x,y):
    print("Function with arguments and with out return type")
    a=x
    b=y
    c=a+b
    print("Sum = ", c)

# Function with out arguments and with   return type
def fun3():
    print("Function with out arguments and with  return type")
    a=20
    b=30
    c=a+b
    return c

# Function with  arguments and with  return type

def fun4(x,y):
    print("Function with arguments and with out return type")
    a=x
    b=y
    c=a+b
    return c


fun1()
fun2(12,15)
res=fun3()
print("Sum = ",res)

print("Sum = ",fun4(15,16))
