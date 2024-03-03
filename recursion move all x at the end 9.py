def move_all_x_at_end(str, idx, n, newstr):
    if idx == len(str):
        return (newstr, n)
    else:
        if str[idx] != "x":
            newstr += str[idx]
            return (move_all_x_at_end(str, idx+1, n, newstr))
        else:
            n += 1
            return (move_all_x_at_end(str, idx+1, n, newstr))


str = "axbxcx"
idx = 0
n = 0
newstr = ""
opstr, k = move_all_x_at_end(str, idx, n, newstr)
for i in range(k):
    opstr += "x"
print(opstr)
