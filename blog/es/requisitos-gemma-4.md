# Requisitos de Gemma 4: qué PC necesitas para usarlo en local

> Requisitos de Gemma 4 E2B, E4B y 12B, medidos en PCs reales: cuánta RAM y VRAM necesita cada uno y a qué velocidad va en portátiles y en tarjetas gráficas gaming.

Canonical: https://blog.greencube.app/blog/es/requisitos-gemma-4  
Published: 2026-10-18  
Author: Hector Gras

El Gemma 4 más pequeño, E2B, funciona en un portátil de 8 GB sin tarjeta gráfica. E4B pide 16 GB de RAM, o cualquier tarjeta gráfica de 6 GB o más, donde va rápido. Gemma 4 12B necesita al menos 10 GB de VRAM para aguantar una conversación de verdad.

Estos números salen de nuestras propias pruebas. GreenCube, la app que hago, funciona con Gemma 4 (Cube 2B está basado en Gemma 4 E2B y Cube 4B en Gemma 4 E4B), así que hemos cronometrado estos modelos en 10 PCs reales, en septiembre y octubre de 2026. Gemma 4 en sí es gratis: Google lo publicó con licencia Apache 2.0, que permite el uso comercial.

## Requisitos de Gemma 4 de un vistazo

| Modelo | Tamaño del archivo | Mínimo que recomendaríamos | Mejor en |
| --- | --- | --- | --- |
| Gemma 4 E2B | 2,6 GB | 8 GB de RAM, sin tarjeta | Portátiles |
| Gemma 4 E4B | 4,2 GB | 16 GB de RAM, o una tarjeta de 6 GB | PCs gaming, portátiles de 16 GB |
| Gemma 4 12B | 6,7 GB | 10 GB de VRAM o más | Tarjetas de 12 GB o más |

El tamaño del archivo es solo el principio. Mientras chateas, la conversación también ocupa memoria, así que deja un par de GB libres de margen. En un portátil de 8 GB eso significa cerrar antes otras apps.

## Velocidades medidas

Esta es la velocidad a la que cada modelo escribe su respuesta, en tokens por segundo. Un token son unos tres cuartos de una palabra en inglés, y la mayoría de la gente lee en inglés unos 5 por segundo, así que todo lo que pase de ahí se nota rápido.

| PC | Modelo | Escribe (tokens/s) |
| --- | --- | --- |
| Sobremesa, AMD RX 5700 XT 8 GB | E4B | **63–72** |
| Sobremesa, NVIDIA RTX 5060 8 GB | E4B | **56** |
| Sobremesa, tarjeta gráfica de 12 GB | E4B | **50–55** |
| Sobremesa, NVIDIA GTX 1660 Super 6 GB | E4B | **35–38** |
| Sobremesa, AMD RX 5700 XT 8 GB | 12B | **20–35** (solo chats cortos) |
| Sobremesa, NVIDIA GTX 1650 4 GB | E4B | **unos 20** |
| Portátil, Intel Core Ultra 5, 16 GB | E2B | **14–18** |
| El mismo portátil | E4B | **8–10** |
| Portátil, Intel Iris Xe, 8 GB | E2B | **5–7** |

## Lo que aprendimos

### E2B es el modelo para portátiles

En un portátil de 16 GB sin tarjeta gráfica, E2B terminó una respuesta completa de estudio en unos 20 segundos. E4B tardó 112 segundos en lo mismo. E2B además acertó nuestras cinco preguntas rápidas de datos. La comparación completa está en [E2B contra E4B, medido](https://blog.greencube.app/blog/gemma-4-e2b-vs-e4b).

### E4B es el modelo para PCs gaming

En cuanto el modelo entero está en una tarjeta gráfica, E4B va de 7 a 9 veces más rápido que en un portátil, y sus respuestas son mejores que las de E2B. Cualquier tarjeta de 6 GB o más lo aloja entero.

### 12B necesita VRAM de verdad, no solo RAM

En una tarjeta de 8 GB, 12B contestó bien una pregunta corta y luego se cayó cada vez que el chat crecía. Ese PC tenía 48 GB de RAM y no le sirvieron de nada, porque el modelo y la conversación tienen que caber los dos en la tarjeta. Hay más sobre esto en [por qué el modelo tiene que caber en tu tarjeta](https://blog.greencube.app/blog/how-much-vram-for-ai).

## ¿Qué Gemma 4 para tu PC?

| Tu PC | Usa |
| --- | --- |
| Portátil de 8 GB | E2B, con las demás apps cerradas |
| Portátil de 16 GB, sin tarjeta gráfica | E2B para ir rápido; E4B funciona pero va lento |
| PC gaming con tarjeta de 6–8 GB | E4B, entero en la tarjeta |
| Tarjeta de 12 GB o más | E4B va rápido; 12B pasa a ser una opción |

Si prefieres no elegir, GreenCube revisa tu PC y elige el adecuado por ti. Las velocidades de cada PC que probamos están en [¿Puede mi PC ejecutar IA?](https://blog.greencube.app/blog/can-my-pc-run-ai)

## FAQ

### ¿Cuáles son los requisitos mínimos para usar Gemma 4 en local?

El más pequeño, Gemma 4 E2B (un archivo de 2,6 GB), funcionó en un portátil con 8 GB de RAM y sin tarjeta gráfica, a entre 5 y 7 tokens por segundo en chats reales. Necesita un par de GB de memoria libre para arrancar.

### ¿Cuánta VRAM necesita Gemma 4 E4B?

E4B es un archivo de 4,2 GB. Cabe entero en una tarjeta de 6 GB, donde escribió de 35 a 38 tokens por segundo en una GTX 1660 Super. En tarjetas de 8 GB fue de 56 a 72. También funciona sin tarjeta con 16 GB de RAM, a unos 8 tokens por segundo.

### ¿Gemma 4 12B funciona en una tarjeta gráfica de 8 GB?

Para una pregunta corta, sí: de 20 a 35 tokens por segundo en una RX 5700 XT. Pero se cayó en cuanto la conversación se alargó, porque a la tarjeta casi no le quedaba sitio. Para él querríamos al menos 10 GB de VRAM.

### ¿Gemma 4 es gratis?

Sí. Google publicó Gemma 4, incluidos E2B y E4B, con licencia Apache 2.0, que permite el uso comercial.
