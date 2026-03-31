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

def cantar_nunca_te_olvide():
    print("\n") 

    
    
    letra = [
        ("Yo sé que a ti ya no te asustan con mi nombre (no) 👻", 0.06, 1.2),
        ("Y de seguro no escondes un suspiro si me ves (si me ves) 😮💨", 0.06, 1.3),
        ("Yo sé que a ti te está fallando la memoria 🧠🚫", 0.07, 1.1),
        ("Y a lo peor, nuestra historia ya no cuelga de un 'tal vez' 📜🤷‍♂️", 0.06, 1.4),
        ("Pero si todo sale bien, ya no tendré más pesadillas 💤🛌", 0.08, 1.0),
        ("Ni raspadas las rodillas por rogar ante tus pies 🛐🩹", 0.06, 1.1),
        ("Y si te atreves a volver (oh), te acordarás sin que te diga (ay) 🔙🗣️", 0.05, 1.4),
        ("Que nunca te olvidé... 💔🎶", 0.08, 3.0)
    ]

    for frase, velocidad, pausa in letra:
        imprimir_con_estilo(frase, velocidad, pausa)

if __name__ == "__main__":
    cantar_nunca_te_olvide()