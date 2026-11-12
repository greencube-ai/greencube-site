# Mejor modelo de IA local para tu PC, según RAM y VRAM (medido)

> El mejor modelo de IA local es el más grande que cabe entero en tu tarjeta gráfica con margen. Qué modelo para portátiles de 8 y 16 GB y para tarjetas de 4, 6, 8 y 12 GB, con velocidades reales de Gemma 4 E2B, E4B y 12B medidas en 10 PCs.

Canonical: https://blog.greencube.app/blog/es/mejor-modelo-ia-local  
Published: 2026-10-23  
Author: Hector Gras

El mejor modelo de IA local para tu PC es el más grande que cabe entero en tu tarjeta gráfica con unos 1,5 GB de margen. Sin tarjeta gráfica, elige un modelo pequeño que funcione en tu RAM. Un modelo más pequeño entero en la tarjeta gana a uno más grande que se sale: cuando parte de un modelo no cabía, lo medimos 6 veces más lento.

Abajo está la elección para cada tipo de PC, con velocidades que medimos en 10 PCs reales. Algo que conviene saber antes: solo hemos cronometrado los modelos Gemma 4 que trae GreenCube (yo hago GreenCube), así que son los únicos modelos de los que doy velocidades. La regla del tamaño vale para cualquier familia de modelos.

## El mejor modelo para tu PC

| Tu PC | Tamaño de modelo que cabe | Lo que medimos |
| --- | --- | --- |
| Portátil de 8 GB, sin tarjeta gráfica | Pequeño, de unos 2–3 GB (Gemma 4 E2B, 2,6 GB) | **5–7** tokens/s en chats reales; cierra antes otras apps |
| Portátil de 16 GB, sin tarjeta gráfica | Pequeño para ir rápido; uno de unos 4 GB funciona, pero lento | E2B **14–18** tokens/s; E4B **8–10** |
| Tarjeta gráfica de 4 GB | Unos 2–3 GB caben enteros; 4 GB se salen | E4B (4,2 GB, en parte en la RAM) unos **20** tokens/s en una GTX 1650 |
| Tarjeta gráfica de 6 GB | Unos 4–4,5 GB | E4B **35–38** tokens/s en una GTX 1660 Super |
| Tarjeta gráfica de 8 GB | Unos 4–6 GB | E4B **56–72** en tarjetas recientes (unos 11 en una RX 580 antigua) |
| Tarjeta gráfica de 12 GB o más | Unos 6–10 GB: modelos de la clase 12B | E4B **50–55** en 12 GB; 12B necesita 10 GB o más para chats largos |

Cada tarjeta tiene su propia página en [¿Puede mi PC ejecutar IA?](https://blog.greencube.app/blog/can-my-pc-run-ai), o puedes escribir la tuya en [el comprobador](https://blog.greencube.app/blog/can-my-pc-run-ai#checker).

## Por qué "que quepa" importa más que "el más grande"

Cuando un modelo se sale de la tarjeta, puede acabar yendo más lento que sin tarjeta. En una RX 5700 XT de 8 GB, Gemma 4 12B escribía 35,6 tokens por segundo entero en la tarjeta, 5,9 con una parte fuera y 4,3 con todavía menos dentro. Ese último número es más lento que un modelo más pequeño funcionando sin tarjeta. La prueba completa está en [cuánta VRAM necesitas para la IA](https://blog.greencube.app/blog/how-much-vram-for-ai).

Caber para una pregunta tampoco es lo mismo que caber para un chat. El mismo modelo 12B cupo en la tarjeta de 8 GB para una pregunta corta y luego se colgó cada vez que la conversación crecía, porque la conversación también necesita sitio en la tarjeta. Para eso es el margen de 1,5 GB.

Y a menudo lo pequeño basta. En un portátil de 16 GB, Gemma 4 E2B dio una respuesta de estudio completa en 20 segundos y acertó 5 de 5 preguntas rápidas de datos. E4B explicaba mejor, pero tardó 112 segundos. Hay más en [E2B contra E4B, medido](https://blog.greencube.app/blog/gemma-4-e2b-vs-e4b).

## Los modelos que medimos

| Modelo | Tamaño del archivo | Mejor en | Licencia |
| --- | --- | --- | --- |
| Gemma 4 E2B | 2,6 GB | Portátiles, 8–16 GB de RAM | Apache 2.0 |
| Gemma 4 E4B | 4,2 GB | Tarjetas gráficas de 6 GB o más | Apache 2.0 |
| Gemma 4 12B | unos 6,7 GB | Tarjetas gráficas de 10–12 GB o más | Apache 2.0 |

Para cualquier otro modelo vale la misma regla: toma el tamaño del archivo, súmale unos 1,5 GB y compáralo con tu VRAM. Los detalles de Gemma están en [requisitos de Gemma 4](https://blog.greencube.app/blog/gemma-4-requirements).

## Cómo ver tu VRAM

1. Pulsa Ctrl + Mayús + Esc para abrir el Administrador de tareas.
2. Ve a Rendimiento y luego a GPU.
3. Mira la memoria dedicada de GPU: esa es tu VRAM. Si no hay memoria dedicada, usa un modelo pequeño en la RAM.

Las apps gratuitas como LM Studio, Jan y Ollama te dejan elegir el modelo tú ([12 apps comparadas](https://blog.greencube.app/blog/best-offline-ai-chatbot)). Si prefieres no elegir nada, GreenCube lee tu tarjeta y tu RAM y escoge un modelo que quepa con margen.

## FAQ

### ¿Cuál es el mejor modelo de IA local?

El modelo más grande que cabe entero en tu tarjeta gráfica con unos 1,5 GB de margen. Un modelo más pequeño entero en la tarjeta gana a uno más grande que se sale a la RAM: en nuestra prueba, un modelo con parte fuera de una tarjeta de 8 GB fue 6 veces más lento.

### ¿Cuál es el mejor modelo de IA local para un portátil sin tarjeta gráfica?

Uno pequeño. Gemma 4 E2B (2,6 GB) escribía de 14 a 18 tokens por segundo en un portátil de 16 GB y de 5 a 7 en uno de 8 GB en chats reales; el E4B, más grande, tardó 112 segundos en una respuesta que el E2B dio en 20.

### ¿Cuál es el mejor modelo de IA local para una tarjeta gráfica de 8 GB?

Un modelo de unos 4 a 5 GB, como Gemma 4 E4B (4,2 GB): escribía de 56 a 72 tokens por segundo en tarjetas gaming de 8 GB. Un modelo de 12.000 millones de parámetros cupo para preguntas cortas pero se colgó en chats largos.

### ¿Cómo sé si un modelo cabe en mi tarjeta gráfica?

Toma el tamaño del archivo del modelo y súmale unos 1,5 GB para la conversación y Windows. Si es menos que la memoria dedicada de tu tarjeta (Administrador de tareas, Rendimiento, GPU), cabe.

### ¿Tengo que elegir yo el modelo?

En apps gratis como LM Studio, Jan u Ollama, sí. GreenCube mira tu tarjeta y tu RAM y elige por ti el modelo que cabe.
