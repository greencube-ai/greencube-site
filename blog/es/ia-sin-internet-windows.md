# IA sin internet en Windows 10 y 11: qué necesita tu PC (medido en 10 PCs)

> Cómo instalar una IA local en tu PC con Windows 10 u 11 y usarla sin internet: la RAM y la tarjeta gráfica que necesitas, velocidades reales en 10 PCs con Windows, las apps que funcionan sin conexión y cómo comprobar que nada sale de tu PC.

Canonical: https://blog.greencube.app/blog/es/ia-sin-internet-windows  
Published: 2026-10-23  
Author: Hector Gras

Cualquier PC con Windows 10 u 11 y 8 GB de RAM puede usar un chatbot de IA sin internet, y con 16 GB o una tarjeta gráfica gaming va cómodo. Descargas la app y el modelo de IA una vez, y a partir de ahí funciona con el wifi apagado. En los 10 PCs con Windows que medimos, fue desde más o menos tu ritmo de lectura en un portátil de 8 GB hasta muchas veces más rápido en un PC gaming.

Yo hago GreenCube, una de las apps de abajo, así que ten eso en cuenta al leer mi opinión. Todas las velocidades de aquí son de GreenCube, porque es con lo que hacemos las pruebas; las otras apps se comparan según lo que dicen sus propias webs.

## Qué necesita tu PC con Windows

|  | Mínimo | Cómodo |
| --- | --- | --- |
| Windows | Windows 10 (64 bits) | Windows 11 |
| RAM | 8 GB, con las demás apps cerradas | 16 GB o más |
| Tarjeta gráfica | No hace falta | Cualquier tarjeta de 6 GB o más de los últimos años |
| Espacio en disco | Unos 3 GB para un modelo pequeño | Unos 11 GB para un modelo más grande e imágenes |
| Internet | Una vez, para descargar la app y el modelo |  |

¿No sabes qué tiene tu PC? Pulsa **Ctrl + Mayús + Esc**, abre **Rendimiento** y mira **Memoria** y **GPU**. O escribe tu tarjeta gráfica en [nuestro comprobador](https://blog.greencube.app/blog/can-my-pc-run-ai#checker), que te dice qué funciona y a qué velocidad fue en un PC real como el tuyo.

## A qué velocidad va en PCs con Windows reales

Todos los números de abajo salen de GreenCube en un PC con Windows real, en septiembre y octubre de 2026, casi todos en chats reales. Un token es un trozo de palabra, y la mayoría de la gente lee en inglés unos 5 por segundo.

| Tu PC con Windows | Escribe | Una imagen (512 por 512) |
| --- | --- | --- |
| Portátil de 8 GB, sin tarjeta gráfica | **5–7** tokens/s, más o menos a tu ritmo de lectura | no puede (necesita unos 7 GB libres) |
| Portátil de 16 GB, sin tarjeta gráfica | **14–18** tokens/s | **2–2,5 min** |
| PC gaming con tarjeta de 6 GB o más | **37–76** tokens/s en casi todas las tarjetas | **8–89 s** |

La única excepción que encontramos fue una AMD RX 580 antigua, que escribía unos 11 tokens por segundo. Aun así es más rápido de lo que lees. Todas las tarjetas que probamos, cada una con su página, están en [¿Puedo usar IA en mi PC?](https://blog.greencube.app/blog/can-my-pc-run-ai)

### La tarjeta gráfica hace el trabajo pesado

En el mismo sobremesa con Windows, la misma IA escribía 5 tokens por segundo con el procesador y 72 con una RX 5700 XT. Ejecutar una IA es sobre todo el tipo de cálculo para el que está hecha una tarjeta gráfica, así que cualquier tarjeta gaming reciente marca una gran diferencia.

Lo que decide cuánto de grande puede ser la IA es la memoria propia de la tarjeta (VRAM), no tu RAM. Hay más sobre eso en [por qué el modelo tiene que caber en la tarjeta](https://blog.greencube.app/blog/how-much-vram-for-ai).

### Sin tarjeta gráfica también sirve para estudiar y chatear

Un portátil normal de 16 GB con solo gráficos Intel terminó una respuesta de estudio completa, una explicación y tres preguntas de examen, en unos 20 segundos. Un portátil de 8 GB también funciona, más despacio, siempre que las demás apps dejen algo de memoria libre ([nuestra prueba con 8 GB](https://blog.greencube.app/blog/run-ai-on-8gb-ram)).

## Apps que usan IA sin internet en Windows

Esto sale de la web de cada app, comprobado el 21 de octubre de 2026. No hemos cronometrado las otras apps en nuestros PCs, así que la tabla no compara velocidad.

| App | Windows | Precio | ¿Elige el modelo por ti? | Lee tus PDFs |
| --- | --- | --- | --- | --- |
| **GreenCube** | Windows 10 y 11 | 9,99 € una vez | Sí, según tu tarjeta y tu RAM | Sí |
| **LM Studio** | Necesita un procesador con AVX2 | Gratis | No, eliges tú de una lista | Sí |
| **Jan** | Windows 10 o posterior | Gratis, código abierto | No | Sí |
| **Ollama** | Windows; ventana de chat desde julio de 2025 | Gratis en tu PC | No | Sí |
| **GPT4All** | Windows (no en PCs ARM) | Gratis, código abierto | No | Sí, con LocalDocs |
| **AnythingLLM** | Windows | Escritorio gratis | No | Sí |
| **Msty** | Windows 10 y 11 | Plan gratis | No | Sí |
| **KoboldCpp** | Un solo .exe, chat en tu navegador | Gratis, código abierto | No | Solo texto |

Las apps gratis encajan bien si te gusta elegir tú los modelos y los ajustes. GreenCube es para quien prefiere que elija por él. Para ver qué envía cada una a internet, además de apps para Mac y móvil, lee [nuestra comparativa de 12 chatbots de IA sin internet](https://blog.greencube.app/blog/best-offline-ai-chatbot).

## ¿Windows 10 o Windows 11?

La IA funciona igual en los dos, porque lo que importa es tu RAM y tu tarjeta gráfica, no la versión de Windows. Algo que conviene saber: Microsoft dejó de dar soporte a Windows 10 el 14 de octubre de 2025, así que un PC con Windows 10 ya no recibe parches de seguridad salvo que te apuntes a las actualizaciones extendidas. Una IA sin internet guarda tus chats en tu PC de todos modos, pero mantener Windows actualizado sigue mereciendo la pena.

## Cómo comprobar que de verdad no sale nada

1. Después de la primera descarga, activa el modo avión (o desenchufa el cable) y chatea. Si responde, la IA está funcionando en tu PC.
2. Vigila la red. Pulsa **Windows + R**, escribe **resmon** y abre la pestaña **Red**. "Procesos con actividad de red" muestra todos los programas que envían o reciben datos mientras chateas.
3. Lee lo que la app dice que se conecta a internet. GreenCube inicia sesión una vez para activarse, descarga la IA y sus actualizaciones, y su búsqueda Online (que empieza apagada cada vez que abres la app) envía términos de búsqueda a buscadores. No sale nada más: "Nunca recibimos tus chats, archivos, recuerdos ni imágenes".

## Lo que no puede hacer una IA sin internet en Windows

No sabe las noticias de hoy. El modelo solo sabe lo que aprendió al entrenarse, así que para cualquier cosa actual necesitas una búsqueda web, y esa parte sí se conecta a internet.

No le va a ganar en todo a las IAs más grandes de la nube. Los modelos que caben en un PC se manejan bien con el estudio, la escritura y las preguntas del día a día, pero los modelos más grandes de la nube siguen siendo más fuertes en los problemas más difíciles.

Y solo va tan rápido como tu PC. Un portátil de 8 GB escribe más o menos a la velocidad a la que lees; un PC gaming va muchísimo más rápido. Si vas a estudiar con ella, [lo que puede hacer una IA sin internet por un estudiante](https://blog.greencube.app/blog/offline-ai-for-students) tiene los tiempos de PDFs, guías de estudio y tarjetas.

## FAQ

### ¿Puedo usar IA sin internet en Windows 11?

Sí. Apps como GreenCube, LM Studio, Jan, Ollama y GPT4All ejecutan el modelo de IA en tu propio PC. Necesitas internet una vez para descargar la app y el modelo; después, el chat funciona con el wifi apagado.

### ¿Funciona la IA local en Windows 10?

Sí. GreenCube, Jan y Msty indican Windows 10 como compatible. Microsoft dejó de dar soporte a Windows 10 el 14 de octubre de 2025: la IA sigue funcionando, pero tu PC ya no recibe parches de seguridad salvo que te apuntes a las actualizaciones extendidas.

### ¿Cuánta RAM necesito para instalar una IA en mi PC?

Con 8 GB funciona con un modelo pequeño: nuestro portátil de 8 GB escribía de 5 a 7 tokens por segundo en chats reales, más o menos a la velocidad a la que lees. Con 16 GB va cómodo: nuestro portátil de 16 GB sin tarjeta gráfica escribía de 14 a 18.

### ¿Necesito tarjeta gráfica para tener IA local en el PC?

No, pero ayuda mucho. En PCs gaming con una tarjeta de 6 GB o más medimos de 37 a 76 tokens por segundo en la mayoría de tarjetas, varias veces más rápido que esos mismos PCs solo con el procesador. Las imágenes necesitan al menos 12 GB de RAM.

### ¿Hay alguna IA sin internet gratis para Windows?

Sí: LM Studio, Jan, Ollama, GPT4All y AnythingLLM son gratis, y eliges y descargas tú el modelo. GreenCube cuesta 9,99 € una vez y elige por ti el modelo que encaja con tu PC.
