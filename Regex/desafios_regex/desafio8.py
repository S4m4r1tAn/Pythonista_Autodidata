import re

frases = (
    'pqrstuv encontrar, wxyz pular, abcdefg pular')
result = re.findall(r"(\w+\s+encontrar?)", frases)
print(result)
 