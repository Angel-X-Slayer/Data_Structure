def find_occurence(str, idx, target, first, last):
    if idx == len(str)-1:
        return (first, last)
    else:
        if str[idx] == target and first != -100:
            last = idx
        elif str[idx] == target and first == -100:
            first = idx
        else:
            pass
        return (find_occurence(str, idx+1, target, first, last))


str = "abbacgsdahjgfs"
target = "a"
first = -100
last = 0
f, l = find_occurence(str, 0, target, first, last)
print(f, l)
