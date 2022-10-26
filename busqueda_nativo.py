
arr = [17, 19, 24, 32, 41, 57, 62, 80]
arr1 = [80, 62, 57, 41, 32, 24, 19, 17]
arr2 = [17, 24, 41, 62, 19, 32, 80, 57]
arreglo = [1, 2, 5, 8, 10, 11, 11, 16, 30, 20, 80, 500, 500, 1000, 1002, 5000]

found = next(i for i in arr if i >= 57)
found1 = next(i for i in arr1 if i < 57)
found2 = next(i for i in arr2 if i > 57)
found3 = next(i for i in arreglo if i >= 500)

print("output metodo next")
print(found)
print(found1)
print(found2)
print(found3)

print("output metodo index")
print(arr.index(80))
print(arr1.index(80))
print(arr2.index(80))
print(arreglo.index(80))
