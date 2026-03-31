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

def cantar_otras_se_pierden():
    print("\n") # Espacio inicial

    # ESTRUCTURA: (Frase con Emoji, Velocidad letra, Pausa final)
    # Tiempos ajustados para la fuerza del coro y el puente rápido
    
    letra =[
        ("Te hacen falta tantas noches en vela 🦉🌛", 0.05, 0.9),
        ("De esas que al doler solo te hacen más fuerte (¡eh!) 💪🩹", 0.045, 1.2),
        ("Porque si el amor es un juego sin reglas 🎲🚫", 0.05, 0.9),
        ("Unas se ganan y otras se pierden (¡eh!) 🏆📉", 0.05, 1.2),
        
        ("Te hacen falta tantas noches en vela 🦉🌛", 0.05, 0.9),
        ("No se aprende a amar ni se olvida por suerte (¡eh!) 🍀🧠", 0.045, 1.2),
        ("Porque en el amor pasa igual que en la guerra ⚔️❤️", 0.05, 0.9),
        ("Unas se ganan y otras se pierden 🏆📉", 0.05, 1.5), # Pausa un poco mayor antes del puente
        
        ("Para olvidar no hay atajos (no, oh-oh) 🚧🛤️", 0.06, 1.0),
        ("Su nombre quiebra tu voz (su nombre quiebra todo) 🗣️💔", 0.05, 1.0),
        ("Pero el tiempo hace el trabajo de juntar los pedazos ⏳🧩", 0.045, 0.5), # Muy rápida por la cantidad de palabras
        ("si se rompe el amor 💔🥀", 0.08, 3.0) # Final dramático y más lento
    ]

    for frase, velocidad, pausa in letra:
        imprimir_con_estilo(frase, velocidad, pausa)

if __name__ == "__main__":
    cantar_otras_se_pierden()