# IA sin internet en Windows 10 y 11: qué necesita tu PC (medido en 10 PCs)

> Cómo instalar una IA local en tu PC con Windows 10 u 11 y usarla sin internet: la RAM y la tarjeta gráfica que necesitas, velocidades reales en 10 PCs con Windows, las apps que funcionan sin conexión y cómo comprobar que nada sale de tu PC.

Canonical: https://blog.greencube.app/blog/es/ia-sin-internet-windows  
Published: 2026-10-23  
Author: Hector Gras

**Respuesta corta:** cualquier PC con Windows 10 u 11 y **8 GB de RAM** puede ejecutar una IA local sin internet, y con **16 GB o una tarjeta gráfica gaming** va cómodo. Descargas la app y el modelo una vez; después funciona con el wifi apagado. Lo medimos en 10 PCs reales con Windows: desde más o menos la velocidad a la que lees en un portátil de 8 GB hasta muchas veces más rápido en un PC gaming.

- **10** PCs reales con Windows medidos, portátiles y sobremesas gaming
- **8 GB** de RAM bastan para empezar, sin tarjeta gráfica
- **0** internet necesario tras la primera descarga

## Qué necesita tu PC con Windows

|  | Mínimo | Cómodo |
| --- | --- | --- |
| **Windows** | Windows 10 (64 bits) | Windows 11 |
| **RAM** | 8 GB, con las demás apps cerradas | 16 GB o más |
| **Tarjeta gráfica** | No hace falta | Cualquiera de 6 GB o más de los últimos años |
| **Espacio en disco** | Unos 3 GB para un modelo pequeño | Unos 11 GB para un modelo mayor más imágenes |
| **Internet** | Una vez, para descargar la app y el modelo |  |

¿No sabes qué tiene tu PC? Pulsa **Ctrl + Shift + Esc**, abre **Rendimiento** y mira **Memoria** y **GPU**. O escribe tu tarjeta en [nuestro comprobador](https://blog.greencube.app/blog/es/ia-en-mi-pc#checker): te dice qué funciona y cómo de rápido fue en un PC real como el tuyo.

## Cómo de rápido va en PCs reales con Windows

Todos los números salen de GreenCube funcionando en PCs reales con Windows en septiembre y octubre de 2026, sobre todo en chats reales. Un token es un trozo de palabra; en español, la mayoría de la gente lee unos 8 por segundo.

| Tu PC con Windows | Escribe | Una imagen (512×512) |
| --- | --- | --- |
| Portátil de 8 GB, sin tarjeta gráfica | **5–7** tokens/s, más o menos a la velocidad a la que lees | no puede (necesita unos 7 GB libres) |
| Portátil de 16 GB, sin tarjeta gráfica | **14–18** tokens/s | **2–2,5 min** |
| PC gaming con tarjeta de 6 GB o más | **37–76** tokens/s en la mayoría de tarjetas | **8–89 s** |

La excepción: una AMD RX 580 antigua escribía unos 11 tokens por segundo, aun así más rápido de lo que lees. Cada tarjeta, con su propia página, está en [¿Puede mi PC ejecutar IA?](https://blog.greencube.app/blog/es/ia-en-mi-pc)

### El trabajo pesado lo hace la tarjeta gráfica

En el mismo sobremesa con Windows, la misma IA escribía **5 tokens por segundo con el procesador y 72 con una RX 5700 XT**. Ejecutar una IA es sobre todo el tipo de cálculo para el que está hecha una tarjeta gráfica, así que cualquier tarjeta gaming reciente marca una gran diferencia. Lo que decide qué tamaño de IA cabe es la memoria propia de la tarjeta (VRAM), no tu RAM: [por qué el modelo tiene que caber en la tarjeta](https://blog.greencube.app/blog/es/cuanta-vram-para-ia).

### ¿Sin tarjeta gráfica? Sirve para estudiar y chatear

Un portátil normal de 16 GB con solo gráficos Intel terminó una respuesta completa de estudio, una explicación más tres preguntas de examen, en unos 20 segundos. En un portátil de 8 GB también funciona, más lento, siempre que las demás apps dejen algo de memoria libre: [nuestra prueba con 8 GB](https://blog.greencube.app/blog/es/ia-con-8gb-de-ram).

## Apps que ejecutan IA sin internet en Windows

Según la web de cada app, comprobado el 21 de octubre de 2026. No hemos medido las demás apps en nuestros PCs, así que esta tabla no compara velocidad.

| App | Windows | Precio | ¿Elige el modelo por ti? | Lee tus PDF |
| --- | --- | --- | --- | --- |
| **GreenCube** | Windows 10 y 11 | 9,99 € una vez | Sí, según tu tarjeta y tu RAM | Sí |
| **LM Studio** | Necesita un procesador con AVX2 | Gratis | No, eliges de una lista | Sí |
| **Jan** | Windows 10 o posterior | Gratis, código abierto | No | Sí |
| **Ollama** | Windows; ventana de chat desde julio de 2025 | Gratis en tu PC | No | Sí |
| **GPT4All** | Windows (no PCs ARM) | Gratis, código abierto | No | Sí, con LocalDocs |
| **AnythingLLM** | Windows | Escritorio gratis | No | Sí |
| **Msty** | Windows 10 y 11 | Plan gratuito | No | Sí |
| **KoboldCpp** | Un solo .exe, chat en el navegador | Gratis, código abierto | No | Solo texto |

¿Quieres ver qué envía cada una a internet, y también apps para Mac y móvil? Mira [nuestra comparativa de 12 chatbots de IA sin internet](https://blog.greencube.app/blog/es/mejor-chatbot-ia-sin-internet).

## ¿Windows 10 o Windows 11?

La IA funciona igual en los dos: lo que importa es tu RAM y tu tarjeta gráfica, no la versión de Windows. Un detalle: Microsoft dejó de dar soporte a Windows 10 el 14 de octubre de 2025, así que un PC con Windows 10 ya no recibe parches de seguridad salvo que te apuntes a las actualizaciones extendidas. Una IA sin internet guarda tus chats en tu PC en cualquier caso, pero merece la pena tener Windows al día.

## Cómo comprobar que de verdad no sale nada

1. **Activa el modo avión** (o desconecta el cable) después de la primera descarga y chatea. Si responde, la IA está funcionando en tu PC.
2. **Vigila la red:** pulsa **Windows + R**, escribe **resmon** y abre la pestaña **Red**. "Procesos con actividad de red" muestra cada programa que envía o recibe datos mientras chateas.
3. **Lee qué dice la app que sale a internet.** En GreenCube: inicias sesión una vez para activarla, descarga la IA y sus actualizaciones, y la búsqueda online (que empieza apagada cada vez que abres la app) envía términos de búsqueda a buscadores. Nada más: "Nunca recibimos tus chats, archivos, recuerdos ni imágenes."

## Lo que una IA sin internet en Windows no puede hacer

- **Las noticias de hoy.** El modelo sabe lo que aprendió al entrenarse. Para lo actual necesitas buscar en la web, y esa parte sí sale a internet.
- **Ganar en todo a las IAs más grandes de la nube.** Los modelos que caben en un PC se defienden bien estudiando, escribiendo y con preguntas del día a día, pero los modelos más grandes de la nube siguen siendo mejores en los problemas más difíciles.
- **Ir rápido en cualquier PC.** El trabajo lo hace tu PC: un portátil de 8 GB va más o menos a la velocidad a la que lees; un PC gaming, mucho más rápido.

¿Es para estudiar? Mira [qué puede hacer una IA sin internet por un estudiante](https://blog.greencube.app/blog/es/ia-sin-internet-para-estudiantes), con tiempos para PDF, guías de estudio y flashcards.

## FAQ

### ¿Puedo usar IA sin internet en Windows 11?

Sí. Apps como GreenCube, LM Studio, Jan, Ollama y GPT4All ejecutan el modelo de IA en tu propio PC. Necesitas internet una vez para descargar la app y el modelo; después, el chat funciona con el wifi apagado.

### ¿Funciona la IA local en Windows 10?

Sí. GreenCube, Jan y Msty indican Windows 10 como compatible. Microsoft dejó de dar soporte a Windows 10 el 14 de octubre de 2025: la IA sigue funcionando, pero tu PC ya no recibe parches de seguridad salvo que te apuntes a las actualizaciones extendidas.

### ¿Cuánta RAM necesito para instalar una IA en mi PC?

Con 8 GB funciona con un modelo pequeño: nuestro portátil de 8 GB escribía de 5 a 7 tokens por segundo en chats reales, más o menos a la velocidad a la que lees. Con 16 GB va cómodo: nuestro portátil de 16 GB sin tarjeta gráfica escribía de 14 a 18.

### ¿Necesito tarjeta gráfica para tener IA local en el PC?

No, pero ayuda mucho. En PCs gaming con una tarjeta de 6 GB o más medimos de 37 a 76 tokens por segundo en la mayoría de tarjetas, varias veces más rápido que esos mismos PCs solo con el procesador. Para crear imágenes necesitas tarjeta gráfica o 16 GB de RAM.

### ¿Hay alguna IA sin internet gratis para Windows?

Sí: LM Studio, Jan, Ollama, GPT4All y AnythingLLM son gratis, y eliges y descargas tú el modelo. GreenCube cuesta 9,99 € una vez y elige por ti el modelo que encaja con tu PC.
