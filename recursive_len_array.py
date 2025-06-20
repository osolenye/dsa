def len_array(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + len_array(arr[1:])

print(len_array([1,2,3,4,5]))
