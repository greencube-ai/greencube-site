# ¿Se puede usar IA con 8 GB de RAM? Probamos el portátil más flojo

> Usar IA con 8 GB de RAM: de 5 a 7 tokens por segundo en chats reales y respuestas en 30 a 40 segundos en nuestro portátil más flojo. Sirve para chatear y estudiar, con una pega: la memoria libre.

Canonical: https://blog.greencube.app/blog/es/ia-con-8gb-de-ram  
Published: 2026-10-18  
Author: Hector Gras

Sí, despacio. Una IA pequeña en un portátil de 8 GB escribe más o menos a la velocidad a la que lees, y una respuesta completa tarda de 30 a 40 segundos. El verdadero problema no es la velocidad, es la memoria libre, así que cierra tus otras apps antes de empezar.

Lo probamos en el PC más flojo que hemos medido, porque "¿funcionará en mi portátil viejo?" es una de las primeras preguntas que se hace la gente sobre la IA local. Funciona. Así es como va.

## La prueba

El portátil tiene 8 GB de RAM y gráficos Intel Iris Xe, sin tarjeta gráfica, y lo usamos con batería. Usamos el modelo pequeño de GreenCube, Cube 2B (basado en [Gemma 4 E2B](https://blog.greencube.app/blog/gemma-4-requirements)), a principios de octubre de 2026.

| Qué | Resultado |
| --- | --- |
| Escritura, en chats reales | **5–7 tokens/s** |
| Escritura, prueba de arranque de GreenCube, procesador | **9,3 tokens/s** |
| Escritura, prueba de arranque de GreenCube, gráficos Iris Xe | **5,0 tokens/s** (más lento) |
| Una respuesta completa | **30–40 s** |
| Memoria libre con otras apps abiertas | **alrededor de 1 GB** |
| Imágenes | **No puede** (la IA de imágenes necesita unos 7 GB) |

## Sirve para chatear y estudiar

De 5 a 7 tokens por segundo en chats reales es más o menos la velocidad de lectura en inglés. La breve prueba de arranque de GreenCube dio 9,3, pero en chats reales salió menos. Para una respuesta larga esperarás medio minuto, pero llega, sin internet y sin límites.

## La memoria libre es el verdadero límite

Con el navegador y otras apps abiertas, al portátil solo le quedaba alrededor de 1 GB de memoria libre. Un día no bastó y la IA ni siquiera pudo arrancar. El modelo pequeño necesita un par de GB para él solo, así que con 8 GB tiene que repartirse con cuidado con todo lo demás que tengas abierto.

## Los gráficos integrados la hicieron más lenta

Cabría esperar que el chip gráfico ayudara, pero en este portátil los gráficos Iris Xe escribían a 5,0 tokens por segundo y el procesador a 9,3. En otro portátil los dos iban más o menos igual. No se puede saber de antemano por las especificaciones, así que GreenCube prueba los dos en tu portátil y usa el más rápido.

## Consejos para un portátil de 8 GB

1. Cierra el navegador, o casi todas sus pestañas, antes de empezar. Los navegadores gastan mucha memoria.
2. Reinicia el portátil antes de una sesión larga de estudio. Libera memoria que otras apps se olvidaron de devolver.
3. Pregunta una cosa cada vez. Las respuestas más cortas llegan antes.
4. Deja las imágenes para un PC más grande. Necesitan unos 7 GB ellas solas.

Para ver cuánto más rápidos son otros PCs, [aquí medimos 10 PCs](https://blog.greencube.app/blog/can-my-pc-run-ai).

## FAQ

### ¿Puedo usar IA en un portátil con 8 GB de RAM?

Sí, un modelo pequeño. En nuestro portátil de 8 GB con gráficos Intel Iris Xe escribía de 5 a 7 tokens por segundo en chats reales, más o menos a ritmo de lectura, y las respuestas tardaban de 30 a 40 segundos. No puede crear imágenes.

### ¿Por qué no arranca la IA en mi portátil de 8 GB?

Normalmente por falta de memoria libre. Nuestro portátil de 8 GB tenía solo 1 GB libre con otras apps abiertas, y un día la IA no pudo cargar. Cerrar el navegador y otras apps antes le deja sitio.

### ¿Los gráficos Intel Iris Xe aceleran la IA en un portátil de 8 GB?

Para chatear, no. En nuestro portátil el procesador escribía a 9,3 tokens por segundo y los gráficos Iris Xe a 5,0. GreenCube prueba los dos en tu portátil y usa el más rápido.
