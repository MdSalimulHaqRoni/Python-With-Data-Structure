def linear_search(L, x):
    n = len(L)
    for i in range(n):
        if L[i] == x:
            return i
    return -1


L = [2, 1, 6, 4, 7, 9, 8]
x = 7
n = len(L)
result = linear_search(L, x)
if result == -1:
    print("Element not found")
else:
    print("Element found at ", result)