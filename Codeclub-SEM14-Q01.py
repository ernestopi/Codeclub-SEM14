#imprime apenas o conteúdo relacionado à chave "rs"
textSpeakDictionary = {"rs":"risos", "tmb":"também"}

print("\nrs =", textSpeakDictionary["rs"])

#texto que a entrada do usuário
key = input("\n0 que você gostaria de converter? : ")
print( key, "=", textSpeakDictionary[key])
