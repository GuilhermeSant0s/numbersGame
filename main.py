# Importa a biblioteca random para gerar um número aleatório
import random

# Gera um número aleatório entre 1 e 100
numero_aleatorio = random.randint(1, 100)

# Inicializa a contagem de tentativas
tentativas = 0

# Loop while para permitir que o usuário faça várias tentativas de adivinhar o número
while True:
    # Pede para o usuário digitar um número entre 1 e 100
    palpite = int(input("Digite um número entre 1 e 100: "))
    
    # Verifica se o palpite do usuário é igual ao número aleatório gerado
    if palpite == numero_aleatorio:
        # Imprime uma mensagem de acerto e sai do loop
        print("Parabéns! Você acertou!")
        break
```
# Importa a biblioteca random para gerar um número aleatório
import random

# Gera um número aleatório entre 1 e 100
numero_aleatorio = random.randint(1, 100)

# Inicializa a contagem de tentativas
tentativas = 0

# Loop while para permitir que o usuário faça várias tentativas de adivinhar o número
while True:
    # Pede para o usuário digitar um número entre 1 e 100
    palpite = int(input("Digite um número entre 1 e 100: "))
    
    # Verifica se o palpite do usuário é igual ao número aleatório gerado
    if palpite == numero_aleatorio:
        # Imprime uma mensagem de acerto e sai do loop
        print("Parabéns! Você acertou!")
        break
    # Se o palpite for menor que o número aleatório, informa para o usuário tentar um número maior
    elif palpite < numero_aleatorio:
        print("Tente um número maior.")
    # Se o palpite for maior que o número aleatório, informa para o usuário tentar um número menor
    else:
        print("Tente um número menor.")
    
    # Incrementa a contagem de tentativas
    tentativas += 1
    
    # Imprime a tentativa atual
    print("Tentativa", tentativas)```
