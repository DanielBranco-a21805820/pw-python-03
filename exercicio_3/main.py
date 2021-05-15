import os

soma = 0

def pede_pasta():
    caminho = input("Insira o caminho para a pasta: ")
    while os.path.exists(caminho) == False:
        caminho = input("Insira o caminho para a pasta: ")
    
    return caminho


def calcula_tamanho_pasta(pasta):
   global soma
   lista_tudo = os.listdir(pasta)
   for coisa in lista_tudo:
       if os.path.isfile(os.path.join(pasta,coisa)):
           soma += os.path.getsize(os.path.join(pasta,coisa))/2**10
       if os.path.isdir(os.path.join(pasta,coisa)):
           soma += calcula_tamanho_pasta(os.path.join(pasta,coisa))
   return soma

def main():
    print(f"O tamanho total da pasta e subpastas é {calcula_tamanho_pasta(pede_pasta())}")

if __name__ == "__main__": 
  main()