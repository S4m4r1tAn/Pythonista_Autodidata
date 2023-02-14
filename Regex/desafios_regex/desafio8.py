import re

frases = (
    'pqrstuv encontrar, wxyz pular, abcdefg pular')
result = re.findall(r"(\w+ encontrar)", frases)
print(result)
 