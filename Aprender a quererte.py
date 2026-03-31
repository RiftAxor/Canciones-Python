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

def cantar_aprender_a_quererte():
    print("\n") # Espacio inicial

    # ESTRUCTURA: (Frase con Emoji, Velocidad letra, Pausa final)
    # Tiempos ajustados para el ritmo acústico de Morat
    
    letra =[
        ("Para aprender a quererte 📖🩶", 0.06, 0.8),
        ("Voy a estudiar cómo se cumplen tus sueños 🤓💭", 0.05, 1.0),
        ("Voy a leerte siempre muy lentamente 📚🐢", 0.05, 0.8),
        ("Quiero entenderte 🧠💡", 0.07, 1.2), # Más lento y con pausa marcada
        
        ("Cuando te vi, tuve un buen presentimiento 👀✨", 0.05, 1.0),
        ("De esos que llegan una vez en la vida ☝️🌠", 0.05, 1.0),
        ("Quiero tenerte aunque sea solo un momento ⏳🫂", 0.05, 1.0),
        ("Y si me dejas, tal vez todos los días 🗓️💞", 0.05, 1.3),
        
        ("No sé nada de tu historia 🤷‍♂️📜", 0.06, 0.8),
        ("Ni de tu filosofía 🤔🏛️", 0.06, 0.8),
        ("Hoy te escribo sin pensar ✍️💨", 0.06, 0.9),
        ("Y sin ortografía 📝❌", 0.08, 3.0) 
    ]

    for frase, velocidad, pausa in letra:
        imprimir_con_estilo(frase, velocidad, pausa)

if __name__ == "__main__":
    cantar_aprender_a_quererte()