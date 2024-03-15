my_list = ['pineapple', 'banana', 'apple', 'melon', 'pear']
print('List: ' + str(my_list))                          # вывод списка
print('First & last elements: ' + str(my_list[0:5:4]))  # вывод первого и последнего элемента списка
print('Third-fifth elements: ' + str(my_list[2:5]))     # вывод с третьего по пятый элемент списка
my_list[2] = 'peach'                                    # замена третьего элемента списка
print('Modified list: ' + str(my_list))                 # вывод измененного списка

my_dict = {'pineapple': 'ананас', 'banana': 'банан', 'apple': 'яблоко'}
print('Dictionary: ' + str(my_dict))                    # вывод словаря
print('Translation: ' + str(my_dict['pineapple']))      # вывод значения для заданного ключа
my_dict['apple'] = 'груша'                              # изменение значения для заданного ключа
print('Modified dictionary: ' + str(my_dict))           # вывод измененного словаря
my_dict.setdefault('pepper', 'перец')                   # добавление нового элемента в словарь
print('Last modified dictionary: ' + str(my_dict))      # вывод измененного словаря
