# IA en un portátil sin tarjeta gráfica: ¿ayudan los gráficos Intel?

> Usamos IA en un portátil sin tarjeta gráfica, en el procesador y en sus gráficos Intel. El chat casi no cambió, leer fue 1,3 veces más rápido y las imágenes, más de 4 veces.

Canonical: https://blog.greencube.app/blog/es/ia-portatil-sin-tarjeta-grafica  
Published: 2026-10-18  
Author: Hector Gras

Sí, puedes usar IA en un portátil sin tarjeta gráfica, y un portátil de 16 GB escribe más rápido de lo que lees. Los gráficos Intel integrados en el chip apenas ayudan al chatear, ayudan un poco al leer textos largos y ayudan mucho con las imágenes, que salieron más de 4 veces más rápido.

Queríamos saber si merece la pena usar para la IA los gráficos que lleva integrados casi cualquier portátil, así que hicimos las mismas tareas con el procesador y con los gráficos Intel de un portátil normal.

## La prueba

El portátil tiene un Intel Core Ultra 5 125U, 16 GB de RAM y ninguna tarjeta gráfica, solo los gráficos integrados en el chip. Ejecutamos la misma IA en el procesador y en los gráficos Intel, enchufado, dos veces cada una, en septiembre y octubre de 2026.

| Tarea | Procesador | Gráficos Intel | Diferencia |
| --- | --- | --- | --- |
| Escribir una respuesta (Gemma 4 E2B) | 13,7–15,5 tokens/s | 14,4–14,5 tokens/s | **más o menos igual** |
| Leer texto pegado (Gemma 4 E2B) | 160–167 tokens/s | 203–211 tokens/s | **1,3× más rápido** |
| Una imagen, 512 por 512 | 11 min 27 s | 2 min 22 s – 2 min 38 s | **más de 4× más rápido** |

## La velocidad del chat depende de la memoria, no del chip

Lo que limita la escritura de una respuesta es lo rápido que el portátil puede mover la IA por su memoria. El procesador y los gráficos Intel comparten esa misma memoria, así que acaban escribiendo más o menos a la misma velocidad.

## Incluso puede ir más lento

Con un modelo pequeño más antiguo, Phi-4 Mini, escribir fue un 29% más lento en los gráficos Intel. Con uno más grande, [Gemma 4 E4B](https://blog.greencube.app/blog/gemma-4-requirements), fue un 26% más rápido. Mismo portátil, resultados opuestos. No se puede adivinar por las especificaciones, así que GreenCube prueba tu portátil y usa lo que vaya más rápido.

## Donde sí compensa es en las imágenes

Hacer una imagen son cálculos pesados, justo para lo que están hechos los chips gráficos, y aquí la diferencia fue enorme: de 11 minutos y medio se pasó a unos 2 y medio. Los detalles están en [cuánto tarda una imagen](https://blog.greencube.app/blog/local-ai-image-generator-speed).

## Qué significa para tu portátil

Para chatear y estudiar, un portátil de 16 GB se basta solo. Escribe más rápido de lo que lees, con o sin los gráficos. Con PDFs largos, los gráficos los leen un poco más rápido, así que la primera respuesta llega antes.

En un portátil así se pueden hacer imágenes, a unos 2 o 3 minutos cada una, mientras que un PC gaming hace una en menos de un minuto. Y si trabajas desenchufado, en nuestras pruebas la batería y la corriente dieron más o menos la misma velocidad de chat.

Para verlo todo, PCs gaming incluidos, [aquí medimos 10 PCs](https://blog.greencube.app/blog/can-my-pc-run-ai).

## FAQ

### ¿Los gráficos integrados hacen la IA más rápida?

Para chatear, casi nada: en nuestro portátil de 16 GB la respuesta salía a unos 14 tokens por segundo con o sin ellos. Para leer textos largos pegados fue unas 1,3 veces más rápido, y para crear imágenes, más de 4 veces.

### ¿Los gráficos integrados pueden hacer la IA más lenta?

A veces. Con un modelo pequeño, escribir fue un 29% más lento en los gráficos Intel que en el procesador; con uno más grande fue un 26% más rápido. Depende del modelo y del portátil, por eso GreenCube prueba tu propio portátil y elige.

### ¿Un portátil sin tarjeta gráfica sirve para usar IA?

Para chatear y estudiar, sí: un portátil de 16 GB escribe más rápido de lo que lees con un modelo pequeño. Las imágenes también funcionan, pero tardan de 2 a 3 minutos cada una.
