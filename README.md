<h1>Desafio Lógica Super Trunfo</h1>

<p>Este código implementa um jogo de Super Trunfo simples em Python, onde dois jogadores competem utilizando cartas com atributos (Poder, Velocidade e Defesa). O objetivo do jogo é comparar esses atributos e determinar o vencedor de cada rodada.

Componentes do código:
Classe Carta:

A classe define uma carta com três atributos: poder, velocidade, e defesa.
O método __str__ exibe as informações da carta de forma legível, mostrando o nome da carta e seus respectivos atributos.
Função comparar_cartas:

Essa função compara os atributos das cartas de dois jogadores, com base no atributo escolhido (poder, velocidade ou defesa).
A função retorna:
1 se o Jogador 1 ganhar a comparação.
2 se o Jogador 2 ganhar a comparação.
0 em caso de empate.
Função jogar:

Define o conjunto de cartas e distribui 3 cartas para cada jogador.
O jogo ocorre em 3 rodadas, onde em cada rodada:
O jogador escolhe um atributo para comparar.
A função comparar_cartas determina o vencedor da rodada.
O contador de vitórias de cada jogador é atualizado.
Ao final das rodadas, o vencedor do jogo é anunciado com base no número de vitórias.
Estrutura do jogo:

O jogo começa com as cartas sendo embaralhadas e divididas entre os dois jogadores.
Durante o jogo, os jogadores escolhem um atributo para comparar a cada rodada.
O vencedor de cada rodada recebe 1 ponto. Ao final de 3 rodadas, o jogador com mais vitórias é declarado o vencedor.
Fluxo do Jogo:
As cartas são embaralhadas e distribuídas entre os jogadores.
Cada rodada permite que o jogador escolha um atributo para comparar entre as cartas.
O resultado da rodada é decidido com base no atributo escolhido, e o vencedor é atualizado.
O jogo termina após 3 rodadas e o vencedor final é anunciado.
Este código é uma implementação básica de um jogo de Super Trunfo, e pode ser expandido para incluir mais cartas, atributos e funcionalidades.</p>
