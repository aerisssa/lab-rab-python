money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

budget = salary + money_capital
count_month = 0
while spend < budget:
     spend += spend * increase
     budget = budget + salary - spend
     count_month += 1

print("Количество месяцев, которое можно протянуть без долгов:", count_month)
