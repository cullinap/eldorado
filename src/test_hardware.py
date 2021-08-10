import unittest
from hardware import Assembly_Builder, Tangent_Assembly


class Test_Tower_Build(unittest.TestCase):
    def test_tower_build(self):
        a = Assembly_Builder.createAssembly(Tangent_Assembly)
        a.clamp = 'basic'
        expected = 'basic'
        self.assertEqual(a.clamp, expected)


if __name__ == '__main__':
    unittest.main()
