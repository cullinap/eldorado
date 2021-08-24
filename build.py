from src.hardware import Tangent_Assembly, Assembly_Builder
from src.tower import TowerBuilder, Tangent, DeadEnd

'''
Notes:
    - type of structure i.e.: lattice, tubular, etc..    
    - drawing number
'''
ad_assembly = Assembly_Builder.createAssembly(Tangent_Assembly)
ad_assembly.shackle = '30k'
ad_assembly.clevis = 'y-clevis'
ad_assembly.clamp = 'basic'
ad_assembly.insulator = '139kV'

t2 = TowerBuilder.createTower(Tangent, 1, 'AD + 6')
t2.add_hardware(6, ad_assembly)

for i in range(6):
    print(f'hardware assembly: {i}')
    print(t2.hardware[i].clamp)
    print(t2.hardware[i].clevis)
    print(t2.hardware[i].insulator)
    print(t2.hardware[i].shackle)
