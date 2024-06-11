c= [10,20,30]
def myfun(d):
    print("value of d is ", d)
    d[0]=99
    d[1]=98
    print("the new value of d is ", d)
myfun(c)