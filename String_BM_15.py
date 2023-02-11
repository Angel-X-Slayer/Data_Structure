def reverese_the_string1(s):
    b=""
    temp=""
    l=len(s)
    print(s[22])
    for i in range(l-1,-1,-1):
        if s[i]!=" ":
            b+=s[i]
        if s[i]==" ":
            temp+=b[::-1]+s[i]
            b=""
    temp+=b[::-1]
    print(temp)
##........................****************************......................##
def reverese_the_string2(A):
        rev = A.split()
        rev.reverse()
        s = ' '
        s = s.join(rev)
        return s
##...............**************************....................##
def reverese_the_string3(A):
        print(' '.join(A.strip().split()[::-1]))
s="I am a boy , my age is 22"
# reverese_the_string1(s)
# reverese_the_string2(s)
reverese_the_string3(s)
