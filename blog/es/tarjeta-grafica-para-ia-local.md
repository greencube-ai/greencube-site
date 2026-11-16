# Mejor tarjeta gráfica para IA local (Black Friday 2026)

> Qué gráfica comprar para usar IA en tu PC: cuánta VRAM hace falta, velocidades que medimos en 8 tarjetas y precios vistos en noviembre de 2026.

Canonical: https://blog.greencube.app/blog/es/tarjeta-grafica-para-ia-local  
Published: 2026-11-16  
Author: Hector Gras

Para usar IA en tu PC, lo primero que decide la tarjeta es qué modelo cabe, y eso lo marca la VRAM: con 8 GB vas bien para los modelos que funcionan cómodos en local. De las tarjetas que hemos medido y que todavía se venden nuevas, la RTX 3060 de 12 GB y la RTX 5060 de 8 GB escribían entre 53 y 56 tokens por segundo, más de diez veces lo que lees. Pero si solo quieres chatear y estudiar, puede que no necesites comprar nada.

Todas las velocidades de este artículo son nuestras: las medimos en PCs reales mientras construíamos GreenCube, la app que hago, que pone la IA a funcionar dentro de tu propio ordenador. Si una tarjeta no la hemos medido, lo digo. Y aviso desde ya: este año las gráficas están caras, así que no des por hecho que el Black Friday las vaya a dejar baratas.

## Lo corto

- **Solo vas a chatear, estudiar o resumir:** no compres una gráfica todavía. Un portátil de 16 GB sin tarjeta escribía 14–18 tokens por segundo ([la prueba del portátil](https://blog.greencube.app/blog/es/ia-portatil-sin-tarjeta-grafica)).
- **Quieres que vuele y hacer imágenes:** una tarjeta de 8 GB o más. La RTX 3060 de 12 GB es la que más nos convence de lo medido que aún se vende nueva.
- **Presupuesto corto:** segunda mano. Una RX 6600 o una GTX 1660 Super escribían 42–44 y 37–38. Ojo con la RX 580: tiene 8 GB pero se quedó en 10–11.
- **Quieres probar modelos más grandes:** ahí sí pagan los 12 o 16 GB.

## Cuánta VRAM hace falta

La VRAM es la memoria propia de la tarjeta gráfica. Para que la IA vaya a toda velocidad, el modelo entero tiene que caber ahí, y además tiene que sobrar sitio para la conversación y para lo que Windows ya está usando. GreenCube deja libres unos 1,5 GB por eso, y no es por exagerar: en una GTX 1650 de 4 GB, un modelo metido a presión falló en el primer mensaje.

Cuando no cabe, el golpe es grande. En una RX 5700 XT de 8 GB, un modelo de 12.000 millones de parámetros escribía 35,6 tokens por segundo entero en la tarjeta y 5,9 con una parte fuera: 6 veces más lento ([la prueba completa de VRAM](https://blog.greencube.app/blog/es/cuanta-vram-para-ia)).

| Modelo | Lo que ocupa | VRAM que necesita |
| --- | --- | --- |
| Cube 2B (Gemma 4 E2B) | 2,6 GB | **unos 4 GB** |
| Cube 4B (Gemma 4 E4B) | 4,2 GB | **unos 6 GB** |
| Gemma 4 12B | 6,4 GB | **10 GB o más** en la práctica: en 8 GB se cayó en chats largos |

La columna de la derecha es el tamaño más ese margen de 1,5 GB. Traducido: una tarjeta de 6 GB ya mueve Cube 4B entero, una de 8 GB lo mueve con holgura, y más de 8 GB solo te cambia algo si vas a usar modelos más grandes.

## Las tarjetas que hemos medido

"Escribe" es lo rápido que la IA teclea su respuesta, en tokens por segundo. Una persona lee unos 5 tokens por segundo, así que todo lo que pase de ahí ya va más rápido que tus ojos. Medimos en septiembre y octubre de 2026, en chats reales y con la prueba de velocidad de la propia GreenCube. Cuando hay varias pruebas, damos el rango.

| Tarjeta | VRAM | Escribe (tokens/s) | Una imagen |
| --- | --- | --- | --- |
| [NVIDIA RTX 2080 Ti](https://blog.greencube.app/blog/es/ia-en-rtx-2080-ti) | 11 GB | **65–71** | 8–9 s |
| [AMD RX 5700 XT](https://blog.greencube.app/blog/es/ia-en-rx-5700-xt) | 8 GB | **63–72** | sin medir |
| [NVIDIA RTX 5060](https://blog.greencube.app/blog/es/ia-en-rtx-5060) | 8 GB | **56** | sin medir |
| [NVIDIA RTX 3060](https://blog.greencube.app/blog/es/ia-en-rtx-3060) | 12 GB | **53–55** | 28 s |
| [AMD RX 6600](https://blog.greencube.app/blog/es/ia-en-rx-6600) | 8 GB | **42–44** | 59 s |
| [NVIDIA GTX 1660 Super](https://blog.greencube.app/blog/es/ia-en-gtx-1660-super) | 6 GB | **37–38** | 89 s |
| [NVIDIA GTX 1650](https://blog.greencube.app/blog/es/ia-en-gtx-1650) | 4 GB | **unos 20** | sin medir |
| [AMD RX 580](https://blog.greencube.app/blog/es/ia-en-rx-580) | 8 GB | **10–11** | sin medir |
| *[Portátil sin tarjeta, 16 GB](https://blog.greencube.app/blog/es/ia-en-portatil-intel-core-ultra-5) (Cube 2B)* | – | **14–18** | unos 2 min y medio |

Todas las tarjetas, con Cube 4B (Gemma 4 E4B); el portátil, con el modelo más pequeño, Cube 2B. Las imágenes son de 512 por 512 con el motor de imágenes de GreenCube. Pulsa una tarjeta para ver su prueba completa.

### VRAM no es lo mismo que velocidad

La RX 580 y la RX 5700 XT tienen los mismos 8 GB, y una escribía 10–11 tokens por segundo y la otra 63–72. La VRAM decide qué cabe; lo rápido que va depende de la propia tarjeta. Al escribir pesa mucho lo rápido que la tarjeta mueve datos por su memoria (el ancho de banda, que sale en la ficha en GB/s), pero no es una regla exacta: la RX 6600 tiene menos ancho de banda que la GTX 1660 Super y escribió más rápido. Por eso preferimos medir a adivinar.

### Cualquier tarjeta decente se nota muchísimo

En el mismo PC y con la misma IA, la RX 5700 XT escribía 14 veces más rápido que el procesador (72,5 contra 5,0), y la RTX 3060, unas 7,5 veces. Hasta la GTX 1650, en la que Cube 4B no cabe entero y una parte se queda en la RAM, escribía unos 20.

### Las que no hemos medido

No hemos probado ni la RTX 5060 Ti, ni la RTX 5070, ni la RTX 5050, ni la RTX 4060, ni la RX 9060 XT, ni la RX 7600, ni ninguna Intel Arc. No te voy a dar números inventados para ellas. Lo que sí puedo decirte es la cuenta de la VRAM: todas las que tienen 8 GB o más mueven Cube 4B entero con margen.

## Por presupuesto

Precios vistos en PcComponentes el 16 de noviembre de 2026, tarjetas nuevas. Este año las gráficas han subido mucho por la escasez de chips de memoria ([Geektopia](https://www.geektopia.es/es/technology/2026/08/11/noticias/las-tarjetas-graficas-suben-fuerte-de-precio-en-agosto-por-la-crisis-de-chips-de-memoria.html)), y cambian casi cada día, así que tómalos como una idea, no como una promesa.

### Menos de 200 €

Nuevo no vimos nada que valga para esto: por debajo de 200 € había tarjetas para conectar una pantalla, como una GT 730, o una GTX 1050 Ti de 4 GB a unos 186 €, más antigua que la GTX 1650 y que no hemos medido.

Aquí tienes dos caminos. Uno es la segunda mano: una RX 6600 (8 GB, 42–44 tokens por segundo) o una GTX 1660 Super (6 GB, 37–38). Busca una con factura o garantía. El otro es no comprar nada: si tienes 16 GB de RAM, tu PC ya chatea sin tarjeta.

### De 200 a 400 €

Lo nuevo de este rango eran sobre todo RTX 3050 de 6 GB (unos 300–350 €) y la Intel Arc B570 de 10 GB (unos 355 €). No las hemos medido. Por VRAM, en las dos cabe Cube 4B entero, pero no sé a qué velocidad.

Si te quieres ir a algo medido, mira la segunda mano: una RTX 3060 de 12 GB usada que entre en este presupuesto es lo que yo buscaría.

### Más de 400 €

- **RTX 3060 de 12 GB, unos 510–540 €.** Escribía 53–55 tokens por segundo y hacía una imagen en 28 segundos. Es una tarjeta de 2021, y que cueste esto dice mucho de cómo está el mercado, pero sus 12 GB te dejan sitio para el día de mañana.
- **RTX 5060 de 8 GB, desde unos 600 €**; solo vimos cuatro anuncios, casi todos de otros vendedores. Escribía 56 tokens por segundo, al nivel de la 3060. A estos precios, para IA no le veo ventaja sobre ella.
- **RTX 5060 Ti** (8 GB, unos 575–650 €; 16 GB, unos 860–950 €), **RX 9060 XT** (8 GB, unos 550–580 €; 16 GB, unos 730–800 €) y **RX 7600** (8 GB, unos 440–520 €). Sin medir.

Una cosa importante: para la IA que usa GreenCube, pagar casi el doble por 16 GB no hace que el chat vaya el doble de rápido. Cube 4B ya cabe en 8 GB con margen. Los 16 GB son para quien quiera modelos más grandes, y eso es otro presupuesto y otro uso.

## AMD o NVIDIA para IA local

Para chatear con GreenCube, las dos valen. GreenCube usa Vulkan, que funciona con tarjetas AMD y NVIDIA, y en nuestras pruebas la marca no decidió nada: la RX 5700 XT (63–72) estuvo al nivel de la RTX 2080 Ti (65–71), y la RX 6600 (42–44) por encima de la GTX 1660 Super (37–38). La más lenta de todas fue una AMD, la RX 580, pero es una tarjeta de 2017.

La diferencia está fuera de GreenCube. Muchas herramientas de IA, sobre todo las de generar imágenes y las que se instalan con Python, están hechas primero para CUDA, que es solo de NVIDIA. Con una AMD suelen funcionar, pero con más pasos o con menos opciones. Si piensas trastear con ese tipo de herramientas, NVIDIA te lo pone más fácil. Si solo vas a usar una app como GreenCube, compra la que te salga mejor de precio.

Las Intel Arc no las hemos probado, así que de ellas no te puedo decir nada medido.

## Si ya tienes PC, mira primero si te basta

Antes de gastarte 500 € en una gráfica, mira lo que tienes. Pulsa Ctrl + Mayús + Esc, entra en Rendimiento y luego en GPU: ahí ves el nombre de tu tarjeta y su Memoria de GPU dedicada, que es tu VRAM. Con eso, en [¿Puedo usar IA en mi PC?](https://blog.greencube.app/blog/es/ia-en-mi-pc#checker) puedes buscar tu tarjeta y ver lo que medimos.

Lo más probable es que te baste. Una tarjeta de 6 GB de hace unos años ya escribe varias veces más rápido de lo que lees, y sin tarjeta un PC de 16 GB va de sobra para estudiar y escribir. Las imágenes son lo único donde una tarjeta potente cambia de verdad la experiencia: de unos 2 minutos y medio en un portátil a menos de 30 segundos en una RTX 3060 ([cuánto tarda una imagen](https://blog.greencube.app/blog/es/generar-imagenes-ia-local)).

GreenCube funciona con tarjeta y sin ella. Al arrancar hace una prueba de velocidad para decidir si usa la tarjeta o el procesador, y elige Cube 2B o Cube 4B según lo que quepa en tu PC. Cuesta 9,99 € una vez y, después de instalarla, funciona sin internet. Si con lo que tienes se te queda corto, entonces sabrás qué te falta y podrás comprar con datos, no a ciegas.

## FAQ

### ¿Cuál es la mejor tarjeta gráfica barata para IA?

De las que hemos medido, una RX 6600 o una GTX 1660 Super de segunda mano: con Cube 4B (Gemma 4 E4B) escribían 42–44 y 37–38 tokens por segundo, mucho más rápido de lo que lees. Las tarjetas nuevas de menos de 400 € que vimos en tienda no las hemos medido todavía.

### ¿Cuánta VRAM necesito para IA en local?

El tamaño del modelo más unos 1,5 GB para la conversación y Windows. Cube 4B ocupa 4,2 GB, así que cabe en una tarjeta de 6 GB, y con 8 GB va holgado. Un modelo de 12.000 millones de parámetros cupo en 8 GB para una pregunta corta y se cayó en cuanto el chat se alargó.

### ¿Sirve una tarjeta gráfica AMD para IA?

Para chatear con GreenCube, sí: usa Vulkan, que funciona con AMD y con NVIDIA. Una RX 5700 XT escribía 63–72 tokens por segundo, al nivel de una RTX 2080 Ti. Fuera de GreenCube, muchas herramientas de IA están pensadas primero para NVIDIA y en AMD piden más configuración.

### ¿Necesito una tarjeta gráfica para usar IA en mi PC?

No. Un portátil de 16 GB sin tarjeta gráfica escribía 14–18 tokens por segundo con Cube 2B (Gemma 4 E2B), más rápido de lo que lees. La tarjeta se nota sobre todo en la velocidad y en las imágenes.
