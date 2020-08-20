M=100000
a-[None]*100000
d=[None]*100000

def line(a,b.c):
    for j in range(b,c):
        a[j]='Y'

fp-open("datal, txt","r")

num-int(fp. readl ine ())
temp-fp. readline( split('')
beint(temp[0])
c-int(temp[1J)
line(a,b,c)#先取第一個線段資料
for i in range(1,num):
    temp=fp. readline() split('')
    b=int(temp[0])
    c-int(temp[1])
    line(d,b.c)#取出下一個新線段
    for j in range(M):#新線段與原線段進行OR運算
        if (a[j]--'Y' or d[j]=-'Y'):
        a[j]='Y'
j=0
n=0#計數器歸零
while j<M:
    if a[j]em'Y':
        ท=n+1 #累加被填滿的線段
        jーf+1
print("&d" %(n))