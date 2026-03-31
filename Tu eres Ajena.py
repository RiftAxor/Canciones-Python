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

def cantar_ajena():
    print("\n") # Espacio inicial

    # ESTRUCTURA: (Frase con Emoji, Velocidad letra, Pausa final)
    # Ajustado para el ritmo de la estrofa romántica del merengue
    
    letra = [
        ("Que me engañabas, que me hablabas mentiras 💭👰", 0.07, 1.0),
        ("Dejaste que de ti me enamorara 😍💘", 0.07, 1.2),
        ("Y me acostumbrara solamente a tu cariño 🤗❤️", 0.06, 1.3),
        ("Y ahora estoy pagando mi condena ⛓️😓", 0.07, 1.5),
        ("Tú no debiste estar conmigo 💍🚫", 0.05, 1.2),
        ("siendo ajenaaaa...😫🎺", 0.05, 1.5)
    ]

    for frase, velocidad, pausa in letra:
        imprimir_con_estilo(frase, velocidad, pausa)

if __name__ == "__main__":
    cantar_ajena()