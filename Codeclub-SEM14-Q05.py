def display():
    print("programa secreto")
    print("=================")
    print("nome: ")
    print("senha: ")
#---------------------------------------------------------

def entrada():

    tentativa = 0
    while tentativa < 3:
        nome = input("Insira um nome: ").lower()
        senha = input("insira uma senha: ").lower()
        translatednome = ""

        for char in '?!.,;':
            nome = nome.replace(char,'')
            senha = senha.replace(char,'')

        # divide a frase em uma lista de palvras
        listanome = nome.split()

        for word in listanome:
            #adciona a palavra traduzida se ela existir no dicionárioa
            if nome in textSpeakDictionary and senha == textSpeakDictionary[nome]:
                translatednome += textSpeakDictionary[word] + " "
                print("SEJA BEM VINDO PROGRAMADOR")

            #mantém a palavra original caso não exista tradução
            else:

                print("nome ou senha não confere")
                translatednome += word + " "





textSpeakDictionary = {
    "miguel": "123456",
    }
running = True

display()

while running == True:

    menuChoice = input(">_").lower()

    # a para converter
    if menuChoice == 'nome':
        entrada()

    else:
        print("Escolha inválida!")

