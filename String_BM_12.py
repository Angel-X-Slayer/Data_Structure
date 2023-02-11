def minimum_parenthisis(s):
    l=len(s)
    left,right=0,0
    for i in range(l):
        if s[i]=="(":
            left+=1
        elif s[i]==")":
            right+=1
    return(print(abs(left-right)))
s="(()((((())))()((()("
minimum_parenthisis(s)