# Напишите скрипт, который принимает цифры от 0 до 9 и возвращает значение прописью.

# Например,
#   при вводе числа 1 получаем 'Один'
#   при вводе числа 3 получаем 'Три'
#   при вводе числа 10000 получаем None

# Использовать условный оператор if-elif-else нельзя!

```
words = ['Ноль', 'Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять']
num = input('Введите число от 0 до 9: ')
try:
    print(words[int(num)])
except (ValueError, IndexError):
    print(None)
```


```
def num_to_word(num):
    words = ['Ноль', 'Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять']
    try:
        return words[num]
    except IndexError:
        return None


get_input = int(input("Enter digit >"))
print(num_to_word(get_input))
```
