from pprint import pprint

def get_data():
    result = dict()
    dict_1 = {}
    list_2 = []
    cook_book = {}
    with open('recipes.txt', "r") as file:
        for line in file:
            dish_name = line.strip()
            dish_quantity = int(file.readline().strip())

            users_list = []
            # Читаем из файла, формируем словарь
            for list in range(dish_quantity):
                data = file.readline().strip()
                users_list.append(data.split(" | "))
            file.readline()
            result[dish_name] = users_list

    # Формируем кулинарную книгу
    for list in result.items():
        for list_1 in list[1]:
            dict_1['ingredient_name'] = list_1[0]
            dict_1['quantity'] = int(list_1[1])
            dict_1['measure'] = list_1[2]
            list_2.append(dict_1.copy())

        cook_book[list[0]] = list_2.copy()
        list_2.clear()

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    dict_2 = {}
    dict_3 = {}

    cook_book = get_data()

    for dish in dishes:
        for list_1 in cook_book.items():
            if dish == list_1[0]:
                for dict_1 in list_1[1]:
                    if dict_1.get('ingredient_name') not in dict_3.keys():
                       dict_2['measure'] = dict_1.get('measure')
                       dict_2['quantity'] = int(dict_1.get('quantity')) * person_count
                       dict_3[dict_1.get('ingredient_name')] = dict_2.copy()
                    else:
                        for list_2 in dict_3.items():
                            if dict_1.get('ingredient_name') == list_2[0]:
                                list_2[1]['quantity'] += int(dict_1.get('quantity')) * person_count
                                dict_3[dict_1.get('ingredient_name')] = list_2[1]
    pprint(dict_3)

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)