import re

frases = (
    '1234 encontrar, 6462 pular')
result = re.findall(r"(\d\d\d4 encontrar)", frases)
print(result)
 