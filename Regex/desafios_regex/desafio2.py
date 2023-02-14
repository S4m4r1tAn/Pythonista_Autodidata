import re

frases = (
    'dev123com, developer123, dev = 123, dev = 1234, dev = 1337, dev = 9000')
result = re.findall(r"(23|00)", frases)
print(result)
