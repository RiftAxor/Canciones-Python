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

def cantar_me_toca_a_mi():
    print("\n") # Espacio inicial

    # ESTRUCTURA: (Frase con Emoji, Velocidad letra, Pausa final)
    # Tiempos ajustados para el sentimiento y ritmo del estribillo
    
    letra =[
        ("Perdona si nuestra amistad se llega a joder 🤝💔", 0.05, 1.0),
        ("Pero me vuelvo a preguntar 🤔", 0.06, 0.8),
        ("¿Por qué me toca a mí? 🤷‍♂️😫", 0.07, 1.2),
        
        ("Tenerte, tragarme un 'te quiero' (oh-oh) 🤐❤️", 0.05, 1.0),
        ("Fingir que estoy hecho de acero 🛡️🤖", 0.05, 1.0),
        
        ("Siempre, siempre que te veo llegar con alguien más 👫💔", 0.045, 1.2), # Más rápida por ser larga
        
        ("¿Por qué me toca a mí? (A mí) 🤦‍♂️", 0.06, 1.0),
        
        ("Vivir disfrazado de amigo (de amigo) 🎭👫", 0.05, 1.0),
        ("Si yo quiero todo contigo (yo quiero todo contigo) 🌌❤️", 0.045, 1.2), # Rápida para entrar en ritmo
        
        ("Siempre, siempre, no pienso quererte a la mitad 🌗🛑", 0.05, 1.2),
        ("¿Por qué me toca a mí? (¿Por qué me toca a mí?) 😫🎶", 0.07, 3.0) # Dramática al final
    ]

    for frase, velocidad, pausa in letra:
        imprimir_con_estilo(frase, velocidad, pausa)

if __name__ == "__main__":
    cantar_me_toca_a_mi()