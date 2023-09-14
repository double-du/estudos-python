# from faker import Faker
import random

def jogar():
    print('****************************************************')
    print('************ Bem vindo ao jogo de forca ************')
    print('****************************************************')

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

    # empty_spaces = []
    # for letra in word:
    # empty_spaces.append('_' for letra in word) 
    empty_spaces = ['_' for letra in word] #A lista é forma colocando um caracter para cada letra da palavra
    #  Isso aqui é conhecido como List Comprehension
    
    hang = False
    win_word = False
    chances = 6

    while(not hang and not win_word):
        for caracter in empty_spaces:
            print(caracter, end = ' ')

        play_char = input('\n\nChute uma letra: ')
        play_char = play_char.strip().upper()
        index = 0
        find = False
        
        for letra in word: # Funciona quase como um Foreach do PHP
            if(play_char == letra):
                print('Encontrei a letra {} na posicao {}'.format(letra, index))
                empty_spaces[index] = letra
                find = True
            index += 1

        if(not find):
            chances -=1
            print("Você tem {} chances".format(chances))
        
        if("_" not in empty_spaces):
            win_word = True
        
        if(chances == 0):
            hang = True
    # Fim código

    if(win_word):
        print('PRABÉNS! Você venceu\nA palavra é {}'.format(word))

    if(hang):
        print('Você perdeu :(\nA palavra era {}'.format(word))

    print('****************************************************')
    print('******************** GAME OVER *********************')
    print('****************************************************')

if(__name__ == '__main__'):
    jogar()