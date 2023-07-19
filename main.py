from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import webbrowser

def castrar():
    tela1.close()
    tela.show()

def voltaplogin():
    tela.close()
    tela1.show()

def cadastrar():
    tela.close()
    tela4.show()



def larginina():
    webbrowser.open("https://www.gsuplementos.com.br/conteudo/arginina-beneficios/")

def creatina():
    webbrowser.open("https://www.gsuplementos.com.br/conteudo/creatina-beneficios")

def bcaa():
    webbrowser.open("https://www.gsuplementos.com.br/conteudo/bcaa-beneficios/")

def glutamina():
    webbrowser.open("https://www.gsuplementos.com.br/conteudo/glutamina-beneficios/")

def omega3():
    webbrowser.open("https://www.gsuplementos.com.br/conteudo/omega-beneficios/")
    
def omega3():
    webbrowser.open("https://www.gsuplementos.com.br/conteudo/whey-beneficios/")


app = QtWidgets.QApplication([])
tela = uic.loadUi("pagina_de_cadastro.ui")
tela1 = uic.loadUi("login.ui")
tela2 = uic.loadUi("pagina_treino_em_casa.ui")
tela3 = uic.loadUi("suplementos1.ui")
tela4 = uic.loadUi("perfil.ui")
tela1.cadastrarlog.clicked.connect(castrar)
tela.voltaplogin.clicked.connect(voltaplogin)
tela3.l_arginina.clicked.connect(larginina)
tela3.l_arginina.clicked.connect(bcaa)
tela3.l_arginina.clicked.connect(whey)
tela3.l_arginina.clicked.connect(creatina)
tela3.l_arginina.clicked.connect(glutamina)
tela3.l_arginina.clicked.connect(omega3)

tela.cadastrar.clicked.connect(cadastrar)
tela3.show()
app.exec()