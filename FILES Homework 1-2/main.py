from pprint import pprint

def reader(file_name):
    with open(file_name, 'r', encoding="utf-8") as file_obj:
        cook_book = {}
        for line in file_obj:
            meal_name = line.strip()
            ingridients_list = []
            for item in range(int(file_obj.readline())):
                ingridients = file_obj.readline()
                ingridient_name, quantity, measure = ingridients.split('|')
                ingridients_list.append({'ingridient_name': ingridient_name.strip(), 'quantity': quantity.strip(), 'measure': measure.strip()})
            cook_book[meal_name] = ingridients_list
            file_obj.readline()
        return cook_book


def get_shop_list_by_meals(meals_list, persons):
    shop_list = {}
    for dish in meals_list:
        for meal_name, ingridients in reader('recipes.txt').items():
            if dish == meal_name:
                for ingridient in ingridients:
                    if ingridient['ingridient_name'] in shop_list.keys():
                        shop_list[ingridient['ingridient_name']]['quantity'] += int(ingridient['quantity']) * persons
                    else:
                        shop_list[ingridient['ingridient_name']] = {}
                        shop_list[ingridient['ingridient_name']].setdefault('measure', ingridient['measure'])
                        shop_list[ingridient['ingridient_name']].setdefault('quantity', (int(ingridient['quantity']) * persons))
    return shop_list




# reader('recipes.txt')
# pprint(cook_book)
pprint(get_shop_list_by_meals(['Омлет', 'Фахитос'], 2))
