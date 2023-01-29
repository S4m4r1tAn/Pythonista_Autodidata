''' Desafio 🥇

Quero que você defina as seguintes variáveis, inicialmente todas como False, a ideia aqui não é de se 
importar com os valores dentro dessas variáveis, mas sim como montar condicionais.

possui_passaporte = False
passagem_comprada = False
menor_de_idade = False

E Crie as seguintes condições usando o que acabou de ver e imprima o resultado na tela. Tente fazer 
cada condição e depois veja a solução no final deste aula.

1) Uma pessoa só pode viajar se possuir  passaporte e tiver a passagem comprada e não for menor de idade

2) Uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada e não for menor de idade

3) Uma pessoa só pode viajar se não possuir passaporte ou tiver a passagem comprada e não for menor de idade

4) Uma pessoa não pode viajar se não possuir passaporte ou não tiver a passagem comprada e for menor de idade '''

possui_passaporte = False
passagem_comprada = False
menor_de_idade = False

print(possui_passaporte and passagem_comprada) and not (menor_de_idade)

print(possui_passaporte or passagem_comprada and not menor_de_idade)

print(not possui_passaporte or passagem_comprada and not menor_de_idade)

print(not possui_passaporte and not passagem_comprada) and (menor_de_idade)