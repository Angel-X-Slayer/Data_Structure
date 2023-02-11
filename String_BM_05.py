def lands(s):
    result=[]
    i=0
    while i<len(s):
        count=1
        while i+1<len(s) and s[i]==s[i+1]:
            count+=1
            i+=1
        result.append(str(count)+s[i])
        i+=1
    return''.join(result)

# s=input("enter the numerical string:")
s="1"
# n=int(input("enter the term u want:"))
n=7
for i in range(n-1):
    s=lands(s)
    print(s)
print()  ## to print the whole sequence write the print statement in for loop
print("the last answer is",s)  ## to print the nthnumber of the sequence write the print statement outside for loop
    