

class Automovel():
    def __init__(self, cap_dep, quant_comb, consumo):
        self.cap_dep = cap_dep
        self.quant_comb = quant_comb
        self.consumo = consumo


    def combustivel(self):
        return self.quant_comb


    def autonomia(self):
        return self.quant_comb * 100 / self.consumo

    def abastece(self, n_litros):
        
        if (self.quant_comb + n_litros) > self.cap_dep:
            print("ERRO! O abastecimento pretendido excede a capacidade do depósito")
        else:
            self.quant_comb += n_litros
        return self.quant_comb * 100 / self.consumo

    def percorre(self, n_km):
        
        if n_km > self.quant_comb * 100 / self.consumo:
            print("ERRO! O carro não tem combustivel suficiente para andar esta distancia")
        else: 
            self.quant_comb -= n_km * self.consumo / 100
        return self.quant_comb * 100 / self.consumo



def main():
    x, y, z = [int(x) for x in input("Introduza os dados do seu automovel, no seguinte formato (capacidade do deposito,quantidade de combustivel, consumo): ").split(",")]
    print(f"Este é o seu carro: (deposito: {x}, combustivel: {y}, consumo: {z})")
    print()
    carro = Automovel(x,y,z)
    print("Este é o menu: \n")
    print("Pode efetuar as seguintes operações: \n")
    print("Para verificar a quantidade de combustível no depósito escreva 1\n")
    print("Para consultar a autonomia escreva 2\n")
    print("Para abastecer escreva 3\n")
    print("Para percorrer um caminho escreva 4\n")
    action = ""
    while action != "-1":
        action = input("O que deseja fazer? ")
        if action == "1":
            print("Combustivel no deposito: ",carro.combustivel())
        if action == "2":
            print("Autonomia: ", carro.autonomia())
        if action == "3":
            litros = int(input("Quantos litros deseja abastecer? "))
            print("Autonomia: ", carro.abastece(litros))
        if action == "4":
            distancia = int(input("Quantos kilómetros vai percorrer? "))
            print("Autonomia: ", carro.percorre(distancia))
    else:
        print("O programa terminou")


if __name__ == "__main__": 
  main()