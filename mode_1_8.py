my_dict = {'Anna': 1994, 'Olga': 1990} #Словарь
print('Dict:', my_dict)

keys = input("Use something name: ") #Ввод имени от пользователя
if keys in my_dict.keys(): print("Existing value:", my_dict.get(keys)) #Если имя совпадает с именем из словаря, то удаляем значение ключа
else: print('Not existing value:    ', my_dict.get(keys)) # Если имени нет в словаре, то пишем None

new_choice = input(f'Write name:   {list(my_dict.keys())[0]} or  {list(my_dict.keys())[1]}') #Пользователь ввел переменную либо Анну, либо Ольгу
if new_choice in my_dict.keys(): print('Deleted value: ', my_dict.pop(new_choice)) # У выбранного имени (ключа) удаляем значение этого ключа

my_dict.update({'Vasya': 2010,
                'Helen': 1999})

#добавили словарь


print('Modified dictionary:', my_dict)

my_set = {1, 2, 3, True, 2, 2, 1}
print("Set: ", my_set)

my_set.update([5,7,"Gleb"])
print("Modified set: ", my_set)