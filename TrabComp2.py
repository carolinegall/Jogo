# Propriedades do documento

'''Sudoku é um jogo Sudoku baseado na lógica de colocação de números.'''
__autor__ = 'Caroline de oliveira gall'
__copyright__ = 'Copyright_2021'
__créditos__ = __autor__
__license__ = 'CG'
__versão__ = '1.0.0'
__maintainer__ = 'Caroline_Gall' # Responsável por manter o programa funcionando
__email__ = 'caroline.gall@poli.ufrj.br'
__status__ = 'Produção'

from validSudoku import *
from tela import *
from tabuleiro import *
from jogador import *
from mecanicas import *

class Sudoku(Mecanicas): #Ira receber as mecanicas do jogo

    def __init__(self, jogador = 1): #Receber o parâmetro de jogadores, sempre 1.
        passar
    def solucao(self, solve): #Mostrara a solução caso seja essencial
        passar
    def ganhou(self, find_empty): #Ira analisar e apresenta uma mensagem que ganhou quando o jogador completa
        passar

    def __str__(self, funcao): #Representação em string
        manual = manual.Tela
        return (print(f'{funcao} : {manual[funcao]}'))
    import os

class Interface():
    '''
    Representara o que ira ocorrer atrás da tela do usuario
    '''

    tabelaCaracteres = {chr(x) : x for x in range(256)} 

    def opcoes(): #contém as opções do jogo
        pass

    def limpaTela():
        """
        Esta função limpara toda a tela do console do Windows. 
        Dessa form, so é  possível dar 'refresh' na tela a ser desenhada.
        """
        os.system('cls')


#Sera criada classe tela, essa interface ira conduzir as letras funções de mover e entre outras.
# menu principal, telapause, tela carregar, tela salvar, opções.
class jogador:
    def __init__(nome, erros = 0, tempo = 0):   #Ira receber dados do jogador, como tambem a quantidade de erros cometidos e o tempo dele de resolução do jogo 
        pass
    from validSudoku import *
import random
from msvcrt import getch

class Mecanicas:

    def __init__(self):
        pass

    def teclas(self):   #Logo usando o getch será definido as funções das teclas nessa função
        pass

    def jogada(self, num, pos): #Com isso, recebendo um numero do 1 a 9, a função analisara que se trata de um numero dentro dos paramentros do jogo e ocorrera a executação da jogada na posição selecionada
        pass

    def apagarjogada(self, pos): #Pegara uma posição do tabuleiro e o removera o seu numero
        pass

    def dicas(self):    # Logo, ira dar uma dica (resposta aleatória dentro do tabuleiro).
        pass


#Movimento do jogador no tabuleiro
#Numeros que seram permitidos
#Mensagem de erro no jogo
#Casas erradas
#Apagar
#Dicas
    from validSudoku import *

class Tabuleiro:

    def __init__(self, tabuleiro = None, numeros = [1,2,3,4,5,6,7,8,9]): #Obterá as configurações do tabuleiro e os números permitidos nele 
        pass
    def atribuir_numeros(self, tabuleiro, numeros): #Concederá os números ao tabuleiro
        pass
    def valido(self, tabuleiro):    #Apurar se a localização de números é correta
        pass

    def preparar(self, tabuleiro):  #Apagar os numeros de forma que seja possivel resolver o tabuleiro
        from interface import *

class Tela(Interface):
    '''
    A tela receberá o que interface que contiver
    '''
    atributos = {'opcoes', 'nome_do_jogo', 'salvar', 'carregar'}
    metodos = {'__init__','__str__','opcao_escolhida','visual','getManual','getAtributos','getMetodos'}
    def __init__(self, opcoes = None, nome_do_jogo = 'Sudoku', salvar = None, carregar = None): #recebe o titulo, o tabuleiro salvo, e carrega ele

        self.nome_do_jogo = nome_do_jogo
        self.opcoes = opcoes
        self.salvar = salvar    # Mostrara o  tabuleiro onde o jogador parou

    def __str__(self): #É o método de representação em string
        pass

    def opcao_escolhida(self, opcoes):  #Ira realizar a opção que o usuario marcou
        pass

    def visual(self, nome_do_jogo, opcoes):   #Ira print a tela principal
        pass

    def getAtributos():
        return atributos

    def getMetodos():
        return metodos

    def getManual():
        """
            Logo esta função será (chamada sempre através de Tela.getManual()) que ira retorna um 
            dicionário que ira mapeia os nomes dos atributos e métodos às suas descrições.
            
            (None) -> dict
        """
        manual = {}
        manual['__init__']              = Tela.__init__.__doc__
        manual['__str__']               = Tela.__str__.__doc__
        manual['visual']                = Tela.visual.__doc__
        manual['opcao_escolhida']       = Tela.opcao_escolhida.__doc__
        manual['getManual']             = Tela.getManual.__doc__
        manual['nome_do_jogo']          = '# Representa o título da tela'
        manual['opcoes']                = '# Representa a lista de opções do usuário'
        manual['getAtributos']          = Tela.getAtributos.__doc__
        manual['getMetodos']            = Tela.getMetodos.__doc__
        manual['getManual']             = Tela.getManual.__doc_

        return manual


'''
2. Criar duas propriedades privadas do tipo conjunto (set), que ira abranger os nomes dos atributos e dos métodos na classe de cada seção do jogo.
	3. Definir os métodos getAtributos() e getMetodos() que regressarão os respectivos conjuntos de nomes.
	4. Preencha o método mágico __str__, a ser acessado quando for dado um "print" de uma instância do seu jogo, que retornará uma string, convenientemente formatada, exibindo os atributos e os métodos com suas respectivas descrições.
'''
#menu principal, tela salvar, opções
"""
    Atenção alunos. Deste código apenas a função getSudoku() deve ser utilizada.
    
    A função getSudoku() não recebe parâmetros e retorna uma lista de listas de inteiros que representam 
    um sudoku válido gerado aleatoriamente.
    
    Este código foi alterado por Gabriel Cardoso de Carvalho a partir do código obtido do endereço https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/
    
    Último acesso em 16/08/2021.
"""
import random



def shuffle(lista):
    random.shuffle(lista)
    return lista

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    
    for i in shuffle(list(range(1,10))):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

def getSudoku():
    board = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    solve(board)
    return board

def main():
    print_board(board)
    solve(board)
    print("___________________")
    print_board(board)

if __name__=="__main__":
    main()
    
