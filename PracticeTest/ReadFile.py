f=open("D:/test.txt",'r')
f=open("D:/GitHub/JSToturial/Basic/clock.html",'r')
# print(f.read()) #read whole file
# print(f.read(2)) #read first 2 char
# print(f.readline()) #read first line

for x in f:
    print(x)        #Read line by line