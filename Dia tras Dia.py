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

def cantar_dia_tras_dia():
    print("\n") # Espacio inicial

    # ESTRUCTURA: (Frase con Emoji, Velocidad letra, Pausa final)
    # Tiempos ajustados para la voz pausada y romántica de Andrés Cepeda
    
    letra =[
        ("Salir al mundo es como caminar en medio de una guerra 🌍⚔️", 0.05, 1.2),
        ("Pero, a tu lado, todo es más seguro porque encuentro paz 🫂🕊️", 0.05, 1.2),
        ("Le pido al cielo que te proteja ☁️🙏", 0.06, 1.5), # Pausa antes de subir la emoción
        
        ("Que siempre estemos igual 👫♾️", 0.06, 1.0),
        ("Que me ames igual ❤️🥺", 0.06, 1.2),
        ("Yo quiero estar contigo el resto de mi vida 🕰️💍", 0.05, 1.5),
        
        ("Que podamos estar juntos hasta el final 🌅💞", 0.05, 1.2),
        ("Poderme despertar con tu sonrisa ☀️😊", 0.06, 1.0),
        
        ("Es mi alegría ✨🥰", 0.07, 1.0),
        ("Día tras día 🗓️💖", 0.08, 3.0) # Final lento y muy dulce
    ]

    for frase, velocidad, pausa in letra:
        imprimir_con_estilo(frase, velocidad, pausa)

if __name__ == "__main__":
    cantar_dia_tras_dia()