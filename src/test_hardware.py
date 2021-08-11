import unittest
from hardware import Assembly_Builder, Tangent_Assembly


class Test_Tower_Build(unittest.TestCase):
    def test_tower_build(self):
        a = Assembly_Builder.createAssembly(Tangent_Assembly)
        a.shackle = 'AS-30BNK'
        a.insulator = 'white'
        a.clevis = 'wye'
        a.clamp = 'hubbell'
        shackle_exp = 'AS-30BNK'
        insulator_exp = 'white'
        clevis_exp = 'wye'
        clamp_exp = 'hubbell'
        self.assertEqual(a.shackle, shackle_exp)
        self.assertEqual(a.insulator, insulator_exp)
        self.assertEqual(a.clevis, clevis_exp)
        self.assertEqual(a.clamp, clamp_exp)


if __name__ == '__main__':
    unittest.main()
