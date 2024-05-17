data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
                  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = 0
def calculate_structure_sum(args):
    global result
    if isinstance(args, (list, tuple, set)):
        for i in args:
            calculate_structure_sum(i)
    elif isinstance(args, int):
        result += args
    elif isinstance(args, str):
        result += len(args)
    elif isinstance(args, dict):
        for key, value in args.items():
            calculate_structure_sum(key)
            calculate_structure_sum(value)
for i in data_structure:
    calculate_structure_sum(i)
print(result)