# from faker import Faker
import random

def imprime_mensagem(mensagem):
    if(mensagem == 'abertura'):
        print('****************************************************')
        print('************ Bem vindo ao jogo de forca ************')
        print('****************************************************')
    if(mensagem == 'encerramento'):
        print('****************************************************')
        print('******************** GAME OVER *********************')
        print('****************************************************')

def seleciona_palavra_da_forca():
    # Código aqui
    # Aqui temos um gerador automático
    # fake = Faker('pt_BR')
    # word = fake.state()
    
    # Aqui temos uma palavra fixa
    # word = "banana" 

    arquivo = open('./palavras.txt', 'r')
    palavras_disponiveis = arquivo.readlines()
    
    arquivo.close()
    
    numero_aleatorio = random.randrange(0, len(palavras_disponiveis))
    word = palavras_disponiveis[numero_aleatorio].upper().strip()  
    return word  

def resolve_espacos_vazios(palavra):
    # espacos_vazios = []
    # for letra in word:
    # espacos_vazios.append('_' for letra in word) 
    espacos_vazios = ['_' for letra in palavra] #A lista é forma colocando um caracter para cada letra da palavra
    #  Isso aqui é conhecido como List Comprehension
    return espacos_vazios

def mensagem_final(encontrou_palavra, enforcado, palavra): 
    if(encontrou_palavra):
        print('PRABÉNS! Você venceu\nA palavra é {}'.format(palavra))

    if(enforcado):
        print('Você perdeu :(\nA palavra era {}'.format(palavra))

def jogar():
    imprime_mensagem('abertura')

    word = seleciona_palavra_da_forca()
    espacos_vazios = resolve_espacos_vazios(word)
    hang = False
    acertou_palavra = False
    chances = 6

    while(not hang and not acertou_palavra):
        for caracter in espacos_vazios:
            print(caracter, end = ' ')

        letra_chutada = input('\n\nChute uma letra: ')
        letra_chutada = letra_chutada.strip().upper()
        index = 0
        encontrou = False
        
        for letra in word: # Funciona quase como um Foreach do PHP
            if(letra_chutada == letra):
                print('Encontrei a letra {} na posicao {}'.format(letra, index))
                espacos_vazios[index] = letra
                encontrou = True
            index += 1

        if(not encontrou):
            chances -=1
            print("Você tem {} chances".format(chances))
        
        if("_" not in espacos_vazios):
            acertou_palavra = True
        
        if(chances == 0):
            hang = True
    
    mensagem_final(acertou_palavra, hang, word)

    imprime_mensagem('encerramento')
    

if(__name__ == '__main__'):
    jogar()