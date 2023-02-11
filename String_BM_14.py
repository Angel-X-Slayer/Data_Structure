def Length_of_Last_Word(s):
    # l=len(s)
    # print(l)
    # print(s[11])
    count=0
    for i in range(len(s)-1,0,-1):
        if s[i]==".":
            count+=1
        if s[i]==" ":
            return(print(len(s)-1-i-count))


s="I am a filthy bitch. Who masterbates everyday looking at the live pussy of various girls accross the world by omegle. i should be ashamed by myself,but i am not."
# s="hello world."
Length_of_Last_Word(s)