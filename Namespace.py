def test_function():
    def inner_function():
          print('Я в области видимости функции test_function')
    inner_function()        #В консоль ничего не выводится
inner_function()            #Функция не определена (не найдена в глобальном пространстве имен)
