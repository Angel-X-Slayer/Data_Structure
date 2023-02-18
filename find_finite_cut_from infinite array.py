arr=list(map(int,input("enter data : ").split(' ')))
op1=0
op2=0
ul=11
ll=4
# k1=ll%len(arr)
# k2=ul-ll
# k3=k2//len(arr)
s=sum(arr)
k1=ul//len(arr)
k2=ul%len(arr)
k3=ll//len(arr)
k4=ll%len(arr)
if k2!=0:
    op1=op1+k1*s+sum(arr[:k2])
else:
    op1=op1+k1*s
if k4!=0:
    op2=op2+k3*s+sum(arr[:k4-1])
else:
    op2=op2+k3*s
op=op1-op2
# print(op1)
print(op)