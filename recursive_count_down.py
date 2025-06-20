def count_down(n):
    if (n >= 1):
        print(n)
    else:
        return
    count_down(n - 1)

count_down(10)
