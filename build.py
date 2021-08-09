from src.hardware import Tangent_Assembly
from src.tower import TowerBuilder, Tangent, DeadEnd

t1 = TowerBuilder.createTower(Tangent, 1, 'short')
t1.ahead = 2
t1.hardware = Tangent_Assembly(1)
t1.hardware.clamp = 'shoe'

print(t1.hardware.clamp)
print(t1.ahead)
print(t1.legs)


