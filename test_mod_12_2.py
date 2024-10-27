import unittest
import module_12_2 as mod


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.alls_results = {}

    def setUp(self):
        self.runner_1 = mod.Runner('Usein', 10)
        self.runner_2 = mod.Runner('Andrey', 9)
        self.runner_3 = mod.Runner('Nick', 3)

    @unittest.skipIf(is_frozen, 'есты в этом кейсе заморожены')
    def test1(self):
        go = mod.Tournament(90, self.runner_1, self.runner_3)
        end = go.start()
        self.assertTrue(end[2] == 'Nick')
        self.__class__.alls_results['1й забег'] = end

    @unittest.skipIf(is_frozen, 'есты в этом кейсе заморожены')
    def test2(self):
        go = mod.Tournament(90, self.runner_2, self.runner_3)
        end = go.start()
        self.assertTrue(end[2] == 'Nick')
        self.__class__.alls_results['2й забег'] = end

    @unittest.skipIf(is_frozen, 'есты в этом кейсе заморожены')
    def test3(self):
        go = mod.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        end = go.start()
        self.assertTrue(end[3] == 'Nick')
        self.__class__.alls_results['3й забег'] = end

    @classmethod
    def tearDownClass(cls):
        for number, result in cls.alls_results.items():
            print(number, ':')
            for i, j in result.items():
                print('    ', i, j)


class RunnerTest(unittest.TestCase):

    is_frozen = False


    @unittest.skipIf(is_frozen, 'YES')
    def test_walk(self):
        runner = mod.Runner('Erzhan')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)


    @unittest.skipIf(is_frozen, 'YES')
    def test_run(self):
        runner = mod.Runner('Erzhan')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)


    @unittest.skipIf(is_frozen, 'YES')
    def test_challenge(self):
        first_runner = mod.Runner("Vova")
        secont_runner = mod.Runner('Petya')
        for _ in range(10):
            first_runner.run()
            secont_runner.walk()
            self.assertNotEqual(first_runner.distance, secont_runner.distance)


if __name__ == '__main__':
    unittest.main()
