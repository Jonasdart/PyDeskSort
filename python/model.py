class model():
    def __init__(self):
        self.itens = open("premios.txt", "r")
        self.cod_premio = list()
        self.nome_premio = list()

    def procura_premio(self, codigo):
        premios = self.itens.readlines()

        for premio in premios:
            premio = premio.strip()
            lista = premio.split("-")
            self.cod_premio.append(str(lista[0]))
            self.nome_premio.append(str(lista[1]))


        quantidade = len(premios)
        for x in range(quantidade):
            cod = self.cod_premio[x].strip()

            if str(cod) == str(codigo):
                print("Somos iguais")
                return self.entrega_premio(codigo, x)
        raise
    def entrega_premio(self, codigo, indice):
        
        return [str(codigo), str(self.nome_premio[indice])]