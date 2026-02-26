77
show(n-1)
def show(n):
    if (n==0):
        return
    print(n)
    show (n-1)
show(5)
def show(a):
    if (a==70):
        return
    print(a)
    show(a-1)
show(90)  
def fact(n):
    if (n==0 or n==1):
        return 1
    return fact(n-1)*n
print(fact(4))
def sum(n):
    if(n==0):
        return 0
    return sum(n-1) +n
summ=sum(10)
print (sum)    

