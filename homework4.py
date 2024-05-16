immutable_var = tuple([1, 5.5, True, 'Python'])     # переменная с кортежем из различных типов элементов
print(immutable_var)                                # вывод кортежа
#immutable_var[0] = 10                              # попытка изменения элемента кортежа
#print(immutable_var)                               # кортеж не поддерживает обращение (назначение) по элементам
mutable_list = [1, 5, False, 2.3]                   # переменная со списком из различных типов элементов
print(mutable_list)                                 # вывод списка переменной
mutable_list[3] = 'Python'                          # изменение элемента списка
print(mutable_list)                                 # вывод измененного списка
