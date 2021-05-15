def calcula_linhas(nome):
    f=open(nome, 'r')
    nrlinhas = f.readlines()
    f.close()
    return len(nrlinhas)


def calcula_carateres(nome):
    f=open(nome,'r')
    count = 0
    data = f.read().replace(" ","").replace("\n", "")
    for letra in data:
        count += 1
    f.close()
    return count

def calcula_palavra_comprida(nome):
    with open(nome,'r') as f:
	    words = f.read().split()
	    max_len_word = max(words,key=len)
    return max_len_word


def calcula_ocorrencia_de_letras(nome):
    all_freq = {}
    f=open(nome,'r')
    data = f.read().replace(" ","").replace("\n", "").lower()
    res = {}
  
    for keys in data:
        res[keys] = res.get(keys, 0) + 1
    f.close()
    return str(res).replace(" ","")

