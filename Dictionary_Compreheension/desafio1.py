import random
from pprint import pprint


sorteios = ['sorteio1', 'sorteio2', 'sorteio3']
participantes = ['Joel', 'Jessica', 'Maria', 'Cris', 'Larissa', 'Rafael', 'Marcus', 'John']

print({sorteio: random.choice(participantes) for sorteio in sorteios})
