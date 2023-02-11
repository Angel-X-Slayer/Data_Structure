## Process !

# def palindrome_string(str):
#     str=str.lower()
#     rev_str=str[ : : -1]
#     if str==rev_str:
#         return("True")
#     else:
#         return("False")

## end of process 1
##.......................**********************.......................##
## Process 2

def palindrome_string(str):
    str=str.lower()
    n=len(str)
    c=0
    for i in range(n):
        if str[i]==str[n-1-i]:
            c+=1
    if c==(n):
        return("1")
    else:
        return("0")

## end of precess 2
##...................****************************.....................##



str=input("enter the string : ")
print(palindrome_string(str.replace(" ","")))
