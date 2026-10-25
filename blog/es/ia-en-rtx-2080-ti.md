# ¿Puede una RTX 2080 Ti ejecutar IA? Medido: 65–71 tokens por segundo

> Prueba real: Gemma 4 E4B escribía 65–71 tokens por segundo en un sobremesa con una NVIDIA RTX 2080 Ti (11 GB) y 128 GB de RAM. Qué significa para chatear, estudiar e imágenes.

Canonical: https://blog.greencube.app/blog/es/ia-en-rtx-2080-ti  
Published: 2026-10-14  
Author: Hector Gras

**Sí.** En un sobremesa con una NVIDIA RTX 2080 Ti (11 GB) y 128 GB de RAM, Gemma 4 E4B escribía 65–71 tokens por segundo. Más rápido de lo que lees.

- **65–71** tokens por segundo con Gemma 4 E4B
- **5,6×** más rápido en la tarjeta que en el procesador
- **8–9 s** para crear una imagen

## Qué significa en la práctica

| Tarea | Tiempo en este PC |
| --- | --- |
| Escribir una respuesta normal (400 tokens, media página) | **6 s** |
| Leer un documento largo que le das (5.000 tokens, unas 6 páginas) | **3–4 s** |
| Crear una imagen (512×512) | **8–9 s (la primera: 83 s)** |

Calculado a partir de las velocidades medidas en este PC: el tiempo es la longitud dividida entre la velocidad, y una respuesta real tarda además un momento en arrancar. Para hacerte una idea, una persona lee unas 4 palabras por segundo ([Brysbaert, 2019](https://doi.org/10.1016/j.jml.2019.104047)), así que solo leer una respuesta de 400 tokens te lleva más de un minuto.

## Lo que medimos

**Escribir** es la velocidad a la que la IA teclea su respuesta, en tokens por segundo; un token es un trozo de palabra, y en español cada palabra suele ocupar uno o dos. **Leer** es lo rápido que asimila lo que le das: tu pregunta, un texto pegado o un PDF. Leer siempre es mucho más rápido que escribir, porque la IA puede leer muchos tokens a la vez pero tiene que escribirlos de uno en uno.

| Qué | Dónde | Resultado | Medido |
| --- | --- | --- | --- |
| Gemma 4 E4B | tarjeta gráfica | **65–71** tokens por segundo escribiendo · 1.380–1.800 leyendo | 14 de octubre de 2026 [1] |
| Gemma 4 E4B | tarjeta gráfica | **75,6** tokens por segundo escribiendo | 14 de octubre de 2026 [2] |
| Gemma 4 E4B | solo procesador | **13,5** tokens por segundo escribiendo | 14 de octubre de 2026 [2] |
| Imagen (512×512) | tarjeta gráfica | **8–9 s** (la primera tardó 83 s mientras cargaba) | 12 de octubre de 2026 [3] |

Cómo se midió cada número: [Más sobre cómo medimos](https://blog.greencube.app/blog/es/como-medimos-la-velocidad-de-la-ia)

1. Chats reales en GreenCube 0.1.44: la velocidad de cada respuesta de 100 tokens o más, sacada del registro de la app. El rango deja fuera la décima parte más lenta y la más rápida.
2. La prueba de velocidad de GreenCube 0.1.44, que hace al arrancar para elegir entre la tarjeta gráfica y el procesador: una respuesta corta escrita una vez en cada uno.
3. El motor de imágenes de GreenCube (Z-Image Turbo), 512×512 píxeles y 8 pasos, cronometrado desde el clic hasta la imagen terminada.

Cuando tenemos varias pruebas damos el rango: la velocidad varía un poco entre pruebas en el mismo PC.

## Qué significa

### La tarjeta gráfica hace el trabajo

Mismo PC, misma IA (Gemma 4 E4B): 13,5 tokens por segundo solo con el procesador y 75,6 con la tarjeta gráfica, unas **5,6 veces más rápido**. Una gráfica está hecha para hacer miles de cuentas pequeñas a la vez para los juegos, y una IA es sobre todo ese mismo tipo de cálculo. GreenCube cronometra las dos al arrancar y usa la más rápida.

### La IA entera cabe en la tarjeta

Gemma 4 E4B ocupa 4,2 GB y la tarjeta tiene 11 GB de memoria propia (VRAM). Cabe entera, con sitio de sobra para la conversación, así que la tarjeta nunca espera a la memoria más lenta del resto del PC. Esa es la razón principal de que vaya tan rápido.

### La más grande, Gemma 4 12B

Debería. Gemma 4 12B ocupa 6,4 GB y esta tarjeta tiene 11, así que queda sitio también para una conversación larga. Aún no la hemos medido con esta tarjeta.

### Imágenes

Sí. Una imagen (512×512) tardó 8–9 s con la tarjeta gráfica (la primera tardó 83 s mientras cargaba). Una imagen usa su propia IA, de unos 6 GB, y muchas más cuentas que una respuesta de chat, así que aquí los gráficos importan todavía más.

## Cómo se compara

De los 8 PCs que medimos con Gemma 4 E4B, este es el **número 1** en velocidad de escritura. La [RX 5700 XT](https://blog.greencube.app/blog/es/ia-en-rx-5700-xt) escribe 63–72, así que este va más o menos igual.

## El PC de la prueba

El PC de un tester real, usado como lo usa siempre, no una máquina de laboratorio:

- Sobremesa
- **Gráfica:** NVIDIA RTX 2080 Ti
- **Memoria gráfica (VRAM):** 11 GB
- **RAM:** 128 GB
- **Procesador:** 32 hilos

## Mira tu propio PC

¿No sabes qué tiene tu PC? Se mira en 30 segundos:

1. Pulsa **Ctrl + Mayús + Esc** para abrir el Administrador de tareas.
2. Ve a **Rendimiento**.
3. Pulsa **Memoria**: el número de arriba a la derecha es tu RAM.
4. Pulsa **GPU**: el nombre de arriba a la derecha es tu tarjeta, y **Memoria de GPU dedicada** es tu VRAM. ¿Solo ves gráficos Intel o AMD sin memoria dedicada? Entonces no tienes tarjeta aparte.

Después busca la tarjeta más parecida en [la tabla completa](https://blog.greencube.app/blog/es/ia-en-mi-pc). La misma tarjeta con más VRAM puede con una IA más grande; una tarjeta más nueva del mismo tamaño suele ir más rápido.

## Otros PCs que medimos

- [RX 5700 XT](https://blog.greencube.app/blog/es/ia-en-rx-5700-xt): 63–72 tokens por segundo (Gemma 4 E4B)
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

### ¿Puede una RTX 2080 Ti ejecutar IA en local?

Sí. En un sobremesa con una NVIDIA RTX 2080 Ti (11 GB) y 128 GB de RAM, Gemma 4 E4B escribía 65–71 tokens por segundo. Más rápido de lo que lees.

### ¿Puede una RTX 2080 Ti crear imágenes con IA?

Sí. Una imagen (512×512) tardó 8–9 s con la tarjeta gráfica (la primera tardó 83 s mientras cargaba).

### ¿La IA va más rápido en la RTX 2080 Ti o en el procesador?

En la tarjeta, de largo: 75,6 tokens por segundo frente a 13,5 en el procesador, unas 5,6 veces más rápido.

### ¿Puede una RTX 2080 Ti ejecutar Gemma 4 12B?

Debería. Gemma 4 12B ocupa 6,4 GB y esta tarjeta tiene 11, así que queda sitio también para una conversación larga. Aún no la hemos medido con esta tarjeta.
