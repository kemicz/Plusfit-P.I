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
    webbrowser.open("https://www.gsuplementos.com.br/oleo-de-peixe-omega-3-75-softgel-growth-supplements-p985848")

def whey():
    webbrowser.open("https://www.gsuplementos.com.br/conteudo/whey-beneficios/")


def menutr():
    tela2.close()
    tela5.show()

def perfiltr():
    tela2.close()
    tela4.show()

# def configtr():
#     tela2.close()
#     tela6.show()



def menusup():
    tela3.close()
    tela5.show()

def perfilsup():
    tela3.close()
    tela4.show()

def treinosup():
    tela3.close()
    tela4.show()

# def configsup():
#     tela3.close()
#     tela6.show()

def menuper():
    tela4.close()
    tela5.show()

def perfilper():
    tela4.close()
    tela4.show()

# def configper():
#     tela4.close()
#     tela6.show()

def treinoemcasa():
    tela5.close()
    tela2.show()

def suplementos():
    tela5.close()
    tela3.show()

def exercicio():
    tela5.close()
    tela7.show()



app = QtWidgets.QApplication([])
tela = uic.loadUi("pagina_de_cadastro.ui")
tela1 = uic.loadUi("login.ui")
tela2 = uic.loadUi("pagina_treino_em_casa.ui")
tela3 = uic.loadUi("suplementos1.ui")
tela4 = uic.loadUi("perfil.ui")
tela5 = uic.loadUi("topicos.ui")
# tela6 = uic.loadUi("config.ui")
tela7 = uic.loadUi("pagina_de_treino.ui")
tela1.cadastrarlog.clicked.connect(castrar)
tela.cadastrar.clicked.connect(cadastrar)
tela.voltaplogin.clicked.connect(voltaplogin)

tela3.l_arginina.clicked.connect(larginina)
tela3.bcaa.clicked.connect(bcaa)
tela3.whey.clicked.connect(whey)
tela3.creatina.clicked.connect(creatina)
tela3.glutamina.clicked.connect(glutamina)
tela3.omega3.clicked.connect(omega3)
tela3.menu_4.clicked.connect(menusup)  #Botões suplementos
tela3.perfil.clicked.connect(perfilsup) 
tela3.treino.clicked.connect(treinosup)  

#tela3.config.clicked.connect(configsup)

tela2.menu_4.clicked.connect(menutr) 
tela2.perfil.clicked.connect(perfiltr) # botões treino em casa
#tela2.config.clicked.connect(configtr)


tela4.menu_4.clicked.connect(menuper)
tela4.perfilbot.clicked.connect(perfilper) # botão perfil
#tela4.config.clicked.connect(configper)

tela5.treinoemcasa.clicked.connect(treinoemcasa)
tela5.suplementos.clicked.connect(suplementos)
tela5.exercicios.clicked.connect(exercicio)

tela1.show()
app.exec()