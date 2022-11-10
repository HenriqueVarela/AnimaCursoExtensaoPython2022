#criação de funções

preco = 1999.90

#Calcular apenas 5% de imposto, guardar na variavel imposto e exibir na tela
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#Criar uma função calcular_imposto() que calcular um imposto de 5% e retorna a quem pediu...
#Isso é a declaração da função (Como ela funciona)
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

#Aqui é o uso... aqui é imposto a calcular.. e exibir na tela
preco = 299
imposto = calcular_imposto(preco)
print(imposto)

print(preco)
preco_produto = 100
print(preco_produto)
    


#Agora calcular o imposto aliquota agora é 7%

valores =  [1.99, 24.50, 78.27, 1515.5]
#se quiser calcular o imposto deste quatro valores... e exibir na tela assim "o imposto de ....... é " (1o. preço 2o preço. imposto )
for valor in valores:
 print(f"o imposto de {valor} é {calcular_imposto(valor)}")


#declarar uma função clacular_imposto_aliquota que recebe dois parâmetros: preço do produto e a alíquota do imposto a ser aplicada e retorna o imposto calculado. Se aliquota não for informada, utilize 7% como padrão.
def calcular_imposto_aliquota(valor, aliquota=7):
  imposto = valor * aliquota / 100
  return imposto

for valor in valores:
 print(f"o imposto de {valor} é {calcular_imposto_aliquota(valor)}")

for valor in valores:
 print(f"o imposto de {valor} é {calcular_imposto_aliquota(valor, 7)}")

# e se agora for 10% ?
for valor in valores:
 print(f"o imposto de {valor} é {calcular_imposto_aliquota(valor, 10)}")
  
