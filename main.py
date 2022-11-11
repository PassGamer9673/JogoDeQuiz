# inicialização do programa
perguntas = [ 
   "Quem descobriu o Brasil?",
   "Qual é a capital do Ceará?",
   "Quanto é 3x71?", 
   "Qual é o propósito do significado?",
  "Quanto é 70+30?"
]
respostas_corretas = [
  "Pedro Alvares Cabral",
  "Fortaleza",
  "203",
  "Não sei",
  "100"
]
pontuacao = [
  5,
  10,
  15,
  0,
  5
]
pontos_do_jogador = 0
# aqui termina a inicialização

#começa o jogo para valer a partir daqui 
# vamos usar um laço de repetição na lista de perguntas
quantasPerguntas = len(perguntas)
for i in range(quantasPerguntas):
  print (perguntas[i])
  resposta = input()
  print ("sua resposta foi "+resposta)
  if (resposta == respostas_corretas[i] ):
    print (" ")
    print (f"Resposta correta! Você ganhou {pontuacao[i]} pontos!")
    print (" ")
    # acumulador
    pontos_do_jogador += pontuacao[i]
  else:
    print (" ")
    print ("Resposta errada")
    print (" ")
print(f"Acabou! Você fez {pontos_do_jogador}")