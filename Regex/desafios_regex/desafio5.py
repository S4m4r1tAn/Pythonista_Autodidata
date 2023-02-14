import re

frases = (
    'bah pular, tah encontrar, jah encontrar, nah encontrar, uai pular')
result = re.findall(r"\w+\s+encontrar", frases)
print(result)
