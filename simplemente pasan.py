import sys
import time

def imprimir_con_estilo(frase, velocidad_escritura, pausa_al_final):
    # Código ANSI para Cyan/Celeste Brillante (Negrita)
    color_cyan = '\033[1;36m'
    reset = '\033[0m'

    sys.stdout.write(color_cyan) 
    
    for caracter in frase:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(velocidad_escritura) # Efecto de máquina de escribir
    
    # Reseteamos el color y bajamos de línea
    print(reset) 
    
    # Esperamos a que la canción avance a la siguiente frase
    time.sleep(pausa_al_final)

def cantar_simplemente_pasan():
    print("\n") # Espacio inicial

    # ESTRUCTURA: ("Frase con Emoji", Velocidad de letra, Pausa al final de la frase)
    
    letra = [
        ("No tengo las palabras de un poeta, pero moría por verla bailar ✍️💃", 0.05, 0.4),
        ("Conmigo ✨", 0.08, 0.8),
        ("Que bailara una de Juan Luis por siempre conmigo 🎶🕺", 0.05, 0.6),
        ("Y emborracharnos por la ciudad con Dios de testigo 🍻🌃", 0.05, 0.8),
        
        ("Ya quiero decirle... 🗣️❤️", 0.06, 1.2),
        
        ("Que bailemos 🪩✨", 0.07, 1.0),
        ("Que lo peor que puede pasar es que nos gustemos 😏💖", 0.045, 0.6),
        ("Que a lo mejor de alguna otra vida nos conocemos 🌌🔮", 0.045, 0.8),
        
        ("Ay, qué suerte la mía que hoy te volví a encontrar 🍀👀", 0.05, 0.4),
        ("En este lugar 📍", 0.07, 0.8),
        
        ("Porque cuando las cosas buenas tienen que pasar 🌟💫", 0.05, 0.8),
        ("Simplemente pasan ✨🕊️", 0.09, 2.0)
    ]

    for frase, velocidad, pausa in letra:
        imprimir_con_estilo(frase, velocidad, pausa)

if __name__ == "__main__":
    cantar_simplemente_pasan()