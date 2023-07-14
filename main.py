import os
from datetime import datetime

data_e_hora_atuais = datetime.now()
data_nota_fiscal = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

preço = 0
quantidade = 0
preçoProduto = 0
preçoTotal = 0
nomes = []
preços = []

continua = 's'
while continua == 's':

    nome = input ("Qual Produto você está levando? \n")
    preço = int (input ("Qual o preço de tabela do produto? \n"))
    quantidade = int (input ("Informe a quantidade do produto. \n"))
    nomes.append(nome)  

    if quantidade >= 1 and quantidade <= 10:
        preço = preço - preço * 5 / 100
    elif quantidade >= 11 and quantidade <= 20:
        preço = preço - preço * 7 / 100
    elif quantidade > 20:
        preço = preço - preço * 10 / 100

    preçoProduto = preço * quantidade
    preçoTotal += preçoProduto
    preços.append(preçoProduto)

    print ("O preço de venda foi: ", preço)
    print ("O valor a pagar por esse produto é: ", preçoProduto)

    continua = input ("Deseja adicionar outro produto? (responda com 's' para sim e 'n' para não) \n")
    
    os.system("cls")


print ("O valor total da sua compra é: ", preçoTotal)


nota = input ("Deseja a sua nota fiscal? (responda com 's' para sim e 'n' para não) \n")
if nota == 's':
    print ("NOTA FISCAL - MERCADINHO DO SEU DURVAL")
    print ("********************")
    for i in range (len(nomes)):
        print(nomes [i]," R$", preços[i])
    print(data_nota_fiscal)
if nota == 'n':
    print ('Obrigado por comprar no mercado do seu durval, volte sempre!')