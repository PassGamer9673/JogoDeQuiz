# inicialização do programa
perguntas = ["Quem descobriu o Brasil?","Qual é a capital do Ceará?","Quanto é 3x71?", "Qual é o propósito do significado?"]
respostas_corretas = ["Pedro Alvares Cabral","Fortaleza","203","Não sei"]
# aqui termina a inicialização

#começa o jogo para valer a partir daqui 
# vamos usar um laço de repetição na lista de perguntas
for i in range(4):
  print (perguntas[i])
  resposta = input()
  print ("sua resposta foi "+resposta)
  if (resposta == respostas_corretas[i] ):
    print (" ")
    print ("Resposta correta!")
    print (" ")
  else:
    print (" ")
    print ("Resposta errada")
    print (" ")
