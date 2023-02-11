def amezing_substrings(s):
    # print(len(s))
    b=[]
    c=[]
    count=0
    for i in range(len(s)+1):
        for j in range(i,len(s)+1):
            b.append(s[i:j])
    # print(b)
    # print(len(b))
    # print(b[3][0])
    for i in range(len(b)):
        if b[i]=="":
            pass
        elif b[i][0]=="a" or b[i][0]=="e" or b[i][0]=="o" or b[i][0]=="i" or b[i][0]=="u":
            c.append(b[i])
            count+=1

    # print(c)   
    print(count%10003)
s="abec"
amezing_substrings(s)