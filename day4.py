#task1
for i in range(1,11,1):
    print(i)
#task2
for i in range(1,11,1):
    print(i,"*","2","=",i*2)
#task3
n=int(input("enter your table:"))
for i in range(1,11,1):
    print(i,"*",n,"=",i*n)
#task4
n=int(input("enter your table:"))
m=[]
for i in range(1,11,1):
    print(i,"*",n,"=",i*n)
    m.append(i*n)
print(m)
