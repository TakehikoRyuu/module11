# Обзор сторонних библиотек Python

# matplotlib (3.9.2)
import matplotlib.pyplot as plt

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


n = 10
fib = list(fibonacci_generator(n))
fib = fib[1:]

x = range(1, n)
y = fib
plt.plot(x, y)
plt.xlabel('X ось')
plt.ylabel('Y ось')
plt.title('тренд фибоначи')
plt.show()


# numpy(2.1.2)

import numpy as np

matrix = np.array([[range(5, n)], [fib[4:]]])
print(matrix)
# Изменение формы массива
transposed = matrix.T
print(transposed)
# Минимум и максимум
print("Минимум:", np.min(matrix))
print("Максимум:", np.max(matrix))


# requests(2.31.0)
import requests

THE_URL = "https://catfact.ninja/fact"

for i in range(3):
    response = requests.get(THE_URL) # делает запрос на сервер
    page = response.json() # переводит в формат python
    print(response.ok)
    print(f"fact in cats №{i+1} - {page['fact']}")


