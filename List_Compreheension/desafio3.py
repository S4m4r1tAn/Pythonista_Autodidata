from pprint import pprint
from termcolor import colored

participantes = ['Joel', 'Jessica', 'Maria', 'Cris', 'Larissa', 'Rafael', 'Marcus', 'John']
pagamento_realizado = ['Joel', 'Jessica', 'Maria', 'Cris']

print('**RESULTADO 1**')
resultado = [colored(i + ' PAGO', 'green', attrs=['bold']) if i in pagamento_realizado else colored(i + ' NAO PAGO', 'red', attrs=['bold']) for i in participantes]
for r in resultado:
    print(r)
print('**' *18)

print('**RESULTADO 2**')   
pprint([i + ' PAGO' if i in pagamento_realizado else i + ' NAO PAGO' for i in participantes])
print('**' *18)

print('**RESULTADO 3**')
def pagadores(i):
    return i + ' PAGO'
pprint([pagadores(i) if i in pagamento_realizado else i for i in participantes])
print('**' *18)
