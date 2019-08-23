from estacionamento_3_classes import estacionar

# Trabalho Estacionamento 3 Classes
# Versão Aula 5 - 21/05/2019 Noite
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

#/////////////////////////////////////////////////////////////////////////////////////////////////
#BIBLIOTECAS
# BOX EM UTILIZAÇÃO
ent_veiculos = {'LYS6256': ('5','15:49:35','--:--:--'), 'ULI3045': ('10','15:50:27','--:--:--')}
# BOX USADO / SAIDA
saida_veiculos = {'LYE1039': ('2','08:30:55','15:53:45'), 'UVI3047': ('4','09:00:55','15:54:10')}
#/////////////////////////////////////////////////////////////////////////////////////////////////

#FUNÇÕES
def hm_gen():
    from datetime import datetime
    data_comp_atual = datetime.now()
    dh_atual = data_comp_atual.strftime("%X")
    return str(dh_atual)

#PROCURA UM BOX ALEATORIO ENTRE OS VAGOS
def box_gen():
    import random
    box_rand = random.randint(1, 20)
    x_it = ent_veiculos.items()
    for k, v in x_it:
        if str(box_rand) == v[0]:
            return box_gen()
        else:
            pass
    return str(box_rand)

#FUNÇÃO PARA CONFIRMAÇÕES
def confirma():
    print("\nDigite S/SIM ou N/NAO/NÃO!")
    sn = input("Confirma: ").upper()
    if sn == "S" or sn == "SIM":
        return True
    elif sn == "N" or sn == "NAO" or sn =="NÃO":
        return False
    else:
        confirma()

# ATUALIZA BIBLIOTECA
def update_bibl(dic,add):
    dic[add.getPlaca()] = (add.getBox(), add.getH_entrada(), add.getH_saida())

#PROCURA PLACA NO DICIONARIO
def proc_placa(plac):
    ent_veiculos_it = ent_veiculos.items()
    for k, v in ent_veiculos_it:
        if plac == k:
            print("\nPLACA ENCONTRADA!")
            c = estacionar(k, v[0], v[1], v[2])
            c.mostraDados()
            print()
            return c
        else:
            pass
    return False

#REGISTRA ENTRADA DE VEICULOS
def reg_ent():
    c = estacionar(input("Digite a Placa(AAA0000): ").upper(), box_gen(), hm_gen(), "--:--:--")
    if proc_placa(c.getPlaca()) == False:
        update_bibl(ent_veiculos,c)
        c.mostraDados()
        return
    else:
        return menu_while()
    
#REGISTRAR SAIDA DE VEICULOS
def reg_saida():
    c = proc_placa(input("Digite a Placa: ").upper())
    if c == False:
        print("SAIDA CANCELADA")
    else:
        print("Fazer saída do automóvel?")
        c.setH_saida(hm_gen())
        print("PLACA    BOX   H ENTRADA   H SAIDA")
        c.mostraDados2()
        if confirma() == True:
            update_bibl(saida_veiculos,c)
            del ent_veiculos[c.getPlaca()]
        else:
            print("SAIDA CANCELADA")
        
#RELATORIO GERAL / ESTACIONADOS E FINALIZADOS
def relat_geral():
    ent_veiculos_it = ent_veiculos.items()
    saida_veiculos_it = saida_veiculos.items()
    def relat_carros(it):
        for k, v in it:
            c = estacionar(k, v[0], v[1], v[2])
            c.mostraDados2()
    print("\nRELATORIO GERAL")
    print("RELATORIO ESTACIONADOS")
    print("PLACA    BOX   H ENTRADA   H SAIDA")
    relat_carros(ent_veiculos_it)
    print("\nRELATORIO FINALIZADOS")
    print("PLACA    BOX   H ENTRADA   H SAIDA")
    relat_carros(saida_veiculos_it)
    
#PROCURA A "PLACA" DE ACORDO COM O TAMANHO DA STRING DIGITADA
def for_placa(busca,it):
    itens = it.items()
    for k, v in itens:
        if busca == k:
            c = estacionar(k, v[0], v[1], v[2])
            print("PLACA ENCONTRADA")
            c.mostraDados()
        else:
            pass
    return

#PROCURA O "BOX"  DE ACORDO COM O TAMANHO DA STRING DIGITADA
def for_box(busca,it):
    itens = it.items()
    for k, v in itens:
        if busca == v[0]:
            c = estacionar(k, v[0], v[1], v[2])
            print("BOX ENCONTRADO")
            c.mostraDados()
        else:
            pass
    return

#BUSCA PLACA OU BOX
def busca_placa_box():
    busca = str(input("Digite Placa ou Box: ").upper())
    if len(busca) <= 2:
        box = for_box(busca,ent_veiculos)
        box = for_box(busca,saida_veiculos)
    elif len(busca) > 2 and len(busca) == 7:
        placa = for_placa(busca,ent_veiculos)
        placa = for_placa(busca,saida_veiculos)
    else:
        print("Não encontrado ou invalido")

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
            pass
menu_while()

