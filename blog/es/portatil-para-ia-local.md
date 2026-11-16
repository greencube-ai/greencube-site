# Mejor portátil para IA local (Black Friday 2026)

> Qué portátil comprar para usar IA sin internet: cuánta RAM hace falta, velocidades medidas en portátiles reales y precios de noviembre de 2026.

Canonical: https://blog.greencube.app/blog/es/portatil-para-ia-local  
Published: 2026-11-16  
Author: Hector Gras

Para usar IA en un portátil sin tarjeta gráfica, lo que más cuenta es la RAM: con 8 GB funciona pero va justo, y con 16 GB vas cómodo. En nuestro portátil de 16 GB, Cube 2B (Gemma 4 E2B) escribía 14–18 tokens por segundo, más rápido de lo que lees; en el de 8 GB, 5–7. Una tarjeta NVIDIA lo hace todo mucho más rápido, pero para chatear y estudiar no necesitas un portátil caro.

Todas las velocidades de este artículo son nuestras: las medimos en portátiles reales mientras construíamos GreenCube, la app que hago, que pone la IA a funcionar dentro de tu propio ordenador. Solo hemos medido dos portátiles, los dos sin tarjeta gráfica, y lo que no hemos probado te lo digo. Tampoco te voy a prometer descuentos de Black Friday: este año la memoria está cara y los portátiles lo notan.

## Lo corto

- **Vas a chatear, estudiar, resumir apuntes:** un portátil con 16 GB de RAM, sin tarjeta gráfica. Es lo que mejor relación tiene entre lo que pagas y lo que notas.
- **Presupuesto muy justo:** 8 GB funciona, despacio y sin imágenes. Si puedes estirarte a 16 GB, hazlo antes que pagar por un procesador mejor.
- **Quieres que vuele y hacer imágenes:** un portátil con tarjeta NVIDIA de 6 u 8 GB de VRAM. No lo hemos medido en portátil, pero en sobremesa la tarjeta cambia el juego.
- **Tienes Mac o quieres uno:** GreenCube hoy es solo para Windows.

## Los portátiles que hemos medido

"Escribe" es lo rápido que la IA teclea su respuesta, en tokens por segundo. Una persona lee unos 5 tokens por segundo, así que todo lo que pase de ahí ya va más rápido que tus ojos. Medimos entre septiembre y octubre de 2026.

| Portátil | Modelo | Escribe (tokens/s) | Una respuesta larga | Una imagen |
| --- | --- | --- | --- | --- |
| [Intel Core Ultra 5 125U, 16 GB](https://blog.greencube.app/blog/es/ia-en-portatil-intel-core-ultra-5) | Cube 2B (Gemma 4 E2B) | **14–18** | unos 19 s | 2–2,5 min |
| [Intel Core Ultra 5 125U, 16 GB](https://blog.greencube.app/blog/es/ia-en-portatil-intel-core-ultra-5) | Cube 4B (Gemma 4 E4B) | **8–10** | unos 64 s | 2–2,5 min |
| [Intel con gráficos Iris Xe, 8 GB](https://blog.greencube.app/blog/es/ia-en-portatil-intel-iris-xe) | Cube 2B (Gemma 4 E2B) | **5–7** | 30–40 s | no puede |

Ninguno de los dos tiene tarjeta gráfica, solo los gráficos que vienen dentro del chip. La "respuesta larga" del portátil de 16 GB es una explicación de 277 tokens, cronometrada dentro de la propia app. Pulsa un portátil para ver su prueba completa.

### Cube 2B o Cube 4B en un portátil sin tarjeta

En el portátil de 16 GB caben los dos modelos. Cube 4B es más listo, pero escribe a la mitad de velocidad: una respuesta larga pasa de unos 19 segundos a algo más de un minuto. Para estudiar, la mayoría de la gente prefiere la rapidez de Cube 2B; para un texto que quieres bien pensado, compensa esperar. GreenCube elige el modelo según lo que quepa en tu PC, y tú puedes cambiarlo ([las diferencias entre los dos](https://blog.greencube.app/blog/es/gemma-4-e2b-vs-e4b)).

## Cuánta RAM necesitas

En un portátil sin tarjeta gráfica, la IA vive en la RAM, la misma memoria que usan Windows, el navegador y todo lo demás que tengas abierto. Si no cabe, no arranca. Esto es lo que llegó a ocupar cada cosa en el portátil de 16 GB, con los ajustes de GreenCube:

| Qué | Memoria que usa |
| --- | --- |
| Cube 2B (Gemma 4 E2B), chateando | **3,3 GB** |
| Cube 4B (Gemma 4 E4B), chateando | **5,1 GB** |
| Crear una imagen | **unos 7 GB** (el chat suelta su memoria mientras tanto) |

### 8 GB: funciona, pero va justo

Con el navegador y otras apps abiertas, a nuestro portátil de 8 GB le quedaba alrededor de 1 GB libre. Un día no bastó y la IA ni siquiera pudo arrancar. Cerrando cosas sí funciona, a 5–7 tokens por segundo en chats reales, más o menos a ritmo de lectura. Lo que no puede es crear imágenes: necesitan unos 7 GB para ellas solas ([la prueba del portátil de 8 GB](https://blog.greencube.app/blog/es/ia-con-8gb-de-ram)).

### 16 GB: cómodo

Con 16 GB caben los dos modelos con el navegador abierto, y hasta las imágenes, a unos 2 minutos y medio cada una. Es la cantidad que yo pediría a cualquier portátil que vaya a usar IA sin tarjeta gráfica.

Un aviso honesto: nuestro portátil de 16 GB escribía unas 2,5 veces más rápido que el de 8 GB, pero no todo es mérito de la RAM. El de 8 GB también tenía un procesador más flojo, de 8 hilos contra 14. Lo que sí es de la RAM es que todo quepa sin pelearse con lo demás.

### 32 GB: no hace falta para esto

Los modelos que usa GreenCube caben de sobra en 16 GB. Más RAM solo te sirve si quieres probar modelos más grandes, y aun así un portátil sin tarjeta los movería despacio. No hemos medido ningún portátil de 32 GB.

### Mira si la RAM se puede ampliar

En muchos portátiles finos la memoria va soldada a la placa y no se puede ampliar nunca. Si compras uno de 8 GB pensando en subirlo a 16 más adelante, comprueba en la ficha que la RAM sea ampliable. Si va soldada, lo que compres es lo que tendrás.

## El procesador y la NPU

Al escribir, lo que frena a un portátil sin tarjeta es lo rápido que puede mover la IA por su memoria, y el procesador y los gráficos integrados comparten esa misma memoria. Por eso, en nuestro portátil de 16 GB, escribir con los gráficos Intel fue más o menos igual de rápido que con el procesador. Donde los gráficos sí ayudaron fue al leer textos largos, 1,3 veces más rápido, y sobre todo en las imágenes: de 11 minutos y medio con el procesador a unos 2 y medio ([la prueba de los gráficos integrados](https://blog.greencube.app/blog/es/ia-portatil-sin-tarjeta-grafica)).

Muchos portátiles se venden ahora como "portátiles con IA" por llevar una NPU, un chip dedicado a eso. Nuestro Core Ultra 5 tiene una, y todas las pruebas de arriba corrieron en el procesador y los gráficos, no en ella. No hemos medido qué aporta la NPU, así que yo no pagaría más por esa etiqueta pensando en GreenCube.

Una buena noticia si estudias fuera de casa: en el portátil de 16 GB, con batería y enchufado la velocidad del chat fue más o menos la misma.

## Portátiles con tarjeta NVIDIA

No hemos medido ningún portátil con tarjeta gráfica. Lo que sí he medido son sobremesas, y ahí la diferencia es enorme: en el mismo PC y con la misma IA, una RTX 3060 escribía unas 7,5 veces más rápido que el procesador, y una RX 5700 XT, 14 veces más. Las imágenes bajaron de unos 2 minutos y medio en el portátil a 28 segundos en la RTX 3060. Si quieres verlas todas, están en [la guía de tarjetas gráficas](https://blog.greencube.app/blog/es/tarjeta-grafica-para-ia-local).

Si vas a por un portátil con tarjeta, fíjate en la VRAM, la memoria propia de la tarjeta. Cube 4B ocupa 4,2 GB y necesita unos 6 GB de VRAM para ir entero en la tarjeta con margen para la conversación. En las fichas, una RTX 4050 de portátil suele traer 6 GB y una RTX 5050 o 5060, 8 GB. Una RTX 3050 de portátil puede venir con 4 GB, y ahí no cabría entera.

No copies tal cual los números de sobremesa: la misma tarjeta en un portátil funciona con menos vatios y suele ir algo por debajo. Aun así, cualquier tarjeta en la que quepa el modelo debería ir varias veces más rápida que un portátil sin ella. Eso es lo que espero; no lo he medido.

## Por presupuesto

Precios vistos el 16 de noviembre de 2026 en PcComponentes y MediaMarkt, portátiles nuevos con Windows salvo que diga otra cosa. La subida de la memoria por la demanda de la IA está encareciendo los portátiles ([Xataka](https://www.xataka.com/seleccion/crisis-precios-ram-ha-encarecido-portatiles-ahora-puedes-llevarte-este-lenovo-a-minimo-historico)), y los precios cambian casi a diario, así que tómalos como una idea.

### Menos de 600 €

Los de 8 GB estaban sobre todo entre 380 y 500 €. Los de 16 GB empezaban en unos 530 €, con procesadores Intel o AMD de gama media, y había reacondicionados de 16 GB desde unos 360 €.

Mi consejo aquí es claro: si puedes, ve a por 16 GB aunque el procesador sea más modesto. Te da margen para tener el navegador abierto mientras estudias y te deja crear imágenes. Ojo con los Chromebook y los portátiles sin Windows que salen en estos precios: GreenCube no funciona en ellos.

### De 600 a 900 €

Aquí había muchos portátiles de 16 GB con Intel Core Ultra, Core 5 o 7 y AMD Ryzen 5 o 7, entre 620 y 800 €. No los hemos medido uno a uno, pero son de la misma clase que nuestro portátil de 16 GB, y para chatear y estudiar no necesitas más.

Al final del rango aparecían los primeros portátiles con tarjeta NVIDIA: con RTX 3050, RTX 4050 o RTX 5050, por unos 870–900 €. Sin medir. Si vas a por uno, mira la VRAM en la ficha antes que nada.

### Más de 900 €

Los portátiles con RTX 5050 de 16 GB estaban entre unos 930 y 1.250 €, y los de RTX 5060, entre unos 1.000 y 1.300 €. Ninguno medido. Por VRAM, en los dos cabe Cube 4B entero con margen.

Para la IA de GreenCube, gastar más que eso no hace que el chat vaya mejor. Tiene sentido si además juegas, editas vídeo o quieres modelos más grandes, pero ese es otro uso y otro presupuesto.

## ¿Y un Mac?

GreenCube hoy funciona solo en Windows 10 y 11, así que no te lo puedo recomendar para un Mac. Hay otras apps de IA sin internet para Mac, y las repaso en [IA sin internet en Mac](https://blog.greencube.app/blog/es/ia-sin-internet-mac). Tampoco hemos medido portátiles Windows con chip Snapdragon (ARM), así que si te interesa uno, no puedo decirte cómo irá.

## Si ya tienes portátil, mira primero si te basta

Antes de comprar nada, mira lo que tienes. Pulsa Ctrl + Mayús + Esc, entra en Rendimiento y luego en Memoria: el número de arriba a la derecha es tu RAM. En GPU verás si tienes tarjeta aparte; si solo aparecen gráficos Intel o AMD sin memoria dedicada, no la tienes. Con eso, en [¿Puedo usar IA en mi PC?](https://blog.greencube.app/blog/es/ia-en-mi-pc#checker) puedes ver lo que medimos en 10 PCs.

Si tu portátil tiene 16 GB, lo más probable es que ya te sirva para estudiar con IA. Si tiene 8 GB, también funciona, cerrando el navegador antes. El disco casi no importa: Cube 4B ocupa 4,2 GB.

GreenCube hace una prueba de velocidad al arrancar para decidir si usa el procesador, los gráficos o la tarjeta, y elige Cube 2B o Cube 4B según lo que quepa en tu portátil. Cuesta 9,99 € una vez y, después de instalarla, funciona sin internet. Si con lo que tienes se te queda corto, sabrás exactamente qué te falta antes de gastar dinero.

## FAQ

### ¿Cuánta RAM necesito para usar IA en un portátil?

Si el portátil no tiene tarjeta gráfica, 16 GB para ir cómodo. Con GreenCube, Cube 2B (Gemma 4 E2B) llegó a usar 3,3 GB y Cube 4B (Gemma 4 E4B), 5,1 GB, además de lo que gastan Windows y el navegador. Con 8 GB funciona, pero va justo: a nuestro portátil de 8 GB le quedaba alrededor de 1 GB libre con otras apps abiertas.

### ¿Sirve un portátil de 8 GB para usar IA sin internet?

Para chatear y estudiar, sí, despacio. En nuestro portátil de 8 GB con gráficos Intel Iris Xe, Cube 2B escribía 5–7 tokens por segundo en chats reales y una respuesta tardaba de 30 a 40 segundos. No puede crear imágenes y conviene cerrar el navegador antes.

### ¿Merece la pena un portátil con tarjeta NVIDIA para IA?

Si quieres velocidad e imágenes, sí. No hemos medido ningún portátil con tarjeta, pero en sobremesas la misma IA fue de 7,5 a 14 veces más rápida en la tarjeta que en el procesador. Para chatear y estudiar no hace falta: un portátil de 16 GB sin tarjeta ya escribe más rápido de lo que lees.

### ¿Qué portátil necesito para estudiar con IA?

Uno con Windows y 16 GB de RAM, aunque no tenga tarjeta gráfica. En el nuestro, con un Intel Core Ultra 5 125U, Cube 2B escribía 14–18 tokens por segundo y terminaba una respuesta larga en unos 19 segundos. En las tiendas vimos portátiles nuevos así desde unos 530 €.
