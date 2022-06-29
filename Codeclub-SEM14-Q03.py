def displayMenu():
    print("Tradutor de expressão")
    print("=" * 13)
    print("Menu:")
    print(" a = adicionar uma palavra")
    print(" c = converter uma frase")
    print(" p = imprimir dicionário")
    print(" d = remover uma palavra")
    print(" q = sair")

#--------------------------------------------------------------------------

def convertSentence():
    sentence = input("Insira uma frase para traduzir: ").lower()
    translatedSentence = ""

    #remove a ponttuação da frase
    for char in '?!.,;':
        sentence = sentence.replace(char, '')

    #divide a frase em uma lista de palvras
    list0fWords = sentence.split()

    for word in list0fWords:
        #adiciona a palavra traduzida se ela existir no dicionário
        if word in textSpeakDictionary:
            translatedSentence += textSpeakDictionary[word] + " "

        #mantém a palavra original caso não exista tradução
        else:
            print(f'Essa expressão {sentence} não existe na lista')
            print('Tente inserir essa expressão na lista')

    #imprime a frase traduzida
    print("==>")
    print(translatedSentence)


#-------------------------------------------------------------------------------
def addDictionaryItem():
    txtToAdd = input("Insira a expressão a ser adicionada ao dicionário: ")
    meaning = input("O que ela significa?: ")

    #só adiciona se nao tiver na lista
    if txtToAdd not in textSpeakDictionary:
        #adiciona a nova tradução ao dicionário
        textSpeakDictionary[txtToAdd] = meaning
    else:
        print("Essa expressão ja existe na lista")
        print("Tente outra palvra que não esteja na lista")

#-------------------------------------------------------------------------------
def deleteDictionayItem():
    txtToDelete = input("Insira a expressão a ser removida ao dicionário: ")

    #só remove itens que existe na lista
    if txtToDelete not in textSpeakDictionary:
        print("Essa expressão nao pode ser removida")
        print("Digite uma expressão que esteja na  lista")

    else:
        # remove a tradução do dicionário
        del textSpeakDictionary[txtToDelete]


#--------------------------------------------------------------------------------
# O programa começa aqui!
#--------------------------------------------------------------------------------

textSpeakDictionary = {
    "rs": "risos",
    "tmb": "também",
    "vc": "você",
    "pq": "porque"
}
running = True

displayMenu()

#repete até que o usuário digite 'q' para sair
while running == True:

    menuChoice = input(">_").lower()

    #c para converter
    if menuChoice == 'c':
        convertSentence()

    #p para imprimir
    elif menuChoice == 'p':
        print(textSpeakDictionary)

    #a para adicionar
    elif menuChoice == 'a':
        addDictionaryItem()

    #d para remover
    elif menuChoice == 'd':
        deleteDictionayItem()

    #q para sair

    elif menuChoice == 'q':
        running = False

    else:
        print("Escolha inválida!")

