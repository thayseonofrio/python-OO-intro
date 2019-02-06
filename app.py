from cachorro import Cachorro
from gato import Gato

cachorro = Cachorro('Tobby', 5, 8)
gato = Gato('Lily', 2, 5)

print(cachorro.dormir())

#print(cachorro.latir())

print(gato.dormir())

#print(gato.miar())

print(cachorro.fazBarulho())
print(gato.fazBarulho())
