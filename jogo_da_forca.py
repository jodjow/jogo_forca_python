
#jogo da forca

secreto = 'perfume'
digitadas = [] #lista vazia para armazenar letras digitadas
chances = 5


while True:
    if chances <=0:
        print('esgotou as chances')
        break

    letra = input('digite uma letra: ')

    if len(letra) > 1: # verificacao para digitar somente uma letra
        print('só pode digitar uma letra')
        continue
    digitadas.append(letra) #armazenando letras digitadas

    if letra in secreto:
     print(f'a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'nao existe "{letra}" na palavra secreta.')
        digitadas.pop() # exclui letra errada que o usuario digitou

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print(f' a palavra secreta é: {secreto_temporario}')
        break
    else:
        print(f' a palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
    print(f'voce ainda tem {chances} chances')
    print() # print para pular linha