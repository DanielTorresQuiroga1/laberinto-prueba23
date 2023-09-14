class Laberinto:
    def __init__(self):
        self.laberinto = [
            ['#', '#', '#', '#', '#', '#', '#'],
            ['#', 'P', '.', '.', '.', '.', '#'],
            ['#', '.', '#', '#', '#', '.', '#'],
            ['#', '.', '#', '.', '.', '.', '#'],
            ['#', '.', '#', '#', '#', '#', '#'],
            ['#', '.', '.', '.', '.', '.', '#'],
            ['#', '#', '#', '#', '#', '#', '#']
        ]
        self.posicion_jugador = [1, 1]

    def mostrar(self):
        for fila in self.laberinto:
            print(' '.join(fila))
        print()

    def mover(self, direccion):
        x, y = self.posicion_jugador
        if direccion == '↑' and self.laberinto[x-1][y] == '.':
            self.laberinto[x][y], self.laberinto[x-1][y] = '.', 'P'
            self.posicion_jugador = [x-1, y]
        elif direccion == '↓' and self.laberinto[x+1][y] == '.':
            self.laberinto[x][y], self.laberinto[x+1][y] = '.', 'P'
            self.posicion_jugador = [x+1, y]
        elif direccion == '←' and self.laberinto[x][y-1] == '.':
            self.laberinto[x][y], self.laberinto[x][y-1] = '.', 'P'
            self.posicion_jugador = [x, y-1]
        elif direccion == '→' and self.laberinto[x][y+1] == '.':
            self.laberinto[x][y], self.laberinto[x][y+1] = '.', 'P'
            self.posicion_jugador = [x, y+1]

def main():
    print("¡Bienvenido al juego del laberinto de texto!")
    nombre = input("Por favor, introduce tu nombre: ")
    print(f"Hola, {nombre}. ¡Prepárate para comenzar la aventura!")
    
    juego = Laberinto()
    juego.mostrar()
    while True:
        movimiento = input('Mueve con las teclas ↑ ↓ ← → (o escribe "salir" para terminar): ')
        if movimiento in ['↑', '↓', '←', '→']:
            juego.mover(movimiento)
            juego.mostrar()
        elif movimiento == 'salir':
            break

if __name__ == '__main__':
    main()