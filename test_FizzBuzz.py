import unittest
from FizzBuzz import Game


class MyTestCase(unittest.TestCase):
    def test_get_1_if_pass_1(self):
        game = Game(1)
        self.assertEqual('1', game.number_off())

    def test_get_Fizz_if_pass_3(self):
        game = Game(3)
        self.assertEqual('Fizz', game.number_off())

    def test_get_Buzz_if_pass_5(self):
        game = Game(5)
        self.assertEqual('Buzz', game.number_off())

    def test_get_FizzBuzz_if_pass_15(self):
        game = Game(15)
        self.assertEqual('FizzBuzz', game.number_off())


if __name__ == '__main__':
    unittest.main()
