import m12
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        first = m12.Runner('Tor')
        for i in range(10):
            first.walk()
        self.assertEqual(first.distance, 50)

    def test_run(self):
        second = m12.Runner('Rot')
        for i in range(10):
            second.run()
        self.assertEqual(second.distance, 100)

    def test_challenge(self):
        first = m12.Runner('Tor')
        second = m12.Runner('Rot')
        for i in range(10):
            first.walk()
            second.run()
        self.assertNotEqual(first.distance, second.distance)

if __name__ == '__main__':
    unittest.main()