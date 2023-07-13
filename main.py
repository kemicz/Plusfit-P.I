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

app = QtWidgets.QApplication([])
tela = uic.loadUi("pagina_de_cadastro.ui")
tela1 = uic.loadUi("login.ui")
tela2 = uic.loadUi("pagina_treino_em_casa.ui")
tela3 = uic.loadUi("suplementos1.ui")
tela4 = uic.loadUi("perfil.ui")
tela1.cadastrarlog.clicked.connect(castrar)
tela.voltaplogin.clicked.connect(voltaplogin)
tela3.l_arginina.clicked.connect(larginina)
tela.cadastrar.clicked.connect(cadastrar)
tela1.show()
app.exec()