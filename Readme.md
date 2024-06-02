# Дослідження

## Завдання 1

Використовуючи бібліотеку pulp ми отримали статус задачі Optimal

```
Статус роботи: Optimal
Лимонаду потрібно виробити: 30.0
Фруктового соку потрібно виробити: 20.0
Загальна кількість продуктів: 50.0
```

## Завдання 2
Результат Методу Монте-Карло, n = кількість точок:

```
Quad_method integral:             2.666
Monte Carlo integral (100):       2.58
Monte Carlo integral (1000):      2.64
Monte Carlo integral (10000):     2.66

```
## Висновок

За допомогою методу Монте-Карло обчислення заданого інтегралу функції дає приблизно 2.66 при 1000 точках та 10000 точках, порівнюючи його з результатом виконання функції quad,який дає значення 2.666. Середнє значення результатів великої кількості експериментів має тенденцію наближатися до очікуваного значення, коли кількість експериментів стає дуже великою. Отримані дані повністю підтверджують переваги та недоліки методу Монте-Карло.
