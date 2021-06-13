import os
from time import sleep

#Função que cria novos jogadores!
def criaNovoJogador():
    #Recebe o nome do usuário
    nome = input("Digite o nome de usuário do jogador: ")
    #Se o jogador já estiver registrado ele avisará
    if os.path.isfile("./Jogo da Velha/" + nome + ".txt"):
        print("Jogador já existente!")
    #Se não ele cria o jogador
    else:
        arquivo = open("./Jogo da Velha/" + nome + ".txt", "w")
        arquivo.write("0\n")#Vitórias
        arquivo.write("0\n")#Derrotas
        arquivo.close()
        print(f"Jogador, {nome} registrado")
#Função de excluir jogadores!
def excluiJogador():
    #Nome a ser excluído
    nome = input("Digite o nome a ser excluído: ")
    #Verifica se o arquivo existe
    if os.path.isfile("./Jogo da Velha/" + nome + ".txt"):
        #Confirmação de excluimento
        confirmacao = input(f"Quer mesmo deletar {nome}: ")
        if confirmacao == "sim" or confirmacao == "s" or confirmacao == "S" or confirmacao == "Sim" or confirmacao == "SIM":
            print("Jogador excluído", nome)
            os.remove("./Jogo da Velha/" + nome + ".txt")
        else:
            print("Ok não vou deletar")
    #Se não existir ele da a mensagem:
    else:
        print("Jogador não existente")
#Função de ler o Histórico do jogador!       
def lerHistorico():
    nome = input("Digite o nome do jogador: ")
    #Verifica se o jogador existe
    if os.path.isfile("./Jogo da Velha/" + nome + ".txt"):
        arquivo = open("./Jogo da Velha/"+ nome + ".txt")
        historico = arquivo.readlines()
        #Histórico de vitórias e derrotas
        vitorias = int(historico[0])
        derrotas = int(historico[1])
        print("Vitórias: {}; Derrotas: {}".format(vitorias, derrotas))
    #Se não existir ele da a mensagem:
    else:
        print("Jogador não existente!")

def main():
    while True:
        #Interface
        def mostraLinha():
            print("-"*24)
        mostraLinha()
        print(".....JOGO DA VELHA......")
        mostraLinha()
        print("----------MENU----------")
        print("1 - Criar novo jogador")
        print("2 - Exibir histórico")
        print("3 - Excluir jogador")
        print("4 - Jogar")
        print("5 - Modo Torneio")
        print("6 - Sair do jogo")

        opcao = input("Escolha uma das opções: ")
        #Funções
        if opcao == "1":
            criaNovoJogador()
        elif opcao == "2":
            lerHistorico()
        elif opcao == "3":
            excluiJogador()
        elif opcao == "4":
            players()
            imprimirJogo()
            jogar()
        elif opcao == "5":
            playersTorneio()
            imprimirJogoTorneio()
            jogarTorneio()
            verificacaoGanhador1()
            imprimirFinal1()
            final1()
            verificacaoGanhador2()
            imprimirFinal2()
            final2()
        elif opcao == "6":
            confirm = input("Tem certeza que você quer sair? ")
            if confirm == "sim" or confirm == "Sim" or confirm == "SIM" or confirm == "s" or confirm == "S":
                break
            else:
                print("Ok vou continuar...")
                pass
            
def players():
    player1 = input("Digite o nome do player 1: ")
    player2 = input("Digite o nome do player 2: ")
    #Verifica se o player1 existe
    if os.path.isfile("./Jogo da Velha/" + player1 + ".txt"):
        arquivo = open("./Jogo da Velha/"+ player1 + ".txt")
        print(f"Jogador {player1} está pronto!")
    #Se não existir
    else:
        print("Jogador inexistente")
        return players()
    #Verifica se o player2 existe
    if os.path.isfile("./Jogo da Velha/" + player2 + ".txt"):
        arquivo = open("./Jogo da Velha/"+ player2 + ".txt")
        print(f"Jogador {player2} está pronto!")
    #Se não existir
    else:
        print("Jogador inexistente")
        return players()

def JogadorVencePerde(player1,player2):
    arquivoGanhou = open("./Jogo da Velha/" + player1 + ".txt", "r+")
    conteudoArquivoGanhou = arquivoGanhou.readlines()
    vitorias = int(conteudoArquivoGanhou[0]) + 1
    derrotas = conteudoArquivoGanhou[1]
    arquivoGanhou.seek(0)
    arquivoGanhou.truncate(0)
    arquivoGanhou.write(f"{vitorias} \n {derrotas}")
    arquivoGanhou.close()

    arquivoPerdeu = open("./Jogo da Velha/" + player2 + ".txt", "r+")
    conteudoArquivoPerdeu = arquivoPerdeu.readlines()
    vitorias = conteudoArquivoPerdeu[0]
    derrotas = int(conteudoArquivoPerdeu[1]) + 1
    arquivoPerdeu.seek(0)
    arquivoPerdeu.truncate(0)
    arquivoPerdeu.write(f"{vitorias}{derrotas}")
    arquivoPerdeu.close

matriz = [
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ']
    ]

def imprimirJogo():
    tabuleiro = """
          0     1     2     3     4
    0:    {}  |  {}  |  {}  |  {}  | {}
        -----------------------------
    1:    {}  |  {}  |  {}  |  {}  | {}
        -----------------------------
    2:    {}  |  {}  |  {}  |  {}  | {}
        -----------------------------
    3:    {}  |  {}  |  {}  |  {}  | {}
        -----------------------------
    4:    {}  |  {}  |  {}  |  {}  | {}
        """.format(
    matriz[0][0],matriz[0][1],matriz[0][2],matriz[0][3],matriz[0][4],
    matriz[1][0],matriz[1][1],matriz[1][2],matriz[1][3],matriz[1][4],
    matriz[2][0],matriz[2][1],matriz[2][2],matriz[2][3],matriz[2][4],
    matriz[3][0],matriz[3][1],matriz[3][2],matriz[3][3],matriz[3][4],
    matriz[4][0],matriz[4][1],matriz[4][2],matriz[4][3],matriz[4][4])
    print(tabuleiro)

def jogar():
    jogadas = 0
    #Enquanto jogadas for menor que 25 continua
    while jogadas < 26: 
        player1 = str("")
        print("Vez do player 1")
        linha = int(input("\33[33;40mDigite a linha: \33[m"))
        coluna = int(input("\33[33;40mDigite a coluna: \33[m"))
        simbolo1 = input("\33[36;40mDigite o símbolo X:\33[m ").strip().upper()[0]
        #Se o simbolo for X continua
        if simbolo1 == "X":
            pass
        #Se não ele fica pedindo pra você colocar o X
        else:
            while simbolo1 != "X":
                simbolo1 = input("Digite o símbolo X:").strip().upper()[0]

        if os.path.isfile("./Jogo da Velha/" + player1 + ".txt"):
            arquivo = open("./Jogo da Velha/"+ player1 + ".txt")
            #Escolha a linha e a coluna
            print(f"Jogador 1 escolha a {linha}, a {coluna} e o {simbolo1} ")

        matriz[linha][coluna] = simbolo1

        imprimirJogo()
        jogadas+=1
        
        #Linha player 1
        if (matriz[0][0]==simbolo1 and matriz[0][1]==simbolo1 and matriz[0][2]==simbolo1 and matriz[0][3]==simbolo1) or (matriz[0][1]==simbolo1 and matriz[0][2]==simbolo1 and matriz[0][3]==simbolo1 and matriz[0][4]==simbolo1) or (matriz[1][0]==simbolo1 and matriz[1][1]==simbolo1 and matriz[1][2]==simbolo1 and matriz[1][3]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        elif(matriz[1][1]==simbolo1 and matriz[1][2]==simbolo1 and matriz[1][3]==simbolo1 and matriz[1][4]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        elif(matriz[2][0]==simbolo1 and matriz[2][1]==simbolo1 and matriz[2][2]==simbolo1 and matriz[2][3]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        elif(matriz[2][1]==simbolo1 and matriz[2][2]==simbolo1 and matriz[2][3]==simbolo1 and matriz[2][4]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        elif(matriz[3][0]==simbolo1 and matriz[3][1]==simbolo1 and matriz[3][2]==simbolo1 and matriz[3][3]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        elif(matriz[3][1]==simbolo1 and matriz[3][2]==simbolo1 and matriz[3][3]==simbolo1 and matriz[3][4]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        elif(matriz[4][0]==simbolo1 and matriz[4][1]==simbolo1 and matriz[4][2]==simbolo1 and matriz[4][3]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        elif(matriz[4][1]==simbolo1 and matriz[4][2]==simbolo1 and matriz[4][3]==simbolo1 and matriz[4][4]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        #Coluna player 1
        elif(matriz[0][0]==simbolo1 and matriz[1][0]==simbolo1 and matriz[2][0]==simbolo1 and matriz[3][0]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        elif(matriz[1][0]==simbolo1 and matriz[2][0]==simbolo1 and matriz[3][0]==simbolo1 and matriz[4][0]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        elif(matriz[0][1]==simbolo1 and matriz[1][1]==simbolo1 and matriz[2][1]==simbolo1 and matriz[3][1]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        elif(matriz[1][1]==simbolo1 and matriz[2][1]==simbolo1 and matriz[3][1]==simbolo1 and matriz[4][1]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        elif(matriz[0][2]==simbolo1 and matriz[1][2]==simbolo1 and matriz[2][2]==simbolo1 and matriz[3][2]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        elif(matriz[1][2]==simbolo1 and matriz[2][2]==simbolo1 and matriz[3][2]==simbolo1 and matriz[4][2]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        elif(matriz[0][3]==simbolo1 and matriz[1][3]==simbolo1 and matriz[2][3]==simbolo1 and matriz[3][3]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        elif(matriz[1][3]==simbolo1 and matriz[2][3]==simbolo1 and matriz[3][3]==simbolo1 and matriz[4][3]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        elif(matriz[0][4]==simbolo1 and matriz[1][4]==simbolo1 and matriz[2][4]==simbolo1 and matriz[3][4]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        elif(matriz[1][4]==simbolo1 and matriz[2][4]==simbolo1 and matriz[3][4]==simbolo1 and matriz[4][4]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        #Diagonal player 1
        elif(matriz[0][0]==simbolo1 and matriz[1][1]==simbolo1 and matriz[2][2]==simbolo1 and matriz[3][3]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        elif(matriz[1][1]==simbolo1 and matriz[2][2]==simbolo1 and matriz[3][3]==simbolo1 and matriz[4][4]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        elif(matriz[0][4]==simbolo1 and matriz[1][3]==simbolo1 and matriz[2][2]==simbolo1 and matriz[3][1]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        elif(matriz[4][0]==simbolo1 and matriz[3][1]==simbolo1 and matriz[2][2]==simbolo1 and matriz[1][3]==simbolo1):
            matriz[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 1\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 2\33[m")
            print("-------------------------")
            return main()
        else:
            if jogadas == 25:
                print("Empate")
                return main()
            
            
        player2 = str("")
        print("Vez do player 2")
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        simbolo2 = input("\33[34;40mDigite o símbolo O: \33[m").strip().upper()[0]
        if simbolo2 == "O":
            pass
        else:
            while simbolo2 != "O":
                simbolo2 = input("Digite o símbolo O:").strip().upper()[0]

        if os.path.isfile("./Jogo da Velha/" + player2 + ".txt"):
            arquivo = open("./Jogo da Velha/"+ player2 + ".txt")
            print(f"Jogador 2 escolha a {linha}, a {coluna} e o {simbolo2}")
        
        matriz[linha][coluna] = simbolo2
        imprimirJogo()
        jogadas+=1
        #Linha player 2
        if(matriz[0][0]==simbolo2 and matriz[0][1]==simbolo2 and matriz[0][2]==simbolo2 and matriz[0][3]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[0][1]==simbolo2 and matriz[0][2]==simbolo2 and matriz[0][3]==simbolo2 and matriz[0][4]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[1][0]==simbolo2 and matriz[1][1]==simbolo2 and matriz[1][2]==simbolo2 and matriz[1][3]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[1][1]==simbolo2 and matriz[1][2]==simbolo2 and matriz[1][3]==simbolo2 and matriz[1][4]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[2][0]==simbolo2 and matriz[2][1]==simbolo2 and matriz[2][2]==simbolo2 and matriz[2][3]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[2][1]==simbolo2 and matriz[2][2]==simbolo2 and matriz[2][3]==simbolo2 and matriz[2][4]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[3][0]==simbolo2 and matriz[3][1]==simbolo2 and matriz[3][2]==simbolo2 and matriz[3][3]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[3][1]==simbolo2 and matriz[3][2]==simbolo2 and matriz[3][3]==simbolo2 and matriz[3][4]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[4][0]==simbolo2 and matriz[4][1]==simbolo2 and matriz[4][2]==simbolo2 and matriz[4][3]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[4][1]==simbolo2 and matriz[4][2]==simbolo2 and matriz[4][3]==simbolo2 and matriz[4][4]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        #Coluna player 2
        elif(matriz[0][0]==simbolo2 and matriz[1][0]==simbolo2 and matriz[2][0]==simbolo2 and matriz[3][0]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[1][0]==simbolo2 and matriz[2][0]==simbolo2 and matriz[3][0]==simbolo2 and matriz[4][0]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[0][1]==simbolo2 and matriz[1][1]==simbolo2 and matriz[2][1]==simbolo2 and matriz[3][1]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[1][1]==simbolo2 and matriz[2][1]==simbolo2 and matriz[3][1]==simbolo2 and matriz[4][1]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[0][2]==simbolo2 and matriz[1][2]==simbolo2 and matriz[2][2]==simbolo2 and matriz[3][2]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[1][2]==simbolo2 and matriz[2][2]==simbolo2 and matriz[3][2]==simbolo2 and matriz[4][2]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[0][3]==simbolo2 and matriz[1][3]==simbolo2 and matriz[2][3]==simbolo2 and matriz[3][3]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[1][3]==simbolo2 and matriz[2][3]==simbolo2 and matriz[3][3]==simbolo2 and matriz[4][3]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[0][4]==simbolo2 and matriz[1][4]==simbolo2 and matriz[2][4]==simbolo2 and matriz[3][4]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[1][4]==simbolo2 and matriz[2][4]==simbolo2 and matriz[3][4]==simbolo2 and matriz[4][4]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        #Diagonal player 2
        elif(matriz[0][0]==simbolo2 and matriz[1][1]==simbolo2 and matriz[2][2]==simbolo2 and matriz[3][3]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[1][1]==simbolo2 and matriz[2][2]==simbolo2 and matriz[3][3]==simbolo2 and matriz[4][4]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[0][4]==simbolo2 and matriz[1][3]==simbolo2 and matriz[2][2]==simbolo2 and matriz[3][1]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        elif(matriz[4][0]==simbolo2 and matriz[3][1]==simbolo2 and matriz[2][2]==simbolo2 and matriz[1][3]==simbolo2):
            matriz[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o Player 2\33[m")
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o Player 1\33[m")
            print("-------------------------")
            return main()
        else:
            if jogadas == 25:
                print("Empate")
                return main()

def playersTorneio():
    import random
    from time import sleep
    global escolhido1
    global escolhido2
    #global matriz
    global player1
    global player2
    global player3
    global player4
    print("\33[33;40mInstruções para o torneio: \33[m")
    sleep(1.5)
    print("\33[36;40mSão 4 combatentes que irão lutar entre si\33[m")
    sleep(1.5)
    print("\33[36;40mGanha quem chegar nas finais\33[m")
    player1 = input("\33[32;40mDigite o nome do primeiro combatente: \33[m")
    player2 = input("\33[32;40mDigite o nome do segundo combatente: \33[m")
    player3 = input("\33[32;40mDigite o nome do terceiro combatente: \33[m")
    player4 = input("\33[32;40mDigite o nome do quarto combatente: \33[m")
    #Verifica se o player1 existe
    if os.path.isfile("./Jogo da Velha/" + player1 + ".txt"):
        arquivo = open("./Jogo da Velha/"+ player1 + ".txt")
        pass
    #Se não existir
    else:
        print("\33[31;40mJogador inexistente\33[m")
        return players()
    #Verifica se o player2 existe
    if os.path.isfile("./Jogo da Velha/" + player2 + ".txt"):
        arquivo = open("./Jogo da Velha/"+ player2 + ".txt")
        pass
    #Se não existir
    else:
        print("\33[31;40mJogador inexistente\33[m")
        return players()
    if os.path.isfile("./Jogo da Velha/" + player3 + ".txt"):
        arquivo = open("./Jogo da Velha/"+ player3 + ".txt")
        pass
    #Se não existir
    else:
        print("\33[31;40mJogador inexistente\33[m")
        return players()
    if os.path.isfile("./Jogo da Velha/" + player4 + ".txt"):
        arquivo = open("./Jogo da Velha/"+ player4 + ".txt")
        print("Todos os jogadores estão prontos!")
    #Se não existir
    else:
        print("\33[31;40mJogador inexistente\33[m")
        return main()

    print("\33[33;40mVamos sortear o primeiro combatente:\33[m ")
    sleep(1)
    print("\33[36;40mSorteando...\33[m")
    sleep(3)
    lista = [player1, player2, player3, player4]
    escolhido1 = random.choice(lista)
    print("O primeiro combatente é \33[32;40m{}\33[m".format(escolhido1))
    sleep(1)
    print("\33[33;40mVamos sortear o segundo combatente:\33[m ")
    sleep(1)
    print("\33[36;40mSorteando...\33[m")
    sleep(3)
    lista = [player1, player2, player3, player4]
    escolhido2 = random.choice(lista)
    while escolhido2 == escolhido1:
        escolhido2 = random.choice(lista)
    print("O segundo combatente é \33[31;40m{}\33[m".format(escolhido2))
    sleep(1)
    print("Carregando...")
    sleep(3)

matrizTorneio = [
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ']
    ]

def imprimirJogoTorneio():
    tabuleiroPrimeiro = """\33[36;40m
          0     1     2     3     4
    0:    {}  |  {}  |  {}  |  {}  | {}
        -----------------------------
    1:    {}  |  {}  |  {}  |  {}  | {}
        -----------------------------
    2:    {}  |  {}  |  {}  |  {}  | {}
        -----------------------------
    3:    {}  |  {}  |  {}  |  {}  | {}
        -----------------------------
    4:    {}  |  {}  |  {}  |  {}  | {}
        \33[m""".format(
    matrizTorneio[0][0],matrizTorneio[0][1],matrizTorneio[0][2],matrizTorneio[0][3],matrizTorneio[0][4],
    matrizTorneio[1][0],matrizTorneio[1][1],matrizTorneio[1][2],matrizTorneio[1][3],matrizTorneio[1][4],
    matrizTorneio[2][0],matrizTorneio[2][1],matrizTorneio[2][2],matrizTorneio[2][3],matrizTorneio[2][4],
    matrizTorneio[3][0],matrizTorneio[3][1],matrizTorneio[3][2],matrizTorneio[3][3],matrizTorneio[3][4],
    matrizTorneio[4][0],matrizTorneio[4][1],matrizTorneio[4][2],matrizTorneio[4][3],matrizTorneio[4][4])
    print(tabuleiroPrimeiro)

def jogarTorneio():
    jogadas = 0
    #Enquanto jogadas for menor que 25 continua
    while jogadas < 26:
        print(f"Vez do combatente {escolhido1}")
        linha = int(input("\33[33;40mDigite a linha: \33[m"))
        coluna = int(input("\33[33;40mDigite a coluna: \33[m"))
        simbolo1 = input("\33[36;40mDigite o símbolo X:\33[m ").strip().upper()[0]
        #Se o simbolo for X continua
        if simbolo1 == "X":
            pass
        #Se não ele fica pedindo pra você colocar o X
        else:
            while simbolo1 != "X":
                simbolo1 = input("Digite o símbolo X:").strip().upper()[0]

        if os.path.isfile("./Jogo da Velha/" + escolhido1 + ".txt"):
            arquivo = open("./Jogo da Velha/"+ escolhido1 + ".txt")

        matrizTorneio[linha][coluna] = simbolo1

        imprimirJogoTorneio()
        jogadas+=1
        

        #Linha player 1
        if (matrizTorneio[0][0]==simbolo1 and matrizTorneio[0][1]==simbolo1 and matrizTorneio[0][2]==simbolo1 and matrizTorneio[0][3]==simbolo1) or (matrizTorneio[0][1]==simbolo1 and matrizTorneio[0][2]==simbolo1 and matrizTorneio[0][3]==simbolo1 and matrizTorneio[0][4]==simbolo1) or (matrizTorneio[1][0]==simbolo1 and matrizTorneio[1][1]==simbolo1 and matrizTorneio[1][2]==simbolo1 and matrizTorneio[1][3]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase!")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[1][1]==simbolo1 and matrizTorneio[1][2]==simbolo1 and matrizTorneio[1][3]==simbolo1 and matrizTorneio[1][4]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[2][0]==simbolo1 and matrizTorneio[2][1]==simbolo1 and matrizTorneio[2][2]==simbolo1 and matrizTorneio[2][3]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[2][1]==simbolo1 and matrizTorneio[2][2]==simbolo1 and matrizTorneio[2][3]==simbolo1 and matrizTorneio[2][4]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[3][0]==simbolo1 and matrizTorneio[3][1]==simbolo1 and matrizTorneio[3][2]==simbolo1 and matrizTorneio[3][3]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[3][1]==simbolo1 and matrizTorneio[3][2]==simbolo1 and matrizTorneio[3][3]==simbolo1 and matrizTorneio[3][4]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[4][0]==simbolo1 and matrizTorneio[4][1]==simbolo1 and matrizTorneio[4][2]==simbolo1 and matrizTorneio[4][3]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[4][1]==simbolo1 and matrizTorneio[4][2]==simbolo1 and matrizTorneio[4][3]==simbolo1 and matrizTorneio[4][4]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        #Coluna player 1
        elif(matrizTorneio[0][0]==simbolo1 and matrizTorneio[1][0]==simbolo1 and matrizTorneio[2][0]==simbolo1 and matrizTorneio[3][0]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[1][0]==simbolo1 and matrizTorneio[2][0]==simbolo1 and matrizTorneio[3][0]==simbolo1 and matrizTorneio[4][0]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[0][1]==simbolo1 and matrizTorneio[1][1]==simbolo1 and matrizTorneio[2][1]==simbolo1 and matrizTorneio[3][1]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[1][1]==simbolo1 and matrizTorneio[2][1]==simbolo1 and matrizTorneio[3][1]==simbolo1 and matrizTorneio[4][1]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[0][2]==simbolo1 and matrizTorneio[1][2]==simbolo1 and matrizTorneio[2][2]==simbolo1 and matrizTorneio[3][2]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[1][2]==simbolo1 and matrizTorneio[2][2]==simbolo1 and matrizTorneio[3][2]==simbolo1 and matrizTorneio[4][2]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[0][3]==simbolo1 and matrizTorneio[1][3]==simbolo1 and matrizTorneio[2][3]==simbolo1 and matrizTorneio[3][3]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[1][3]==simbolo1 and matrizTorneio[2][3]==simbolo1 and matrizTorneio[3][3]==simbolo1 and matrizTorneio[4][3]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[0][4]==simbolo1 and matrizTorneio[1][4]==simbolo1 and matrizTorneio[2][4]==simbolo1 and matrizTorneio[3][4]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[1][4]==simbolo1 and matrizTorneio[2][4]==simbolo1 and matrizTorneio[3][4]==simbolo1 and matrizTorneio[4][4]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        #Diagonal player 1
        elif(matrizTorneio[0][0]==simbolo1 and matrizTorneio[1][1]==simbolo1 and matrizTorneio[2][2]==simbolo1 and matrizTorneio[3][3]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[1][1]==simbolo1 and matrizTorneio[2][2]==simbolo1 and matrizTorneio[3][3]==simbolo1 and matrizTorneio[4][4]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[0][4]==simbolo1 and matrizTorneio[1][3]==simbolo1 and matrizTorneio[2][2]==simbolo1 and matrizTorneio[3][1]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[4][0]==simbolo1 and matrizTorneio[3][1]==simbolo1 and matrizTorneio[2][2]==simbolo1 and matrizTorneio[1][3]==simbolo1):
            matrizTorneio[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta = input("Continuar S/N? ")
            if pergunta == "S" or pergunta == "Sim" or pergunta == "SIM" or pergunta == "sim" or pergunta == "s":
                return verificacaoGanhador1()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        else:
            if jogadas == 25:
                print("Empate")
                return main()
            

        print(f"Vez do combatente {escolhido2}")
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        simbolo2 = input("\33[34;40mDigite o símbolo O: \33[m").strip().upper()[0]
        if simbolo2 == "O":
            pass
        else:
            while simbolo2 != "O":
                simbolo2 = input("Digite o símbolo O:").strip().upper()[0]

        if os.path.isfile("./Jogo da Velha/" + escolhido2 + ".txt"):
            arquivo = open("./Jogo da Velha/"+ escolhido2 + ".txt")
        
        matrizTorneio[linha][coluna] = simbolo2
        imprimirJogoTorneio()
        jogadas+=1
        #Linha player 2
        if(matrizTorneio[0][0]==simbolo2 and matrizTorneio[0][1]==simbolo2 and matrizTorneio[0][2]==simbolo2 and matrizTorneio[0][3]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[0][1]==simbolo2 and matrizTorneio[0][2]==simbolo2 and matrizTorneio[0][3]==simbolo2 and matrizTorneio[0][4]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[1][0]==simbolo2 and matrizTorneio[1][1]==simbolo2 and matrizTorneio[1][2]==simbolo2 and matrizTorneio[1][3]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[1][1]==simbolo2 and matrizTorneio[1][2]==simbolo2 and matrizTorneio[1][3]==simbolo2 and matrizTorneio[1][4]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[2][0]==simbolo2 and matrizTorneio[2][1]==simbolo2 and matrizTorneio[2][2]==simbolo2 and matrizTorneio[2][3]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[2][1]==simbolo2 and matrizTorneio[2][2]==simbolo2 and matrizTorneio[2][3]==simbolo2 and matrizTorneio[2][4]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[3][0]==simbolo2 and matrizTorneio[3][1]==simbolo2 and matrizTorneio[3][2]==simbolo2 and matrizTorneio[3][3]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[3][1]==simbolo2 and matrizTorneio[3][2]==simbolo2 and matrizTorneio[3][3]==simbolo2 and matrizTorneio[3][4]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[4][0]==simbolo2 and matrizTorneio[4][1]==simbolo2 and matrizTorneio[4][2]==simbolo2 and matrizTorneio[4][3]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[4][1]==simbolo2 and matrizTorneio[4][2]==simbolo2 and matrizTorneio[4][3]==simbolo2 and matrizTorneio[4][4]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        #Coluna player 2
        elif(matrizTorneio[0][0]==simbolo2 and matrizTorneio[1][0]==simbolo2 and matrizTorneio[2][0]==simbolo2 and matrizTorneio[3][0]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[1][0]==simbolo2 and matrizTorneio[2][0]==simbolo2 and matrizTorneio[3][0]==simbolo2 and matrizTorneio[4][0]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[0][1]==simbolo2 and matrizTorneio[1][1]==simbolo2 and matrizTorneio[2][1]==simbolo2 and matrizTorneio[3][1]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[1][1]==simbolo2 and matrizTorneio[2][1]==simbolo2 and matrizTorneio[3][1]==simbolo2 and matrizTorneio[4][1]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[0][2]==simbolo2 and matrizTorneio[1][2]==simbolo2 and matrizTorneio[2][2]==simbolo2 and matrizTorneio[3][2]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[1][2]==simbolo2 and matrizTorneio[2][2]==simbolo2 and matrizTorneio[3][2]==simbolo2 and matrizTorneio[4][2]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[0][3]==simbolo2 and matrizTorneio[1][3]==simbolo2 and matrizTorneio[2][3]==simbolo2 and matrizTorneio[3][3]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[1][3]==simbolo2 and matrizTorneio[2][3]==simbolo2 and matrizTorneio[3][3]==simbolo2 and matrizTorneio[4][3]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[0][4]==simbolo2 and matrizTorneio[1][4]==simbolo2 and matrizTorneio[2][4]==simbolo2 and matrizTorneio[3][4]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[1][4]==simbolo2 and matrizTorneio[2][4]==simbolo2 and matrizTorneio[3][4]==simbolo2 and matrizTorneio[4][4]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        #Diagonal player 2
        elif(matrizTorneio[0][0]==simbolo2 and matrizTorneio[1][1]==simbolo2 and matrizTorneio[2][2]==simbolo2 and matrizTorneio[3][3]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[1][1]==simbolo2 and matrizTorneio[2][2]==simbolo2 and matrizTorneio[3][3]==simbolo2 and matrizTorneio[4][4]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[0][4]==simbolo2 and matrizTorneio[1][3]==simbolo2 and matrizTorneio[2][2]==simbolo2 and matrizTorneio[3][1]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        elif(matrizTorneio[4][0]==simbolo2 and matrizTorneio[3][1]==simbolo2 and matrizTorneio[2][2]==simbolo2 and matrizTorneio[1][3]==simbolo2):
            matrizTorneio[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você está na próxima fase")
            print("-------------------------")
            pergunta2 = input("Continuar S/N? ")
            if pergunta2 == "S" or pergunta2 == "Sim" or pergunta2 == "SIM" or pergunta2 == "sim" or pergunta2 == "s":
                return verificacaoGanhador2()
            else:
                print("Ok até logo!")
                sleep(1)
                return main()
        else:
            if jogadas == 25:
                print("Empate")
                return main()

def verificacaoGanhador1():
    import random
    global escolhido3
    print(f"Vencedor da primeira partida foi {escolhido1}")
    lista = [player1, player2, player3, player4]
    escolhido3 = random.choice(lista)
    while escolhido3 == escolhido1 or escolhido3 == escolhido2:
        escolhido3 = random.choice(lista)
    print(f"O vencedor da outra partida foi {escolhido3}")
    print("-"*15)
    print("!FINAL!")
    print("-"*15)
    print(f"{escolhido1} vs {escolhido3}")
    print("-"*15)
    ir1 = input(f"{escolhido1} pronto? ")
    if ir1 == "Sim" or ir1 == "sim" or ir1 == "SIM" or ir1 == "s" or ir1 == "S":
        return final1()
    else:
        return main()
    ir3 = input(f"{escolhido3} pronto? ")
    if ir3 == "Sim" or ir3 == "sim" or ir3 == "SIM" or ir3 == "s" or ir3 == "S":
        return final1()
    else:
        return main()
    
def verificacaoGanhador2():
    import random
    global escolhido3s
    print(f"Vencedor da primeira partida {escolhido2}")
    lista = [player1, player2, player3, player4]
    escolhido3s = random.choice(lista)
    while escolhido3s == escolhido1 or escolhido3s == escolhido2:
        escolhido3s = random.choice(lista)
    print(f"O vencedor da outra partida foi {escolhido3s}")
    print("-"*15)
    print("!FINAL!")
    print("-"*15)
    print(f"{escolhido2} vs {escolhido3s}")
    print("-"*15)
    ir1 = input(f"{escolhido2} pronto?")
    ir3s = input(f"{escolhido3s} pronto?")
    if ir1 == "Sim" or ir1 == "sim" or ir1 == "SIM" or ir1 == "s" or ir1 == "S" and ir3s == "Sim" or ir3s == "sim" or ir3s == "SIM" or ir3s == "s" or ir3s == "S":
        return final2()
    else:
        return main()

matriz1 = [
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ']
    ]

def imprimirFinal1():
    tabuleiroFinal1 = """\33[36;40m
          0     1     2     3     4
    0:    {}  |  {}  |  {}  |  {}  | {}
        -----------------------------
    1:    {}  |  {}  |  {}  |  {}  | {}
        -----------------------------
    2:    {}  |  {}  |  {}  |  {}  | {}
        -----------------------------
    3:    {}  |  {}  |  {}  |  {}  | {}
        -----------------------------
    4:    {}  |  {}  |  {}  |  {}  | {}
        \33[m""".format(
    matriz1[0][0],matriz1[0][1],matriz1[0][2],matriz1[0][3],matriz1[0][4],
    matriz1[1][0],matriz1[1][1],matriz1[1][2],matriz1[1][3],matriz1[1][4],
    matriz1[2][0],matriz1[2][1],matriz1[2][2],matriz1[2][3],matriz1[2][4],
    matriz1[3][0],matriz1[3][1],matriz1[3][2],matriz1[3][3],matriz1[3][4],
    matriz1[4][0],matriz1[4][1],matriz1[4][2],matriz1[4][3],matriz1[4][4])
    print(tabuleiroFinal1)

def final1():
    jogadas = 0
    #Enquanto jogadas for menor que 25 continua
    while jogadas < 26:
        print(f"Vez do combatente {escolhido1}")
        linha = int(input("\33[33;40mDigite a linha: \33[m"))
        coluna = int(input("\33[33;40mDigite a coluna: \33[m"))
        simbolo1 = input("\33[36;40mDigite o símbolo X:\33[m ").strip().upper()[0]
        #Se o simbolo for X continua
        if simbolo1 == "X":
            pass
        #Se não ele fica pedindo pra você colocar o X
        else:
            while simbolo1 != "X":
                simbolo1 = input("Digite o símbolo X:").strip().upper()[0]

        if os.path.isfile("./Jogo da Velha/" + escolhido1 + ".txt"):
            arquivo = open("./Jogo da Velha/"+ escolhido1 + ".txt")

        matriz1[linha][coluna] = simbolo1

        imprimirFinal1()
        jogadas+=1
        
        #Linha player 1
        if (matriz1[0][0]==simbolo1 and matriz1[0][1]==simbolo1 and matriz1[0][2]==simbolo1 and matriz1[0][3]==simbolo1) or (matriz1[0][1]==simbolo1 and matriz1[0][2]==simbolo1 and matriz1[0][3]==simbolo1 and matriz1[0][4]==simbolo1) or (matriz1[1][0]==simbolo1 and matriz1[1][1]==simbolo1 and matriz1[1][2]==simbolo1 and matriz1[1][3]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[1][1]==simbolo1 and matriz1[1][2]==simbolo1 and matriz1[1][3]==simbolo1 and matriz1[1][4]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[2][0]==simbolo1 and matriz1[2][1]==simbolo1 and matriz1[2][2]==simbolo1 and matriz1[2][3]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[2][1]==simbolo1 and matriz1[2][2]==simbolo1 and matriz1[2][3]==simbolo1 and matriz1[2][4]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[3][0]==simbolo1 and matriz1[3][1]==simbolo1 and matriz1[3][2]==simbolo1 and matriz1[3][3]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[3][1]==simbolo1 and matriz1[3][2]==simbolo1 and matriz1[3][3]==simbolo1 and matriz1[3][4]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[4][0]==simbolo1 and matriz1[4][1]==simbolo1 and matriz1[4][2]==simbolo1 and matriz1[4][3]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[4][1]==simbolo1 and matriz1[4][2]==simbolo1 and matriz1[4][3]==simbolo1 and matriz1[4][4]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        #Coluna player 1
        elif(matriz1[0][0]==simbolo1 and matriz1[1][0]==simbolo1 and matriz1[2][0]==simbolo1 and matriz1[3][0]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[1][0]==simbolo1 and matriz1[2][0]==simbolo1 and matriz1[3][0]==simbolo1 and matriz1[4][0]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[0][1]==simbolo1 and matriz1[1][1]==simbolo1 and matriz1[2][1]==simbolo1 and matriz1[3][1]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[1][1]==simbolo1 and matriz1[2][1]==simbolo1 and matriz1[3][1]==simbolo1 and matriz1[4][1]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[0][2]==simbolo1 and matriz1[1][2]==simbolo1 and matriz1[2][2]==simbolo1 and matriz1[3][2]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[1][2]==simbolo1 and matriz1[2][2]==simbolo1 and matriz1[3][2]==simbolo1 and matriz1[4][2]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[0][3]==simbolo1 and matriz1[1][3]==simbolo1 and matriz1[2][3]==simbolo1 and matriz1[3][3]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[1][3]==simbolo1 and matriz1[2][3]==simbolo1 and matriz1[3][3]==simbolo1 and matriz1[4][3]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[0][4]==simbolo1 and matriz1[1][4]==simbolo1 and matriz1[2][4]==simbolo1 and matriz1[3][4]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[1][4]==simbolo1 and matriz1[2][4]==simbolo1 and matriz1[3][4]==simbolo1 and matriz1[4][4]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        #Diagonal player 1
        elif(matriz1[0][0]==simbolo1 and matriz1[1][1]==simbolo1 and matriz1[2][2]==simbolo1 and matriz1[3][3]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[1][1]==simbolo1 and matriz1[2][2]==simbolo1 and matriz1[3][3]==simbolo1 and matriz1[4][4]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[0][4]==simbolo1 and matriz1[1][3]==simbolo1 and matriz1[2][2]==simbolo1 and matriz1[3][1]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[4][0]==simbolo1 and matriz1[3][1]==simbolo1 and matriz1[2][2]==simbolo1 and matriz1[1][3]==simbolo1):
            matriz1[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido1}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        else:
            if jogadas == 25:
                print("Empate")
                print("Ninguém ganhou!")
                return main()
            

        print(f"Vez do combatente {escolhido3}")
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        simbolo2 = input("\33[34;40mDigite o símbolo O: \33[m").strip().upper()[0]
        if simbolo2 == "O":
            pass
        else:
            while simbolo2 != "O":
                simbolo2 = input("Digite o símbolo O:").strip().upper()[0]

        if os.path.isfile("./Jogo da Velha/" + escolhido3 + ".txt"):
            arquivo = open("./Jogo da Velha/"+ escolhido3 + ".txt")
        
        matriz1[linha][coluna] = simbolo2

        imprimirFinal1()
        jogadas+=1
        #Linha player 2
        if(matriz1[0][0]==simbolo2 and matriz1[0][1]==simbolo2 and matriz1[0][2]==simbolo2 and matriz1[0][3]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[0][1]==simbolo2 and matriz1[0][2]==simbolo2 and matriz1[0][3]==simbolo2 and matriz1[0][4]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[1][0]==simbolo2 and matriz1[1][1]==simbolo2 and matriz1[1][2]==simbolo2 and matriz1[1][3]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[1][1]==simbolo2 and matriz1[1][2]==simbolo2 and matriz1[1][3]==simbolo2 and matriz1[1][4]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[2][0]==simbolo2 and matriz1[2][1]==simbolo2 and matriz1[2][2]==simbolo2 and matriz1[2][3]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[2][1]==simbolo2 and matriz1[2][2]==simbolo2 and matriz1[2][3]==simbolo2 and matriz1[2][4]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[3][0]==simbolo2 and matriz1[3][1]==simbolo2 and matriz1[3][2]==simbolo2 and matriz1[3][3]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[3][1]==simbolo2 and matriz1[3][2]==simbolo2 and matriz1[3][3]==simbolo2 and matriz1[3][4]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[4][0]==simbolo2 and matriz1[4][1]==simbolo2 and matriz1[4][2]==simbolo2 and matriz1[4][3]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[4][1]==simbolo2 and matriz1[4][2]==simbolo2 and matriz1[4][3]==simbolo2 and matriz1[4][4]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        #Coluna player 2
        elif(matriz1[0][0]==simbolo2 and matriz1[1][0]==simbolo2 and matriz1[2][0]==simbolo2 and matriz1[3][0]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[1][0]==simbolo2 and matriz1[2][0]==simbolo2 and matriz1[3][0]==simbolo2 and matriz1[4][0]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[0][1]==simbolo2 and matriz1[1][1]==simbolo2 and matriz1[2][1]==simbolo2 and matriz1[3][1]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[1][1]==simbolo2 and matriz1[2][1]==simbolo2 and matriz1[3][1]==simbolo2 and matriz1[4][1]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[0][2]==simbolo2 and matriz1[1][2]==simbolo2 and matriz1[2][2]==simbolo2 and matriz1[3][2]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[1][2]==simbolo2 and matriz1[2][2]==simbolo2 and matriz1[3][2]==simbolo2 and matriz1[4][2]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[0][3]==simbolo2 and matriz1[1][3]==simbolo2 and matriz1[2][3]==simbolo2 and matriz1[3][3]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[1][3]==simbolo2 and matriz1[2][3]==simbolo2 and matriz1[3][3]==simbolo2 and matriz1[4][3]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[0][4]==simbolo2 and matriz1[1][4]==simbolo2 and matriz1[2][4]==simbolo2 and matriz1[3][4]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[1][4]==simbolo2 and matriz1[2][4]==simbolo2 and matriz1[3][4]==simbolo2 and matriz1[4][4]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        #Diagonal player 2
        elif(matriz1[0][0]==simbolo2 and matriz1[1][1]==simbolo2 and matriz1[2][2]==simbolo2 and matriz1[3][3]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[1][1]==simbolo2 and matriz1[2][2]==simbolo2 and matriz1[3][3]==simbolo2 and matriz1[4][4]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[0][4]==simbolo2 and matriz1[1][3]==simbolo2 and matriz1[2][2]==simbolo2 and matriz1[3][1]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        elif(matriz1[4][0]==simbolo2 and matriz1[3][1]==simbolo2 and matriz1[2][2]==simbolo2 and matriz1[1][3]==simbolo2):
            matriz1[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido1}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido1}\n2°Lugar-{escolhido3}")
            return main()
        else:
            if jogadas == 25:
                print("Empate")
                print("Ninguém ganhou!")
                return main()

matriz2 = [
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ']
    ]

def imprimirFinal2():
    tabuleiroFinal2 = """\33[36;40m
          0     1     2     3     4
    0:    {}  |  {}  |  {}  |  {}  | {}
        -----------------------------
    1:    {}  |  {}  |  {}  |  {}  | {}
        -----------------------------
    2:    {}  |  {}  |  {}  |  {}  | {}
        -----------------------------
    3:    {}  |  {}  |  {}  |  {}  | {}
        -----------------------------
    4:    {}  |  {}  |  {}  |  {}  | {}
        \33[m""".format(
    matriz2[0][0],matriz2[0][1],matriz2[0][2],matriz2[0][3],matriz2[0][4],
    matriz2[1][0],matriz2[1][1],matriz2[1][2],matriz2[1][3],matriz2[1][4],
    matriz2[2][0],matriz2[2][1],matriz2[2][2],matriz2[2][3],matriz2[2][4],
    matriz2[3][0],matriz2[3][1],matriz2[3][2],matriz2[3][3],matriz2[3][4],
    matriz2[4][0],matriz2[4][1],matriz2[4][2],matriz2[4][3],matriz2[4][4])
    print(tabuleiroFinal2)

def final2():
    jogadas = 0
    #Enquanto jogadas for menor que 25 continua
    while jogadas < 26:
        print(f"Vez do combatente {escolhido2}")
        linha = int(input("\33[33;40mDigite a linha: \33[m"))
        coluna = int(input("\33[33;40mDigite a coluna: \33[m"))
        simbolo1 = input("\33[36;40mDigite o símbolo X:\33[m ").strip().upper()[0]
        #Se o simbolo for X continua
        if simbolo1 == "X":
            pass
        #Se não ele fica pedindo pra você colocar o X
        else:
            while simbolo1 != "X":
                simbolo1 = input("Digite o símbolo X:").strip().upper()[0]

        if os.path.isfile("./Jogo da Velha/" + escolhido2 + ".txt"):
            arquivo = open("./Jogo da Velha/"+ escolhido2 + ".txt")

        matriz2[linha][coluna] = simbolo1

        imprimirFinal2()
        jogadas+=1
        
        #Linha player 1
        if (matriz2[0][0]==simbolo1 and matriz2[0][1]==simbolo1 and matriz2[0][2]==simbolo1 and matriz2[0][3]==simbolo1) or (matriz2[0][1]==simbolo1 and matriz2[0][2]==simbolo1 and matriz2[0][3]==simbolo1 and matriz2[0][4]==simbolo1) or (matriz2[1][0]==simbolo1 and matriz2[1][1]==simbolo1 and matriz2[1][2]==simbolo1 and matriz2[1][3]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        elif(matriz2[1][1]==simbolo1 and matriz2[1][2]==simbolo1 and matriz2[1][3]==simbolo1 and matriz2[1][4]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        elif(matriz2[2][0]==simbolo1 and matriz2[2][1]==simbolo1 and matriz2[2][2]==simbolo1 and matriz2[2][3]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        elif(matriz2[2][1]==simbolo1 and matriz2[2][2]==simbolo1 and matriz2[2][3]==simbolo1 and matriz2[2][4]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        elif(matriz2[3][0]==simbolo1 and matriz2[3][1]==simbolo1 and matriz2[3][2]==simbolo1 and matriz2[3][3]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        elif(matriz2[3][1]==simbolo1 and matriz2[3][2]==simbolo1 and matriz2[3][3]==simbolo1 and matriz2[3][4]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        elif(matriz2[4][0]==simbolo1 and matriz2[4][1]==simbolo1 and matriz2[4][2]==simbolo1 and matriz2[4][3]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        elif(matriz2[4][1]==simbolo1 and matriz2[4][2]==simbolo1 and matriz2[4][3]==simbolo1 and matriz2[4][4]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        #Coluna player 1
        elif(matriz2[0][0]==simbolo1 and matriz2[1][0]==simbolo1 and matriz2[2][0]==simbolo1 and matriz2[3][0]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        elif(matriz2[1][0]==simbolo1 and matriz2[2][0]==simbolo1 and matriz2[3][0]==simbolo1 and matriz2[4][0]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        elif(matriz2[0][1]==simbolo1 and matriz2[1][1]==simbolo1 and matriz2[2][1]==simbolo1 and matriz2[3][1]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        elif(matriz2[1][1]==simbolo1 and matriz2[2][1]==simbolo1 and matriz2[3][1]==simbolo1 and matriz2[4][1]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        elif(matriz2[0][2]==simbolo1 and matriz2[1][2]==simbolo1 and matriz2[2][2]==simbolo1 and matriz2[3][2]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        elif(matriz2[1][2]==simbolo1 and matriz2[2][2]==simbolo1 and matriz2[3][2]==simbolo1 and matriz2[4][2]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        elif(matriz2[0][3]==simbolo1 and matriz2[1][3]==simbolo1 and matriz2[2][3]==simbolo1 and matriz2[3][3]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        elif(matriz2[1][3]==simbolo1 and matriz2[2][3]==simbolo1 and matriz2[3][3]==simbolo1 and matriz2[4][3]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        elif(matriz2[0][4]==simbolo1 and matriz2[1][4]==simbolo1 and matriz2[2][4]==simbolo1 and matriz2[3][4]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        elif(matriz2[1][4]==simbolo1 and matriz2[2][4]==simbolo1 and matriz2[3][4]==simbolo1 and matriz2[4][4]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        #Diagonal player 1
        elif(matriz2[0][0]==simbolo1 and matriz2[1][1]==simbolo1 and matriz2[2][2]==simbolo1 and matriz2[3][3]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        elif(matriz2[1][1]==simbolo1 and matriz2[2][2]==simbolo1 and matriz2[3][3]==simbolo1 and matriz2[4][4]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        elif(matriz2[0][4]==simbolo1 and matriz2[1][3]==simbolo1 and matriz2[2][2]==simbolo1 and matriz2[3][1]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        elif(matriz2[4][0]==simbolo1 and matriz2[3][1]==simbolo1 and matriz2[2][2]==simbolo1 and matriz2[1][3]==simbolo1):
            matriz2[linha][coluna] = simbolo1
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido3s}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido2}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido2}\n2°Lugar-{escolhido3s}")
            return main()
        else:
            if jogadas == 25:
                print("Empate")
                print("Ninguém ganhou!")
                return main()
            

        print(f"Vez do combatente {escolhido3s}")
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        simbolo2 = input("\33[34;40mDigite o símbolo O: \33[m").strip().upper()[0]
        if simbolo2 == "O":
            pass
        else:
            while simbolo2 != "O":
                simbolo2 = input("Digite o símbolo O:").strip().upper()[0]

        if os.path.isfile("./Jogo da Velha/" + escolhido3s + ".txt"):
            arquivo = open("./Jogo da Velha/"+ escolhido3s + ".txt")
        
        matriz2[linha][coluna] = simbolo2

        imprimirFinal2()
        jogadas+=1
        #Linha player 2
        if(matriz2[0][0]==simbolo2 and matriz2[0][1]==simbolo2 and matriz2[0][2]==simbolo2 and matriz2[0][3]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[0][1]==simbolo2 and matriz2[0][2]==simbolo2 and matriz2[0][3]==simbolo2 and matriz2[0][4]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[1][0]==simbolo2 and matriz2[1][1]==simbolo2 and matriz2[1][2]==simbolo2 and matriz2[1][3]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[1][1]==simbolo2 and matriz2[1][2]==simbolo2 and matriz2[1][3]==simbolo2 and matriz2[1][4]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[2][0]==simbolo2 and matriz2[2][1]==simbolo2 and matriz2[2][2]==simbolo2 and matriz2[2][3]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[2][1]==simbolo2 and matriz2[2][2]==simbolo2 and matriz2[2][3]==simbolo2 and matriz2[2][4]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[3][0]==simbolo2 and matriz2[3][1]==simbolo2 and matriz2[3][2]==simbolo2 and matriz2[3][3]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[3][1]==simbolo2 and matriz2[3][2]==simbolo2 and matriz2[3][3]==simbolo2 and matriz2[3][4]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[4][0]==simbolo2 and matriz2[4][1]==simbolo2 and matriz2[4][2]==simbolo2 and matriz2[4][3]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[4][1]==simbolo2 and matriz2[4][2]==simbolo2 and matriz2[4][3]==simbolo2 and matriz2[4][4]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        #Coluna player 2
        elif(matriz2[0][0]==simbolo2 and matriz2[1][0]==simbolo2 and matriz2[2][0]==simbolo2 and matriz2[3][0]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[1][0]==simbolo2 and matriz2[2][0]==simbolo2 and matriz2[3][0]==simbolo2 and matriz2[4][0]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[0][1]==simbolo2 and matriz2[1][1]==simbolo2 and matriz2[2][1]==simbolo2 and matriz2[3][1]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[1][1]==simbolo2 and matriz2[2][1]==simbolo2 and matriz2[3][1]==simbolo2 and matriz2[4][1]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[0][2]==simbolo2 and matriz2[1][2]==simbolo2 and matriz2[2][2]==simbolo2 and matriz2[3][2]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[1][2]==simbolo2 and matriz2[2][2]==simbolo2 and matriz2[3][2]==simbolo2 and matriz2[4][2]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[0][3]==simbolo2 and matriz2[1][3]==simbolo2 and matriz2[2][3]==simbolo2 and matriz2[3][3]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[1][3]==simbolo2 and matriz2[2][3]==simbolo2 and matriz2[3][3]==simbolo2 and matriz2[4][3]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[0][4]==simbolo2 and matriz2[1][4]==simbolo2 and matriz2[2][4]==simbolo2 and matriz2[3][4]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[1][4]==simbolo2 and matriz2[2][4]==simbolo2 and matriz2[3][4]==simbolo2 and matriz2[4][4]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        #Diagonal player 2
        elif(matriz2[0][0]==simbolo2 and matriz2[1][1]==simbolo2 and matriz2[2][2]==simbolo2 and matriz2[3][3]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[1][1]==simbolo2 and matriz2[2][2]==simbolo2 and matriz2[3][3]==simbolo2 and matriz2[4][4]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[0][4]==simbolo2 and matriz2[1][3]==simbolo2 and matriz2[2][2]==simbolo2 and matriz2[3][1]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        elif(matriz2[4][0]==simbolo2 and matriz2[3][1]==simbolo2 and matriz2[2][2]==simbolo2 and matriz2[1][3]==simbolo2):
            matriz2[linha][coluna] = simbolo2
            print("-------------------------")
            print(f"\33[31;40mO perdedor é o combatente {escolhido2}\33[m")
            print("Sinto muito seu jogo acaba aqui")
            print("-------------------------")
            print(f"\33[32;40mO vencedor é o combatente {escolhido3s}\33[m")
            print("Parabéns você ganhou o torneio!")
            print("-------------------------")
            print(f"1°Lugar-{escolhido3s}\n2°Lugar-{escolhido2}")
            return main()
        else:
            if jogadas == 25:
                print("Empate")
                print("Ninguém ganhou!")
                return main()
main()
