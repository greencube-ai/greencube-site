# ¿Puede una RTX 5060 ejecutar IA? Medido: 56 tokens por segundo

> Prueba real: Gemma 4 E4B escribía 56 tokens por segundo en un sobremesa con una NVIDIA RTX 5060 (8 GB) y 32 GB de RAM. Qué significa para chatear, estudiar e imágenes.

Canonical: https://blog.greencube.app/blog/es/ia-en-rtx-5060  
Published: 2026-10-01  
Author: Hector Gras

**Sí.** En un sobremesa con una NVIDIA RTX 5060 (8 GB) y 32 GB de RAM, Gemma 4 E4B escribía 56 tokens por segundo. Más rápido de lo que lees.

- **56** tokens por segundo con Gemma 4 E4B
- **4,6×** más rápido en la tarjeta que en el procesador

## Qué significa en la práctica

| Tarea | Tiempo en este PC |
| --- | --- |
| Escribir una respuesta normal (400 tokens, media página) | **7 s** |

Calculado a partir de las velocidades medidas en este PC: el tiempo es la longitud dividida entre la velocidad, y una respuesta real tarda además un momento en arrancar. Para hacerte una idea, una persona lee unas 4 palabras por segundo ([Brysbaert, 2019](https://doi.org/10.1016/j.jml.2019.104047)), así que solo leer una respuesta de 400 tokens te lleva más de un minuto.

## Lo que medimos

**Escribir** es la velocidad a la que la IA teclea su respuesta, en tokens por segundo; un token es un trozo de palabra, y en español cada palabra suele ocupar uno o dos. **Leer** es lo rápido que asimila lo que le das: tu pregunta, un texto pegado o un PDF. Leer siempre es mucho más rápido que escribir, porque la IA puede leer muchos tokens a la vez pero tiene que escribirlos de uno en uno.

| Qué | Dónde | Resultado | Medido |
| --- | --- | --- | --- |
| Gemma 4 E4B | tarjeta gráfica | **55,9** tokens por segundo escribiendo | 1 de octubre de 2026 |
| Gemma 4 E4B | solo procesador | **12,1** tokens por segundo escribiendo | 1 de octubre de 2026 |

Cómo se midió cada número: [Más sobre cómo medimos](https://blog.greencube.app/blog/es/como-medimos-la-velocidad-de-la-ia)

1. La prueba de velocidad de GreenCube 0.1.42, que hace al arrancar para elegir entre la tarjeta gráfica y el procesador: una respuesta corta escrita una vez en cada uno.

Cuando tenemos varias pruebas damos el rango: la velocidad varía un poco entre pruebas en el mismo PC.

## Qué significa

### La tarjeta gráfica hace el trabajo

Mismo PC, misma IA (Gemma 4 E4B): 12,1 tokens por segundo solo con el procesador y 55,9 con la tarjeta gráfica, unas **4,6 veces más rápido**. Una gráfica está hecha para hacer miles de cuentas pequeñas a la vez para los juegos, y una IA es sobre todo ese mismo tipo de cálculo. GreenCube cronometra las dos al arrancar y usa la más rápida.

### La IA entera cabe en la tarjeta

Gemma 4 E4B ocupa 4,2 GB y la tarjeta tiene 8 GB de memoria propia (VRAM). Cabe entera, con sitio de sobra para la conversación, así que la tarjeta nunca espera a la memoria más lenta del resto del PC. Esa es la razón principal de que vaya tan rápido.

### La más grande, Gemma 4 12B

No con holgura. GreenCube solo propone la más grande, Gemma 4 12B, con tarjetas de 10 GB de VRAM o más, y esta tiene 8. En una AMD RX 5700 XT de 8 GB respondió preguntas cortas y luego se colgó en un chat largo.

### Imágenes

Muy probablemente, pero aún no hemos cronometrado una imagen con esta tarjeta. Cuando lo hagamos, el número irá aquí. Una imagen usa su propia IA, de unos 6 GB, y muchas más cuentas que una respuesta de chat, así que aquí los gráficos importan todavía más.

## Cómo se compara

De los 8 PCs que medimos con Gemma 4 E4B, este es el **número 3** en velocidad de escritura. La [RX 5700 XT](https://blog.greencube.app/blog/es/ia-en-rx-5700-xt) escribe 63–72, un 20% más rápido. La [RTX 3060](https://blog.greencube.app/blog/es/ia-en-rtx-3060) escribe 53–55, así que este va un 5% más rápido.

Medimos 4 tarjetas de 8 GB, y hay mucha diferencia entre ellas:

- [RX 5700 XT](https://blog.greencube.app/blog/es/ia-en-rx-5700-xt): 63–72 tokens por segundo
- **RTX 5060**: 56 tokens por segundo (prueba de arranque)
- [RX 6600](https://blog.greencube.app/blog/es/ia-en-rx-6600): 42–44 tokens por segundo
- [RX 580](https://blog.greencube.app/blog/es/ia-en-rx-580): 10–11 tokens por segundo

La memoria decide qué IA cabe. Lo nueva que sea la tarjeta decide lo rápido que va.

## El PC de la prueba

El PC de un tester real, usado como lo usa siempre, no una máquina de laboratorio:

- Sobremesa
- **Gráfica:** NVIDIA RTX 5060
- **Memoria gráfica (VRAM):** 8 GB
- **RAM:** 32 GB
- **Procesador:** 16 hilos

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
- [RTX 3060](https://blog.greencube.app/blog/es/ia-en-rtx-3060): 53–55 tokens por segundo (Gemma 4 E4B)
- [RX 6600](https://blog.greencube.app/blog/es/ia-en-rx-6600): 42–44 tokens por segundo (Gemma 4 E4B)
- [GTX 1660 Super](https://blog.greencube.app/blog/es/ia-en-gtx-1660-super): 37–38 tokens por segundo (Gemma 4 E4B)
- [GTX 1650](https://blog.greencube.app/blog/es/ia-en-gtx-1650): unos 20 tokens por segundo (Gemma 4 E4B)
- [portátil con Intel Core Ultra 5](https://blog.greencube.app/blog/es/ia-en-portatil-intel-core-ultra-5): 14–18 tokens por segundo (Gemma 4 E2B)
- [RX 580](https://blog.greencube.app/blog/es/ia-en-rx-580): 10–11 tokens por segundo (Gemma 4 E4B)
- [portátil con Intel Iris Xe](https://blog.greencube.app/blog/es/ia-en-portatil-intel-iris-xe): 5–7 tokens por segundo (Gemma 4 E2B)

[¿Puedo usar IA en mi PC?](https://blog.greencube.app/blog/es/ia-en-mi-pc) Los 10 PCs en una tabla, y cómo irá el tuyo.

## FAQ

### ¿Puede una RTX 5060 ejecutar IA en local?

Sí. En un sobremesa con una NVIDIA RTX 5060 (8 GB) y 32 GB de RAM, Gemma 4 E4B escribía 56 tokens por segundo. Más rápido de lo que lees.

### ¿Puede una RTX 5060 crear imágenes con IA?

Muy probablemente, pero aún no hemos cronometrado una imagen con esta tarjeta. Cuando lo hagamos, el número irá aquí.

### ¿La IA va más rápido en la RTX 5060 o en el procesador?

En la tarjeta, de largo: 55,9 tokens por segundo frente a 12,1 en el procesador, unas 4,6 veces más rápido.

### ¿Puede una RTX 5060 ejecutar Gemma 4 12B?

No con holgura. GreenCube solo propone la más grande, Gemma 4 12B, con tarjetas de 10 GB de VRAM o más, y esta tiene 8. En una AMD RX 5700 XT de 8 GB respondió preguntas cortas y luego se colgó en un chat largo.
