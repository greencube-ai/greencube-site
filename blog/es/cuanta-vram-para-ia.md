# ¿Cuánta VRAM necesitas para la IA? Por qué tiene que caber en tu gráfica

> ¿Cuánta VRAM necesitas para usar IA en local? Lo medimos: un modelo que no cabe en tu tarjeta gráfica va 6 veces más lento y falla en chats largos. Cómo elegir uno que quepa.

Canonical: https://blog.greencube.app/blog/es/cuanta-vram-para-ia  
Published: 2026-10-18  
Author: Hector Gras

Necesitas VRAM suficiente para el modelo entero más unos 1,5 GB para la conversación y Windows. Una IA que cabe entera en la memoria de tu tarjeta gráfica va rápida. Una que se sale puede acabar yendo más lenta que si no usaras la tarjeta, y puede fallar. Más pequeña y entera en la tarjeta gana a más grande y a medias.

No lo sacamos de una ficha técnica. Lo medimos en un PC gaming real mientras construíamos GreenCube, la app que hago, y los resultados cambiaron cómo GreenCube elige el modelo.

## La prueba

El PC era un sobremesa con una AMD RX 5700 XT (8 GB de VRAM) y 48 GB de RAM. Cargamos un modelo de 12.000 millones de parámetros (Gemma 4 12B, unos 6,7 GB) y pusimos más o menos parte de él en la tarjeta, todo en una misma sesión, en septiembre de 2026.

| Cuánto del modelo estaba en la tarjeta | Escribe (tokens/s) |
| --- | --- |
| Todo | **35,6** |
| 28 de sus capas | **5,9** |
| 20 de sus capas | **4,3** |
| *Para comparar: un modelo más pequeño (Gemma 4 E4B) solo en el procesador* | **5,0** |
| *Ese modelo más pequeño, entero en la tarjeta* | **72,5** |

## Lo que aprendimos

### Es casi todo o nada

Dejar solo una parte del modelo fuera de la tarjeta lo hizo 6 veces más lento. Con 20 capas en la tarjeta fue más lento que un modelo más pequeño funcionando sin tarjeta. A medias en la tarjeta tienes lo peor de los dos mundos.

### El modelo más grande que carga no es el mejor

El modelo 12B sí cabía entero en la tarjeta de 8 GB, para una pregunta corta. Al crecer el chat, se cayó todas las veces, porque a la tarjeta casi no le quedaba sitio para la conversación. El modelo más pequeño tenía unos 3 GB de margen e iba a entre 63 y 72 tokens por segundo.

### Deja margen

En una GTX 1650 de 4 GB, un modelo de 4,2 GB se metió a presión en una tarjeta de 3,9 GB, y el primer mensaje ya falló con "no hay memoria suficiente". Desde entonces, GreenCube deja libres unos 1,5 GB de la tarjeta para el chat y para Windows.

## Cómo elegir un modelo para tu tarjeta

1. Mira tu VRAM: Administrador de tareas → Rendimiento → GPU → Memoria de GPU dedicada.
2. Suma unos 1,5 GB al tamaño del archivo del modelo. Ese total tiene que caber en tu VRAM.
3. Si dudas, elige uno más pequeño. Un modelo más pequeño entero en la tarjeta gana a uno más grande a medias.

Si prefieres no hacer cuentas, GreenCube lee tu tarjeta y elige un modelo que quepa con margen. Las velocidades reales en 10 PCs, de una GTX 1650 a una RTX 5060, están en [¿Puede mi PC ejecutar IA?](https://blog.greencube.app/blog/can-my-pc-run-ai)

## FAQ

### ¿Qué pasa si un modelo de IA no cabe en la VRAM?

La parte que no cabe funciona desde la memoria normal y todo va más lento. En nuestra tarjeta de 8 GB, un modelo con 28 de sus capas en la tarjeta escribía a 5,9 tokens por segundo en vez de 35,6 con todas: 6 veces más lento.

### ¿Debería usar el modelo más grande que cargue mi tarjeta?

No. Deja sitio para la conversación. Un modelo de 12.000 millones de parámetros cupo en una tarjeta de 8 GB para una pregunta corta, y se cayó en cuanto el chat se alargó. Uno más pequeño que cabía con margen fue más rápido y nunca falló.

### ¿Cuánta VRAM debo dejar libre?

GreenCube deja libres unos 1,5 GB de la tarjeta para la conversación y para Windows. Sin ese margen, una tarjeta de 4 GB se quedó sin memoria en el primer mensaje.
