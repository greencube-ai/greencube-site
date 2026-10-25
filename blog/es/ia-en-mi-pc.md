# ¿Puedo usar IA en mi PC? Lo medimos en 10 PCs gaming y portátiles

> ¿Puedes tener IA en tu PC? Velocidades reales de 10 PCs, de una GTX 1650 a una RTX 2080 Ti y portátiles sin tarjeta gráfica, y qué significan tu gráfica, la VRAM y la RAM.

Canonical: https://blog.greencube.app/blog/es/ia-en-mi-pc  
Published: 2026-10-18  
Author: Hector Gras

**Respuesta corta: sí.** Si tu PC mueve juegos, puede mover una IA. Lo medimos en 10 PCs reales: sobremesas gaming desde una GTX 1650 veterana hasta una RTX 2080 Ti, y dos portátiles sin tarjeta gráfica. Todos chatearon con una IA que funciona entera dentro del PC: sin internet y sin suscripción. Lo único que cambia es la velocidad.

- **14×** más rápida en la tarjeta gráfica que en el procesador, mismo PC y misma IA
- **20** tokens por segundo con una GTX 1650 de 4 GB. Más rápido de lo que lees.
- **8–9 s** por imagen con una RTX 2080 Ti, una vez cargada

## ¿Funcionará la IA en tu PC?

Escribe tu tarjeta gráfica y elige tu RAM: verás qué funciona, a qué velocidad fue en PCs reales y qué no hemos medido aún. Interactive, on the page: https://blog.greencube.app/blog/es/ia-en-mi-pc#checker

## Los números

"Escribe" es la velocidad a la que la IA teclea su respuesta, en tokens por segundo. Un token es un trozo de palabra: en español, cada palabra suele ocupar uno o dos. Una persona lee unas 4 palabras por segundo ([Brysbaert, 2019](https://doi.org/10.1016/j.jml.2019.104047)), así que a partir de unos 8 tokens por segundo la IA ya escribe más rápido de lo que tus ojos leen.

| PC | Gráfica | RAM | IA | Escribe (tokens/s) |
| --- | --- | --- | --- | --- |
| Sobremesa | [NVIDIA RTX 2080 Ti, 11 GB](https://blog.greencube.app/blog/es/ia-en-rtx-2080-ti) | 128 GB | Gemma 4 E4B | **65–71** |
| Sobremesa | [AMD RX 5700 XT, 8 GB](https://blog.greencube.app/blog/es/ia-en-rx-5700-xt) | 48 GB | Gemma 4 E4B | **63–72** |
| Sobremesa | [NVIDIA RTX 5060, 8 GB](https://blog.greencube.app/blog/es/ia-en-rtx-5060) | 32 GB | Gemma 4 E4B | **56** |
| Sobremesa | [NVIDIA RTX 3060, 12 GB](https://blog.greencube.app/blog/es/ia-en-rtx-3060) | 32 GB | Gemma 4 E4B | **53–55** |
| Sobremesa | [AMD RX 6600, 8 GB](https://blog.greencube.app/blog/es/ia-en-rx-6600) | 16 GB | Gemma 4 E4B | **42–44** |
| Sobremesa | [NVIDIA GTX 1660 Super, 6 GB](https://blog.greencube.app/blog/es/ia-en-gtx-1660-super) | 16 GB | Gemma 4 E4B | **37–38** |
| Sobremesa | [NVIDIA GTX 1650, 4 GB](https://blog.greencube.app/blog/es/ia-en-gtx-1650) | 16 GB | Gemma 4 E4B | **unos 20** |
| Portátil | [Solo gráficos Intel (Core Ultra 5)](https://blog.greencube.app/blog/es/ia-en-portatil-intel-core-ultra-5) | 16 GB | Gemma 4 E2B | **14–18** |
| Sobremesa | [AMD RX 580, 8 GB](https://blog.greencube.app/blog/es/ia-en-rx-580) | 16 GB | Gemma 4 E4B | **10–11** |
| Portátil | [Solo Intel Iris Xe](https://blog.greencube.app/blog/es/ia-en-portatil-intel-iris-xe) | 8 GB | Gemma 4 E2B | **5–7** |

Pulsa una gráfica para ver su prueba completa.

Medido con GreenCube entre septiembre y octubre de 2026, en chats reales y con la prueba de velocidad de la propia app. La velocidad varía un poco entre pruebas en el mismo PC, así que cuando tenemos varias damos el rango. [Cómo medimos, y todos los datos](https://blog.greencube.app/blog/es/como-medimos-la-velocidad-de-la-ia).

## Lo que aprendimos

### 1. La gráfica hace el trabajo duro, como en un juego

En el sobremesa con la RX 5700 XT, la misma IA escribía **5 tokens por segundo en el procesador y 72 en la tarjeta gráfica**. Una IA es sobre todo el tipo de cálculo para el que están hechas las gráficas. Cualquier tarjeta de los últimos años ayuda muchísimo, incluso una GTX 1650 de 4 GB.

### 2. La VRAM decide qué IA cabe

Para ir a tope, la IA tiene que caber en la memoria propia de la tarjeta (la VRAM). Ese sobremesa tenía 48 GB de RAM y no le sirvieron para una IA más grande: un modelo de 12.000 millones de parámetros cupo en la tarjeta de 8 GB para una pregunta corta, y se cayó en cuanto la conversación se alargó, con la tarjeta casi llena. **Para la IA, la VRAM pesa más que la RAM.** Eso sí, más VRAM no es más velocidad: cuatro tarjetas de 8 GB que medimos escribían desde unos 11 tokens por segundo (RX 580) hasta 72 (RX 5700 XT). Por eso GreenCube mira tu tarjeta y elige una IA que quepa, no simplemente la más grande.

### 3. ¿Sin tarjeta gráfica? Funciona igual

Un portátil normal de 16 GB con solo gráficos Intel escribía entre 14 y 18 tokens por segundo con la IA pequeña, y terminó una respuesta completa (una explicación y tres preguntas de examen) en unos 20 segundos. Para estudiar y escribir va de sobra. Uno de 8 GB también funciona, a entre 5 y 7 tokens por segundo en chats reales, si las demás apps le dejan memoria libre.

### 4. Las imágenes son lo pesado

Crear una imagen cuesta mucho más que chatear. **De 8 a 9 segundos** con una RTX 2080 Ti de 11 GB (la primera tardó 83 mientras cargaba), **28 segundos** con una RTX 3060 de 12 GB, un minuto con una RX 6600 de 8 GB, minuto y medio con una GTX 1660 Super de 6 GB y unos **2 minutos y medio** en el portátil de 16 GB. Un portátil de 8 GB no puede crear imágenes: la IA de imágenes necesita unos 7 GB ella sola.

## Mira tu PC en 30 segundos

1. Pulsa **Ctrl + Mayús + Esc** para abrir el Administrador de tareas.
2. Entra en **Rendimiento**.
3. Pulsa en **Memoria**: el número de arriba a la derecha es tu RAM.
4. Pulsa en **GPU**: arriba a la derecha sale el nombre de tu tarjeta, y **Memoria de GPU dedicada** es tu VRAM. ¿Solo ves gráficos Intel? Entonces no tienes tarjeta aparte.

## Cómo irá en tu PC

#### Tarjeta de 6 GB o más

Rápido en casi todas las tarjetas de los últimos años: de 37 a 76 tokens por segundo en nuestras pruebas, muchas veces más rápido de lo que lees, e imágenes en segundos o minuto y medio. Una excepción: una RX 580 antigua escribía unos 11, aun así más rápido de lo que lees.

#### Tarjeta de 4 GB y 16 GB de RAM

Bien. Unos 20 tokens por segundo en nuestra prueba.

#### Sin tarjeta y 16 GB de RAM

De sobra para chatear y estudiar, con una IA más pequeña. Las imágenes tardan un par de minutos.

#### Sin tarjeta y 8 GB de RAM

Funciona para chatear, despacio. Cierra otras apps antes. Sin imágenes.

## ¿Y por qué tener la IA en tu propio PC?

Porque es tuya. Sin límites de mensajes, sin cuota mensual, y sigue funcionando sin internet: en el tren, en la montaña o en una biblioteca con un wifi horrible. No le gana en todo a las IAs más grandes de la nube, pero para estudiar, escribir, resumir y dudas del día a día, una IA en tu propia tarjeta va sobrada, y nunca se acaba. ¿Lo vas a montar en Windows? [Qué necesita un PC con Windows para usar IA sin internet](https://blog.greencube.app/blog/es/ia-sin-internet-windows).

## FAQ

### ¿Funciona la IA en local con una tarjeta gráfica AMD?

Sí. Medimos tarjetas AMD (RX 5700 XT, RX 6600, RX 580) y también NVIDIA. GreenCube usa Vulkan, que funciona con las dos.

### ¿Cuánta VRAM necesito para usar IA en mi PC?

No hace falta ninguna, pero con 4 GB o más se nota muchísimo. En nuestras pruebas, una GTX 1650 de 4 GB escribía unos 20 tokens por segundo y una RTX 5060 de 8 GB, unos 56. Con más VRAM cabe una IA más grande en la tarjeta.

### ¿Puedo usar IA en un portátil sin tarjeta gráfica?

Sí. Un portátil de 16 GB con solo gráficos Intel escribía entre 14 y 18 tokens por segundo con una IA pequeña, más rápido de lo que lees. Uno de 8 GB también funciona, más despacio, y no puede crear imágenes.

### ¿Más RAM hace que la IA vaya más rápido?

No por sí sola. En un PC con 48 GB de RAM, la misma IA fue 14 veces más rápida en la tarjeta gráfica de 8 GB que en el procesador. La RAM importa si no tienes tarjeta; si la tienes, lo que más cuenta es la VRAM.

### ¿Necesito internet para usar IA en mi PC?

Solo una vez, para descargar la app y la IA y activarla. Después, puedes chatear sin ninguna conexión.
