import random
n = int(input('Введите количество элементов списка: '))
arr = [random.randint(0, 100) for i in range(n)]
print(arr) 
k = -1
   
for i in range(len(arr)//2):
    print("\nбыло   ", i, arr)
    arr[k], arr[i] = arr[i], arr[k]
    print("стало    ", arr)
    k -= 1    