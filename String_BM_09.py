##......................************************.......................##

## Method 1: Partial correct

def making_palin_string(stri):## append at the fornt
    # n=len(stri)
    # m=(n*(-1))-1
    b=''
    c=stri
    i=0
    count=0
    count1=0
    j=len(stri)-1
    while i<j:
        if stri[i]==stri[j]:
            count+=1
            i+=1
            j-=1
        else:
            i+=1
            j-=1
    i=0
    j=len(stri)-1
    if count != 0:
        while i<j:
            if stri[i]!=stri[j]:
                c=b.join(((stri[j]),c))
                count1+=1
                j-=1
                i+=1
            else:
                i+=1
                j-=1
    else:
        for i in range(1,len(stri)):
            c=b.join(((stri[i]),c))
            count1+=1
    print(c)
    print(count1)

## end of Method 1

##....................*********************.....................##

## Method 2: Copied

def making_palin_string_1(A): ## Append at the front
    L = len(A)
    if L<2: return 0
        
    A_r = A[::-1]
        
    for i in range(L):
        if A_r[i:] == A[:L-i]:
            return(print(i))
    return(print(L))

## End of Method 2

##......................*********************.....................##



# stri="AACECAAAA"
# stri="ABCDEF"
stri="ABCA"
# making_palin_string(stri)
making_palin_string_1(stri)
