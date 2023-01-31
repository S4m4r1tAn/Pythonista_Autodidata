import json
from pathlib import Path

pikachu_json = Path('pikachu.json').read_text()
resultado = json.loads(pikachu_json)
print(resultado['abilities'][1]['ability']['name'].upper())