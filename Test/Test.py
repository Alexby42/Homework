import main
import unittest
class Test(unittest.TestCase):
    def test1(self):
        x = main.Student('Greg')
        [x.walk() for _ in range(9)]
        self.assertEqual(x.walk(), 500, f'Дистанции не равны: {x.distance} != 500')
    def test2(self):
        y = main.Student('Paul')
        [y.run() for _ in range(9)]
        self.assertEqual(y.run(), 1000, f'Дистанции не равны: {y.distance} != 1000')
    def test3(self):
        x = main.Student('Greg')
        y = main.Student('Paul')
        [x.walk() for _ in range(9)]
        [y.run() for _ in range(9)]
        self.assertLess(y.run(), x.walk(), f'{y} должен преодолеть дистанцию больше, чем {x}')
if __name__ == '__main__':
    unittest.main()
