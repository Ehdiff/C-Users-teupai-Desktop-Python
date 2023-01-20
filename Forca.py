#Biblioteca pra pegar as aleatoriedade 
import random
#Variáveis

#Palavras que tão na pool do jogo
palavras = ['pica', 'menina', 'etrom', 'mizera', 'ednaldo']
#--------------------------------------------------------------------------------------
#Pra me dar uma palavra aleatória da pool
palavra_aleatoria = random.choice(palavras).lower()
#--------------------------------------------------------------------------------------
#Váriavel com lista em branco pras letras corretas só o básico
letras_corretas = []
#--------------------------------------------------------------------------------------
#Número de tentativas para letras
tentativas = 6
#--------------------------------------------------------------------------------------

#Loop
while tentativas > 0:
#Mostra o número de tentativas
    print("Você tem", tentativas ,"tentativas >:)")
#Variável pra armazenar se acharao ou não a letra
    letra_encontrada = False
#Um input pro player dizer a letra
    letra = input('Adivinhe uma letra:')
    for i in range(len(palavra_aleatoria)):
        if palavra_aleatoria[i] == letra:
            letras_corretas.append(letra)
            letra_encontrada = True
#---------------------------------------------------------------------------------------

#Pra mostrar a palavra com as letras certas
    palavra_exibida = ''
    for l in palavra_aleatoria:
        if l in letras_corretas:
            palavra_exibida += l
        else:
            palavra_exibida += '_'
    print(palavra_exibida)
#----------------------------------------------------------------------------------------- 

#Pra ver se a letra foi errada e dizer 
    if not letra_encontrada:
        tentativas -= 1
#----------------------------------------------------------------------------------------- 
    if '_' not in palavra_exibida:
         print('PARABÉNS ZÉ HA HA HAAH HA HAAAAH!')
         break
#----------------------------------------------------------------------------------------- 

#Mensagenzinha pro sabe nada
if tentativas == 0:
    print('Aqui acabou filho, a palavra era,', palavra_aleatoria)

