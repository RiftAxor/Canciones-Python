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

def cantar_causa_perdida():
    print("\n") # Espacio inicial

  
    
    letra =[
        ("Y no me voy a perdonar 🙏❌", 0.06, 0.8),
        ("Si conocerte fue una causa perdida 🥀📉", 0.05, 1.0),
        ("Y si no te vuelvo a encontrar 🔍💔", 0.06, 0.9),
        ("Será por mala suerte, no por cobardía 🍀🏃‍♂️", 0.05, 1.1),
        
        ("Tú me lograste enamorar 😍🎯", 0.06, 0.8),
        ("Y aunque podría negarlo una y mil veces 🙅‍♂️🔢", 0.05, 1.0),
        ("Yo no me voy a perdonar 🙏❌", 0.06, 0.8),
        ("Si por nunca admitirlo, tú desapareces 😶‍🌫️👻", 0.05, 1.2),
        
        ("Y no me voy a perdonar 😔🎸", 0.06, 1.2),
        
        ("Oh oh-oh oh-oh oh-oh oh (uoh, oh, oh, oh) 🎶🗣️", 0.06, 1.5),
        ("Oh oh-oh oh-oh oh-oh oh 🎶🥁", 0.06, 1.2),
        
        ("Terminaré lo que empezó la suerte 🎲✍️", 0.05, 0.8),
        ("Y escribiré un final 📖🖋️", 0.06, 0.8),
        ("Donde yo no me paralizo al verte 🥶👀", 0.05, 0.9),
        ("Donde tú no te vas 🚪🚶‍♀️🚫", 0.08, 3.0)
    ]

    for frase, velocidad, pausa in letra:
        imprimir_con_estilo(frase, velocidad, pausa)

if __name__ == "__main__":
    cantar_causa_perdida()