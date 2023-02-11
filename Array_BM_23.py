import sys
sys.setrecursionlimit(10**4)
def fact(n):
    if(n==0):
        return(1)
    else:
        return(n*fact(n-1))
if __name__=="__main__":
    n=int(input("enter the number:"))
    t=(fact(n))
    print(t)

# import sys
# sys.setrecursionlimit(1000)
# def fact(n):
#     if(n == 0):
# 	    return 1
#     return n * fact(n - 1)

# if __name__ == '__main__':

# 	f = int(input('Enter the number: \n'))

# 	print(fact(f))
