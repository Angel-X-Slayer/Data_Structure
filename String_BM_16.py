def Compare_Version_Numbers(s1,s2):

## Nice try............................ Method 1

    # temp1=0
    # temp2=0
    # for i in range(len(s1)):
    #     if s1[i]==".":
    #         pass
    #     else:
    #         temp1+=s1[i]
    # for i in range(len(s2)):
    #     if s2[i]==".":
    #         pass
    #     else:
    #         temp2+=s2[i]
    # if temp1>temp2:
    #     print(1)
    # elif temp2==temp1:
    #     print(0)
    # else:
    #     print(-1)

## end of method 1......................

##.................********************.....................##

## Method 2..........................

    temp1=''
    temp2=''

    for i in range(len(s1)):
        if s1[i]==".":
            pass
        else:
            temp1+=s1[i]
    for i in range(len(s2)):
        if s2[i]==".":
            pass
        else:
            temp2+=s2[i]
    temp1=int(temp1)
    temp2=int(temp2)
    if temp1>temp2:
        print(1)
    elif temp2==temp1:
        print(0)
    else:
        print(-1)

## end of method 2........................

##...................**********************..................##

## Driver Function

s1="1.23.11.1"
s2="1.23.11.2"
Compare_Version_Numbers(s1,s2)