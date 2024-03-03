def tower_of_hanoi(n, s, d, h):
    if n == 1:
        print(n, s, d)
        return
    else:
        tower_of_hanoi(n-1, s, h, d)
        print(n, s, h)
        tower_of_hanoi(n-1, h, d, s)


n = 3
tower_of_hanoi(n, "source", "destination", "helper")
