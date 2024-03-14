immutable_var = tuple([1, 5.5, True, 'Python'])
print(immutable_var)
immutable_var[0] = 10
print(immutable_var)    # кортеж не поддерживает обращение (назначение) по элементам
mutable_list = ([1, 5], False, 2.3)
print(mutable_list)
mutable_list[0][1] = 8
print(mutable_list)
print((mutable_list) + (10, 30))
