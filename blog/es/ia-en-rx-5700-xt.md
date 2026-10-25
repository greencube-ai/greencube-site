# ¿Puede una RX 5700 XT ejecutar IA? Medido: 63–72 tokens por segundo

> Prueba real: Gemma 4 E4B escribía 63–72 tokens por segundo en un sobremesa con una AMD RX 5700 XT (8 GB) y 48 GB de RAM. Qué significa para chatear, estudiar e imágenes.

Canonical: https://blog.greencube.app/blog/es/ia-en-rx-5700-xt  
Published: 2026-09-22  
Author: Hector Gras

**Sí.** En un sobremesa con una AMD RX 5700 XT (8 GB) y 48 GB de RAM, Gemma 4 E4B escribía 63–72 tokens por segundo. Más rápido de lo que lees.

- **63–72** tokens por segundo con Gemma 4 E4B
- **14×** más rápido en la tarjeta que en el procesador
- **20–36** con Gemma 4 12B (solo chats cortos)

## Qué significa en la práctica

| Tarea | Tiempo en este PC |
| --- | --- |
| Escribir una respuesta normal (400 tokens, media página) | **6 s** |
| Leer un documento largo que le das (5.000 tokens, unas 6 páginas) | **8 s** |

Calculado a partir de las velocidades medidas en este PC: el tiempo es la longitud dividida entre la velocidad, y una respuesta real tarda además un momento en arrancar. Para hacerte una idea, una persona lee unas 4 palabras por segundo ([Brysbaert, 2019](https://doi.org/10.1016/j.jml.2019.104047)), así que solo leer una respuesta de 400 tokens te lleva más de un minuto.

## Lo que medimos

**Escribir** es la velocidad a la que la IA teclea su respuesta, en tokens por segundo; un token es un trozo de palabra, y en español cada palabra suele ocupar uno o dos. **Leer** es lo rápido que asimila lo que le das: tu pregunta, un texto pegado o un PDF. Leer siempre es mucho más rápido que escribir, porque la IA puede leer muchos tokens a la vez pero tiene que escribirlos de uno en uno.

| Qué | Dónde | Resultado | Medido |
| --- | --- | --- | --- |
| Gemma 4 E4B | tarjeta gráfica | **63–72** tokens por segundo escribiendo · 594–609 leyendo | 22 de septiembre de 2026 |
| Gemma 4 E4B | solo procesador | **5** tokens por segundo escribiendo · 357 leyendo | 22 de septiembre de 2026 |
| Gemma 4 12B | tarjeta gráfica | **20–36** tokens por segundo escribiendo · 108–113 leyendo | 22 de septiembre de 2026 |

Cómo se midió cada número: [Más sobre cómo medimos](https://blog.greencube.app/blog/es/como-medimos-la-velocidad-de-la-ia)

1. La prueba de velocidad de llama.cpp (llama-bench), el motor sobre el que funciona GreenCube, con los mismos archivos de IA: escribe 128 tokens y lee un texto de 512.

Cuando tenemos varias pruebas damos el rango: la velocidad varía un poco entre pruebas en el mismo PC.

## Qué significa

### La tarjeta gráfica hace el trabajo

Mismo PC, misma IA (Gemma 4 E4B): 5 tokens por segundo solo con el procesador y 63–72 con la tarjeta gráfica, unas **14 veces más rápido**. Una gráfica está hecha para hacer miles de cuentas pequeñas a la vez para los juegos, y una IA es sobre todo ese mismo tipo de cálculo. GreenCube cronometra las dos al arrancar y usa la más rápida.

### La IA entera cabe en la tarjeta

Gemma 4 E4B ocupa 4,2 GB y la tarjeta tiene 8 GB de memoria propia (VRAM). Cabe entera, con sitio de sobra para la conversación, así que la tarjeta nunca espera a la memoria más lenta del resto del PC. Esa es la razón principal de que vaya tan rápido.

### La más grande, Gemma 4 12B

Solo para chats cortos. La más grande, Gemma 4 12B (6,4 GB), escribía 20–36 tokens por segundo con una pregunta corta, pero cuando el chat llegó a 8.192 tokens (una conversación larga) se colgó, con la tarjeta casi llena. Por eso GreenCube solo propone la 12B con tarjetas de 10 GB o más.

### Imágenes

Muy probablemente, pero aún no hemos cronometrado una imagen con esta tarjeta. Cuando lo hagamos, el número irá aquí. Una imagen usa su propia IA, de unos 6 GB, y muchas más cuentas que una respuesta de chat, así que aquí los gráficos importan todavía más.

## Cómo se compara

De los 8 PCs que medimos con Gemma 4 E4B, este es el **número 2** en velocidad de escritura. La [RTX 2080 Ti](https://blog.greencube.app/blog/es/ia-en-rtx-2080-ti) escribe 65–71, más o menos lo mismo. La [RTX 5060](https://blog.greencube.app/blog/es/ia-en-rtx-5060) escribe 56 (prueba de arranque), así que este va un 20% más rápido.

Medimos 4 tarjetas de 8 GB, y hay mucha diferencia entre ellas:

- **RX 5700 XT**: 63–72 tokens por segundo
- [RTX 5060](https://blog.greencube.app/blog/es/ia-en-rtx-5060): 56 tokens por segundo (prueba de arranque)
- [RX 6600](https://blog.greencube.app/blog/es/ia-en-rx-6600): 42–44 tokens por segundo
- [RX 580](https://blog.greencube.app/blog/es/ia-en-rx-580): 10–11 tokens por segundo

La memoria decide qué IA cabe. Lo nueva que sea la tarjeta decide lo rápido que va.

## El PC de la prueba

El PC de un tester real, usado como lo usa siempre, no una máquina de laboratorio:

- Sobremesa
- **Gráfica:** AMD RX 5700 XT
- **Memoria gráfica (VRAM):** 8 GB
- **RAM:** 48 GB
- **Procesador:** Intel Core i7-9700, 8 hilos

## Mira tu propio PC

¿No sabes qué tiene tu PC? Se mira en 30 segundos:

1. Pulsa **Ctrl + Mayús + Esc** para abrir el Administrador de tareas.
2. Ve a **Rendimiento**.
3. Pulsa **Memoria**: el número de arriba a la derecha es tu RAM.
4. Pulsa **GPU**: el nombre de arriba a la derecha es tu tarjeta, y **Memoria de GPU dedicada** es tu VRAM. ¿Solo ves gráficos Intel o AMD sin memoria dedicada? Entonces no tienes tarjeta aparte.

Después busca la tarjeta más parecida en [la tabla completa](https://blog.greencube.app/blog/es/ia-en-mi-pc). La misma tarjeta con más VRAM puede con una IA más grande; una tarjeta más nueva del mismo tamaño suele ir más rápido.

## Otros PCs que medimos

- [RTX 2080 Ti](https://blog.greencube.app/blog/es/ia-en-rtx-2080-ti): 65–71 tokens por segundo (Gemma 4 E4B)
- [RTX 5060](https://blog.greencube.app/blog/es/ia-en-rtx-5060): 56 tokens por segundo (Gemma 4 E4B)
- [RTX 3060](https://blog.greencube.app/blog/es/ia-en-rtx-3060): 53–55 tokens por segundo (Gemma 4 E4B)
- [RX 6600](https://blog.greencube.app/blog/es/ia-en-rx-6600): 42–44 tokens por segundo (Gemma 4 E4B)
- [GTX 1660 Super](https://blog.greencube.app/blog/es/ia-en-gtx-1660-super): 37–38 tokens por segundo (Gemma 4 E4B)
- [GTX 1650](https://blog.greencube.app/blog/es/ia-en-gtx-1650): unos 20 tokens por segundo (Gemma 4 E4B)
- [portátil con Intel Core Ultra 5](https://blog.greencube.app/blog/es/ia-en-portatil-intel-core-ultra-5): 14–18 tokens por segundo (Gemma 4 E2B)
- [RX 580](https://blog.greencube.app/blog/es/ia-en-rx-580): 10–11 tokens por segundo (Gemma 4 E4B)
- [portátil con Intel Iris Xe](https://blog.greencube.app/blog/es/ia-en-portatil-intel-iris-xe): 5–7 tokens por segundo (Gemma 4 E2B)

[¿Puedo usar IA en mi PC?](https://blog.greencube.app/blog/es/ia-en-mi-pc) Los 10 PCs en una tabla, y cómo irá el tuyo.

## FAQ

### ¿Puede una RX 5700 XT ejecutar IA en local?

Sí. En un sobremesa con una AMD RX 5700 XT (8 GB) y 48 GB de RAM, Gemma 4 E4B escribía 63–72 tokens por segundo. Más rápido de lo que lees.

### ¿Puede una RX 5700 XT crear imágenes con IA?

Muy probablemente, pero aún no hemos cronometrado una imagen con esta tarjeta. Cuando lo hagamos, el número irá aquí.

### ¿La IA va más rápido en la RX 5700 XT o en el procesador?

En la tarjeta, de largo: 63–72 tokens por segundo frente a 5 en el procesador, unas 14 veces más rápido.

### ¿Puede una RX 5700 XT ejecutar Gemma 4 12B?

Solo para chats cortos. La más grande, Gemma 4 12B (6,4 GB), escribía 20–36 tokens por segundo con una pregunta corta, pero cuando el chat llegó a 8.192 tokens (una conversación larga) se colgó, con la tarjeta casi llena. Por eso GreenCube solo propone la 12B con tarjetas de 10 GB o más.
