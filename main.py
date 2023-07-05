from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

app = QtWidgets.QApplication([])
tela = uic.loadUi("suplementos.ui")
tela2 = uic.loadUi("untitled.ui")

def botao():
    tela.close()
    tela2.show()

tela.show()


app.exec()