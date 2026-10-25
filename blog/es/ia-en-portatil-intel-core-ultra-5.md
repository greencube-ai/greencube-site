# ¿Puede un portátil con Intel Core Ultra 5 ejecutar IA? Medido: 14–18 tokens por segundo

> Prueba real: Gemma 4 E2B escribía 14–18 tokens por segundo en un portátil sin tarjeta gráfica (Intel Core Ultra 5 125U) y 16 GB de RAM. Qué significa para chatear, estudiar e imágenes.

Canonical: https://blog.greencube.app/blog/es/ia-en-portatil-intel-core-ultra-5  
Published: 2026-10-14  
Author: Hector Gras

**Sí.** En un portátil sin tarjeta gráfica (Intel Core Ultra 5 125U) y 16 GB de RAM, Gemma 4 E2B escribía 14–18 tokens por segundo. Más rápido de lo que lees.

- **14–18** tokens por segundo con Gemma 4 E2B
- **2:02–2:38 min** para crear una imagen
- **8–10** con Gemma 4 E4B

## Qué significa en la práctica

| Tarea | Tiempo en este PC |
| --- | --- |
| Escribir una respuesta normal (400 tokens, media página) | **22–29 s** |
| Crear una imagen (512×512, gráficos integrados) | **2:02–2:38 min** |
| Crear una imagen (512×512, solo procesador) | **11:27–13:32 min** |

Calculado a partir de las velocidades medidas en este PC: el tiempo es la longitud dividida entre la velocidad, y una respuesta real tarda además un momento en arrancar. Para hacerte una idea, una persona lee unas 4 palabras por segundo ([Brysbaert, 2019](https://doi.org/10.1016/j.jml.2019.104047)), así que solo leer una respuesta de 400 tokens te lleva más de un minuto.

## Lo que medimos

**Escribir** es la velocidad a la que la IA teclea su respuesta, en tokens por segundo; un token es un trozo de palabra, y en español cada palabra suele ocupar uno o dos. **Leer** es lo rápido que asimila lo que le das: tu pregunta, un texto pegado o un PDF. Leer siempre es mucho más rápido que escribir, porque la IA puede leer muchos tokens a la vez pero tiene que escribirlos de uno en uno.

| Qué | Dónde | Resultado | Medido |
| --- | --- | --- | --- |
| Gemma 4 E2B | solo procesador | **14–18** tokens por segundo escribiendo | 28 de septiembre de 2026 [1] |
| Gemma 4 E4B | solo procesador | **8–10** tokens por segundo escribiendo | 28 de septiembre de 2026 [1] |
| Imagen (512×512) | gráficos Intel integrados | **2:02–2:38 min** | 27 de septiembre de 2026 [2] |
| Imagen (512×512) | solo procesador | **11:27–13:32 min** | 14 de octubre de 2026 [2] |

Cómo se midió cada número: [Más sobre cómo medimos](https://blog.greencube.app/blog/es/como-medimos-la-velocidad-de-la-ia)

1. La prueba de velocidad de llama.cpp (llama-bench), el motor sobre el que funciona GreenCube, con los mismos archivos de IA: escribe 128 tokens y lee un texto de 512.
2. El motor de imágenes de GreenCube (Z-Image Turbo), 512×512 píxeles y 8 pasos, cronometrado desde el clic hasta la imagen terminada.

Cuando tenemos varias pruebas damos el rango: la velocidad varía un poco entre pruebas en el mismo PC.

## Qué significa

### ¿Sin tarjeta gráfica? Funciona igual

Sin tarjeta gráfica, la IA funciona en el procesador. Va más lenta que en un PC gaming, pero la pequeña, Gemma 4 E2B, escribe 14–18 tokens por segundo, suficiente para estudiar, resumir y escribir. La más grande, Gemma 4 E4B, también funciona, a 8–10: más lista, pero en respuestas largas se nota la espera.

### Imágenes

Sí. Una imagen (512×512) tardó 2:02–2:38 min con los gráficos Intel integrados, y 11:27–13:32 min con solo el procesador. Una imagen usa su propia IA, de unos 6 GB, y muchas más cuentas que una respuesta de chat, así que aquí los gráficos importan todavía más.

## Cómo se compara

De los 2 PCs que medimos con Gemma 4 E2B, este es el **número 1** en velocidad de escritura. El [portátil con Intel Iris Xe](https://blog.greencube.app/blog/es/ia-en-portatil-intel-iris-xe) escribe 5–7, así que este va unas 2,5 veces más rápido.

## El PC de la prueba

El PC de un tester real, usado como lo usa siempre, no una máquina de laboratorio:

- Portátil
- **Gráfica:** solo gráficos Intel integrados
- **Memoria gráfica (VRAM):** ninguna (sin tarjeta gráfica aparte)
- **RAM:** 16 GB
- **Procesador:** Intel Core Ultra 5 125U, 14 hilos

## Mira tu propio PC

¿No sabes qué tiene tu PC? Se mira en 30 segundos:

1. Pulsa **Ctrl + Mayús + Esc** para abrir el Administrador de tareas.
2. Ve a **Rendimiento**.
3. Pulsa **Memoria**: el número de arriba a la derecha es tu RAM.
4. Pulsa **GPU**: el nombre de arriba a la derecha es tu tarjeta, y **Memoria de GPU dedicada** es tu VRAM. ¿Solo ves gráficos Intel o AMD sin memoria dedicada? Entonces no tienes tarjeta aparte.

Después busca la tarjeta más parecida en [la tabla completa](https://blog.greencube.app/blog/es/ia-en-mi-pc). La misma tarjeta con más VRAM puede con una IA más grande; una tarjeta más nueva del mismo tamaño suele ir más rápido.

## Otros PCs que medimos

- [RTX 2080 Ti](https://blog.greencube.app/blog/es/ia-en-rtx-2080-ti): 65–71 tokens por segundo (Gemma 4 E4B)
- [RX 5700 XT](https://blog.greencube.app/blog/es/ia-en-rx-5700-xt): 63–72 tokens por segundo (Gemma 4 E4B)
- [RTX 5060](https://blog.greencube.app/blog/es/ia-en-rtx-5060): 56 tokens por segundo (Gemma 4 E4B)
- [RTX 3060](https://blog.greencube.app/blog/es/ia-en-rtx-3060): 53–55 tokens por segundo (Gemma 4 E4B)
- [RX 6600](https://blog.greencube.app/blog/es/ia-en-rx-6600): 42–44 tokens por segundo (Gemma 4 E4B)
- [GTX 1660 Super](https://blog.greencube.app/blog/es/ia-en-gtx-1660-super): 37–38 tokens por segundo (Gemma 4 E4B)
- [GTX 1650](https://blog.greencube.app/blog/es/ia-en-gtx-1650): unos 20 tokens por segundo (Gemma 4 E4B)
- [RX 580](https://blog.greencube.app/blog/es/ia-en-rx-580): 10–11 tokens por segundo (Gemma 4 E4B)
- [portátil con Intel Iris Xe](https://blog.greencube.app/blog/es/ia-en-portatil-intel-iris-xe): 5–7 tokens por segundo (Gemma 4 E2B)

[¿Puedo usar IA en mi PC?](https://blog.greencube.app/blog/es/ia-en-mi-pc) Los 10 PCs en una tabla, y cómo irá el tuyo.

## FAQ

### ¿Puede un portátil con Intel Core Ultra 5 ejecutar IA en local?

Sí. En un portátil sin tarjeta gráfica (Intel Core Ultra 5 125U) y 16 GB de RAM, Gemma 4 E2B escribía 14–18 tokens por segundo. Más rápido de lo que lees.

### ¿Puede un portátil con Intel Core Ultra 5 crear imágenes con IA?

Sí. Una imagen (512×512) tardó 2:02–2:38 min con los gráficos Intel integrados, y 11:27–13:32 min con solo el procesador.
