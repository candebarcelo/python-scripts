import unittest
import guessing_game

class TestClass(unittest.TestCase):
    def test1(self):
        param = 1
        param2 = 10
        result = guessing_game.guessing_game(param, param2)
        self.assertIn(guessing_game.random_number, range(param,param2+1))


if __name__ == '__main__':
    unittest.main()