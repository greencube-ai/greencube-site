# Ollama vs LM Studio: diferencias y cuál va más rápido (2026)

> Ollama frente a LM Studio, según sus propias páginas: código abierto frente a cerrado, línea de comandos frente a app de escritorio, requisitos en Mac con Intel y Windows, qué envía cada uno a internet y qué decide la velocidad. Y la opción que elige el modelo por ti.

Canonical: https://blog.greencube.app/blog/es/ollama-vs-lm-studio  
Published: 2026-10-23  
Author: Hector Gras

Ollama es de código abierto (MIT) y está pensado para programadores: línea de comandos, API local y, desde julio de 2025, una ventana de chat sencilla. LM Studio es una app de escritorio de código cerrado con una ventana de chat completa, un buscador de modelos y un servidor local, y también es gratis para el trabajo. En cuanto a la velocidad, depende sobre todo de tu hardware y de si el modelo cabe en tu tarjeta gráfica, no de cuál de los dos elijas.

Los datos de abajo salen de la web, la documentación y la página de privacidad de cada app, comprobadas el 21 y el 23 de octubre de 2026. Yo hago GreenCube, que aparece al final como tercera opción, así que ten eso en cuenta con mi opinión.

## Ollama frente a LM Studio, uno al lado del otro

|  | Ollama | LM Studio |
| --- | --- | --- |
| Licencia | Código abierto, MIT ([web](https://ollama.com/download)) | Código cerrado; gratis, también para el trabajo ([LM Studio](https://lmstudio.ai/blog/free-for-work)) |
| Cómo se usa | Línea de comandos y API local; ventana de chat de escritorio en Windows y Mac desde julio de 2025 ([Ollama](https://ollama.com/blog/new-app)) | App de escritorio con chat, búsqueda y descarga de modelos, y un servidor local al estilo de OpenAI |
| Windows | Sí | Sí; el procesador necesita AVX2 ([requisitos](https://lmstudio.ai/docs/app/system-requirements)) |
| Mac | Chip de Apple con GPU, o Intel solo con procesador; macOS 14+ ([documentación](https://docs.ollama.com/macos)) | Solo chip de Apple; macOS 14+ |
| Linux | Sí | Sí |
| Tus PDF | Arrastrar y soltar texto o PDF | PDF, DOCX, TXT ([documentación](https://lmstudio.ai/docs/app/basics/rag)) |
| Qué sale a internet | No ve los prompts en local; puede recoger metadatos limitados del dispositivo y del uso ([privacidad](https://ollama.com/privacy)) | En local no se envían mensajes ni documentos, sin telemetría; comprobar actualizaciones y descargar modelos sí sale a internet ([privacidad](https://lmstudio.ai/app-privacy)) |
| Opción en la nube | Planes en la nube desde 20 $ al mes ([precios](https://ollama.com/pricing)) | Modelos en la nube y búsqueda web de pago, como extras |

Las mayores diferencias en la práctica son la licencia, la forma de usar cada uno y los Mac con Intel, donde solo Ollama sigue apareciendo como compatible (y solo con el procesador).

## ¿Cuál va más rápido?

Los dos usan por debajo motores abiertos de la familia de llama.cpp. Así que en el mismo PC, con el mismo archivo de modelo y los mismos ajustes, el hardware decide casi toda la velocidad. No hemos cronometrado las dos apps una al lado de la otra, así que no voy a nombrar un ganador.

Lo que sí hemos medido, con GreenCube en 10 PCs, es lo que más mueve la velocidad. Estos números son de nuestras pruebas con GreenCube, no de Ollama ni de LM Studio, pero las mismas reglas de hardware valen para cualquier app:

- Si el modelo cabe en la tarjeta gráfica. El mismo modelo 12B escribía 35,6 tokens por segundo entero en una tarjeta de 8 GB y 5,9 con una parte fuera, [6 veces más lento](https://blog.greencube.app/blog/how-much-vram-for-ai).
- Tarjeta frente a procesador. La misma IA en el mismo sobremesa escribía 5 tokens por segundo en el procesador y 72 en una RX 5700 XT.
- Lo nueva que sea la tarjeta. Cuatro tarjetas de 8 GB iban de unos 11 a 72 tokens por segundo con el mismo modelo.

Así que, en cualquiera de las dos apps, elige un modelo que quepa en tu VRAM con unos 1,5 GB de margen. [Qué modelo cabe en tu PC](https://blog.greencube.app/blog/best-local-ai-models) lo repasa tarjeta por tarjeta.

## ¿Cuál elegir?

Si programas, Ollama es la elección natural: es de código abierto, funciona como servicio en segundo plano y tiene una API a la que se conectan otras herramientas.

Si quieres una ventana y un buscador de modelos, LM Studio te deja buscar, descargar y chatear sin abrir nunca una terminal.

Si tienes un Mac con Intel, la decisión está tomada. LM Studio no se instala, y Ollama funciona solo con el procesador, así que cuenta con que vaya lento.

Y si no quieres elegir modelos en absoluto, ese es el hueco que cubre GreenCube. Es para Windows, cuesta 9,99 € una vez y lee tu tarjeta y tu RAM para elegir el modelo que cabe. Hay más opciones en [alternativas a LM Studio](https://blog.greencube.app/blog/lm-studio-alternatives).

## FAQ

### ¿Qué va más rápido, Ollama o LM Studio?

En el mismo PC, con el mismo modelo y los mismos ajustes, la velocidad la marca sobre todo tu hardware: los dos usan por debajo motores abiertos de la familia de llama.cpp. Lo que más cambia la velocidad es si el modelo cabe entero en tu tarjeta gráfica. No hemos medido las dos apps una al lado de otra, así que no diremos cuál es más rápida.

### ¿Qué diferencia hay entre Ollama y LM Studio?

Ollama es de código abierto (MIT), pensado en torno a la línea de comandos y una API local, con ventana de chat de escritorio en Windows y Mac desde julio de 2025. LM Studio es una app de escritorio de código cerrado con ventana de chat, buscador de modelos y servidor local estilo OpenAI, gratis también para el trabajo.

### ¿Cuál es mejor para empezar, Ollama o LM Studio?

LM Studio, si quieres buscar y descargar modelos en una ventana. Ollama es más sencillo para programadores que quieren un servicio en segundo plano y una API. Si prefieres no elegir modelo, GreenCube (Windows, 9,99 € una vez) elige uno para tu PC.

### ¿Ollama o LM Studio funcionan en un Mac con Intel?

La documentación de Ollama incluye los Mac con Intel, solo con el procesador, en macOS 14 o posterior. LM Studio necesita un Mac con chip de Apple.

### ¿Ollama y LM Studio envían datos a internet?

LM Studio dice que no transmite mensajes ni documentos cuando funciona en local y que no tiene telemetría; comprobar actualizaciones y descargar modelos sí sale a internet. Ollama dice que no ve tus prompts en local, pero puede recoger metadatos limitados del dispositivo y del uso. Los dos pueden usar modelos en la nube si los eliges.
