def test_(a, b, c, *args, **kwargs):
    print(a, b, c)
    print(args)
    print(kwargs)
test_(5, 'computer', True, 4.7, [4, 'delta'], name1='Phantom', name2='503', name3='65.2')
print()
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n=n - 1)
print(factorial(5))