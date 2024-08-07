import unittest
import Run_tourn as rt
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    @classmethod
    def setUp(self):
        self.student1 = rt.Student('Усэйн', 10)
        self.student2 = rt.Student('Андрей', 9)
        self.student3 = rt.Student('Ник', 3)
    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'{key}: {value.name}')
    def test_turn1(self):
        turn1 = rt.Tournament(90, self.student1, self.student3)
        result = turn1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ник всегда должен быть последним')
        self.all_results['test_turn1'] = result
    def test_turn2(self):
        turn2 = rt.Tournament(90, self.student2, self.student3)
        result = turn2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ник всегда должен быть последним')
        self.all_results['test_turn2'] = result
    def test_turn3(self):
        turn3 = rt.Tournament(90, self.student1, self.student2, self.student3)
        result = turn3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ник всегда должен быть последним')
        self.all_results['test_turn3'] = result
if __name__ == '__main__':
    unittest.main()