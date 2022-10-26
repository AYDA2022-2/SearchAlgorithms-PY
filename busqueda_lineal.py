arregloAl = [1, 2, 5, 8, 10, 11, 11, 316, 20, 800, 500, 500, 1000, 1002, 5000]
arr = [17, 19, 24, 32, 41, 57, 62]
arr1 = [62, 57, 41, 32, 24, 19, 17]
arr2 = [17, 24, 41, 62, 19, 32, 57]

def sequential_search(element, array):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1


print("output arregloAl")
print(sequential_search(5000, arregloAl))
