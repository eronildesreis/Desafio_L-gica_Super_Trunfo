import random

# Definindo a classe Carta
class Carta:
    def __init__(self, nome, poder, velocidade, defesa):
        self.nome = nome
        self.poder = poder
        self.velocidade = velocidade
        self.defesa = defesa

    def __str__(self):
        return f'{self.nome} (Poder: {self.poder}, Velocidade: {self.velocidade}, Defesa: {self.defesa})'

# Função para comparar as cartas
def comparar_cartas(carta_jogador1, carta_jogador2, atributo_escolhido):
    atributo1 = getattr(carta_jogador1, atributo_escolhido)
    atributo2 = getattr(carta_jogador2, atributo_escolhido)
    
    print(f"\nAtributo escolhido: {atributo_escolhido.capitalize()}")
    print(f"{carta_jogador1.nome} tem {atributo_escolhido.capitalize()}: {atributo1}")
    print(f"{carta_jogador2.nome} tem {atributo_escolhido.capitalize()}: {atributo2}")
    
    if atributo1 > atributo2:
        return 1  # Jogador 1 ganha
    elif atributo2 > atributo1:
        return 2  # Jogador 2 ganha
    else:
        return 0  # Empate

# Função para jogar o Super Trunfo
def jogar():
    # Cartas do Super Trunfo
    cartas = [
        Carta("Dragão", 90, 80, 70),
        Carta("Fênix", 85, 95, 75),
        Carta("Unicórnio", 70, 85, 90),
        Carta("Leão", 80, 70, 80),
        Carta("Grifo", 75, 60, 100)
    ]
    
    # Embaralhando as cartas
    random.shuffle(cartas)

    # Dividindo as cartas entre os dois jogadores
    jogador1_cartas = cartas[:3]
    jogador2_cartas = cartas[3:]
    
    # Início do jogo
    print("Bem-vindo ao Super Trunfo!")
    
    vitorias_jogador1 = 0
    vitorias_jogador2 = 0
    empates = 0

    # Jogar 3 rodadas
    for i in range(3):
        print(f"\nRodada {i+1}:")
        
        carta_jogador1 = jogador1_cartas[i]
        carta_jogador2 = jogador2_cartas[i]

        print(f"\nJogador 1: {carta_jogador1}")
        print(f"Jogador 2: {carta_jogador2}")
        
        # Perguntar qual atributo o jogador quer comparar
        print("\nEscolha o atributo para comparar: Poder, Velocidade ou Defesa.")
        atributo_escolhido = input("Digite o atributo: ").strip().lower()

        # Verificar se o atributo é válido
        while atributo_escolhido not in ['poder', 'velocidade', 'defesa']:
            print("Atributo inválido! Escolha entre 'Poder', 'Velocidade' ou 'Defesa'.")
            atributo_escolhido = input("Digite o atributo: ").strip().lower()

        # Comparar as cartas
        resultado = comparar_cartas(carta_jogador1, carta_jogador2, atributo_escolhido)
        
        if resultado == 1:
            print("Jogador 1 ganhou a rodada!")
            vitorias_jogador1 += 1
        elif resultado == 2:
            print("Jogador 2 ganhou a rodada!")
            vitorias_jogador2 += 1
        else:
            print("Empate na rodada!")
            empates += 1
    
    # Resultado final do jogo
    print("\nResultado final do jogo:")
    print(f"Jogador 1 venceu {vitorias_jogador1} rodadas.")
    print(f"Jogador 2 venceu {vitorias_jogador2} rodadas.")
    print(f"Houve {empates} empate(s).")

    if vitorias_jogador1 > vitorias_jogador2:
        print("\nJogador 1 é o vencedor do Super Trunfo!")
    elif vitorias_jogador2 > vitorias_jogador1:
        print("\nJogador 2 é o vencedor do Super Trunfo!")
    else:
        print("\nO jogo terminou em empate!")

# Iniciar o jogo
if __name__ == "__main__":
    jogar()