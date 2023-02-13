'''
Regex ou Regular Expression
De forma geral, o regex eh como se fosse uma forma de encontrar, 
substituir e extrair um unico ou uma sequencia de caracteres de 
dentro de uma string.
CARACTERE: qualquer letra, digito ou simbolo
'''
import re

hey = 'carol@gmail.com'
# Findall
result = re.findall(r"(@.{1,8}\.)", hey)
print(result)
# Search
result = re.search(r"(@.{1,8}\.)", hey)
print(result)
# Split
result = re.split(r"(@.{1,8}\.)", hey)
print(result)
# Sub
result = re.sub(r"(@.{1,8}\.)", '@hotmail.', hey)
print(result)
