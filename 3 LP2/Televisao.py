class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

    def aumenta_canal(self):
        self.canal += 1
        print("aumenta canal")
    
    def diminui_canal(self):
        self.canal -= 1
        print("diminuir canal")


