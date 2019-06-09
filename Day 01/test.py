import unittest
import Sol

class MyTestCase(unittest.TestCase):
    def test_something(self):
        list = [10, 15, 3, 7]
        k = 17
        result = Sol.solution(list, k)
        self.assertEqual(True, result)
        k = 15
        result = Sol.solution(list, k)
        self.assertEqual(False, result)
        k = 12
        result = Sol.solution(list, k)
        self.assertEqual(False, result)


if __name__ == '__main__':
    unittest.main()
