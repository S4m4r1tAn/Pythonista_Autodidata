import random
from pprint import pprint

grupos = ['grupo 1', 'grupo 2', 'grupo 3']

pprint({grupo: [random.randint(1, 101) for i in range(5)] for grupo in grupos})
