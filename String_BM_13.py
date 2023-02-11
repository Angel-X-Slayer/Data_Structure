def Longest_Palindromic_Substring(s):
    temp_max=0
    temp_i=0
    temp_j=0
    for i in range(len(s)):
        j=len(s)-1
        while i<j:
            if i==0:
                if s[i:j+1]==s[j::-1]:
                    temp=j-i
                    if temp>temp_max:
                        temp_max=temp
                        temp_i=i
                        temp_j=j
                        

                    
            else:
                if s[i:j+1]==s[j:i-1:-1]:
                    temp=j-i
                    if temp>temp_max:
                        temp_max=temp
                        temp_i=i
                        temp_j=j
                
            j-=1
    print(s[temp_i:temp_j+1])
# s="aaaabaaa"
s="aabaababbbababbbabab"
# s="ababbbababbbaba"
Longest_Palindromic_Substring(s)
