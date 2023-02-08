import unittest
import random
import io
import sys
from project import main, pick, random_cpu, play

class TestRockPaperScissors(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdin = sys.stdin, io.StringIO('rock\n')

    def test_pick(self):
        result = pick()
        self.assertIn(result, ["rock", "paper", "scissor"])

    def test_random_cpu(self):
        result = random_cpu()
        self.assertIn(result, ["rock", "paper", "scissor"])

    def test_play(self):
        user = "rock"
        cpu = "scissor"
        result = play(user, cpu)
        self.assertEqual(result, "You win")

        user = "scissor"
        cpu = "paper"
        result = play(user, cpu)
        self.assertEqual(result, "You win")

        user = "paper"
        cpu = "rock"
        result = play(user, cpu)
        self.assertEqual(result, "You win")

        user = "rock"
        cpu = "rock"
        result = play(user, cpu)
        self.assertEqual(result, "Tie!")

        user = "scissor"
        cpu = "rock"
        result = play(user, cpu)
        self.assertEqual(result, "You lose")

    def tearDown(self):
        sys.stdin = self.held

if __name__ == '__main__':
    unittest.main()
