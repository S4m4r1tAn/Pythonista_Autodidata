import re

frases = (
    '2 pizzas enviadas, 1 pizza enviada, 3 pizzas enviadas')
result = re.findall(r"\d\s+\w+\s+\w+", frases)
print(result)
 