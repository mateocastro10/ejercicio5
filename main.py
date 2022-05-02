from claseManejador import Lista
from menu import claseMenu

if __name__ == '__main__':
    mp = Lista()
    mp.test()
    xmenu = claseMenu()
    b = False
    while not b:
        print('-------MENU DE OPCIONES-------')
        print(
            'opcion 1: Actualizar el valor del vehículo de cada plan \nopcion 2: Dado un valor, mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado.\nopcion 3:  Mostrar el monto que se debe haber pagado para licitar el vehículo\nopcion 4: modificar la cantidad cuotas que debe tener pagas para licitar.\nopcion 5:salir')
        op = int(input('seleccione opcion'))
        if op == 0 or op>5:
            print('OPCION INCORRECTA')
        else:
            b = True
            xmenu.opcion(op, mp)
