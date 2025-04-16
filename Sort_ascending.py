"""Сортировка по возрастанию и сортировка выбором"""

arr = [343 : 1, 42124:13, 5:0, 325:43, 3435:99]

def find smallest(arr):
    smallest = arr[0] #Для хранения найменьшего значения
    smallest_index = 0 #Для хранения найменьшегои нднеса
    for i in range(1, len(arr)):
        if  arr[i] < smallest:
            smallest = arr [i]
            smallest_index = i
    return smallest_index          

#На Основе сортировки выше делаем сортировку по выбору

def selectuibsort(arr):
    newarr = []
    for i in range(len(arr)):
        smallest = indsmallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr

