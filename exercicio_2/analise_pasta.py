import csv
from matplotlib import pyplot as plt
import os


path = ''
dic_info = {}
list_quantidade = []
list_volume = []



def pede_pasta():
    caminho = input("Insira o caminho para a pasta: ")
    os.path.exists(caminho)
    return caminho

    
def faz_calculos():
    global dic_info
    lista_ficheiros = []
    tipoF = []
    global path
    path = pede_pasta()
    lista_tudo = os.listdir(path)
    for coisa in lista_tudo:
        if os.path.isfile(os.path.join(path,coisa)):
            tipoF.append(coisa.split(".")[1])
            lista_ficheiros.append((coisa.split(".")[1], os.path.getsize(os.path.join(path,coisa))/2**10))
            dic_info={tipo[0] : {"Quantidade": tipoF.count(tipo[0]), "Tamanho[kByte]": sum(v for k, v in lista_ficheiros if k==tipo[0])} for tipo in lista_ficheiros} 
    print(dic_info)
    
    return dic_info      

def guarda_resultados():
    global dic_info
    print(f"Os resultados foram guardados no ficheiro '{os.path.basename(path)}'")
    with open(path + '.csv','w', newline='') as ficheiro:
        campos = ['Extensão', 'Quantidade', 'Tamanho[kByte]']
        writer = csv.DictWriter(ficheiro, fieldnames=campos)
        writer.writeheader()
        for key,val in dic_info.items():
            row = {'Extensão':key}
            row.update(val)
            writer.writerow(row)


            

def faz_grafico_queijos():
    global list_volume
    global list_quantidade

    chaves = dic_info.keys()
    for p_id, p_info in dic_info.items():
    
        for key in p_info:
            if key == 'Quantidade':
                list_quantidade.append(p_info[key])
            if key == 'Tamanho[kByte]':
                list_volume.append(p_info[key])
    
    plt.pie(list_quantidade, labels=chaves, autopct='%1.0f%%')
    plt.title("Resultados: Quantidade")
    plt.show()

    plt.pie(list_volume, labels=chaves, autopct='%1.0f%%')
    plt.title("Resultados: Tamanho")
    plt.show()
    

    
        

def faz_grafico_barras():
    global list_volume
    global list_quantidade
    chaves = dic_info.keys()
    plt.bar(chaves, list_quantidade)
    plt.title("Resultados: Quantidade")
    plt.show()

    plt.bar(chaves, list_volume)
    plt.title("Resultados: Quantidade")
    plt.show()


   
    



