from view import view
from model import model

class controller():
    def __init__(self):
        self.model = model()
        self.view = view()

    def inicio(self):
        premio = self.view.tela_inicial()
        self.chama_premio(premio)

    def chama_premio(self, cod_premio):
        try:
            premio = self.model.procura_premio(cod_premio)
        except:
            print("Não Encontrado")
            self.view.popup_premio(existe = False)
        else:
            cod_premio = premio[0]
            nome_premio = premio[1]
            print(cod_premio)
            print(nome_premio)
            
            self.view.popup_premio(existe = True, cod_premio = cod_premio, premio = nome_premio)

if __name__ == '__main__':
    controller = controller()
    controller.inicio()