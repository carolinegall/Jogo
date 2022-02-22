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
