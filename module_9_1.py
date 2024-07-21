def apply_all_func(int_list, *functions):
    results = {}
    for func_ in functions:
        results[func_.__name__] = func_(int_list)
    return results
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))