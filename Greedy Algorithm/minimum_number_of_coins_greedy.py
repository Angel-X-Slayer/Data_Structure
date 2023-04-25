coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
coins = sorted(coins, reverse=True)
v = int(input(" enter input: "))
op = []
i = 0
while i < len(coins):
    if coins[i] <= v:
        v -= coins[i]
        op.append(coins[i])
        i = 0
    else:
        i += 1
print(*op, sep=" ")
