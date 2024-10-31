import unittest
import runner_and_tournament as runner


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = runner.Runner('Usein', 10)
        self.runner_2 = runner.Runner('Andrew', 9)
        self.runner_3 = runner.Runner('Nick', 3)


    def test_round_1(self):
        # Usein and Nick
        round_1 = runner.Tournament(90, self.runner_1, self.runner_3)
        result = round_1.start()
        self.all_results[1] = result
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == 'Nick')

    def test_round_2(self):
        # Andrew and Nick
        round_2 = runner.Tournament(90, self.runner_2, self.runner_3)
        result = round_2.start()
        self.all_results[2] = result
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == 'Nick')

    def test_round_3(self):
        # all runners
        round_3 = runner.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = round_3.start()
        self.all_results[3] = result
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == 'Nick')

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print(f'{{',', '.join(f'{place}: {runner}' for place, runner in result.items()),'}')



if __name__ == '__main__':
    unittest.main()
