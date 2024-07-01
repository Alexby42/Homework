import inspect
string = 'Python'
number = 42
list_ = [string, number]
def func(num):
    res = num + 2
class Example():
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
example = Example('Python')

print(func.__name__)                #Вызов имени объекта
print(Example.__name__)
print(inspect.__name__)
print(type(string))                 #Вызов типа объекта, к какому классу относится
print(type(example.get_name))
print(type(inspect.isfunction))
print(dir(list_))                   #Вызов всех атрибутов и методов объекта
print(dir(example))
print(dir(example.get_name))
print(hasattr(example, 'name'))     #Проверка существования атрибута у объекта
print(getattr(example, 'name'))     #Вывод значения атрибута объекта
print(type(number) is float)        #Прверка на принадлежность объекта указанному классу
print(type(number) is int)
print(callable(number))             #Проверка "вызываемости" объекта
print(callable(func))
print(isinstance(list_, str))       #Прверка на принадлежность объекта указанному классу
print(isinstance(string, str))
print(inspect.getmodule(example))   #Прверка на принадлежностb объекта модулю
print(help(hasattr))                #Вызов справки по указанной функции
for attributes in dir(inspect):     #Вызов всех переменных, функций, классов библиотеки inspect совместно с их типами
    attrib = getattr(inspect, attributes)
    print(attributes, type(attrib))