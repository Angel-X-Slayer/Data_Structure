def vow_cons_substring(str_g):
    n=len(str_g)
    str_g=str_g.lower()
    vow=["a","e","i","o","u"]
    c=0
    
    res = [str_g[i: j] for i in range(n) for j in range(i + 1,n+1)]
    # print(res)
    for i in res:
        if len(i)==1:
            pass
        else:
            if (i[0] in vow and i[len(i)-1] not in vow) or (i[0] not in vow and i[len(i)-1] in vow):
                c+=1
    return(c)

str_g=input("enter the string : ")
str_g=str_g.replace(" ","")
# str_g=str_g.replace(":","")
# str_g=str_g.replace('"','')
# print(str_g)

print(vow_cons_substring(str_g))