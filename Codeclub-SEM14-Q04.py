def displayMenu():
    print("Distâncias da Terra para os planetas ")
    print("=" * 13)
    print("Menu:")
    print(" a = Planeta")
    print(" b = imprimir as distâncias")
    print(" q = sair")

#-----------------------------------------------------------------------

def distancias_planetas():
    planetas = input("Insira o nome do planeta: ").lower()
    translatedPlanetas = ""

    #remove a ponttuação da frase
    for char in '?!.,;':
        planetas = planetas.replace(char,'')

    #divide a frase em uma lista de palvras
    listaPlanetas = planetas.split()

    for word in listaPlanetas:
        #adciona a palavra traduzida se ela existir no dicionárioa
        if word in dicionarioPlanetas:
            translatedPlanetas += dicionarioPlanetas[word] + " "

        #mantém a palavra original caso não exista tradução
        else:

            translatedPlanetas += word + " "

  #imprime a frase traduzida
    print("====================================================")
    print(f'{planetas} está a {translatedPlanetas}Km da Terra')
    print("====================================================")
#--------------------------------------------------------------------------------------
# Inicio do programa
#-------------------------------------------------------------------------------------

dicionarioPlanetas = {
    "sol": "149.600.000",
    "mercúrio": "91.700.000",
    "vênus": "41.400.000",
    "lua": "384.400",
    "marte": "78.300.000",
    "júpiter": "628.000.000",
    "saturno": "1.280.400.000",
    "urano": "2.720.400.000",
    "neturno": "4.350.400.000",
    "plutão": "5.750.400.000"
}
running = True

displayMenu()

#repete até que o usuário digite 'q' para sair
while running == True:

    menuChoice = input(">_").lower()

    # a para converter
    if menuChoice == 'a':
        distancias_planetas()

    # b para imprimir
    elif menuChoice == 'b':
        print(dicionarioPlanetas)

    # q para sair

    elif menuChoice == 'q':
        running = False

    else:
        print("Escolha inválida!")


