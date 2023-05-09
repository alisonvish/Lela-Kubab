# Алгоритм 7

# 1. Напишите алгоритм пирамидальной сортировки (heap sort)
# Рассмотрите, как алгоритм работает в отладчике (debug)
# список для сортировки 
lst = [3, 14, 1, 7, 9, 8, 11, 6, 4, 2]


# Дополнительно
# 2. Создайте функцию min/max, которая использует алгоритм сортировки написанный выше 




# Решение


def heapify(numbers, n, i):
    largest = i    # Initialize largest as root. (Инициализировать наибольший как root)
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2
  # Проверяем существует ли левый дочерний элемент 
    if l <= n and numbers[l] > numbers[largest]:
        largest = l

    # Проверяем существует ли правый дочерний элемент 

    if r <= n and numbers[largest] > numbers[r]:
        largest = r
    if largest == i:
          return
    else:
        numbers[largest], numbers[i] = numbers[i], numbers[largest]
        heapify(numbers , n, largest)



# Основная функция для сортировки 
def build_max_heap(numbers):
    middle = len(numbers) // 2
    for idx in reversed(range(0, middle + 1)):
	    heapify(numbers, idx, len(numbers) - 1)

def heap_sort(numbers):
    build_max_heap(numbers)
    for idx in reversed(range(0, len(numbers))):
        numbers[0], numbers[idx] = numbers[idx], numbers[0]
        heapify(numbers, 0, idx - 1)
numbers = [3, 14, 1, 7, 9, 8, 11, 6, 4, 2]
heap_sort(numbers)
print(numbers)


#ответ

[14, 1, 7, 9, 8, 11, 6, 4, 2, 3]
