from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import webbrowser

app = QtWidgets.QApplication([])
tela = uic.loadUi("pagina_de_cadastro.ui")
tela2 = uic.loadUi("pagina_treino_em_casa.ui")
tela3 = uic.loadUi("suplementos1.ui")
tela4 = uic.loadUi("testee.ui")
tela4.show()

def testee():
    url = "https://www.gsuplementos.com.br/"
    webbrowser.open(url)
    testee()

app.exec()