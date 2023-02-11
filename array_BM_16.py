def finding_similar (a1,a2,a3):
    n1=len(a1)
    n2=len(a2)
    n3=len(a3)
    i,j,k=0,0,0
    while i<n1 and j<n2 and k<n3:
        if a1[i]==a2[j] and a2[j]==a3[k]:
            print(a1[i])
            i+=1
            j+=1
            k+=1
        elif a1[i]<a2[j]:
            i+=1
        elif a2[j]<a3[k]:
            j+=1
        else:
            k+=1


##nicher poddhoti teo kora jabe, khali ek2 chnge krte hbe code ta.......

#ei code tar basic byapar ho66e j 1st 2to array theke intersection kore temporary array te store, then temporary arr
#ar last array tar moddhe intersection perform kore value gulo k show kora....... 


    # m=max(n1,n2,n3)
    # n=min(n1,n2,n3)
    # a4=[]
    # a5=[]
    # if n1>n2:
    #     j1=n1-1
    #     j2=n2-1
    #     while j1>0 and j2>0:
    #         if a1[j1]==a2[j2]:
    #             a4.append(a1[j1])
    #             j1-=1
    #             j2-=1
    #         if a1[j1]>a2[j2]:
    #             j1-=1
    #         if a2[j2]>a1[j1]:
    #             j2-=1
    # a4.sort()
    # print(a4)

    # if len(a4)<n3:
    #     j1=len(a4)-1
    #     j2=n3-1
    #     while j1>0 and j2>0:
    #         if a4[j1]==a3[j2]:
    #             a5.append(a4[j1])
    #             j1-=1
    #             j2-=1
    #         if a4[j1]>a3[j2]:
    #             j1-=1
    #         if a3[j2]>a4[j1]:
    #             j2-=1

    # print(a5)

    

    

if __name__=="__main__":
    n1=int(input("enter the lymyt: "))
    n2=int(input("enter the lymyt: "))
    n3=int(input("enter the lymyt: "))
    a1=[]
    a2=[]
    a3=[]
    for i in range(n1):
        num=int(input("enter the number:"))
        a1.append(num)
    for i in range(n2):
        num=int(input("enter the number:"))
        a2.append(num)
    for i in range(n3):
        num=int(input("enter the number:"))
        a3.append(num)
    finding_similar(a1,a2,a3)    




