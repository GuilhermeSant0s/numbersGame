import random


numero_aleatorio = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Digite um número entre 1 e 100: "))
    
    if palpite == numero_aleatorio:
        print("Parabéns! Você acertou!")
        break
    elif palpite < numero_aleatorio:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
    
    tentativas += 1
    
    print("Tentativa", tentativas)
