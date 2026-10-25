# Mejor modelo de IA local para tu PC, según RAM y VRAM (medido)

> El mejor modelo de IA local es el más grande que cabe entero en tu tarjeta gráfica con margen. Qué modelo para portátiles de 8 y 16 GB y para tarjetas de 4, 6, 8 y 12 GB, con velocidades reales de Gemma 4 E2B, E4B y 12B medidas en 10 PCs.

Canonical: https://blog.greencube.app/blog/es/mejor-modelo-ia-local  
Published: 2026-10-23  
Author: Hector Gras

**Respuesta corta:** el mejor modelo de IA local para *tu* PC es **el más grande que cabe entero en tu tarjeta gráfica, con unos 1,5 GB de margen**. ¿Sin tarjeta? Un **modelo pequeño** en tu RAM. Un modelo más pequeño entero en la tarjeta gana a uno más grande que se sale: lo medimos y salirse fue **6 veces más lento**. Abajo, la elección para cada tipo de PC, con velocidades medidas en 10 PCs reales.

- **+1,5 GB** el archivo del modelo más unos 1,5 GB tienen que caber en tu VRAM
- **6×** más lento cuando parte del modelo no cabe en la tarjeta
- **10** PCs reales medidos, de portátiles a sobremesas gaming

## El mejor modelo para tu PC

| Tu PC | Tamaño de modelo que cabe | Lo que medimos |
| --- | --- | --- |
| Portátil de 8 GB, sin tarjeta gráfica | Pequeño, unos 2–3 GB (Gemma 4 E2B, 2,6 GB) | **5–7** tokens/s en chats reales; cierra antes las demás apps |
| Portátil de 16 GB, sin tarjeta gráfica | Pequeño para ir rápido; unos 4 GB funciona pero lento | E2B **14–18** tokens/s; E4B **8–10** |
| Tarjeta gráfica de 4 GB | Unos 2–3 GB caben enteros; 4 GB se sale | E4B (4,2 GB, en parte en RAM) unos **20** tokens/s en una GTX 1650 |
| Tarjeta gráfica de 6 GB | Unos 4–4,5 GB | E4B **35–38** tokens/s en una GTX 1660 Super |
| Tarjeta gráfica de 8 GB | Unos 4–6 GB | E4B **56–72** en tarjetas recientes (unos 11 en una RX 580 antigua) |
| Tarjeta gráfica de 12 GB o más | Unos 6–10 GB: modelos tipo 12B | E4B **50–55** en 12 GB; el 12B necesita 10 GB o más para chats largos |

Cada tarjeta con su propia página: [¿Puede mi PC ejecutar IA?](https://blog.greencube.app/blog/es/ia-en-mi-pc) O escribe tu tarjeta en [el comprobador](https://blog.greencube.app/blog/es/ia-en-mi-pc#checker).

## Por qué "que quepa" importa más que "el más grande"

### Si se sale, va más lento que sin tarjeta

En una RX 5700 XT de 8 GB, Gemma 4 12B escribía 35,6 tokens por segundo entero en la tarjeta, 5,9 con parte fuera y 4,3 con todavía menos dentro: más lento que un modelo pequeño sin tarjeta. [La prueba de VRAM completa](https://blog.greencube.app/blog/es/cuanta-vram-para-ia).

### Cabe para una pregunta, se cuelga en un chat largo

El mismo 12B cupo en la tarjeta de 8 GB para una pregunta corta, y se colgó cada vez que el chat crecía: la conversación también necesita sitio. Para eso son los 1,5 GB de margen.

### Lo pequeño a menudo basta

En un portátil de 16 GB, Gemma 4 E2B dio una respuesta de estudio completa en 20 segundos y acertó 5 de 5 comprobaciones rápidas de datos; el E4B explicaba mejor pero tardó 112 segundos. [E2B frente a E4B, medido](https://blog.greencube.app/blog/es/gemma-4-e2b-vs-e4b).

## Los modelos que medimos

| Modelo | Tamaño del archivo | Mejor en | Licencia |
| --- | --- | --- | --- |
| **Gemma 4 E2B** | 2,6 GB | Portátiles, 8–16 GB de RAM | Apache 2.0 |
| **Gemma 4 E4B** | 4,2 GB | Tarjetas gráficas de 6 GB o más | Apache 2.0 |
| **Gemma 4 12B** | unos 6,4 GB | Tarjetas gráficas de 10–12 GB o más | Apache 2.0 |

Son los archivos que distribuye GreenCube y los únicos que hemos cronometrado, así que son los únicos de los que damos velocidades. Las demás familias de modelos siguen la misma regla: mira el tamaño del archivo, súmale unos 1,5 GB y compáralo con tu VRAM. [Requisitos de Gemma 4 en detalle](https://blog.greencube.app/blog/es/requisitos-gemma-4).

## Cómo mirar tu VRAM

1. Pulsa **Ctrl + Shift + Esc** para abrir el Administrador de tareas.
2. Ve a **Rendimiento** y luego a **GPU**.
3. **Memoria dedicada de GPU** es tu VRAM. ¿No tienes memoria dedicada? Usa un modelo pequeño en la RAM.

¿Prefieres no elegir? GreenCube mira tu tarjeta y tu RAM y elige el modelo que cabe, con margen. Las apps gratis como LM Studio, Jan y Ollama te dejan elegir a ti: [12 apps comparadas](https://blog.greencube.app/blog/es/mejor-chatbot-ia-sin-internet).

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
