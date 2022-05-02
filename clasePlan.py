class PlanAhorro:
    __codigo = 0
    __modelo = ''
    __version = ''
    __valor = 0.0
    __cantcuotas = 0
    __cp = 0
    __valorcuota = 0.0

    def __init__(self, cod, mod, ver, val, cc, cpag):
        self.__codigo = cod
        self.__modelo = mod
        self.__version = ver
        self.__valor = val
        self.__cantcuotas = cc
        self.__cp = cpag
        self.__valorcuota = (float(self.__valor)/float(self.__cantcuotas)) + float(self.__valor) * 0.10

    def actuplan(self):
        print(self.__codigo, self.__modelo, self.__version)
        self.__valor = float(input('Ingrese valor nuevo del vehiculo '))
        print('NUEVO VALOR DEL VEHICULO {}: {}'.format(self.__modelo, self.__valor))

    def cuotainferior(self, valordado):
        if self.__valorcuota < valordado:
            print(self.__codigo, self.__modelo, self.__version)

    def licitacion(self):
        x = float(self.__cp) * self.__valorcuota
        print('VALOR NECESARIO PARA LICITAR EL VEHICULO: {}'.format(x))

    def modificacuot(self, cod):
        if cod==self.__codigo:
            self.__cp = int(input('Ingrese nueva cantidad de cuotas para licitar '))
            return
