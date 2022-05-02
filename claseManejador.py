import csv
from clasePlan import PlanAhorro

class Lista:
    def __init__(self):
        self.__listaPlanes = []

    def agregarPlan(self, unPlan):
        if(type(unPlan)) == PlanAhorro:
            self.__listaPlanes.append(unPlan)
            print('Plan cargado con éxito')
        else:
            print('ERROR DE DATO EN LA CREACION DEL PLAN')
    def test(self):
        archivo = open('planes.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            cod = int(fila[0])
            mod = fila[1]
            ver = fila[2]
            val = fila[3]
            cc = fila[4]
            cpag = fila[5]
            unPlan = PlanAhorro(cod, mod, ver, val, cc, cpag)
            self.agregarPlan(unPlan)
        archivo.close()

    def actualiza(self):
        for i in range(len(self.__listaPlanes)):
            self.__listaPlanes[i].actuplan()

    def cuotainf(self, valordado):
        if(type(valordado)==float):
            for i in range (len(self.__listaPlanes)):
                self.__listaPlanes[i].cuotainferior(valordado)

    def importelicito(self):
        for i in range (len(self.__listaPlanes)):
            self.__listaPlanes[i].licitacion()

    def modificacclicitacion(self, cod):
        if (type(cod)==int):
            for i in range (len(self.__listaPlanes)):
                self.__listaPlanes[i].modificacuot(cod)
