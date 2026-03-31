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

def cantar_coqueta():
    print("\n") # Espacio inicial

    # ESTRUCTURA: (Frase con Emoji, Velocidad letra, Pausa final)
    # Tiempos ajustados para el ritmo cumbia/urbano
    
    letra = [
        ("Pensando y viendo las estrellas, pregunté 🌌🤔", 0.06, 1.0),
        ("Si en algún lugar esto se estaría repitiendo 🔁🌍", 0.05, 1.0),
        ("Si es que en otro mundo, tal vez, nos ganó el deseo ❤️‍🔥🛸", 0.05, 1.0),
        ("O si solo fuimos un error del universo 🌠❌", 0.06, 1.5),
        
        ("Baby, bésame 💋😗", 0.08, 0.8), # Lento y con énfasis
        
        ("Quiero que vuelvas a mis brazos pa sentirnos eternos 🫂♾️", 0.05, 0.6), # Rápido (flow)
        ("Como la última vez 🔙🕰️", 0.07, 1.2),
        
        ("Quiero confesarte: te extraño, como un loco te pienso 🤪📝", 0.05, 0.8),
        ("Yo sé que tú también 👁️✨", 0.07, 1.2),
        
        ("Porfa, ma, ya vuelve conmigo, pero no como amigos 👫🚫", 0.05, 0.6), 
        ("Como la última vez 🔙🔥", 0.07, 1.0),
        
        ("Quiero confesarte: te extraño, como un loco te pienso 🧠💭", 0.05, 0.8),
        ("Yo sé que tú también... ❤️🤠", 0.08, 3.0)
    ]

    for frase, velocidad, pausa in letra:
        imprimir_con_estilo(frase, velocidad, pausa)

if __name__ == "__main__":
    cantar_coqueta()