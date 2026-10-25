# Cómo medimos la velocidad de la IA en PCs reales, y por qué no la adivinamos

> Cada velocidad del blog de GreenCube sale de uno de 10 PCs reales. Cómo medimos, cada PC que probamos, los datos en CSV y la prueba que muestra por qué no estimamos el resto.

Canonical: https://blog.greencube.app/blog/es/como-medimos-la-velocidad-de-la-ia  
Published: 2026-10-14  
Author: Hector Gras

Cada velocidad de este blog sale de un PC real con GreenCube: 10 PCs hasta ahora, medidos entre el 22 de septiembre de 2026 y el 14 de octubre de 2026. No estimamos velocidades de tarjetas que no hemos medido: cuando probamos a estimar las que sí tenemos, la estimación típica fallaba un 19% y la peor un 239%.

- **10** PCs reales medidos, sobremesas y portátiles
- **34** mediciones, todas en el CSV de abajo
- **239%** lo que falló la peor estimación de velocidad

## Qué medimos

Tres cosas, porque son lo que notas al usar una IA en tu propio PC:

- **Velocidad de escritura:** lo rápido que la IA teclea su respuesta, en tokens por segundo. Un token es un trozo de palabra (en español cada palabra suele ocupar uno o dos), y una persona lee unos 8 tokens por segundo, así que por encima de eso la respuesta sale más rápido de lo que lees.
- **Velocidad de lectura:** lo rápido que asimila lo que le das: tu pregunta, un texto pegado o un PDF. Siempre es mucho más rápida que la escritura, porque la IA lee muchos tokens a la vez pero los escribe de uno en uno.
- **Tiempo por imagen:** lo que tarda una imagen de 512×512, desde el clic hasta la imagen terminada.

Medimos las IAs que trae GreenCube, los mismos archivos que descarga cualquier usuario: Gemma 4 E2B (2,6 GB), Gemma 4 E4B (4,2 GB) y Gemma 4 12B (6,4 GB) de Google para chatear, y Z-Image Turbo para las imágenes. Otra IA, o la misma comprimida de otra forma, daría otros números, así que solo comparamos lo comparable.

## Cómo medimos

De cuatro formas, y cada número del blog dice de cuál sale:

### Chats reales

Chats reales en GreenCube: la velocidad de cada respuesta de 100 tokens o más, sacada del registro de la app. El rango deja fuera la décima parte más lenta y la más rápida.

Usado en: [RTX 2080 Ti](https://blog.greencube.app/blog/es/ia-en-rtx-2080-ti), [RTX 3060](https://blog.greencube.app/blog/es/ia-en-rtx-3060), [RX 6600](https://blog.greencube.app/blog/es/ia-en-rx-6600), [GTX 1660 Super](https://blog.greencube.app/blog/es/ia-en-gtx-1660-super), [GTX 1650](https://blog.greencube.app/blog/es/ia-en-gtx-1650), [RX 580](https://blog.greencube.app/blog/es/ia-en-rx-580), [portátil con Intel Iris Xe](https://blog.greencube.app/blog/es/ia-en-portatil-intel-iris-xe).

### La prueba de arranque de GreenCube

La prueba de velocidad de GreenCube, que hace al arrancar para elegir entre la tarjeta gráfica y el procesador: una respuesta corta escrita una vez en cada uno.

Usado en: [RTX 2080 Ti](https://blog.greencube.app/blog/es/ia-en-rtx-2080-ti), [RTX 5060](https://blog.greencube.app/blog/es/ia-en-rtx-5060), [RTX 3060](https://blog.greencube.app/blog/es/ia-en-rtx-3060), [RX 6600](https://blog.greencube.app/blog/es/ia-en-rx-6600), [GTX 1660 Super](https://blog.greencube.app/blog/es/ia-en-gtx-1660-super), [RX 580](https://blog.greencube.app/blog/es/ia-en-rx-580), [portátil con Intel Iris Xe](https://blog.greencube.app/blog/es/ia-en-portatil-intel-iris-xe).

### La prueba de velocidad de llama.cpp

La prueba de velocidad de llama.cpp (llama-bench), el motor sobre el que funciona GreenCube, con los mismos archivos de IA: escribe 128 tokens y lee un texto de 512.

Usado en: [RX 5700 XT](https://blog.greencube.app/blog/es/ia-en-rx-5700-xt), [portátil con Intel Core Ultra 5](https://blog.greencube.app/blog/es/ia-en-portatil-intel-core-ultra-5).

### Prueba de imágenes

El motor de imágenes de GreenCube (Z-Image Turbo), 512×512 píxeles y 8 pasos, cronometrado desde el clic hasta la imagen terminada.

Usado en: [RTX 2080 Ti](https://blog.greencube.app/blog/es/ia-en-rtx-2080-ti), [RTX 3060](https://blog.greencube.app/blog/es/ia-en-rtx-3060), [RX 6600](https://blog.greencube.app/blog/es/ia-en-rx-6600), [GTX 1660 Super](https://blog.greencube.app/blog/es/ia-en-gtx-1660-super), [portátil con Intel Core Ultra 5](https://blog.greencube.app/blog/es/ia-en-portatil-intel-core-ultra-5).

Los chats reales son la mejor prueba, porque es lo que vas a notar, así que el número principal de cada página sale de chats reales siempre que los tenemos. La prueba de arranque es una sola respuesta corta, así que la usamos para comparar tarjeta y procesador (mide los dos igual), y como número principal solo cuando un tester no mandó respuestas largas.

## Todos los PCs que medimos

Los PCs de testers reales, usados como los usan siempre, no máquinas de laboratorio. No publicamos sus nombres.

| PC | Tipo | VRAM | RAM | Número principal | GreenCube | Fecha | Escribe (tokens/s) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [RTX 2080 Ti](https://blog.greencube.app/blog/es/ia-en-rtx-2080-ti) | Sobremesa | 11 GB | 128 GB | Chats reales | 0.1.44 | 14 de octubre de 2026 | **65–71** |
| [RX 5700 XT](https://blog.greencube.app/blog/es/ia-en-rx-5700-xt) | Sobremesa | 8 GB | 48 GB | La prueba de velocidad de llama.cpp | – | 22 de septiembre de 2026 | **63–72** |
| [RTX 5060](https://blog.greencube.app/blog/es/ia-en-rtx-5060) | Sobremesa | 8 GB | 32 GB | La prueba de arranque de GreenCube | 0.1.42 | 1 de octubre de 2026 | **56** |
| [RTX 3060](https://blog.greencube.app/blog/es/ia-en-rtx-3060) | Sobremesa | 12 GB | 32 GB | Chats reales | 0.1.42–0.1.43 | 6 de octubre de 2026 | **53–55** |
| [RX 6600](https://blog.greencube.app/blog/es/ia-en-rx-6600) | Sobremesa | 8 GB | 16 GB | Chats reales | 0.1.42–0.1.44 | 9 de octubre de 2026 | **42–44** |
| [GTX 1660 Super](https://blog.greencube.app/blog/es/ia-en-gtx-1660-super) | Sobremesa | 6 GB | 16 GB | Chats reales | 0.1.42 | 1 de octubre de 2026 | **37–38** |
| [GTX 1650](https://blog.greencube.app/blog/es/ia-en-gtx-1650) | Sobremesa | 4 GB | 16 GB | Chats reales | 0.1.40 | 23 de septiembre de 2026 | **unos 20** |
| [portátil con Intel Core Ultra 5](https://blog.greencube.app/blog/es/ia-en-portatil-intel-core-ultra-5) | Portátil | – | 16 GB | La prueba de velocidad de llama.cpp | – | 28 de septiembre de 2026 | **14–18** |
| [RX 580](https://blog.greencube.app/blog/es/ia-en-rx-580) | Sobremesa | 8 GB | 16 GB | Chats reales | 0.1.42 | 1 de octubre de 2026 | **10–11** |
| [portátil con Intel Iris Xe](https://blog.greencube.app/blog/es/ia-en-portatil-intel-iris-xe) | Portátil | – | 8 GB | Chats reales | 0.1.42 | 4 de octubre de 2026 | **5–7** |

## Por qué los números son rangos

- **Otras apps.** Un navegador, un launcher de juegos o una videollamada usan la misma memoria y la misma tarjeta.
- **La primera vez va más lenta.** La primera respuesta tras instalar, o la primera imagen, incluye cargar y preparar la tarjeta. Lo decimos donde importa (por ejemplo, "la primera tardó 83 s mientras cargaba").
- **Las respuestas cortas salen más lentas.** Cada respuesta tiene un pequeño arranque fijo, que pesa más en una de 20 tokens que en una de 400. Por eso los rangos de chats reales cuentan respuestas de 100 tokens o más, y lo avisamos cuando un tester solo mandó respuestas cortas.
- **Dejamos fuera los extremos.** Los rangos de chats reales van del percentil 10 al 90, así que una respuesta rara no los mueve.

## ¿Se puede adivinar la velocidad de una tarjeta por sus especificaciones?

Sería práctico: hay cientos de tarjetas y hemos medido 10 PCs. Lo habitual es usar el ancho de banda de memoria. Para escribir cada token, la IA lee su modelo entero de la memoria de la tarjeta, así que en teoría la velocidad es más o menos el ancho de banda dividido entre el tamaño del modelo, por cierta eficiencia. Muchas calculadoras online funcionan así.

Así que lo probamos con nuestros datos. Escondimos una tarjeta cada vez, calculamos la velocidad por GB/s con las demás, predijimos la escondida a partir de su ancho de banda (de las especificaciones de los fabricantes, recogidas en la [base de datos de TechPowerUp](https://www.techpowerup.com/gpu-specs/)) y lo comparamos con lo medido. La misma IA en todas (Gemma 4 E4B, entera en la tarjeta).

| Tarjeta | Ancho de banda | Medido (tokens/s) | Predicho | Error |
| --- | --- | --- | --- | --- |
| [RTX 2080 Ti](https://blog.greencube.app/blog/es/ia-en-rtx-2080-ti) | 616 GB/s | 68 | 79 | **+17%** |
| [RX 5700 XT](https://blog.greencube.app/blog/es/ia-en-rx-5700-xt) | 448 GB/s | 68 | 55 | **−19%** |
| [RTX 5060](https://blog.greencube.app/blog/es/ia-en-rtx-5060) | 448 GB/s | 56 | 57 | **+1%** |
| [RTX 3060](https://blog.greencube.app/blog/es/ia-en-rtx-3060) | 360 GB/s | 54 | 44 | **−19%** |
| [RX 6600](https://blog.greencube.app/blog/es/ia-en-rx-6600) | 224 GB/s | 43 | 26 | **−41%** |
| [GTX 1660 Super](https://blog.greencube.app/blog/es/ia-en-gtx-1660-super) | 336 GB/s | 38 | 43 | **+14%** |
| [RX 580](https://blog.greencube.app/blog/es/ia-en-rx-580) | 256 GB/s | 11 | 36 | **+239%** |

La estimación típica falló un 19%. La peor fue la [RX 580](https://blog.greencube.app/blog/es/ia-en-rx-580): por su memoria tocarían unos 36 tokens por segundo, pero escribía 11. Repitiendo la prueba sin ella, las demás siguen fallando hasta un 33%. La RX 6600, más nueva, fue al revés, más rápida de lo que dice su ancho de banda; su gran caché dentro del chip (AMD la llama Infinity Cache) puede ser parte del motivo. Cada número medido es el número principal de su tarjeta, así que no todos salen del mismo tipo de prueba; eso añade algo de ruido, pero no explica fallar por tres veces.

**No es suficiente.** Una estimación que puede fallar un 33% en una tarjeta moderna, o un 239% en una antigua, le diría a alguien que su PC va bien cuando va lento, o al revés. Así que el comprobador y las páginas de tarjetas solo muestran tarjetas medidas, y dicen claramente cuándo la tuya no es una de ellas. Repetimos esta prueba con cada tarjeta nueva, y si el error baja, lo diremos aquí antes de mostrar una sola estimación.

## Lo que aún no hemos medido

- Un portátil con tarjeta gaming.
- Gemma 4 12B en una tarjeta de 10 GB o más.
- Imágenes en la [RX 5700 XT](https://blog.greencube.app/blog/es/ia-en-rx-5700-xt), la [RTX 5060](https://blog.greencube.app/blog/es/ia-en-rtx-5060), la [GTX 1650](https://blog.greencube.app/blog/es/ia-en-gtx-1650), la [RX 580](https://blog.greencube.app/blog/es/ia-en-rx-580).
- Otras IAs aparte de las que trae GreenCube, y Linux o Mac (GreenCube es para Windows).

## Descarga los datos

Todas las mediciones de esta página, una por fila, están en [greencube-ai-speeds.csv](https://blog.greencube.app/blog/greencube-ai-speeds.csv): el PC, la IA, dónde funcionó, velocidades de escritura y lectura, tiempos por imagen, cómo se midió, la versión de GreenCube y la fecha. Si lo usas, cita "GreenCube, mediciones de velocidad de IA en PCs reales, 2026" y enlaza a esta página.

## Añade tu PC

¿Ya usas GreenCube? Mándanos tu registro a [support@greencube.app](mailto:support@greencube.app). Añadimos tu PC a las pruebas, sin tu nombre, y una tarjeta nueva tiene su propia página. ¿No sabes qué tiene tu PC? [Míralo aquí](https://blog.greencube.app/blog/es/ia-en-mi-pc#checker).

## FAQ

### ¿De dónde salen los números de velocidad de GreenCube?

De 10 PCs reales con GreenCube, medidos en chats reales, con la prueba de arranque de GreenCube, con la prueba de velocidad de llama.cpp y con una prueba de imágenes. Cada número dice de cuál sale.

### ¿Se puede estimar la velocidad de la IA con las especificaciones de la tarjeta?

Aún no de forma fiable. Prediciendo por ancho de banda, nuestras estimaciones fallaban un 19% de media y hasta un 239%, así que solo mostramos tarjetas medidas.

### ¿Puedo descargar los datos?

Sí: todas las mediciones están en greencube-ai-speeds.csv, enlazado en esta página.
