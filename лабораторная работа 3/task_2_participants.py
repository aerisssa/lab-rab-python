# TODO Напишите функцию find_common_participants
# task_2_participants
def find_common_participants(first_group, second_group, splitter=","):
    result = []
    first_group = first_group.split(splitter)
    second_group = second_group.split(splitter)

    for i in first_group:
        for j in second_group:
            if i == j:
                result.append(i)

    result.sort()
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))

# TODO Провеьте работу функции с разделителем отличным от запятой
