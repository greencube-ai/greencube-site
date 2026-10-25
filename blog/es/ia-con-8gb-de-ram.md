# ¿Se puede usar IA con 8 GB de RAM? Probamos el portátil más flojo

> Usar IA con 8 GB de RAM: de 5 a 7 tokens por segundo en chats reales y respuestas en 30 a 40 segundos en nuestro portátil más flojo. Sirve para chatear y estudiar, con una pega: la memoria libre.

Canonical: https://blog.greencube.app/blog/es/ia-con-8gb-de-ram  
Published: 2026-10-18  
Author: Hector Gras

**Respuesta corta: sí, despacio.** Una IA pequeña en un portátil de 8 GB escribe algo más rápido de lo que lees. La pega no es la velocidad: es la **memoria libre**. Cierra las demás apps antes.

- **9,3** tokens por segundo en el procesador: algo más rápido de lo que lees
- **30–40 s** por respuesta completa
- **~1 GB** de memoria libre con otras apps abiertas, el verdadero problema

## La prueba

El PC más flojo que hemos medido: un portátil con 8 GB de RAM, gráficos Intel Iris Xe, sin tarjeta gráfica y con batería. Modelo pequeño (Gemma 4 E2B), a principios de octubre de 2026.

| Qué | Resultado |
| --- | --- |
| Escribir, en chats reales | **5–7 tokens/s** |
| Escribir, prueba de arranque de GreenCube, procesador | **9,3 tokens/s** |
| Escribir, prueba de arranque de GreenCube, gráficos Iris Xe | **5,0 tokens/s** (más lento) |
| Una respuesta completa | **30–40 s** |
| Memoria libre con otras apps abiertas | **alrededor de 1 GB** |
| Imágenes | **No puede** (la IA de imágenes necesita unos 7 GB) |

## Lo que aprendimos

### 1. Sirve para chatear y estudiar

De 5 a 7 tokens por segundo en chats reales es más o menos ritmo de lectura (la prueba corta de arranque dio 9,3). Esperarás medio minuto para una respuesta larga, pero llega, sin internet y sin límites.

### 2. La memoria libre es el verdadero límite

Con el navegador y otras apps abiertas, al portátil le quedaba solo 1 GB libre. Un día no fue suficiente y la IA ni siquiera arrancó. El modelo pequeño necesita un par de GB para él solo.

### 3. Los gráficos integrados lo hicieron más lento

En este portátil los gráficos Iris Xe escribían a 5,0 tokens por segundo y el procesador a 9,3. En otro portátil iban casi igual. No se puede saber de antemano, así que GreenCube prueba los dos y usa el más rápido.

## Consejos para un portátil de 8 GB

1. **Cierra el navegador** (o casi todas las pestañas) antes de empezar. Los navegadores se comen la memoria.
2. **Reinicia el portátil** antes de una sesión larga de estudio. Libera memoria que otras apps no devolvieron.
3. **Haz preguntas más cortas**, o de una en una. Las respuestas cortas llegan antes.
4. **Olvídate de las imágenes.** Necesitan unos 7 GB; usa un PC más grande para eso.

Mira cuánto más rápidos son otros PCs: [medimos 10 PCs aquí](https://blog.greencube.app/blog/es/ia-en-mi-pc).

## FAQ

### ¿Puedo usar IA en un portátil con 8 GB de RAM?

Sí, un modelo pequeño. En nuestro portátil de 8 GB con gráficos Intel Iris Xe escribía de 5 a 7 tokens por segundo en chats reales, más o menos a ritmo de lectura, y las respuestas tardaban de 30 a 40 segundos. No puede crear imágenes.

### ¿Por qué no arranca la IA en mi portátil de 8 GB?

Normalmente por falta de memoria libre. Nuestro portátil de 8 GB tenía solo 1 GB libre con otras apps abiertas, y un día la IA no pudo cargar. Cerrar el navegador y otras apps antes le deja sitio.

### ¿Los gráficos Intel Iris Xe aceleran la IA en un portátil de 8 GB?

Para chatear, no. En nuestro portátil el procesador escribía a 9,3 tokens por segundo y los gráficos Iris Xe a 5,0. GreenCube prueba los dos en tu portátil y usa el más rápido.
