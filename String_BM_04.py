##...........***********..............##
## Method 1: BRUTE FORCE 

def longest_cmon_pref(a):
    c=100
    b=[]
    for i in range(len(a)):
        if len(a[i])<c:
            temp=a[i]
            c=len(a[i])
            idx=i
    count=0
    for i in range(len(temp)):
        for j in range(len(a)):
            if j==idx:
                pass
            else:
                if a[j][i]==temp[i]:
                    count+=1
    t=count//(len(a)-1)
    if t==0:
        print(" ")
    else:               
        print(temp[:t])

## END OF METHOD 1
##...........................***************************.........................##
## METHOD 2: EFFICIENT APPROACH

def longest_cmon_pref1(words):
    min_word = min(words, key=lambda word: len(word))
    n = len(min_word)
    m = len(words)
        
    for i in range(n):
        for j in range(m):
            if words[j][i] != min_word[i]:
                return min_word[:i]

    return min_word
    

 


    







a = ["abcdefgh", "aefghijk", "abcefgh"]
# a = ["abab", "ab", "abcd"]
# a=["abc","def","ghi"]
print(longest_cmon_pref1(a))
# longest_cmon_pref(a)