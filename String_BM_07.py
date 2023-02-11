def strstr(haystack,needle):
    n=len(needle)
    b=''
    c=0
    for i in range(len(haystack)-n+1):
        b=b+haystack[i:i+n]
        if b==needle:
            c=i

            
        b=''
    if c!=0:
        print(c)
    else:
        print(-1)
haystack="hellow"
needle="ow"
strstr(haystack,needle)


