# IA en un portátil sin tarjeta gráfica: ¿ayudan los gráficos Intel?

> Usamos IA en un portátil sin tarjeta gráfica, en el procesador y en sus gráficos Intel. El chat casi no cambió, leer fue 1,3 veces más rápido y las imágenes, más de 4 veces.

Canonical: https://blog.greencube.app/blog/es/ia-portatil-sin-tarjeta-grafica  
Published: 2026-10-18  
Author: Hector Gras

**Respuesta corta:** para chatear, **casi nada**. Para leer textos largos, **un poco**. Para imágenes, **muchísimo**: más de 4 veces más rápido.

- **~14** tokens por segundo al chatear, con o sin gráficos Intel
- **1,3×** más rápido leyendo textos largos que pegas
- **4×** más rápido creando imágenes

## La prueba

Un portátil: Intel Core Ultra 5 125U, 16 GB de RAM, sin tarjeta gráfica, solo con los gráficos integrados en el chip. Usamos la misma IA en el procesador y en los gráficos Intel, enchufado, dos veces cada una, en septiembre y octubre de 2026.

| Tarea | Procesador | Gráficos Intel | Diferencia |
| --- | --- | --- | --- |
| Escribir una respuesta (Gemma 4 E2B) | 13,7–15,5 tokens/s | 14,4–14,5 tokens/s | **casi igual** |
| Leer texto pegado (Gemma 4 E2B) | 160–167 tokens/s | 203–211 tokens/s | **1,3× más rápido** |
| Una imagen de 512 por 512 | 11 min 27 s | 2 min 22 s – 2 min 38 s | **más de 4× más rápido** |

## Lo que aprendimos

### 1. La velocidad del chat depende de la memoria, no del chip

Escribir una respuesta está limitado por lo rápido que el portátil mueve la IA por su memoria, y el procesador y los gráficos Intel comparten la misma memoria. Por eso escriben a una velocidad parecida.

### 2. Incluso puede ir más lento

Con un modelo pequeño más antiguo (Phi-4 Mini), escribir fue un **29% más lento** en los gráficos Intel. Con uno más grande (Gemma 4 E4B) fue un **26% más rápido**. Mismo portátil, resultados opuestos. No se puede adivinar por las especificaciones, así que GreenCube prueba tu portátil y usa lo que vaya más rápido.

### 3. Donde brillan es en las imágenes

Crear una imagen es cálculo pesado, justo para lo que están hechos los chips gráficos. De 11 minutos y medio a unos 2 y medio.

## ¿Y qué significa para ti?

#### Chatear y estudiar

Un portátil de 16 GB va de sobra. Escribe más rápido de lo que lees.

#### PDFs largos

Los gráficos los leen algo más rápido, así que la primera respuesta llega antes.

#### Imágenes

Se puede, de 2 a 3 minutos cada una. Un PC gaming lo hace en menos de un minuto.

#### Batería

En nuestras pruebas, con batería y enchufado el chat fue a una velocidad parecida.

¿Quieres ver también los PCs gaming? [Medimos 10 PCs aquí.](https://blog.greencube.app/blog/es/ia-en-mi-pc)

## FAQ

### ¿Los gráficos integrados hacen la IA más rápida?

Para chatear, casi nada: en nuestro portátil de 16 GB la respuesta salía a unos 14 tokens por segundo con o sin ellos. Para leer textos largos fue unas 1,3 veces más rápido, y para crear imágenes, más de 4 veces.

### ¿Los gráficos integrados pueden hacer la IA más lenta?

A veces. Con un modelo pequeño, escribir fue un 29% más lento en los gráficos Intel que en el procesador; con uno más grande fue un 26% más rápido. Depende del modelo y del portátil, por eso GreenCube prueba tu propio portátil y elige.

### ¿Un portátil sin tarjeta gráfica sirve para usar IA?

Para chatear y estudiar, sí: un portátil de 16 GB escribe más rápido de lo que lees con un modelo pequeño. Las imágenes también funcionan, pero tardan de 2 a 3 minutos cada una.
