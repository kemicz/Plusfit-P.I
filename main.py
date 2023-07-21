from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import webbrowser
import mysql.connector

banco=  mysql.connector.connect(
   host= 'localhost',
   user= 'root',
   password= '',
   database= 'planusfit',
)

def cadastro():
    cadastrar= tela.nome.text() and tela.sobrenome.text() and tela.email.text and tela.senha.text and tela.peso.text and tela.altura.text
    if cadastrar == '':
        QMessageBox.about(tela, 'Atenção', 'Preencha os campos solicitados.')

    else:
        QMessageBox.about(tela, 'Salvo com sucesso', 'Informações registradas')
        tela.close()
        tela1.show()
    nome= tela.nome.text()
    sobrenome= tela.sobrenome.text()
    email= tela.email.text()
    senha= tela.senha.text()
    peso= tela.peso.text()
    altura= tela.altura.text()

    cursor= banco.cursor()
    sql= "INSERT INTO cadastro (nome, sobrenome, email, senha, peso, altura) VALUES (%s, %s, %s, %s, %s, %s)"
    colunas= (str(nome), str(sobrenome), str(email), str(senha), str(peso), str(altura))
    cursor.execute(sql, colunas)
    banco.commit()



def entrar():
    login_input = tela1.loginemail.text()
    senha_input = tela1.loginsenha.text()
    sql = "select senha from cadastro where email = '{}'".format(login_input)
    cursor = banco.cursor()
    cursor.execute(sql)
    senha_banco = cursor.fetchall()

    if login_input != '' and senha_input != '':
        if senha_input == senha_banco[0][0]:
            QMessageBox.about(tela, "Bem-vindo(a)", "Seja Bem-vindo(a) ao PlanusFit.")
            #TELA ´PRINCIPAL AQUI
            tela1.close()

def logincadastro():
    tela.show()
    tela1.close()

def voltaplogin():
    tela.close()
    tela1.show()

def cadastrar():
    tela.close()
    tela4.show()

########################################################

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

########################################################


def menutr():
    tela2.close()
    tela5.show()

def perfiltr():
    tela2.close()
    tela4.show()

# def configtr():
#     tela2.close()
#     tela6.show()

########################################################

def menusup():
    tela3.close()
    tela5.show()

def perfilsup():
    tela3.close()
    tela4.show()

def treinosup():
    tela3.close()
    tela7.show()

# def configsup():
#     tela3.close()
#     tela6.show()

########################################################

def menuper():
    tela4.close()
    tela5.show()

def perfilper():
    tela4.close()
    tela4.show()

def treinoper():
    tela4.close()
    tela7.show()

# def configper():
#     tela4.close()
#     tela6.show()

########################################################

def treinoemcasa():
    tela5.close()
    tela2.show()

def suplementos():
    tela5.close()
    tela3.show()

def exercicio():
    tela5.close()
    tela7.show()

def menutop():
    tela5.close()
    tela5.show()

def perfiltop():
    tela5.close()
    tela4.show()

def treinotop():
    tela5.close()
    tela7.show()

# def configtop():
#     tela5.close()
#     tela6.show()

########################################################

def menupagtr():
    tela7.close()
    tela5.show()

def perfilpagtr():
    tela7.close()
    tela4.show()

def treinopagtr():
    tela7.close()
    tela7.show()

# def configpagtr():
#     tela7.close()
#     tela6.show()

def tela_principal():
    tela1.close()
    tela4.show()

app = QtWidgets.QApplication([])
tela = uic.loadUi("pagina_de_cadastro.ui")
tela1 = uic.loadUi("login.ui")
tela2 = uic.loadUi("pagina_treino_em_casa.ui")
tela3 = uic.loadUi("suplementos1.ui")
tela4 = uic.loadUi("perfil.ui")
tela5 = uic.loadUi("topicos.ui")
# tela6 = uic.loadUi("config.ui")
tela7 = uic.loadUi("pagina_de_treino.ui")

tela.cadastrar.clicked.connect(cadastrar)
tela.voltaplogin.clicked.connect(voltaplogin)

tela1.entrar.clicked.connect(entrar)
tela1.cadastrar.clicked.connect(logincadastro)
tela1.entrar.clicked.connect(tela_principal)

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
tela4.treino.clicked.connect(treinoper) 
#tela4.config.clicked.connect(configper)

tela5.treinoemcasa.clicked.connect(treinoemcasa)
tela5.suplementos.clicked.connect(suplementos)
tela5.exercicios.clicked.connect(exercicio)
tela5.menu_4.clicked.connect(menutop)
tela5.perfil.clicked.connect(perfiltop) # botão 
tela5.treino.clicked.connect(treinotop)  
#tela5.config.clicked.connect(configtop)

tela7.menu_4.clicked.connect(menupagtr)
tela7.perfil.clicked.connect(perfilpagtr) # botão 
tela7.treino.clicked.connect(treinopagtr)  
#tela5.config.clicked.connect(configpagtr)

tela7.show()
app.exec()