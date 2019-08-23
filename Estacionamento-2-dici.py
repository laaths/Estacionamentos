# Trabalho Estacionamento
# Versão Aula 5 - 09/04/2019 Noite
# Leonardo Soares Duarte
menu = """
ESCOLHA A OPÇÃO DESEJADA:
0 - Sair
1 - Registrar entrada.
2 - Registrar saida.
3 - Relatorio geral.
4 - Buscar placas ou Vagas.
--------------------------
Opção: """
#////////////////////////////////////////////////////////////////////////////////
#LISTAS
# BOX EM UTILIZAÇÃO
ent_box = {'LYS6256': '5', 'ULI3045': '10', 'AWD2936': '14'}
ent_hentrada = {'LYS6256': '10:30:55', 'ULI3045': '11:00:55', 'AWD2936': '11:30:55'}
ent_hsaida = {'LYS6256': '--:--:--', 'ULI3045': '--:--:--', 'AWD2936': '--:--:--'}

# BOX USADO / SAIDA
saida_box = {'LYE1039': '2', 'UVI3047': '4', 'CVF6996': '3'}
saida_hentrada = {'LYE1039': '08:30:55', 'UVI3047': '09:00:55', 'CVF6996': '09:30:55'}
saida_hsaida = {'LYE1039': '14:30:55', 'UVI3047': '15:00:55', 'CVF6996': '15:30:55'}
#////////////////////////////////////////////////////////////////////////////////
#FUNÇÕES
#DEFINE HORA ATUAL PARA ENTRADA DO VEICULO
def hm_gen():
    from datetime import datetime
    data_comp_atual = datetime.now()
    dh_atual = data_comp_atual.strftime("%X")
    return str(dh_atual)

#PROCURA UM BOX ALEATORIO ENTRE OS VAGOS
def box_gen():
    import random
    box_rand = random.randint(1, 20)
    x_it = ent_box.items()
    for k, v in x_it:
        if str(box_rand) == v:
            return box_gen()
        else:
            pass
    return str(box_rand)

#INSERE A PLACA E VERIFICA SE EXISTE NO CADASTRO
def placa_ent():
    global digita_placa
    for key in ent_box:
        if digita_placa == key:
            print(key, "Esta na Vaga", ent_box[key])
            print()
            return reg_ent()
        else:
            pass
    return digita_placa

#REGISTRAR ENTRADA
def reg_ent():
    digita_placa = str(input("Digita a Placa: ")).upper()
    digita_box = box_gen()
    digita_hentrada = hm_gen()
    digita_hsaida = "--:--:--"
    print("")
    print("Placa     :", digita_placa)
    print("BOX       :", digita_box)
    print("H Entrada :", digita_hentrada)
    print("H Saida   :", "--:--:--")
    ent_box[digita_placa] = digita_box
    ent_hentrada[digita_placa] = digita_hentrada
    ent_hsaida[digita_placa] =  digita_hsaida
    digita_placa = ""
    input()

#INSERE A PLACA E VERIFICA SE EXISTE NO CADASTRO
def placa_saida():
    global digita_placa
    for key in ent_box:
        if digita_placa == key:
            print(key,"na vaga", ent_box[key])
            return digita_placa
        else:
            pass
    print("Placa não encontrada!\n")
    return reg_saida()

#REGISTRAR SAIDA DE VEICULOS
def reg_saida():
    global digita_placa
    digita_placa = str(input("Digita a Placa: ")).upper()
    placa_saida()
    print("\nENCONTRADO")
    print("Placa     :",digita_placa)
    print("BOX       :",ent_box[digita_placa])
    print("H Entrada :",ent_hentrada[digita_placa],"\n")
    print("Confirmar Saida?")
    confirm = confirma()
    if confirm == True:
        print("SAIDA CONCLUIDA!")
        update_bibl()
        return
    elif confirm == False:
        print("SAIDA CANCELADA!")
#ATUALIZA BIBLIOTECA COM OS NOVOS DADOS DA SAIDA
def update_bibl():
    digita_box = ent_box[digita_placa]
    digita_hentrada = ent_hentrada[digita_placa]
    digita_hsaida = hm_gen()
    saida_box[digita_placa] = digita_box
    saida_hentrada[digita_placa] = digita_hentrada
    saida_hsaida[digita_placa] = digita_hsaida
    del ent_box[digita_placa]
    del ent_hentrada[digita_placa]
    del ent_hsaida[digita_placa]
    return

#FUNÇÃO PARA CONFIRMAÇÕES
def confirma():
    count = 1
    while count <= 1:
        s_n = str(input("S ou N")).upper()
        if s_n == "S" or s_n == "SIM":
            count += 1
            return True
        elif s_n == "N" or s_n == "NAO":
            count += 1
            return False
        else:
            print("Apenas S ou N!")

#RELATORIO GERAL DE TODOS VEICULOS
def relat_geral():
    ent_tupla = {}
    saida_tupla = {}
    def relat_estacionados():
        for key in ent_box:
            ent_tupla[key] = ent_box[key], ent_hentrada[key], ent_hsaida[key]
            ent_tupla_it = ent_tupla.items()
        for k, v in ent_tupla_it:
            print(k, v[0], v[1], v[2])
    def relat_finalizados():
        for key in saida_box:
            saida_tupla[key] = saida_box[key], saida_hentrada[key], saida_hsaida[key]
            saida_tupla_it = saida_tupla.items()
        for k, v in saida_tupla_it:
            print(k, v[0], v[1], v[2])
    print("RELATORIO GERAL")
    print("RELATORIO ESTACIONADOS")
    relat_estacionados()
    print()
    print("RELATORIO FINALIZADOS")
    relat_finalizados()
    print()

#BUSCAR PLACAS NOS DICIONARIOS
def proc_placa():
    global digita_placa
    for key in ent_box:
        if digita_placa == key:
            print(key, "Esta na Vaga", ent_box[key])
            return
        else:
            pass

#BUSCAR BOX NOS DICIONARIOS
def proc_box():
    box_dict = {}
    for key in ent_box:
        box_dict[key] = ent_box[key], ent_hentrada[key], ent_hsaida[key]
        box_dict_it = box_dict.items()
    for k, v in box_dict_it:
        if v[0] == digita_box:
            print(k, v[0], v[1], v[2])
        else:
            pass
    return

#BUSCAR PLACAS OU BOX
def busca_placa_box():
    global digita_placa
    global digita_box
    print("1 para buscar Placa.\n2 para buscar box.")
    p_ou_b = input("1 ou 2? ")
    if p_ou_b != "1" and p_ou_b != "2":
        print("Apenas 1 para buscar Placa e 2 para buscar box")
        return busca_placa_box()
    elif  p_ou_b == "1":
        digita_placa = str(input("Digita a Placa: ")).upper()
        proc_placa()
        return
    elif p_ou_b == "2":
        digita_box = str(input("Digite o Box: "))
        proc_box()
        return

#MENU
def menu_while():
    while True:
        menu_op = int(input(menu))
        if menu_op == 0:
            print("Programa finalizado")
            break
        elif menu_op == 1: #REGISTRAR ENTRADA
            reg_ent()
        elif menu_op == 2: #REGISTRAR SAIDA
            reg_saida()
        elif menu_op == 3: #RELATORIO GERAL
            relat_geral()
        elif menu_op == 4: #BUSCAR PLACAS OU VAGAS
            busca_placa_box()
        else:
            print()
menu_while()