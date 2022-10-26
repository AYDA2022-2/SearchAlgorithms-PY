arr = [17, 19, 24, 32, 41, 57, 62, 80]
arr1 = [80, 62, 57, 41, 32, 24, 19, 17]
arr2 = [17, 24, 41, 62, 19, 32, 80, 57]
arreglo = [1, 2, 5, 8, 10, 11, 11, 16, 30, 20, 80, 500, 500, 1000, 1002, 5000]


def binary_search(value, array):
    first = 0
    last = len(array) - 1
    position = -1
    found = False

    while found == False and first <= last:
        middle = (first + last) // 2
        if array[middle] == value:
            found = True
            position = middle
        elif array[middle] > value:
            last = middle - 1
        else:
            first = middle + 1
    return position


print("output arreglo")
print(binary_search(80, arreglo))
