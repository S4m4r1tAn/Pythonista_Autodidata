import re

frases = (
    '13.35.86, 22.36.77, 53.12.34')
result = re.findall(r"(\d{2}\.\d{2}\.\d{2})", frases)
print(result)
