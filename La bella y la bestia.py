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

def cantar_bella_y_bestia_ajustada():
    print("\n") # Espacio inicial

    # ESTRUCTURA: (Frase con Emoji, Velocidad letra, Pausa final)
    # Tiempos ajustados para frases cortas y continuas
    
    letra =[
        ("Y si se apaga la luna 🌑", 0.05, 0.2), # Pausa muy corta porque conecta rápido
        ("y si se van las estrellas ✨", 0.05, 0.6),
        
        ("Y si se calla la música que me inventé por ella 🔇🎸", 0.045, 0.8), # Línea larga, va rápido
        
        ("Tal vez se acabe esta noche 🌃", 0.05, 0.2),
        ("tal vez se borren sus huellas 👣", 0.05, 0.6),
        
        ("Tal vez termine esta historia de una bestia 🐺📖", 0.045, 0.2),
        ("sin su bella 🥀", 0.06, 0.8),
        
        ("que me obliga a no dejarte ⛓️❤️", 0.06, 0.4),
        ("Y no me deja olvidarte 🧠💔", 0.05, 0.3),
        ("y no me deja olvidarte 😭🎶", 0.06, 3.0) # Final dramático
    ]

    for frase, velocidad, pausa in letra:
        imprimir_con_estilo(frase, velocidad, pausa)

if __name__ == "__main__":
    cantar_bella_y_bestia_ajustada()