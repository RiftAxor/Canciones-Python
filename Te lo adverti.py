import sys
import time

def imprimir_con_estilo(frase, velocidad_escritura, pausa_al_final):
    # Código ANSI para Blanco Brillante (Negrita)
    blanco_brillante = '\033[1;37m'
    reset = '\033[0m'

    sys.stdout.write(blanco_brillante) 
    
    for caracter in frase:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(velocidad_escritura) # Velocidad de escritura
    
    # Reseteamos el color y bajamos de línea (sin espacios extra)
    print(reset) 
    
    # Esperamos a que la canción avance
    time.sleep(pausa_al_final)

def cantar_te_lo_adverti():
    print("\n") # Espacio inicial

    # ESTRUCTURA: (Frase con Emoji, Velocidad letra, Pausa final)
    # Ajustado para el ritmo de Morat en esta canción
    
    letra = [
        ("No te estés apresurando ✋🛑", 0.07, 1.0),
        ("Tómate tu tiempo que esto es importante y antes ⏳👀", 0.05, 0.4), # Rápida porque conecta con la siguiente
        ("De salir por esa puerta 🚪🏃", 0.06, 0.8),
        ("Solo ten en cuenta, no es un viaje de ida y vuelta 🎫🔄", 0.07, 1.5),
        
        ("Y si no hay vuelta atrás 🚫🔙", 0.06, 0.9),
        ("Yo solo sé que verás que... 👁️🔮", 0.06, 0.6),
        ("Estás buscando algo que ya tienes 🔎❤️", 0.05, 2.0), # Pausa musical
        
        ("Entonces sigue tu camino 🚶‍♂️🛣️", 0.06, 1.0),
        ("Yo te cedo el paso, claramente es necesario 🚦👐", 0.08, 0.5),
        ("El que yo te dé un espacio 🌌🧘", 0.06, 1.5),
        
        ("Y si no hay vuelta atrás 🚫🔙", 0.06, 0.9),
        ("Yo solo sé que verás que... 👁️🔮", 0.06, 0.6),
        ("Estás buscando algo que ya tienes 🔎💎", 0.065, 3.0)
    ]

    for frase, velocidad, pausa in letra:
        imprimir_con_estilo(frase, velocidad, pausa)

if __name__ == "__main__":
    cantar_te_lo_adverti()