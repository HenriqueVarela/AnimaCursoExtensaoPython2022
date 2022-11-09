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
  
  #Pede o nome do aluno e sua nota (de 0 a 10)e , se ele tirou nota 10, mostra "Você é o bichão mesmo"
nome = input("Informe seu nome:")
nota = float(input("digite sua nota:"))


if nota ==  10:
 print(f"{nome}, você é o biichão mesmo hein!!!")
elif (nota >= 6 and nota < 10):
 print("Bom trabalho, mas se você se esforçar mais você consegue!!")
  
else:
  print("precisa estudar mais!!!!!!")






print("vai ser executada de qualquer jeito")