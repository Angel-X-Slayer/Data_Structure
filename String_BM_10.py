def making_palindrome(stri):
    i=0
    j=len(stri)-1
    count=0
    while i<j:
        if stri[i]!=stri[j]:
            count+=1
            j-=1
        else:
            i+=1
            j-=1
    if count==0 or count==1:
        print(1)
    else:
        print(0)

# stri="abcbad"
stri="abcba"
# stri="abecbea"
making_palindrome(stri)