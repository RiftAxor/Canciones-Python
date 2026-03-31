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

def cantar_consejo_de_amor():
    print("\n") # Espacio inicial

    # ESTRUCTURA: (Frase con Emoji, Velocidad letra, Pausa final)
    # Tiempos ajustados para el ritmo de Morat y Tini
    
    letra = [
        ("Pude haber sido yo... 🙋‍♂️💔", 0.08, 1.5),
        ("Pero dejaste un loco enamorado 🤪💘", 0.06, 1.2),
        ("Buscando un beso tuyo en la estación 🚉💋", 0.06, 1.3),
        
        ("Y no hay peor desgracia que extrañar lo que nunca pasó 😢🚫", 0.045, 1.0), # Un poco más rápido por ser larga
        
        ("Pude haber sido yo (oh-oh-oh) 🎶🙋‍♀️", 0.06, 1.2),
        ("La que a tu lado siempre se despierte 🛌☀️", 0.05, 1.1),
        ("Pero el futuro nunca nos llegó (nos llegó) 🔮❌", 0.05, 1.2),
        
        ("Me prometí que nunca iba a perderte... 🤞🖇️", 0.05, 0.5),
        ("Y no sé qué pasó 🤷‍♂️🥀", 0.06, 1.0),
        
        ("Pude haber sido yo, oh (pude haber sido yo) 🎤✨", 0.05, 1.0),
        
        ("Si tú tan solo me hubieras pedido un consejo de amor 📜❤️", 0.06, 1.5),
        ("Oh-oh-oh-oh, oh-oh 🎵🔚", 0.1, 3.0)
    ]

    for frase, velocidad, pausa in letra:
        imprimir_con_estilo(frase, velocidad, pausa)

if __name__ == "__main__":
    cantar_consejo_de_amor()