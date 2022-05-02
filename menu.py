from claseManejador import Lista

class claseMenu:
    __op = 0

    def __init__(self):
        self.__op = None

    def opcion(self, op, mp):
        if op == 1:
            self.opcion1(mp)
        elif op == 2:
            self.opcion2(mp)
        elif op == 3:
            self.opcion3(mp)
        elif op == 4:
            self.opcion4(mp)
        elif op == 5:
            self.salir()

    def salir(self):
        print('Usted salio del programa')

    def opcion1(self, mp):
        mp.actualiza()

    def opcion2(self, mp):
        x = float(input('Ingrese valor: '))
        mp.cuotainf(x)

    def opcion3(self, mp):
        mp.importelicito()

    def opcion4(self, mp):
        cod = int(input('Ingrese codigo de plan: '))
        mp.modificacclicitacion(cod)
