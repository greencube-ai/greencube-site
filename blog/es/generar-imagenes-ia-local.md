# Generar imágenes con IA en local: cuánto tarda en tu PC

> Cronometramos cómo generar imágenes con IA en local en una tarjeta de 12 GB, un portátil con gráficos Intel y el procesador de un portátil: de 28 segundos a 11 minutos.

Canonical: https://blog.greencube.app/blog/es/generar-imagenes-ia-local  
Published: 2026-10-18  
Author: Hector Gras

En un PC con una tarjeta gráfica decente, alrededor de medio minuto por imagen. En un portátil normal de 16 GB, de 2 a 3 minutos. En un portátil de 8 GB no funciona, porque la IA de imágenes necesita más memoria de la que el portátil puede dejarle libre.

Cronometramos la misma imagen en tres tipos de PC, y la diferencia es mayor de lo que casi todo el mundo espera: de 28 segundos a más de 11 minutos.

## La prueba

Usamos la misma IA de imágenes en todos los PCs (Z-Image Turbo, dentro de GreenCube) e hicimos una imagen de 512 por 512 con 8 pasos. Medimos desde que se pulsa el botón hasta la imagen terminada, en septiembre y octubre de 2026.

| PC | Quién hizo el trabajo | Tiempo por imagen |
| --- | --- | --- |
| Sobremesa, tarjeta de 12 GB, 32 GB de RAM | Tarjeta gráfica | **28 s** |
| Portátil, Core Ultra 5, 16 GB | Gráficos Intel integrados | **2 min 22 s – 2 min 38 s** |
| El mismo portátil | Solo el procesador | **11 min 27 s** |
| Portátil, 8 GB | No hay memoria para arrancar | **No puede** |

## Cualquier gráfica ayuda mucho

La sorpresa fue el portátil. Hasta el pequeño chip gráfico que lleva integrado el procesador hizo las imágenes unas 4 veces más rápido que el procesador solo. Hacer una imagen son muchas cuentas pesadas y repetitivas, y justo para eso están hechos los chips gráficos.

Una tarjeta gráfica de verdad es otras 5 veces más rápida además de eso. Si quieres hacer muchas imágenes, la tarjeta gráfica es la pieza del PC que importa.

## Por qué 8 GB no bastan

La IA de imágenes le pide a Windows unos 7 GB mientras trabaja, y un portátil de 8 GB no puede liberar tanto. Por eso GreenCube solo hace imágenes en PCs con al menos 12 GB de RAM, y comprueba que hay sitio antes de empezar en vez de bloquearse a mitad. Chatear y estudiar siguen funcionando con 8 GB, solo que despacio ([nuestra prueba con 8 GB](https://blog.greencube.app/blog/run-ai-on-8gb-ram)).

## ¿Lo frenan otras apps?

No mucho, en nuestra prueba. En el portátil de 16 GB hicimos la misma imagen con un editor de código y un navegador abiertos, y otra vez con 4 GB de memoria ocupados a propósito. Siguió tardando unos 2 minutos cada vez, porque Windows aparta los programas que no se están usando para hacer sitio.

## Qué esperar en tu PC

Con tarjeta gráfica, una imagen tarda menos de un minuto, así que puedes hacer varias y quedarte con la mejor. En un portátil de 16 GB sin tarjeta, 2 o 3 minutos están bien para unas pocas imágenes: lanza una y ponte con otra cosa mientras trabaja.

Nada cuenta cuántas imágenes haces, así que el único límite es cuánto estás dispuesto a esperar. Para ver lo que puede hacer tu tarjeta, prueba [¿Puedo usar IA en mi PC?](https://blog.greencube.app/blog/can-my-pc-run-ai#checker) Las velocidades de chat de este mismo portátil están en [IA en un portátil sin tarjeta gráfica](https://blog.greencube.app/blog/ai-on-laptop-without-gpu).

## FAQ

### ¿Cuánto tarda en crear una imagen con IA mi PC?

En nuestras pruebas, una imagen de 512 por 512 tardó 28 segundos en un sobremesa con una tarjeta de 12 GB, unos 2 minutos y medio en un portátil de 16 GB con sus gráficos Intel, y unos 11 minutos y medio en el procesador de ese mismo portátil.

### ¿Puedo crear imágenes con IA en un portátil sin tarjeta gráfica?

Sí, si tiene 16 GB de RAM. Los gráficos Intel integrados lo hicieron unas 4 veces más rápido que el procesador solo. Con 8 GB de RAM no funciona: la IA de imágenes necesita unos 7 GB ella sola.

### ¿Tengo que cerrar otras apps para crear imágenes con IA?

En un portátil de 16 GB, no. Con un editor de código y un navegador abiertos, la imagen tardó lo mismo. Lo que importa es que Windows pueda reservarle unos 7 GB.
