import unittest
from tower import TowerBuilder, Tangent, DeadEnd
from hardware import Assembly_Builder, Tangent_Assembly


class Test_Tower_Build(unittest.TestCase):
    def test_tower_build(self):
        t1 = TowerBuilder.createTower(Tangent, 1, 'short')
        a = Assembly_Builder.createAssembly(Tangent_Assembly)
        t1.hardware = a

        t1.hardware.shackle = 'AS-30BNK'
        t1.hardware.insulator = 'white'
        t1.hardware.clevis = 'wye'
        t1.hardware.clamp = 'hubbell'
        
        shackle_exp = 'AS-30BNK'
        insulator_exp = 'white'
        clevis_exp = 'wye'
        clamp_exp = 'hubbell'

        self.assertEqual(t1.hardware.shackle, shackle_exp)
        self.assertEqual(t1.hardware.insulator, insulator_exp)
        self.assertEqual(t1.hardware.clevis, clevis_exp)
        self.assertEqual(t1.hardware.clamp, clamp_exp)


if __name__ == '__main__':
    unittest.main()
