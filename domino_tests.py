import unittest
from domino import Brick, encode, decode, domino_algorithm


class TestDominoBrick(unittest.TestCase):

    def test_brick_create(self):
        brick = Brick(1, 2, 0)
        self.assertEqual(brick.state, 1)
        self.assertEqual(brick.previous, 2)
        self.assertEqual(brick.next, 0)

    def test_brick_next_state_none_falling(self):
        brick = Brick(1, 1, 1)
        brick.next_state()
        self.assertEqual(brick.state, 1)

    def test_brick_next_state_left_falling(self):
        brick = Brick(1, 2, 1)
        brick.next_state()
        self.assertEqual(brick.state, 2)

    def test_brick_next_state_right_falling(self):
        brick = Brick(1, 1, 0)
        brick.next_state()
        self.assertEqual(brick.state, 0)

    def test_brick_next_state_both_falling(self):
        brick = Brick(1, 2, 0)
        brick.next_state()
        self.assertEqual(brick.state, 1)

    def test_brick_previous_state_all_falling_left(self):
        brick = Brick(2, 2, 2)
        brick.previous_state()
        self.assertEqual(brick.state, 2)

    def test_brick_previous_state_all_falling_right(self):
        brick = Brick(0, 0, 0)
        brick.previous_state()
        self.assertEqual(brick.state, 0)

    def test_brick_previous_state_falling_left(self):
        brick = Brick(0, 1, 0)
        brick.previous_state()
        self.assertEqual(brick.state, 1)

    def test_brick_previous_state_falling_right(self):
        brick = Brick(2, 2, 1)
        brick.previous_state()
        self.assertEqual(brick.state, 1)

    def test_brick_previous_state_none_falling(self):
        brick = Brick(1, 1, 1)
        brick.previous_state()
        self.assertEqual(brick.state, 1)

    def test_brick_previous_state_both_falling_different_directions(self):
        brick = Brick(1, 2, 0)
        brick.previous_state()
        self.assertEqual(brick.state, 1)


class TestDominoEncodeDecode(unittest.TestCase):

    def test_encode_all_standing(self):
        code = encode(r'|||')
        values = [brick.state for brick in code]
        self.assertEqual(values, [1, 1, 1])

    def test_encode_left_falling_left(self):
        code = encode(r'\||')
        values = [brick.state for brick in code]
        self.assertEqual(values, [0, 1, 1])

    def test_encode_left_falling_right(self):
        code = encode(r'/||')
        values = [brick.state for brick in code]
        self.assertEqual(values, [2, 1, 1])

    def test_encode_left_and_center_falling_right(self):
        code = encode(r'//|')
        values = [brick.state for brick in code]
        self.assertEqual(values, [2, 2, 1])

    def test_encode_example(self):
        code = encode(r'||//||\||/\|')
        values = [brick.state for brick in code]
        self.assertEqual(values, [1, 1, 2, 2, 1, 1, 0, 1, 1, 2, 0, 1])

    def test_decode_all_ones(self):
        symbols = decode([Brick(1), Brick(1), Brick(1)])
        self.assertEqual(symbols, r"|||")

    def test_decode_zero_one_one(self):
        symbols = decode([Brick(0), Brick(1), Brick(1)])
        self.assertEqual(symbols, r"\||")

    def test_decode_two_one_one(self):
        symbols = decode([Brick(2), Brick(1), Brick(1)])
        self.assertEqual(symbols, r"/||")

    def test_decode_two_one_two(self):
        symbols = decode([Brick(2), Brick(1), Brick(2)])
        self.assertEqual(symbols, r"/|/")

    def test_decode_two_two_two(self):
        symbols = decode([Brick(2), Brick(2), Brick(2)])
        self.assertEqual(symbols, r"///")

    def test_decode_two_zero_two(self):
        symbols = decode([Brick(2), Brick(0), Brick(2)])
        self.assertEqual(symbols, r"/\/")


class TestDominoAlgorithm(unittest.TestCase):

    def test_algorithm_forward_one_iteration(self):
        result = domino_algorithm(r"|//|||", "forward", 1)
        self.assertEqual(result, r"|///||")

    def test_algorithm_forward_two_iterations(self):
        result = domino_algorithm(r"|//|||", "forward", 2)
        self.assertEqual(result, r"|////|")

    def test_algorithm_forward_two_iterations_two_simultaneous_actions(self):
        result = domino_algorithm(r"|//|||||\||", "forward", 2)
        self.assertEqual(result, r"|////|\\\||")

    def test_algorithm_forward_given_example(self):
        result = domino_algorithm(r"||//||\||/\|", "forward", 1)
        self.assertEqual(result, r"||///\\||/\|")

    def test_algorithm_backward_one_iteration(self):
        result = domino_algorithm(r"|///||", "backward", 1)
        self.assertEqual(result, r"|//|||")

    def test_algorithm_backward_two_iterations(self):
        result = domino_algorithm(r"|////|", "backward", 2)
        self.assertEqual(result, r"|//|||")

    def test_algorithm_backward_two_iterations_two_simultaneous_actions(self):
        result = domino_algorithm(r"|////|\\\||", "backward", 2)
        self.assertEqual(result, r"|//|||||\||")

    def test_algorithm_backward_two_iterations_given_example(self):
        result = domino_algorithm(r"||////\\\|////|", "backward", 2)
        self.assertEqual(result, r"||//||||\|//|||")


if __name__ == "__main__":
    unittest.main()