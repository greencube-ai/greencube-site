# ¿Puede un portátil con Intel Iris Xe ejecutar IA? Medido: 5–7 tokens por segundo

> Prueba real: Gemma 4 E2B escribía 5–7 tokens por segundo en un portátil sin tarjeta gráfica (procesador Intel con gráficos Iris Xe) y 8 GB de RAM. Qué significa para chatear, estudiar e imágenes.

Canonical: https://blog.greencube.app/blog/es/ia-en-portatil-intel-iris-xe  
Published: 2026-10-04  
Author: Hector Gras

**Sí.** En un portátil sin tarjeta gráfica (procesador Intel con gráficos Iris Xe) y 8 GB de RAM, Gemma 4 E2B escribía 5–7 tokens por segundo. Más o menos a tu ritmo de lectura.

- **5–7** tokens por segundo con Gemma 4 E2B

## Qué significa en la práctica

| Tarea | Tiempo en este PC |
| --- | --- |
| Escribir una respuesta normal (400 tokens, media página) | **55–75 s** |
| Leer un documento largo que le das (5.000 tokens, unas 6 páginas) | **51–85 s** |

Calculado a partir de las velocidades medidas en este PC: el tiempo es la longitud dividida entre la velocidad, y una respuesta real tarda además un momento en arrancar. Para hacerte una idea, una persona lee unas 4 palabras por segundo ([Brysbaert, 2019](https://doi.org/10.1016/j.jml.2019.104047)), así que solo leer una respuesta de 400 tokens te lleva más de un minuto.

## Lo que medimos

**Escribir** es la velocidad a la que la IA teclea su respuesta, en tokens por segundo; un token es un trozo de palabra, y en español cada palabra suele ocupar uno o dos. **Leer** es lo rápido que asimila lo que le das: tu pregunta, un texto pegado o un PDF. Leer siempre es mucho más rápido que escribir, porque la IA puede leer muchos tokens a la vez pero tiene que escribirlos de uno en uno.

| Qué | Dónde | Resultado | Medido |
| --- | --- | --- | --- |
| Gemma 4 E2B | solo procesador | **5,3–7,3** tokens por segundo escribiendo · 59–98 leyendo | 4 de octubre de 2026 [1] |
| Gemma 4 E2B | solo procesador | **9,3** tokens por segundo escribiendo | 4 de octubre de 2026 [2] |
| Gemma 4 E2B | gráficos Intel integrados | **5** tokens por segundo escribiendo | 4 de octubre de 2026 [2] |

Cómo se midió cada número: [Más sobre cómo medimos](https://blog.greencube.app/blog/es/como-medimos-la-velocidad-de-la-ia)

1. Chats reales en GreenCube 0.1.42: la velocidad de cada respuesta de 100 tokens o más, sacada del registro de la app. El rango deja fuera la décima parte más lenta y la más rápida.
2. La prueba de velocidad de GreenCube 0.1.42, que hace al arrancar para elegir entre la tarjeta gráfica y el procesador: una respuesta corta escrita una vez en cada uno.

Cuando tenemos varias pruebas damos el rango: la velocidad varía un poco entre pruebas en el mismo PC.

## Qué significa

### ¿Sin tarjeta gráfica? Funciona igual

Sin tarjeta gráfica, la IA funciona en el procesador. Va más lenta que en un PC gaming, pero la pequeña, Gemma 4 E2B, escribe 5–7 tokens por segundo, suficiente para estudiar, resumir y escribir. La prueba de arranque de GreenCube también probó a escribir con los gráficos Intel integrados: 5, frente a 9,3 con el procesador, así que aquí escribe con el procesador.

### Imágenes

No. La IA de imágenes necesita unos 7 GB de memoria para ella sola, más de lo que puede liberar un portátil de 8 GB. Chatear y estudiar sí funcionan.

## Cómo se compara

De los 2 PCs que medimos con Gemma 4 E2B, este es el **número 2** en velocidad de escritura. El [portátil con Intel Core Ultra 5](https://blog.greencube.app/blog/es/ia-en-portatil-intel-core-ultra-5) escribe 14–18, unas 2,5 veces más rápido.

## El PC de la prueba

El PC de un tester real, usado como lo usa siempre, no una máquina de laboratorio:

- Portátil
- **Gráfica:** solo gráficos Intel integrados
- **Memoria gráfica (VRAM):** ninguna (sin tarjeta gráfica aparte)
- **RAM:** 8 GB
- **Procesador:** Intel, 8 hilos

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
- [portátil con Intel Core Ultra 5](https://blog.greencube.app/blog/es/ia-en-portatil-intel-core-ultra-5): 14–18 tokens por segundo (Gemma 4 E2B)
- [RX 580](https://blog.greencube.app/blog/es/ia-en-rx-580): 10–11 tokens por segundo (Gemma 4 E4B)

[¿Puedo usar IA en mi PC?](https://blog.greencube.app/blog/es/ia-en-mi-pc) Los 10 PCs en una tabla, y cómo irá el tuyo.

## FAQ

### ¿Puede un portátil con Intel Iris Xe ejecutar IA en local?

Sí. En un portátil sin tarjeta gráfica (procesador Intel con gráficos Iris Xe) y 8 GB de RAM, Gemma 4 E2B escribía 5–7 tokens por segundo. Más o menos a tu ritmo de lectura.

### ¿Puede un portátil con Intel Iris Xe crear imágenes con IA?

No. La IA de imágenes necesita unos 7 GB de memoria para ella sola, más de lo que puede liberar un portátil de 8 GB. Chatear y estudiar sí funcionan.
