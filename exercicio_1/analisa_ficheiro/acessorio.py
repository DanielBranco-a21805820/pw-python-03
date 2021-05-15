import json

def pede_nome(nome):
    verify = nome.split(".")[1]
    if (verify == "txt"):
        try:
            f=open(nome, 'r')
            f.close()
            return nome
        except OSError:
            print("Não conseguiu abrir/ler o ficheiro: ", nome)
    else: 
        print("Deve usar um ficheiro txt")


def gera_nome(nome):
    f=open(nome, 'r')
    conteudo = f.readlines()
    f.close()

    content = {}

    for linha in conteudo:
        (key,value) = linha.split()
        content[key] = value
    with open(nome.split(".")[0] + ".json", 'w') as json_file:
        json.dump(content, json_file, indent = 4)



