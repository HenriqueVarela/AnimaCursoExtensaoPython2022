#comando input(): quer permitir que o usuario digite algo...
nome = input("digite seu nome:")
#pede a idade para o usuario "qual a sua idade?"
idade= int(input("digite sua idade:"))



#comando de saida.. exibir na tela 
print(f"Boa noite, seus nome é {nome}")
#exiba "sua idade é" ..."
print("Sua idade é {}".format(idade))

#se eu quiser  mostrar o dobro da idade informada ?
dobro = idade * 2

print(" o dobro da idade informada é {}". format(dobro)) 

#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber ou dirigir"
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")
else:
  print("Você é xóven ainda, xóven ainda...")

#E se eu quisessem perguntar o gênero (M = Masculino e F = Feminino)
#Mostre (...e você também precisa/precisou prestar o serviço militar obrigatório)
genero = input("informe o gênero M= Masculino, F= Feminino, O= Outros: ")
print("Você precisa ou precisou prestar o serviço militar obrigatório ")
if idade >= 18 and genero == "M":
 print("E você precisa ou precisou prestar o serviço militar obrigatório")
if idade >= 18 and genero == "F":
  print("Você não pricisa ou não precisou prestar o serviço militar obrigatório")







print("vai ser executada de qualquer jeito")
