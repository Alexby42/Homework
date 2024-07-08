import main
import unittest
class Test(unittest.TestCase):
    def test1(self):
        x = main.Student('Greg')
        for _ in range(10):
            x.walk()
        self.assertEqual(x.distance, 50, f'Дистанции не равны: {x.distance} != 500')
    def test2(self):
        y = main.Student('Paul')
        for _ in range(10):
            y.run()
        self.assertEqual(y.distance, 100, f'Дистанции не равны: {y.distance} != 1000')
    def test3(self):
        x = main.Student('Greg')
        y = main.Student('Paul')
        for _ in range(10):
            x.walk()
            y.run()
        self.assertGreater(y.distance, x.distance, f'{y} должен преодолеть дистанцию больше, чем {x}')
if __name__ == '__main__':
    unittest.main()
