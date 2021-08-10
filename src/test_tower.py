import unittest
from tower import TowerBuilder, Tangent, DeadEnd

class Test_Tower_Build(unittest.TestCase):
    def test_tower_build(self):
        t = TowerBuilder.createTower(Tangent, 1, 'short')
        expected = 1
        self.assertEqual(t.tower_number, expected)


if __name__ == '__main__':
    unittest.main()
