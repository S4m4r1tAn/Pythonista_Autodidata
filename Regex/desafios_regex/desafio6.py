import re

frases = (
    '(123)1234-1235 encontrar, (123)1234-1235 encontrar, (129)1234-1235 pular, (129)1234-1235 pular')
result = re.findall(r"[(]\d{3}[)]\d{4}[-]\d{4} encontrar", frases)
# result = re.findall(r"[(]\d{2}3[)]\d{4}[-]\d{4}", frases)
print(result)
