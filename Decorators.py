def is_prime(sum_three):
    def wrapper(*arg):
        if sum_three(*arg) % 2 == 0:
            print('Составное')
        else:
            print('Простое')
        return sum_three(*arg)
    return wrapper
@is_prime
def sum_three(a, b, c):
    return a + b + c
result = sum_three(2, 3, 6)
print(result)