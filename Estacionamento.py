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
ent_placa = ["LYS6256", "ULI3045", "AWD2936"]  # Plcas de carros no local.
box_util = ["5", "10", "14"]  # Vagas utilizadas.
box_vago = ["Vago"] * 20  # 20 Vagas livres.
hr_ent_local = ["10:30:55", "11:00:55", "11:30:55"]  # Horários de entrada.

# BOX USADO / SAIDA
box_usados = ["2", "4", "3", "6"]
saida_placa = ["LYE1039", "UVI3047", "CVF6996", "IIS6266"]
hr_ent_saida = ["08:30:55", "09:00:55", "09:30:55", "10:00:55"]
hr_saida = ["14:30:55", "15:00:55", "15:30:55", "16:00:55"]
#////////////////////////////////////////////////////////////////////////////////
#FUNÇÕES
#INSERE A PLACA E VERIFICA SE NÃO EXISTE NO CADASTRO
def placa_ent():
    plac = input(str("Placa(LLL-NNNN): ")).upper()
    for i in range(len(ent_placa)):
        if plac == ent_placa[i]:
            print("O esta na Vaga 00.")
            return placa_ent()
        else:
            return plac

#PROCURA UM BOX ALEATORIO ENTRE OS VAGOS
def box_ent():
    import random
    box_verif = random.randint(1, 20)
    if str(box_verif) in box_util:
        return box_ent()
    else:
        return box_verif

#PROCURAR PLACA NAS LISTAS
def proc_placa():
    plac = input(str("Placa(LLL-NNNN): ")).upper()
    placa_encont = 0
    for i in range(len(ent_placa)):
        if plac == ent_placa[i]:
            print("PLACA   /  BOX  /  H ENTRADA  /  H SAIDA")
            print(ent_placa[i], "   ", int(box_util[i])+1, "    ", hr_ent_local[i])
            placa_encont = ent_placa[i]
        else:
            pass
    for x in range(len(saida_placa)):
        if plac == saida_placa[x]:
            print("PLACA   /  BOX  /  H ENTRADA  /  H SAIDA")
            print(saida_placa[x], "   ", int(box_usados[x])+1, "    ", hr_ent_saida[x], "    ", hr_saida[x])
            placa_encont = saida_placa[x]
        else:
            pass
    if plac == placa_encont:
        return placa_encont
    else:
        print("PLACA NÃO ENCONTRADA")
        return proc_placa()

#PROCURAR BOX NAS LISTAS
def proc_box():
    print("BOX de 1 a 20:")
    pbox = input(int())
    pbox_encont = 0
    for i in range(len(box_util)):
        if pbox == box_util[i]:
            print("PLACA   /  BOX  /  H ENTRADA  /  H SAIDA")
            print(ent_placa[i], "   ", int(box_util[i])+1, "    ", hr_ent_local[i])
            pbox_encont = box_util[i]
        else:
            pass
    for x in range(len(box_usados)):
        if pbox == box_usados[x]:
            print("PLACA   /  BOX  /  H ENTRADA  /  H SAIDA")
            print(saida_placa[x], "   ", int(box_usados[x])+1, "    ", hr_ent_saida[x], "    ", hr_saida[x])
            pbox_encont = box_usados[x]
        else:
            pass
    if pbox == pbox_encont:
        return pbox_encont
    else:
        print("BOX NÃO ENCONTRADO")
        return proc_box()

def busca_placa_box():
    print("="*20+"\nA para Buscar Placa\nB para Buscar BOX\nC para Cancelar\n"+"="*20)
    conf_opc = confirm()
    if conf_opc == "A":
        proc_placa()
    if conf_opc == "B":
        proc_box()
    if conf_opc == "C":
        return

#DEFINE HORA ATUAL PARA ENTRADA DO VEICULO
def hm_ent():
    from datetime import datetime
    data_comp_atual = datetime.now()
    dh_atual = data_comp_atual.strftime("%X")
    return dh_atual

#REGISTRAR ENTRADA
def reg_ent():
    #FALTA ERRO SE TIVER LOTADO!!!!
    ent_placa.append(placa_ent())
    box_util.append(str(box_ent()))
    hr_ent_local.append(hm_ent())

#RELATORIO GERAL DE TODOS VEICULOS
def relat_geral():
    print("\n" + "=" * 50)
    print("EM UTILIZAÇÃO")
    print("PLACA   /  BOX  /  H ENTRADA  /  H SAIDA")
    for x in range(len(box_vago)):
        if str(x) in box_util:
            relat_index = box_util.index(str(x))
            print(ent_placa[relat_index], "   ", x+1, "    ", hr_ent_local[relat_index])
        elif str(x) not in box_util:
            print(box_vago[x], "      ", x+1)
    print("=" * 50)
    print("FECHADOS")
    print("PLACA   /  BOX  /  H ENTRADA  /  H SAIDA")
    for i in range(len(saida_placa)):
        print(saida_placa[i], "   ", int(box_usados[i])+1, "    ", hr_ent_saida[i], "    ", hr_saida[i])
    print("=" * 50)
    return

#CONFIRMAR
def confirm():
    conf_opc = input(str("Digite a opção desejada: ")).upper()
    if conf_opc == "A":
        return "A"
    elif conf_opc == "B":
        return "B"
    elif conf_opc == "C":
        return "C"
    else:
        print("Opção incorreta")
        return confirm()

#REGISTRAR SAIDA DE VEICULOS
def reg_saida():
    global index_saida_veic
    plac_saida_veic = proc_placa()
    if plac_saida_veic in ent_placa:
        index_saida_veic = ent_placa.index(plac_saida_veic)
    elif plac_saida_veic in saida_placa:
        index_saida_veic = saida_placa.index(plac_saida_veic)
        print("Veiculo já deu saída")
        return
    else:
        pass
    print("Confirmar saida?")
    print("A para SIM ou B para NÃO")
    conf_opc = confirm()
    if conf_opc == "A":
        #Adiciona informações nas listas BOX USADO / SAIDA
        saida_placa.append(ent_placa[index_saida_veic])
        box_usados.append(box_util[index_saida_veic])
        hr_ent_saida.append(hr_ent_local[index_saida_veic])
        hr_saida.append(hm_ent())
        #Retira informações nas listas BOX EM UTILIZAÇÃO
        ent_placa.pop(index_saida_veic)
        box_util.pop(index_saida_veic)
        hr_ent_local.pop(index_saida_veic)
    elif conf_opc == "B":
        print(plac_saida_veic)
        print("Veiculo não deu saída")
    else:
        pass

#MENU
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
