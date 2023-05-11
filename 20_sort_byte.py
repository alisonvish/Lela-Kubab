# Дано целое число без знака в качестве входных данных, 
# Отсортируйте его байты в порядке убывания, возвращая целое число без знака.

# Например:
# число в python занимает 4 байта.
#   в десятичной системе           – 3735928559 
#   набор байт в шестнадцатеричной  – b'\xde\xad\xbe\xef', 
#   набор байт в двоичной          – 11011110 10101101 10111110 11101111, 

# после сортировки байтов получим
#   набор байт в двоичной          – 11101111 11011110 10111110 10101101,
#   набор байт в шестнадцатеричной  – b'\xef\xde\xbe\xad'
#   в десятичной системе           – 4024352429

# Примеры:
#   sort_bytes(0), 0
#   sort_bytes(1), 16777216
#   sort_bytes(2), 33554432
#   sort_bytes(4294967295), 4294967295
#   sort_bytes(3735928559), 4024352429
#   sort_bytes(19088743), 1732584193




# Решение
x = 3735928559
byte_val = x.to_bytes(4)  # превратили в байтовую строку
byte_val_lst = list(byte_val)  # превратили в список кодов
sort_byte_val = sorted(byte_val_lst)  # сортируем список кодов
invert_byte_val = sort_byte_val[::-1]  # инвертируем список значений
int_val = int.from_bytes(invert_byte_val, "big")
print(int_val)

# В результате твоего кода получалось исходное число(
# Здесь записано все по шагам. Это можно конечно же сократить.
# Следующим заданием будет записать решение в виде функции в сжатом виде.
# Разметить новую функцию в отдельном файле и закинуть через git



# Измененное решение кодом:


x = 3735928559
x.to_bytes(4, byteorder = 'big')
int_val = int.from_bytes(byte_val, "big")
print(int_val)


array = [3735928559]
for i in array:
  print(hex(i))


int_val = int.from_bytes(byte_val, "big")
print(int_val)


# решение функцией версия 1:

def bytes(n):
  x.to_bytes(4, byteorder = 'big')
  int_val = int.from_bytes(byte_val, "big")
  array = [n]
  for i in array:
    print(hex(n))
print(bytes)
n = 3735928559

# ответ:
<function bytes at 0x7f4891edfeb0>



# решение версия 2:

def bytes2(i):
  bytes_list = i.to_bytes((i.bit_length() + 7) // 8, byteorder='big', signed=False)
  bytes_list.sort(reverse=True)
  sorted_num = int.from_bytes(bytes_list, byteorder='big', signed=False)
  return sorted_num
i = 3735928559
print(bytes2)

# ответ:
<function bytes2 at 0x7f48638f45e0>
  
  

