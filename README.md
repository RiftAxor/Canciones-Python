# Aesthetic Terminal Lyrics 🎵💻

¡Bienvenido! Este repositorio contiene una colección de scripts en Python diseñados para imprimir letras de canciones en la terminal con un **efecto de máquina de escribir sincronizado al ritmo de la música**. 

Están optimizados para tener una estética limpia (texto blanco brillante sobre fondo negro, sin espacios extra y con emojis), ideal para grabar la pantalla y crear videos para **TikTok, Instagram Reels o YouTube Shorts**.

## Características
- **Efecto de escritura:** Letra por letra simulando un hacker/programador.
- **Sincronización:** Tiempos de pausa y velocidad ajustados para encajar con los fragmentos de las canciones reales.
- **Estética:** Uso de códigos ANSI para resaltar el texto (Blanco Brillante) sobre el fondo oscuro de la terminal.

## 🎶 Canciones incluidas en el repositorio
Actualmente, el repositorio cuenta con scripts sincronizados para los siguientes temazos:

* **Morat**
  * Al aire
  * Nunca te olvidé
  * Amor con hielo
  * Consejo de amor (ft. Tini)
  * Te lo advertí
  * Causa perdida (Coro y Puente)
  * Me toca a mí
  * Mi vida entera
  * Aprender a quererte
  * Otras se pierden
  * Eclipse solar
  * La bella y la bestia (ft. Reik)
  * simplemente pasan
* **Los Caligaris** - Kilómetros
* **Eddy Herrera** - Tú eres ajena
* **Grupo Frontera** - Coqueta
* **Andrés Cepeda** - Día tras día

## 🛠️ ¿Cómo usarlo?

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/RiftAxor/Canciones-Python.git


  Abre tu editor favorito (Recomendado: Visual Studio Code para usar la terminal integrada).  
  Ejecuta el script: 
    
   Abre el archivo de la canción que quieras grabar y ejecútalo con Python:

    python nombre_del_archivo.py

    
## ⚙️ ¿Cómo crear tu propia canción?

  Si quieres añadir una nueva canción, solo tienes que modificar la lista *letra* en cualquiera de los scripts. Funciona con una estructura de tuplas:
  
    letra =[
      ("Frase de la canción 🚀", velocidad_de_escritura, pausa_despues_de_la_frase),
      ("Siguiente frase ❤️", 0.05, 1.2)
    ]
    
  Velocidad de escritura: 0.05 es un buen estándar. Bájalo a 0.04 si cantan muy rápido.
  Pausa: Son los segundos de espera antes de imprimir la siguiente línea.
  
## 🤝 Contribuciones
  ¡Las contribuciones son bienvenidas! Si sincronizas una canción nueva que quede brutal, haz un fork del repositorio, añade tu script y envía un pull request.

    
