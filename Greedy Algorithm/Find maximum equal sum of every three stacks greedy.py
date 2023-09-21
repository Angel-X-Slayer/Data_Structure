def maxSum(stack1, stack2, stack3, n1, n2, n3):
    sum1 = sum(stack1)
    sum2 = sum(stack2)
    sum3 = sum(stack3)
    top1 = 0
    top2 = 0
    top3 = 0
    while True:
        if sum1 == 0 or sum2 == 0 or sum3 == 0:
            return (0)
        if sum1 == sum2 and sum2 == sum3:
            return (sum1)
        if (sum1 >= sum2 and sum1 >= sum3):
            sum1 -= stack1[top1]
            top1 = top1+1
        elif (sum2 >= sum1 and sum2 >= sum3):
            sum2 -= stack2[top2]
            top2 = top2+1
        elif (sum3 >= sum2 and sum3 >= sum1):
            sum3 -= stack3[top3]
            top3 = top3+1


stack1 = [3, 2, 1, 1, 1]
stack2 = [4, 3, 2]
stack3 = [1, 1, 4, 1]

n1 = len(stack1)
n2 = len(stack2)
n3 = len(stack3)

print(maxSum(stack1, stack2, stack3, n1, n2, n3))
