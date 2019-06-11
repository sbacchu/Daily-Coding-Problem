import unittest
import day_2 as Sol


class MyTestCase(unittest.TestCase):
    def test_something(self):
        list = [1, 2, 3, 4, 5]
        self.assertEqual([120, 60, 40, 30, 24], Sol.solution(list))
        list = [3, 2, 1]
        self.assertEqual([2, 3, 6], Sol.solution(list))


if __name__ == '__main__':
    unittest.main()
