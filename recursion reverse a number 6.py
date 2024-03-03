def reverse(str, n, temp):
    if n == len(str)-1:
        return (str[n])
    else:

        return (reverse(str, n+1, temp)+str[n])


str = "ishan"
temp = ""
k = reverse(str, 0, temp)
print(k)
