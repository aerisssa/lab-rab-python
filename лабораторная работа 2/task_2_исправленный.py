salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

money_capital = 0
count_month = 10
for i in range(count_month):
    money_capital += salary - spend
    spend += spend * increase
    count_month -= 1
money_capital *= -1
if (money_capital > round(money_capital)):
    money_capital = round(money_capital) + 1
else:
    money_capital = round(money_capital)
#print(money_capital, spend, count_month)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
