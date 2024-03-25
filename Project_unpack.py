def print_params(a = 1, b = 'string', c = True):
	print(a, b, c)
print_params()
print_params(a = 'Python')
print_params(b = 25)
print_params(c = [1, 2, 3])
print()
values_list = [56, 'Prog', False]
print_params(*values_list)
values_dict = {'a': 81, 'b': 'book', 'c': [1, 2]}
print_params(**values_dict)
print()
values_list_2 = ['sport', 245]
print_params(*values_list_2, 42)