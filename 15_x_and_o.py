# Проверьте, содержит ли строка одинаковое количество "x" и "o".
# Верните логическое значение True или False 
# Строка может быть в любом регистре и содержать любые символы!

# Примеры ввода/вывода:
#   строка "ooxx" => true
#   строка "xooxx" => false
#   строка "ooxXm" => true
#   строка "zpzpzpp" => true # когда нет "x" и "o", должно быть возвращено значение true
#   строка "zzoo" => false




# решение кодом

str = input()
count_x = 0
count_o = 0
for letter in str:
    if letter == 'x':
        count_x +=1
    elif letter == 'o':
        count_o +=1
if count_x == count_o:
    print(True)
else:
    print(False)
    
#   решение функцией 
    
def xoteam(m):
    return m.count('x') == m.count('o')
print(xoteam('xoxo'))

 
