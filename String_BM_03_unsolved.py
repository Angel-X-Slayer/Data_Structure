def delete_by_inte(str_g,int_g):
    n=len(str_g)
    m=0
    c=1
    t=[]
    t1=[]
    # for i in range(n-1):

    #     if str_g[i]==str_g[i+1]:
    #         c+=1
    #     else:
    #         c=1
    while m<=n:
        if str_g[m]==str_g[m+1]:
            c+=1
            m+=1
        else:
            if c==int_g:
                t.append(m-int_g)
                # t.append(m)

            c=1
            m+=1
    for i in range(len(t)):
        if t[i]==0:
            



##..........................**********************.......................##


# def solve(A,B):

#     c=1

#     i=0

#     s=""

#     while i<len(A):

#         c=1

#         j=i

#     while j<len(A)-1 and A[j]==A[j+1]:

#         j+=1

#         c+=1


#     if c!=B:
#         s+=c*A[i]
            
#         i+=c
        
#     return s



# A="aabbccd"
# B=2
# print(solve(A,B))

        
            
        