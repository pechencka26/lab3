# TODO Напишите функцию find_common_participants
def find_common_participants(first,second,razdel=','):
    one=set(first.split(razdel))
    two=set(second.split(razdel))
    three=one.intersection(two)
    four= list(three)
    four.sort()
    return four
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group,participants_second_group,razdel=',')