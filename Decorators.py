def is_prime(func):
    def wrapper(*arg):
        if func(*arg) % 2 == 0:
            print('Составное')
        else:
            print('Простое')
        return func(*arg)
    return wrapper
@is_prime
def sum_three(a, b, c):
    return a + b + c
result = sum_three(2, 3, 6)
print(result)
