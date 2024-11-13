import unittest
import PaperRockScissors

class TestCalc(unittest.TestCase):
    def test_game(self):
        self.assertEqual(PaperRockScissors.GamePaperRockScissors("paper", "rock"), "paper")
        self.assertEqual(PaperRockScissors.GamePaperRockScissors("paper", "paper"), "remis")
        self.assertEqual(PaperRockScissors.GamePaperRockScissors("paper", "scissors"), "scissors")
        self.assertEqual(PaperRockScissors.GamePaperRockScissors("rock", "paper"), "paper")
        self.assertEqual(PaperRockScissors.GamePaperRockScissors("scissors", "paper"), "scissors")

        with self.assertRaises(ValueError):
            PaperRockScissors.GamePaperRockScissors("fire", "paper")
            PaperRockScissors.GamePaperRockScissors(1, 3)
            PaperRockScissors.GamePaperRockScissors([], "scissors")
            PaperRockScissors.GamePaperRockScissors("rock", None)


if __name__ == '__main__':
    unittest.main()
