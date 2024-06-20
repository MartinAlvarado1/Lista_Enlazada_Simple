class Jugador():
    
    def __init__(self, nombre, numero, posicion):
        self.nombre=nombre
        self.numero=numero
        self.posicion=posicion
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Número: {self.numero}, Posición: {self.posicion}"