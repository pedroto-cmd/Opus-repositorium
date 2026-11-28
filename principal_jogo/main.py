#iniciara o game
import interface.py

interface.janela()

nome = interface.nome()
if nome == 0:
    print("Nome inválido! Digite um nome válido.")

interface.botao()
