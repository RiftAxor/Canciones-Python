import sys
import time

def imprimir_con_estilo(frase, velocidad_escritura, pausa_al_final):
    # Código ANSI para Blanco Brillante (Negrita)
    blanco_brillante = '\033[1;37m'
    reset = '\033[0m'

    sys.stdout.write(blanco_brillante) # Ponemos el color
    
    for caracter in frase:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(velocidad_escritura) # Velocidad de escritura
    
    # Reseteamos el color
    sys.stdout.write(reset)
    
    # Salto de línea simple (sin espacios extra)
    print("") 
    
    # Esperamos a que la canción avance
    time.sleep(pausa_al_final)

def cantar_kilometros():
    print("\n") # Un pequeño espacio al inicio para que no se pegue al borde

    # ESTRUCTURA: (Frase con Emoji, Velocidad letra, Pausa final)
    letra = [
        ("Cada vez que pienso 🤔", 0.08, 1.3),
        ("Hoy me doy cuenta donde estoy y entiendo menos 🗺️", 0.05, 1.0),
        ("Nunca supe bien por qué ni en qué momento 🕑", 0.05, 1.1),
        ("Me empezó a ganar a mí este sentimiento ❤️", 0.06, 1.5),
        ("Tan buenos momentos ✨", 0.09, 1.0),
        ("Tanto andar como el Quijote contra el viento 🌬️", 0.045, 0.8),
        ("Tanto miedo de vivir en la aventura 🙀", 0.045, 0.8),
        ("De tratar de ser feliz con mi locura 🤪", 0.045, 1.0),
        ("Tantos amigos, tantas cervezas 🍻", 0.06, 0.9),
        ("Tantos bagartos, tantas princesas 🐸👸", 0.06, 0.9),
        ("Las razones que me hacen aguantar... 💪🤡", 0.1, 4.0)
    ]

    for frase, velocidad, pausa in letra:
        imprimir_con_estilo(frase, velocidad, pausa)

if __name__ == "__main__":
    cantar_kilometros()