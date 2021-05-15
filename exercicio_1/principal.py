import analisa_ficheiro
import json

def main(nome):
    f = open(nome.split(".")[0] + "_resultados"+".txt", "a")
    f.write("linhas " + str(analisa_ficheiro.calcula_linhas(nome))+"\n")
    f.write("carateres " + str(analisa_ficheiro.calcula_carateres(nome))+"\n")
    f.write("palavra_maior " + str(analisa_ficheiro.calcula_palavra_comprida(nome))+"\n")
    f.write("ocorrencia_das_letras " +str(analisa_ficheiro.calcula_ocorrencia_de_letras(nome)))
    f.close()
    analisa_ficheiro.gera_nome(analisa_ficheiro.pede_nome(nome.split(".")[0] + "_resultados"+".txt"))
    
if __name__ == "__main__": 
    main("teste1.txt")
