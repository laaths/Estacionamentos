# - Trabalho - Estacionamento
# Versão Aula05
# Autor: Ivonei Marques

vagas      = [True]*20  # True significa vaga livre 
                        # False significa vaga ocupada

# as listas abaixo estão inicializadas apenas para testes.                        
l_hEntrada = ["11:11","10:10","13:13"]
l_hSaida   = ["  :  ","  :  ","  :  "]
l_Placa    = ["AAA1111","AAA2222","AAA3333"]
l_Box      = ["3","6","11"]
vagas[2]   = False
vagas[5]   = False
vagas[10]  = False




def localizaPlacaNoBox(box):
    ''' retorna a placa que ocupa determinado box
    '''
    for ind,b in enumerate(l_Box): #[::-1]:
        if b == str(box+1) and l_hSaida[ind] == "  :  ":
            return l_Placa[ind]

def livreOcupada(vaga,i):
    if vaga:  # Se vaga True (livre) retorna a palavra 'LIVRE'
        return " Livre "
    return localizaPlacaNoBox(i) # Caso contrário retorna a PLACA
                                 # que ocupa esta vaga   

def imprimeVagas():
    ''' imprime na tela o mapa com box livres e ocupados
    '''
    print("\n"*15)
    print("Mapa de Vagas:")
    print(("box"+" "*10)*5) # igual a "box          "*5
    # verifica na lista boleana de vagas se a posição está
    # True (livre), ou False (ocupada). Se estiver ocupada
    # retorna a placa
    for ind,v in enumerate(vagas):
        print("%2d [%s]" %((ind+1),livreOcupada(v,ind)),end=" " )
        if (ind+1)%5 == 0: print()
        
def menu():
    m = '''

########################################
Menu
########################################
  1- Registrar Entrada de Veículos
  2- Registrar Saída de Veículos
  3- Relatório
  0- Fim
#########################################
Escolha: '''
    return input(m)


def placaOk(placa):
    ''' verifica se a placa está dentro dos critérios.
        Neste caso apenas se possui 7 caracteres.
    '''
    if len(placa) == 7:
        return placa.upper()
    print("...Erro. ")
    return placaOk(input("Placa: ")).upper()


def horaES_Ok():
    ''' Esta função tem a finalidade de capturar a data
        do sistema e armazená-la como horário de entrada
        e saída do veículo.
    '''
    def horaMinuto(t):
        if t < 10:
            return "0"+str(t)
        return str(t)
    
    from datetime import datetime
    hora = datetime.now()
    return horaMinuto(hora.hour)+":"+horaMinuto(hora.minute)


    
def boxOk(boxE):
    ''' verifica se o box digitado existe, ou já está ocupado
    '''
    try:
        if vagas[int(boxE)-1]:
            vagas[int(boxE)-1] = False
            return boxE
        else:
            print("....Erro. Box já ocupado.")
    except:
        print("....Erro. Box inexistente.")

    return boxOk(input("Box: "))

def boxSaidaOk(boxE):
    ''' verifica se o box digitado existe ou está livre
    '''
    try:
        if not vagas[int(boxE)-1]:  
            vagas[int(boxE)-1] = True
            return boxE
        else:
            print("....Erro. Box Não ocupado.")
    except:
        print("....Erro. Box inexistente.")

    return boxSaidaOk(input("Box: "))

def registraEntrada():
    ''' insere nas listas os dados de entrada
    '''
    l_Placa.append(placaOk(input("Placa: ")))
    l_hEntrada.append(horaES_Ok())
    l_Box.append(boxOk(input("Box: ")))
    l_hSaida.append("  :  ")

def ehPlaca(placa):
    ''' verifica se a placa é válida
    '''
    if len(placa.upper()) == 7:
        return True
    return False

def ehBox(bx):
    ''' verifica se o box digitado é válido.
    '''
    if int(bx) in range(1,21): 
        return True
    return False

def localizaPlaca(placa):
    ''' recebe o argumento placa, verifica se a placa digitada é
        a mesma cadastrada e, verifica o horario de saída e retorna
        o indice da l_Placa.
    '''
    for i,x in enumerate(l_Placa):
        if x == placa.upper() and l_hSaida[i] == "  :  ":
            return i
    return "....Erro. Placa Não localizada." 
    
def localizaBox(bx):
    ''' recebe o argumento bx como sendo o box digitado e retorna
        o indice desse box na lista. Ou retorna uma mensagem de erro
    '''
    i_box = int(bx)-1
    for i,x in enumerate(l_Box):
        # retorna o indice do box digitado quando a saída não foi
        # ainda efetivada
        if x == bx and l_hSaida[i] == "  :  ":
            return i
    return "....Erro. Box Não existente, ou Box não ocupado." 

def registraSaida():
    ''' Função que localiza o veículo pela placa ou pelo box,
        e efetiva sua saída atualizando o horário de saída na
        lista l_hSaida (horasES_Ok()) e também atualiza a lista
        vagas[] com True (liberada)
    '''
    strSaida = input("Placa ou Box: ")

    # verifica se o que foi digitado é uma placa
    if ehPlaca(strSaida):
        indPlaca  = localizaPlaca(strSaida) # localiza o indice da placa digitada
        # se o retorno do método localizaPlaca() for uma string
        # é porque a placa não existe, imprimindo uma mensagem de erro
        # na variável indPlaca
        if type(indPlaca) == str:
            print(indPlaca)
        else: # significa que localizou o indice da placa
            l_hSaida[indPlaca] = horaES_Ok() # retorna o horário de
                                             # de saída do sistema
            vagas[int(l_Box[indPlaca])-1] = True # libera o box
    # verifica se o que foi digitado é um box
    elif ehBox(strSaida):
        indBox = localizaBox(strSaida) # localiza o indice do box (l_box) pelo valor do box digitado
        # se o retorno for uma string. É uma mensagem de erro
        if type(indBox) == str:
            print(indBox) # imprime a mensagem como string
        else: # significa que localizou o indice do box
            l_hSaida[indBox] = horaES_Ok()# retorna o horário de saída
                                          # do sistema  
            vagas[int(strSaida)-1] = True # libera o box
    # Se o digitado não for um box ou uma placa. Mensagem de erro
    # e chama a função novamente por recursão
    else:
        print("....Erro. Você não digitou um Box válido ou uma Placa válida.")
        registraSaida()
    
def relatorio():
    ''' Impressão do movimento do dia.
        Apresenta todas entradas e saidas do dia.
        Apresenta também o total do dia.
    '''
    def calculaValorDoDia(qtVeiculos):
        ''' Esta função existe porque entende-se que a realização
            do calculo do caixa é uma funcionalidade do programa
        '''
        return qtVeiculos * 15

    def contaQtVeiculos(qt):
        ''' Esta função existe para imprimir o relatório e
            retornar a quantidade de veículos que já deixaram
            o estacionamento.
        '''
        for i in range(len(l_Box)):
            # verifica se o veiculo já tem um horario de saída
            if l_hSaida[i] != "  :  ":
                print(l_Placa[i].rjust(10,' '),l_hEntrada[i].rjust(10,' '),l_hSaida[i].rjust(10,' '),l_Box[i].rjust(5,' '))
                qt += 1
        return qt
    
    print("Relatório:".center(50,'-'))
    print("Veículo:".rjust(10,' '),"H.Entrada:".rjust(12,' '),"H.Saida:".rjust(10,' '),"Box:".rjust(5,' '))

    # calcula a quantidade de veículos que passou pelo estacionamento
    qtVeiculos = contaQtVeiculos(0)
    print("-"*50)
    print("Total de veículos do dia: %d " % qtVeiculos)
                                # realiza o calculo do caixa do dia
    print("Total: %.2f Reais" % calculaValorDoDia(qtVeiculos))
    print("-"*50)
    input("Enter para voltar ao menu.")


#################################################################    
# programa Principal
#################################################################    
''' Este laço infinito tem a finalidade de ler a opção de esolha
    e direcionar o código para a função desejada.
'''
while True:
    imprimeVagas()          # monta o mapa de box livres e ocupados
    escolha = menu()        # retorna uma das opções do menu
    # decide qual função chamar conforme a opção escolhida
    if escolha == '0':
        break
    elif escolha == '1':
        registraEntrada()
    elif escolha == '2':
        registraSaida()
    elif escolha == '3':
        relatorio()

