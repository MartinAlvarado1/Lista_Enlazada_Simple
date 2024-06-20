from ListaEnlazada import ListaEnlazada
from jugador import Jugador
miLista=ListaEnlazada()
numero=0
opcion=0

print("-----------------ALINEACIONES EQUIPO-----------------")
while opcion != 6:
    opcion=int(input("Digite la opcion que requiera \n"
              "1.Crear Alineación \n"
              "2.Mostrar Alineación \n"
              "3.Buscar un jugador \n"
              "4.Cambiar un jugador \n"
              "5.Expulsar un jugador \n"
              "6.Salir: \n"))
    match opcion:
        case 1:
            for x in range(11):
                nombre=input("Digite el nombre del jugador: ")
                numero= int(input("Digite el numero de camiseta del jugador: "))
                posición=input(f"Digite la pocisión del jugador {nombre}: ")
                jugadorNuevo=Jugador(nombre,numero,posición)
                miLista.insertarNodo(jugadorNuevo)
        case 2: 
            print(miLista.mostrarLista())
        
        case 3:
            numero=int(input("Digite el numero del jugador que desea buscar: "))
            jugador = miLista.buscar_lista(numero)
            if jugador:
                print(jugador.get_dato())
            else:
                print("Jugador no encontrado")
        case 4:
            numero = int(input("Digite el numero del jugador que desea cambiar: "))
            nuevo_nombre = input("Digite el nuevo nombre del jugador: ")
            nuevo_numero = int(input("Digite el nuevo numero del jugador: "))
            nueva_posicion = input(f"Digite la nueva posición del jugador {nuevo_nombre}: ")
            if miLista.modificar_lista(numero, nuevo_nombre, nuevo_numero, nueva_posicion):
                print("Jugador actualizado")
            else:
                print("Jugador no encontrado")     
        case 5:
            numero = int(input("Digite el numero del jugador que desea expulsar: "))
            if miLista.eliminar_nodo(numero):
                print("Jugador expulsado")
            else:
                print("Jugador no encontrado")          
            
        case 6:
            print("Saliendo del programa")
        case _:
            print("Opcion invalida")
            
    

