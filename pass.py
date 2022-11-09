import time
import random


upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
lower = 'qwertyuiopasdfghjklzxcvbnm'
numbers = '1234567890'
symbols = '!$%^&&*()'

together = upper + lower + numbers + symbols

lenght = 16

# создаем пароль методом обьеденения join приравнивает все к строке;
#sample метод random который возвращает списко рандомных елементов;
password = ''.join(random.sample(together, lenght))


print('Идет генерация пароля:')
time.sleep(5)

print('Индексация рандомных символов:')
time.sleep(3)
print('Successful')
print('Создание двоичной кодировки пароля:')
time.sleep(3)
print('Generation successful')
time.sleep(2)
print('Ваш пароль создан:')
print(password)
input()