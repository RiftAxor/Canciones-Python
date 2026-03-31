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

def cantar_mi_vida_entera():
    print("\n") # Espacio inicial

    # ESTRUCTURA: (Frase con Emoji, Velocidad letra, Pausa final)
    # Tiempos ajustados para las pausas del inicio y la rapidez del final
    
    letra =[
        ("Y si bailamos, tan sólo bailamos 💃🕺", 0.06, 1.0),
        ("Y si tus pies nuestra historia escribieran 👣✍️", 0.05, 1.0),
        ("Como si fuera este el final de un cuento 📖🏰", 0.05, 1.0),
        ("Y nadie más en el mundo existiera 🌍🤫", 0.06, 1.2),
        
        ("Y si bailamos, tan solo bailamos 🎶💃", 0.06, 1.0),
        ("Al ritmo y paso que tú prefieras 🥁❤️", 0.05, 1.0),
        ("Voy a rogarle sin descanso al tiempo ⏳🙏", 0.05, 1.0),
        ("Que esta canción dure mi vida entera 🎵♾️", 0.06, 0.8),
        ("Que esta canción dure mi vida entera 🎧💖", 0.06, 1.5), # Pausa un poco más larga antes del cambio de ritmo
        
        ("Sinceramente sólo siento pánico en escena 🎭😰", 0.045, 0.8), # Aquí acelera la canción
        ("Y sostenerte la mirada me quema 👀🔥", 0.05, 0.9),
        ("Pero que hoy vivas con mi amor corriendo por tus venas 🩸❤️‍🔥", 0.045, 0.8),
        ("Es por robarme el corazón tu condena ⚖️💘", 0.05, 1.0),
        
        ("Y es que al fin si te casas con un loco 💍🤪", 0.05, 0.8),
        ("Vas a ver que es la magia poco a poco ✨🎩", 0.05, 0.8),
        ("No podrás distinguir entre besos y palabras 💋🗣️", 0.045, 0.8),
        ("Un te quiero no me alcanza 🤏❤️", 0.06, 1.0),
        ("Dame todo, di que sí 🥺💍", 0.08, 3.0) # Final con mucha fuerza
    ]

    for frase, velocidad, pausa in letra:
        imprimir_con_estilo(frase, velocidad, pausa)

if __name__ == "__main__":
    cantar_mi_vida_entera()