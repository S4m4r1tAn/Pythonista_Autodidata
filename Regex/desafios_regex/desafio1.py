import re

frase = 'Ola, sou uma frase simples.'
result = re.findall(r'simples', frase)
print(result)
