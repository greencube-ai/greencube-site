# ¿Cuánta VRAM necesitas para la IA? Por qué tiene que caber en tu gráfica

> ¿Cuánta VRAM necesitas para usar IA en local? Lo medimos: un modelo que no cabe en tu tarjeta gráfica va 6 veces más lento y falla en chats largos. Cómo elegir uno que quepa.

Canonical: https://blog.greencube.app/blog/es/cuanta-vram-para-ia  
Published: 2026-10-18  
Author: Hector Gras

**Respuesta corta:** una IA que cabe entera en la memoria de tu tarjeta gráfica (la VRAM) va rápida. Una que se sale va **más lenta que si no usaras la tarjeta**, y puede fallar. Más pequeña y entera en la tarjeta gana a más grande y a medias.

- **35,6** tokens por segundo con el modelo entero en la tarjeta
- **5,9** con una parte fuera de la tarjeta: 6 veces más lento
- **Fallo** cuando un modelo que apenas cabe se encuentra con un chat largo

## La prueba

Un sobremesa con una AMD RX 5700 XT (8 GB de VRAM) y 48 GB de RAM. Cargamos un modelo de 12.000 millones de parámetros (Gemma 4 12B, unos 6,2 GB) y pusimos más o menos parte de él en la tarjeta, todo en la misma sesión, en septiembre de 2026.

| Cuánto del modelo estaba en la tarjeta | Escribe (tokens/s) |
| --- | --- |
| Todo | **35,6** |
| 28 de sus capas | **5,9** |
| 20 de sus capas | **4,3** |
| *Para comparar: un modelo más pequeño (Gemma 4 E4B) solo en el procesador* | **5,0** |
| *Ese modelo pequeño, entero en la tarjeta* | **72,5** |

## Lo que aprendimos

### 1. Todo o nada

Dejar solo una parte del modelo fuera de la tarjeta lo hizo **6 veces más lento**. Con 20 capas en la tarjeta fue más lento que un modelo más pequeño sin usar la tarjeta. A medias es lo peor de los dos mundos.

### 2. El más grande no es el mejor

El modelo 12B sí cabía entero en la tarjeta de 8 GB, para una pregunta corta. Al crecer el chat, falló todas las veces: a la tarjeta casi no le quedaba sitio para la conversación. El modelo más pequeño tenía unos 3 GB de margen e iba a entre 63 y 72 tokens por segundo.

### 3. Deja margen

En una GTX 1650 de 4 GB, un modelo de 4,2 GB se metió a presión en una tarjeta de 3,9 GB, y el primer mensaje ya falló con "no hay memoria suficiente". GreenCube deja ahora unos **1,5 GB de la tarjeta libres** para el chat y para Windows.

## Cómo elegir un modelo para tu tarjeta

#### Mira tu VRAM

Administrador de tareas → Rendimiento → GPU → Memoria de GPU dedicada.

#### Tamaño del modelo + 1,5 GB

El archivo del modelo más unos 1,5 GB tienen que caber en ese número.

#### Si dudas, más pequeño

Un modelo pequeño entero en la tarjeta gana a uno grande a medias.

#### O deja que elija la app

GreenCube mira tu tarjeta y elige un modelo que quepa con margen.

Velocidades reales en 10 PCs, de una GTX 1650 a una RTX 5060: [míralas aquí](https://blog.greencube.app/blog/es/ia-en-mi-pc).

## FAQ

### ¿Qué pasa si un modelo de IA no cabe en la VRAM?

La parte que no cabe funciona desde la memoria normal y todo va más lento. En nuestra tarjeta de 8 GB, un modelo con 28 de sus capas en la tarjeta escribía a 5,9 tokens por segundo en vez de 35,6 con todas: 6 veces más lento.

### ¿Debería usar el modelo más grande que cargue mi tarjeta?

No. Deja sitio para la conversación. Un modelo de 12.000 millones de parámetros cupo en una tarjeta de 8 GB para una pregunta corta, y se cayó en cuanto el chat se alargó. Uno más pequeño que cabía con margen fue más rápido y nunca falló.

### ¿Cuánta VRAM debo dejar libre?

GreenCube deja libres unos 1,5 GB de la tarjeta para la conversación y para Windows. Sin ese margen, una tarjeta de 4 GB se quedó sin memoria en el primer mensaje.
