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

def cantar_amor_con_hielo():
    print("\n") # Espacio inicial

    # ESTRUCTURA: (Frase con Emoji, Velocidad letra, Pausa final)
    # He ajustado la velocidad porque esta canción es rápida.
    
    letra = [
        ("Yo ya me olvidé del nombre de tu perro 🐶", 0.06, 0.9),
        ("Y de esa despedida en la estación 🚉👋", 0.07, 1.0),
        ("Y aunque mi dolor jure que aquí te espero 🤕⏳", 0.07, 0.8),
        ("Otra boca un beso me robó 💋🏃", 0.07, 1.2),
        
        ("Y eso que tú tanto dices que te debo 🗣️💸", 0.08, 0.3),
        ("Se lo llevó... 💨", 0.099, 1.0), # Pausa dramática antes del coro
        
        ("No vengas a cobrarme porque no te debo 🚫💰", 0.075, 0.4),
        ("No te debo nada, uh-oh (hey) 🙅‍♂️🎶", 0.08, 0.9),
        
        ("Ya entendí que no te quiero 💔🧠", 0.075, 0.4),
        ("No te quiero nada, uh-oh (hey) 🚮👋", 0.08, 0.9),
        
        ("Y aunque te extrañé 😿", 0.06, 0.7),
        ("Ya ha pasado tanto tiempo, que te olvidé 🕒🤷‍♂️", 0.075, 0.9),
        
        ("Porque quien pegó primero 🥊💥", 0.07, 0.5),
        ("No es siempre el que gana, uh-oh (hey) 🏆❌", 0.075, 1.1),
        
        ("Yo intenté salvar todo este amor con hielo... 🧊", 0.065, 1.0),
        ("Y se murió 💀🥀", 0.1, 3.0)
    ]

    for frase, velocidad, pausa in letra:
        imprimir_con_estilo(frase, velocidad, pausa)

if __name__ == "__main__":
    cantar_amor_con_hielo()