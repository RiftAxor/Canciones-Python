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

def cantar_eclipse_solar():
    print("\n") # Espacio inicial

    # ESTRUCTURA: (Frase con Emoji, Velocidad letra, Pausa final)
    # Tiempos ajustados desde la calma inicial hasta el gran coro
    
    letra =[
        ("Mi vida ahora se ve 🫥👀", 0.07, 0.8),
        ("Como nadar a oscuras en el fondo del mar 🌊🤿", 0.05, 1.0),
        ("Como llegar al cielo para luego bajar ☁️📉", 0.05, 1.0),
        ("Mi canción favorita no volverla a escuchar, qué duro me da 🎧💔", 0.045, 1.2), # Más rápida por ser tan larga
        
        ("Pero, ¿cuántos besos nos prestábamos? 💋🤔", 0.05, 0.8),
        ("Que en el fondo nos debíamos 🧾❤️", 0.06, 0.8),
        ("Yo no entiendo cómo acabamos 🤷‍♂️🥀", 0.06, 0.8),
        ("No había dolido tanto un amanecer (no) 🌅🤕", 0.05, 1.2), # Pausa dramática antes del coro
        
        ("Estar contigo fue como un eclipse solar 🌒☀️", 0.05, 1.2),
        ("Que puede que en mi vida nunca vuelva a pasar 🚫⏳", 0.05, 1.2),
        
        ("Aquí me tienes otra vez 🙋‍♂️🔄", 0.06, 0.8),
        ("Aquí me tienes otra vez 🙋‍♂️🔄", 0.06, 0.8),
        
        ("Si no existe un futuro en el que te convencí 🔮🗣️", 0.05, 1.0),
        ("Si no hay una galaxia en la que pueda olvidar 🌌🧠", 0.05, 1.0),
        
        ("Aquí me tienes otra vez (mi vida) 🙋‍♂️❤️‍🩹", 0.06, 1.0),
        ("Porque sé que después de ti no hay un después 🔚🖤", 0.07, 3.0) 
    ]

    for frase, velocidad, pausa in letra:
        imprimir_con_estilo(frase, velocidad, pausa)

if __name__ == "__main__":
    cantar_eclipse_solar()