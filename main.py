#Pede o nome do aluno e sua nota (de 0 a 10)e , se ele tirou nota 10, mostra "Você é o bichão mesmo"
nome = input("Informe seu nome:")
nota = float(input("digite sua nota:"))


if nota ==  10:
 print(f"{nome}, você é o biichão mesmo hein!!!")
elif (nota >= 6 and nota < 10):
 print("Bom trabalho, mas se você se esforçar mais você consegue!!")
  
else:
  print("precisa estudar mais!!!!!!")
