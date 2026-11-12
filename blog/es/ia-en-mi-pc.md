# ¿Puedo usar IA en mi PC? Lo medimos en 10 PCs gaming y portátiles

> ¿Puedes tener IA en tu PC? Velocidades reales de 10 PCs, de una GTX 1650 a una RTX 2080 Ti y portátiles sin tarjeta gráfica, y qué significan tu gráfica, la VRAM y la RAM.

Canonical: https://blog.greencube.app/blog/es/ia-en-mi-pc  
Published: 2026-10-18  
Author: Hector Gras

Sí. Si tu PC mueve juegos, puede mover una IA. Lo medimos en 10 PCs reales, desde sobremesas gaming con una GTX 1650 veterana hasta una RTX 2080 Ti, más dos portátiles sin tarjeta gráfica, y todos chatearon con una IA que funcionaba entera dentro del PC, sin internet. Lo que cambia de un PC a otro es la velocidad.

Hicimos todas las pruebas con GreenCube, la app que hago yo, porque es la que podemos medir al detalle. La velocidad depende mucho más del hardware que de la app. Escribe tu tarjeta gráfica aquí abajo para ver lo que encontramos con ella.

## ¿Funcionará la IA en tu PC?

Escribe tu tarjeta gráfica y elige tu RAM: verás qué funciona, a qué velocidad fue en PCs reales y qué no hemos medido aún. Interactive, on the page: https://blog.greencube.app/blog/es/ia-en-mi-pc#checker

## Los números

"Escribe" es la velocidad a la que la IA teclea su respuesta, en tokens por segundo. Un token son unos tres cuartos de una palabra en inglés. La mayoría de la gente lee en inglés unas 4 palabras por segundo ([Brysbaert, 2019](https://doi.org/10.1016/j.jml.2019.104047)), que son más o menos 5 tokens, así que todo lo que pase de 5 va más rápido que tus ojos.

| PC | Gráfica | RAM | IA | Escribe (tokens/s) |
| --- | --- | --- | --- | --- |
| Sobremesa | [NVIDIA RTX 2080 Ti, 11 GB](https://blog.greencube.app/blog/es/ia-en-rtx-2080-ti) | 128 GB | Cube 4B (Gemma 4 E4B) | **65–71** |
| Sobremesa | [AMD RX 5700 XT, 8 GB](https://blog.greencube.app/blog/es/ia-en-rx-5700-xt) | 48 GB | Cube 4B (Gemma 4 E4B) | **63–72** |
| Sobremesa | [NVIDIA RTX 5060, 8 GB](https://blog.greencube.app/blog/es/ia-en-rtx-5060) | 32 GB | Cube 4B (Gemma 4 E4B) | **56** |
| Sobremesa | [NVIDIA RTX 3060, 12 GB](https://blog.greencube.app/blog/es/ia-en-rtx-3060) | 32 GB | Cube 4B (Gemma 4 E4B) | **53–55** |
| Sobremesa | [AMD RX 6600, 8 GB](https://blog.greencube.app/blog/es/ia-en-rx-6600) | 16 GB | Cube 4B (Gemma 4 E4B) | **42–44** |
| Sobremesa | [NVIDIA GTX 1660 Super, 6 GB](https://blog.greencube.app/blog/es/ia-en-gtx-1660-super) | 16 GB | Cube 4B (Gemma 4 E4B) | **37–38** |
| Sobremesa | [NVIDIA GTX 1650, 4 GB](https://blog.greencube.app/blog/es/ia-en-gtx-1650) | 16 GB | Cube 4B (Gemma 4 E4B) | **unos 20** |
| Portátil | [Solo gráficos Intel (Core Ultra 5)](https://blog.greencube.app/blog/es/ia-en-portatil-intel-core-ultra-5) | 16 GB | Cube 2B (Gemma 4 E2B) | **14–18** |
| Sobremesa | [AMD RX 580, 8 GB](https://blog.greencube.app/blog/es/ia-en-rx-580) | 16 GB | Cube 4B (Gemma 4 E4B) | **10–11** |
| Portátil | [Solo Intel Iris Xe](https://blog.greencube.app/blog/es/ia-en-portatil-intel-iris-xe) | 8 GB | Cube 2B (Gemma 4 E2B) | **5–7** |

Pulsa una tarjeta gráfica para ver su prueba completa. Medimos en septiembre y octubre de 2026, en chats reales y con la prueba de velocidad de la propia GreenCube. La velocidad varía un poco entre pruebas en el mismo PC, así que cuando tenemos varias damos el rango.

## Lo que aprendimos

### La tarjeta gráfica hace el trabajo duro, como en un juego

En el sobremesa con la RX 5700 XT, la misma IA escribía 5 tokens por segundo en el procesador y 72 en la tarjeta gráfica. Son 14 veces más rápido, en el mismo PC y con la misma IA. Una IA es sobre todo el tipo de cálculo para el que están hechas las tarjetas gráficas, así que cualquier tarjeta de los últimos años ayuda muchísimo. Hasta una GTX 1650 antigua de 4 GB escribía unos 20 tokens por segundo.

### La VRAM decide qué tamaño de IA cabe

Para ir a toda velocidad, la IA tiene que caber en la memoria propia de la tarjeta (la VRAM). Ese mismo sobremesa tenía 48 GB de RAM y no le sirvieron para un modelo más grande: una IA de 12.000 millones de parámetros cupo en la tarjeta de 8 GB para una pregunta corta y se cayó en cuanto el chat se alargó, con la tarjeta casi llena. Para la IA, la VRAM importa más que la RAM ([la prueba completa de VRAM](https://blog.greencube.app/blog/how-much-vram-for-ai)).

Eso sí, VRAM no es velocidad. Cuatro tarjetas de 8 GB que medimos escribían desde unos 11 tokens por segundo (RX 580) hasta 72 (RX 5700 XT). Por eso GreenCube mira tu tarjeta y elige una IA que quepa, en vez de la más grande.

### Sin tarjeta gráfica también funciona

Un portátil normal de 16 GB con solo gráficos Intel escribía entre 14 y 18 tokens por segundo con la IA más pequeña, y terminó una respuesta completa (una explicación y tres preguntas de examen) en unos 20 segundos. Para estudiar y escribir va de sobra. Uno de 8 GB también funciona, a entre 5 y 7 tokens por segundo en chats reales, siempre que las demás apps le dejen algo de memoria libre.

### Las imágenes son lo pesado

Crear una imagen cuesta mucho más que chatear. Tardó de 8 a 9 segundos con una RTX 2080 Ti de 11 GB (la primera, 83 mientras cargaba), 28 segundos con una RTX 3060 de 12 GB, un minuto con una RX 6600 de 8 GB, minuto y medio con una GTX 1660 Super de 6 GB y unos dos minutos y medio en el portátil de 16 GB. Un portátil de 8 GB no puede crear imágenes, porque la IA de imágenes necesita ella sola unos 7 GB.

## Mira tu PC en 30 segundos

1. Pulsa Ctrl + Mayús + Esc para abrir el Administrador de tareas.
2. Entra en Rendimiento.
3. Pulsa en Memoria. El número de arriba a la derecha es tu RAM.
4. Pulsa en GPU. El nombre de arriba a la derecha es tu tarjeta, y la Memoria de GPU dedicada es tu VRAM. Si solo ves gráficos Intel, no tienes tarjeta aparte.

## Cómo irá en tu PC

| Tu PC | Qué esperar |
| --- | --- |
| Tarjeta gráfica de 6 GB o más | Rápido en la mayoría de tarjetas de los últimos años: de 37 a 76 tokens por segundo en nuestras pruebas, e imágenes en segundos o en minuto y medio. La excepción fue una RX 580 antigua, con unos 11, aun así más rápido de lo que lees. |
| Tarjeta de 4 GB, 16 GB de RAM | Bien: unos 20 tokens por segundo en nuestra prueba. |
| Sin tarjeta, 16 GB de RAM | Suficiente para chatear y estudiar con una IA más pequeña. Las imágenes tardan un par de minutos. |
| Sin tarjeta, 8 GB de RAM | Funciona para chatear, despacio. Cierra antes otras apps. Sin imágenes. |

## ¿Y para qué tener la IA en tu propio PC?

Una IA en tu propio PC no tiene límites de mensajes ni cuota mensual, y sigue funcionando sin internet, en el tren o en una biblioteca con un wifi horrible. No le gana en todo a las IAs más grandes de la nube, y va tan rápido como tu hardware. Pero para estudiar, escribir, resumir y dudas del día a día, la IA de un PC normal cumple, y nunca se acaba.

Si la vas a montar en Windows, [qué necesita un PC con Windows para usar IA sin internet](https://blog.greencube.app/blog/local-ai-chatbot-windows) repasa los detalles.

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
