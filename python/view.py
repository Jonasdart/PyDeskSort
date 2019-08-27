import tkinter as tk

class view():
	def tela_inicial(self):
		return input("Aguardando Código QR: ")

	def popup_premio(self, existe = False, cod_premio = None, premio = None):
		if not existe:
			pop_up = tk.Tk()
			pop_up_label = tk.Label(pop_up, text = "NENHUM PREMIO", fg = "white", bg = "red")
			pop_up_label.pack()
			pop_up.mainloop()

		if existe:
			pop_up = tk.Tk()
			imagem = tk.PhotoImage(file=f"imagens/{cod_premio}.png")
			label_premio = tk.Label(pop_up, text = f"PARABENS VOCE GANHOU {premio}", fg = "white", bg = "green")
			label_premio.pack()
			imagem_premio = tk.Label(pop_up, image = imagem)
			imagem_premio.imagem = imagem
			imagem_premio.pack()
			pop_up.mainloop()


