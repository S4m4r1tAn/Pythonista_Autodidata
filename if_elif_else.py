""" Desafio 🥇
Monte o seguinte cenário usando condicionais
Você está montando um sistema para um salão de beleza para calcular o preço do corte de cabelos 
grandes que irá seguir as seguinte regras
Disclaimer the haircut values are completely ficticious, I have no ideia of actual prices
Se seu cabelo estiver com ou abaixo de 20cm você paga o valor de R$50,00
Se seu cabelo estiver entre 21cm a 30cm você paga o valor de R$70,00
Se seu cabelo estiver entre 31cm a 50cm você paga o valor de R$100,00
Acima de 50cm Favor consultar na recepção
Declare uma variável que represente o tamanho atual do cabelo
Apenas imprima na tela a mensagem apropriada, nada além disso é necesário """

cabelo = int(input('Qual o tamanho do seu cabelo: '))

if cabelo <= 20:
    print(f'Voce paga o valor de R$50,00 pelo corte se seu cabelo tiver {cabelo}cm de cumprimento.')
elif cabelo >= 21 and cabelo <= 30:
    print(f'Voce paga R$ 70,00 pelo corte se seu cabelo tiver {cabelo}cm de cumprimento.')
elif cabelo >= 31 and cabelo <= 50:
    print(f'Voce paga R$ 100,00 pelo corte se seu cabelo tiver {cabelo}cm de cumprimento.')
else:
    print('Favor consultar a Recepção!')
    