from src.hardware import Tangent_Assembly, Assembly_Builder, DeadEnd_Assembly
from src.tower import TowerBuilder, Tangent, DeadEnd

'''
Notes:
    - type of structure i.e.: lattice, tubular, etc..    
    - drawing number
    - The idea is you make XX number of tower types and YY assembly types
    and you can combine in them in various combinations
    - For example tangent is a class AD may be an instance of the 
    tangent class 
    - How do I create an tower number instance of the Tangent instance?
'''
ad_assembly = Assembly_Builder.createAssembly(Tangent_Assembly)
ad_assembly.shackle = '30k'
ad_assembly.clevis = 'y-clevis'
ad_assembly.clamp = 'basic'
ad_assembly.insulator = '139kV'

de_assembly = Assembly_Builder.createAssembly(DeadEnd_Assembly)
de_assembly.shackle = '60k'
de_assembly.clevis = 'y-clevis'
de_assembly.clamp = 'de_clamp'
de_assembly.insulator = '138kV'

t2 = TowerBuilder.createTower(Tangent, 1, 'AD + 6')
t2.add_hardware(6, ad_assembly)

t3 = TowerBuilder.createTower(DeadEnd, 2, 'DD + 4')
t3.add_hardware(6, de_assembly)

for i in range(6):
    print(f'hardware assembly: {i}')
    print(t2.hardware[i].clamp)
    print(t2.hardware[i].clevis)
    print(t2.hardware[i].insulator)
    print(t2.hardware[i].shackle)

    print(t3.hardware[i].clamp)
    print(t3.hardware[i].clevis)
    print(t3.hardware[i].insulator)
    print(t3.hardware[i].shackle)




    
