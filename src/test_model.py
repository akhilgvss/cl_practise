import unittest
import model

class TestModel(unittest.TestCase):

    def test_add(self):
        l=[i for i in range(-2,3)]
        for i in l:
            self.assertEqual(model.square(i), i**2)

if __name__ == '__main__':
    unittest.main()