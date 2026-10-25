# Requisitos de Gemma 4: qué PC necesitas para usarlo en local

> Requisitos de Gemma 4 E2B, E4B y 12B, medidos en PCs reales: cuánta RAM y VRAM necesita cada uno y a qué velocidad va en portátiles y en tarjetas gráficas gaming.

Canonical: https://blog.greencube.app/blog/es/requisitos-gemma-4  
Published: 2026-10-18  
Author: Hector Gras

**Respuesta corta:** el pequeño **Gemma 4 E2B** funciona en un **portátil de 8 GB**. **E4B** quiere 16 GB de RAM, o vuela en cualquier **tarjeta gráfica de 6 GB o más**. **12B** necesita **10 GB de VRAM o más** para aguantar una conversación de verdad.

- **8 GB** de RAM bastan para Gemma 4 E2B, sin tarjeta gráfica
- **56–72** tokens por segundo de E4B en tarjetas gaming de 8 GB
- **10 GB** de VRAM antes de fiarnos de 12B en un chat largo

## Requisitos de Gemma 4 de un vistazo

| Modelo | Tamaño | Mínimo recomendado | Mejor en |
| --- | --- | --- | --- |
| **Gemma 4 E2B** | 2,6 GB | 8 GB de RAM, sin tarjeta | Portátiles |
| **Gemma 4 E4B** | 4,2 GB | 16 GB de RAM, o una tarjeta de 6 GB | PCs gaming, portátiles de 16 GB |
| **Gemma 4 12B** | 6,2 GB | 10 GB de VRAM o más | Tarjetas de 12 GB o más |

## Velocidades medidas

A qué velocidad escribe cada uno su respuesta, en tokens por segundo (un token es un trozo de palabra; a partir de unos 8 escribe más rápido de lo que lees). Medido con GreenCube en septiembre y octubre de 2026.

| PC | Modelo | Escribe (tokens/s) |
| --- | --- | --- |
| Sobremesa, AMD RX 5700 XT 8 GB | E4B | **63–72** |
| Sobremesa, NVIDIA RTX 5060 8 GB | E4B | **56** |
| Sobremesa, tarjeta de 12 GB | E4B | **50–55** |
| Sobremesa, NVIDIA GTX 1660 Super 6 GB | E4B | **35–38** |
| Sobremesa, AMD RX 5700 XT 8 GB | 12B | **20–35** (solo chats cortos) |
| Sobremesa, NVIDIA GTX 1650 4 GB | E4B | **unos 20** |
| Portátil, Intel Core Ultra 5, 16 GB | E2B | **14–18** |
| El mismo portátil | E4B | **8–10** |
| Portátil, Intel Iris Xe, 8 GB | E2B | **5–7** |

## Lo que aprendimos

### 1. E2B es el modelo para portátiles

En un portátil de 16 GB sin tarjeta gráfica terminó una respuesta completa de estudio en unos 20 segundos, donde E4B tardó 112. En cinco preguntas rápidas de datos no falló ninguna. [E2B contra E4B, medido.](https://blog.greencube.app/blog/es/gemma-4-e2b-vs-e4b)

### 2. E4B es el modelo para PCs gaming

Cuando el modelo entero está en una tarjeta gráfica, E4B va **de 7 a 9 veces más rápido** que en un portátil, y sus respuestas son mejores. Cualquier tarjeta de 6 GB o más lo consigue.

### 3. 12B necesita VRAM de verdad, no solo RAM

En una tarjeta de 8 GB, 12B contestó bien una pregunta corta y luego falló cada vez que el chat crecía. Ese PC tenía 48 GB de RAM y no le sirvieron. [Por qué el modelo tiene que caber en tu tarjeta.](https://blog.greencube.app/blog/es/cuanta-vram-para-ia)

## ¿Qué Gemma 4 para tu PC?

#### Portátil de 8 GB

E2B. Cierra otras apps antes.

#### Portátil de 16 GB sin tarjeta

E2B para ir rápido. E4B funciona pero va lento.

#### PC gaming, tarjeta de 6–8 GB

E4B, entero en la tarjeta.

#### Tarjeta de 12 GB o más

E4B va rápido; 12B pasa a ser una opción.

Google publica Gemma 4 con licencia Apache 2.0. GreenCube elige el adecuado para tu PC automáticamente. [Mira los 10 PCs que medimos.](https://blog.greencube.app/blog/es/ia-en-mi-pc)

## FAQ

### ¿Cuáles son los requisitos mínimos para usar Gemma 4 en local?

El más pequeño, Gemma 4 E2B (un archivo de 2,6 GB), funcionó en un portátil con 8 GB de RAM y sin tarjeta gráfica, a entre 5 y 7 tokens por segundo en chats reales. Necesita un par de GB de memoria libre para arrancar.

### ¿Cuánta VRAM necesita Gemma 4 E4B?

E4B es un archivo de 4,2 GB. Cabe entero en una tarjeta de 6 GB, donde escribió de 35 a 38 tokens por segundo en una GTX 1660 Super. En tarjetas de 8 GB fue de 56 a 72. También funciona sin tarjeta con 16 GB de RAM, a unos 8 tokens por segundo.

### ¿Gemma 4 12B funciona en una tarjeta gráfica de 8 GB?

Para una pregunta corta, sí: de 20 a 35 tokens por segundo en una RX 5700 XT. Pero se cayó en cuanto la conversación se alargó, porque a la tarjeta casi no le quedaba sitio. Para él querríamos al menos 10 GB de VRAM.

### ¿Gemma 4 es gratis?

Sí. Google publicó Gemma 4, incluidos E2B y E4B, con licencia Apache 2.0, que permite el uso comercial.
