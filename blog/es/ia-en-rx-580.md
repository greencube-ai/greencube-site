# ¿Puede una RX 580 ejecutar IA? Medido: 10–11 tokens por segundo

> Prueba real: Gemma 4 E4B escribía 10–11 tokens por segundo en un sobremesa con una AMD RX 580 (8 GB) y 16 GB de RAM. Qué significa para chatear, estudiar e imágenes.

Canonical: https://blog.greencube.app/blog/es/ia-en-rx-580  
Published: 2026-10-01  
Author: Hector Gras

**Sí.** En un sobremesa con una AMD RX 580 (8 GB) y 16 GB de RAM, Gemma 4 E4B escribía 10–11 tokens por segundo. Más rápido de lo que lees.

- **10–11** tokens por segundo con Gemma 4 E4B
- **2,7×** más rápido en la tarjeta que en el procesador

## Qué significa en la práctica

| Tarea | Tiempo en este PC |
| --- | --- |
| Escribir una respuesta normal (400 tokens, media página) | **37–38 s** |
| Leer un documento largo que le das (5.000 tokens, unas 6 páginas) | **30–35 s** |

Calculado a partir de las velocidades medidas en este PC: el tiempo es la longitud dividida entre la velocidad, y una respuesta real tarda además un momento en arrancar. Para hacerte una idea, una persona lee unas 4 palabras por segundo ([Brysbaert, 2019](https://doi.org/10.1016/j.jml.2019.104047)), así que solo leer una respuesta de 400 tokens te lleva más de un minuto.

## Lo que medimos

**Escribir** es la velocidad a la que la IA teclea su respuesta, en tokens por segundo; un token es un trozo de palabra, y en español cada palabra suele ocupar uno o dos. **Leer** es lo rápido que asimila lo que le das: tu pregunta, un texto pegado o un PDF. Leer siempre es mucho más rápido que escribir, porque la IA puede leer muchos tokens a la vez pero tiene que escribirlos de uno en uno.

| Qué | Dónde | Resultado | Medido |
| --- | --- | --- | --- |
| Gemma 4 E4B\* | tarjeta gráfica | **10,5–10,7** tokens por segundo escribiendo · 144–169 leyendo | 1 de octubre de 2026 [1] |
| Gemma 4 E4B | tarjeta gráfica | **10,1** tokens por segundo escribiendo | 1 de octubre de 2026 [2] |
| Gemma 4 E4B | solo procesador | **3,8** tokens por segundo escribiendo | 1 de octubre de 2026 [2] |

Cómo se midió cada número: [Más sobre cómo medimos](https://blog.greencube.app/blog/es/como-medimos-la-velocidad-de-la-ia)

1. Chats reales en GreenCube 0.1.42: la velocidad de cada respuesta de 100 tokens o más, sacada del registro de la app. El rango deja fuera la décima parte más lenta y la más rápida.
2. La prueba de velocidad de GreenCube 0.1.42, que hace al arrancar para elegir entre la tarjeta gráfica y el procesador: una respuesta corta escrita una vez en cada uno.

Cuando tenemos varias pruebas damos el rango: la velocidad varía un poco entre pruebas en el mismo PC. \* Este tester hizo sobre todo preguntas cortas, así que también cuentan las respuestas de menos de 100 tokens. Las respuestas cortas salen algo más lentas.

## Qué significa

### La tarjeta gráfica hace el trabajo

Mismo PC, misma IA (Gemma 4 E4B): 3,8 tokens por segundo solo con el procesador y 10,1 con la tarjeta gráfica, unas **2,7 veces más rápido**. Una gráfica está hecha para hacer miles de cuentas pequeñas a la vez para los juegos, y una IA es sobre todo ese mismo tipo de cálculo. GreenCube cronometra las dos al arrancar y usa la más rápida.

### Cabe, pero esta tarjeta es lenta para IA

Gemma 4 E4B (4,2 GB) cabe entera en los 8 GB de la tarjeta, y aun así solo escribe 10–11 tokens por segundo. Las tarjetas antiguas son mucho más lentas en este tipo de cálculo, y tener más memoria no lo arregla. Para comparar, otras tarjetas de 8 GB que medimos escriben 63–72 ([RX 5700 XT](https://blog.greencube.app/blog/es/ia-en-rx-5700-xt)), 56 ([RTX 5060](https://blog.greencube.app/blog/es/ia-en-rtx-5060)), 42–44 ([RX 6600](https://blog.greencube.app/blog/es/ia-en-rx-6600)) con la misma IA. Sigue escribiendo más rápido de lo que lees, así que chatear y estudiar funcionan; solo se nota más lenta que una tarjeta nueva.

### La más grande, Gemma 4 12B

No con holgura. GreenCube solo propone la más grande, Gemma 4 12B, con tarjetas de 10 GB de VRAM o más, y esta tiene 8. En una AMD RX 5700 XT de 8 GB respondió preguntas cortas y luego se colgó en un chat largo.

### Imágenes

Muy probablemente, pero aún no hemos cronometrado una imagen con esta tarjeta. Cuando lo hagamos, el número irá aquí. Una imagen usa su propia IA, de unos 6 GB, y muchas más cuentas que una respuesta de chat, así que aquí los gráficos importan todavía más.

## Cómo se compara

De los 8 PCs que medimos con Gemma 4 E4B, este es el **número 8** en velocidad de escritura. La [GTX 1650](https://blog.greencube.app/blog/es/ia-en-gtx-1650) escribe unos 20, un 90% más rápido.

Medimos 4 tarjetas de 8 GB, y hay mucha diferencia entre ellas:

- [RX 5700 XT](https://blog.greencube.app/blog/es/ia-en-rx-5700-xt): 63–72 tokens por segundo
- [RTX 5060](https://blog.greencube.app/blog/es/ia-en-rtx-5060): 56 tokens por segundo (prueba de arranque)
- [RX 6600](https://blog.greencube.app/blog/es/ia-en-rx-6600): 42–44 tokens por segundo
- **RX 580**: 10–11 tokens por segundo

La memoria decide qué IA cabe. Lo nueva que sea la tarjeta decide lo rápido que va.

## El PC de la prueba

El PC de un tester real, usado como lo usa siempre, no una máquina de laboratorio:

- Sobremesa
- **Gráfica:** AMD RX 580
- **Memoria gráfica (VRAM):** 8 GB
- **RAM:** 16 GB
- **Procesador:** 12 hilos

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
- [portátil con Intel Iris Xe](https://blog.greencube.app/blog/es/ia-en-portatil-intel-iris-xe): 5–7 tokens por segundo (Gemma 4 E2B)

[¿Puedo usar IA en mi PC?](https://blog.greencube.app/blog/es/ia-en-mi-pc) Los 10 PCs en una tabla, y cómo irá el tuyo.

## FAQ

### ¿Puede una RX 580 ejecutar IA en local?

Sí. En un sobremesa con una AMD RX 580 (8 GB) y 16 GB de RAM, Gemma 4 E4B escribía 10–11 tokens por segundo. Más rápido de lo que lees.

### ¿Puede una RX 580 crear imágenes con IA?

Muy probablemente, pero aún no hemos cronometrado una imagen con esta tarjeta. Cuando lo hagamos, el número irá aquí.

### ¿La IA va más rápido en la RX 580 o en el procesador?

En la tarjeta, de largo: 10,1 tokens por segundo frente a 3,8 en el procesador, unas 2,7 veces más rápido.

### ¿Puede una RX 580 ejecutar Gemma 4 12B?

No con holgura. GreenCube solo propone la más grande, Gemma 4 12B, con tarjetas de 10 GB de VRAM o más, y esta tiene 8. En una AMD RX 5700 XT de 8 GB respondió preguntas cortas y luego se colgó en un chat largo.
