list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

count_players = len(list_players)
middle = count_players // 2

first_team = list_players[:middle]
second_team = list_players[middle:]

print(", ".join(first_team))
print(", ".join(second_team))