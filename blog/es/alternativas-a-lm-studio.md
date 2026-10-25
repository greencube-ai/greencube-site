# Alternativas a LM Studio: 9 opciones para Windows, Mac, Linux y móvil (2026)

> LM Studio es gratis pero de código cerrado, necesita AVX2 en Windows y un chip de Apple en Mac. Las alternativas para código abierto, Mac con Intel, Android y Windows sin complicaciones: Jan, Ollama, GPT4All, AnythingLLM, Msty, KoboldCpp, PocketPal AI, Atomic Chat y GreenCube, según sus propias páginas.

Canonical: https://blog.greencube.app/blog/es/alternativas-a-lm-studio  
Published: 2026-10-23  
Author: Hector Gras

**Respuesta corta: depende de por qué dejas LM Studio.** Para código abierto, **Jan** es el cambio más parecido (Apache 2.0, ejecuta los modelos ella misma, Windows, Mac y Linux), y **Ollama** (MIT) es la otra gran opción. En un **Mac con Intel**, Ollama es la que sigue incluyendo Intel en su documentación. En el **móvil**, PocketPal AI o Atomic Chat. En **Windows sin elegir modelos**, GreenCube (9,99 € una vez) elige la IA que encaja con tu PC.

- **9** alternativas comprobadas en sus propias páginas, octubre 2026
- **AVX2** LM Studio lo necesita en Windows; en Mac, un chip de Apple
- **8 de 9** se pueden probar gratis; GreenCube cuesta 9,99 € una vez

## Por qué la gente busca una alternativa a LM Studio

LM Studio es una buena app: gratis, también para el trabajo, con ventana de chat y un servidor local estilo OpenAI, y lee PDF ([LM Studio](https://lmstudio.ai/blog/free-for-work)). Lo que no hace, según sus propias páginas:

- **Es de código cerrado.** Si quieres código que puedas leer o compilar tú, necesitas otra cosa.
- **Tiene límites de hardware.** En Windows el procesador necesita AVX2; en Mac necesita chip de Apple y macOS 14 o posterior ([requisitos](https://lmstudio.ai/docs/app/system-requirements)). Los PCs antiguos y los Mac con Intel se quedan fuera.
- **No tiene app para móvil.**
- **Eliges tú el modelo.** Es libertad si conoces los modelos, y un muro de nombres si no.

## Elige según el motivo para cambiar

### Quieres código abierto

**Jan** es el cambio más parecido: una app de chat de escritorio que ejecuta los modelos ella misma, lee PDF y archivos de Office y ofrece una API local compatible con OpenAI, con licencia Apache 2.0 ([GitHub](https://github.com/janhq/jan)). **Ollama** (MIT) es un motor de línea de comandos con ventana de chat en Windows y Mac desde julio de 2025 ([Ollama](https://ollama.com/blog/new-app)). **AnythingLLM** (MIT) está pensada para chatear con tus documentos.

### Tienes un Mac con Intel

LM Studio y Jan necesitan chip de Apple ([Jan](https://jan.ai/docs/desktop/install/mac)). La página de macOS de Ollama incluye Apple serie M y x86 (solo procesador), en macOS 14 Sonoma o posterior ([documentación de Ollama](https://docs.ollama.com/macos)). Cuenta con que irá lento: un Mac con Intel ejecuta el modelo solo con el procesador.

### Lo quieres en el móvil

**PocketPal AI** (iPhone y Android, MIT) y **Atomic Chat** (iPhone y Android, Apache 2.0) ejecutan los modelos en el propio móvil; **AnythingLLM** tiene app para Android. En un móvil caben modelos más pequeños que en un PC, así que las respuestas son más sencillas.

### Usas Windows y no quieres elegir modelos

**GreenCube** mira tu tarjeta gráfica y tu RAM y descarga la IA que encaja; después chatea, lee PDF y fotos, hace flashcards y crea imágenes, sin internet. Cuesta 9,99 € una vez y funciona en Windows 10 y 11. [Qué necesita un PC con Windows, medido](https://blog.greencube.app/blog/es/ia-sin-internet-windows).

## Las 9 alternativas, una al lado de otra

Según la web, la documentación o el GitHub de cada app, comprobado el 21 y el 23 de octubre de 2026. "No lo dice" significa que sus páginas no lo indican. No hemos comparado estas apps entre sí con pruebas de velocidad.

| App | Funciona en | Licencia y precio | ¿Elige el modelo por ti? | Tus PDF |
| --- | --- | --- | --- | --- |
| **Jan** ([GitHub](https://github.com/janhq/jan)) | Windows 10+, Mac con chip de Apple (macOS 13.6+), Linux | Apache 2.0, gratis | No | Sí: PDF, archivos de Office |
| **Ollama** ([web](https://ollama.com/download)) | Windows, Mac (chip de Apple, o Intel solo con procesador, macOS 14+), Linux | MIT, gratis en tu PC; planes en la nube desde 20 $ al mes | No | Sí, arrastrando |
| **GPT4All** ([GitHub](https://github.com/nomic-ai/gpt4all)) | Windows, macOS 12.6+, Linux (no PCs ARM) | MIT, gratis; última versión de escritorio el 25 feb 2025 | No | Sí, con LocalDocs |
| **AnythingLLM** ([web](https://anythingllm.com/desktop)) | Windows, macOS, Linux; app para Android | MIT, escritorio gratis | No | Sí: PDF, TXT, DOCX |
| **Msty** ([web](https://msty.ai/pricing)) | Windows 10/11, macOS 11+, Linux | Plan gratuito; Aurum 149 $ al año o 349 $ una vez; licencia: no lo dice | No | Sí, Knowledge Stacks |
| **KoboldCpp** ([GitHub](https://github.com/LostRuins/koboldcpp)) | Windows, Linux, Mac con chip de Apple | AGPL-3.0, gratis; un solo .exe, chat en el navegador | No | Búsqueda de texto; PDF: no lo dice |
| **PocketPal AI** ([GitHub](https://github.com/a-ghorbani/pocketpal-ai)) | iPhone/iPad (iOS 15.1+), Android | MIT, gratis | No | No lo dice |
| **Atomic Chat** ([web](https://atomic.chat/offline-ai)) | Windows, macOS 13.6+, Linux; iPhone y Android | Apache 2.0, gratis | No | Sí: archivos y PDF |
| **GreenCube** ([web](https://greencube.app)) | Windows 10 y 11 | 9,99 € (9,99 US$) una vez; código cerrado | **Sí**, según tu tarjeta y tu RAM | Sí: PDF, apuntes, fotos |

¿Quieres ver qué envía cada una a internet, según sus páginas de privacidad? Mira [nuestra comparativa de 12 chatbots de IA sin internet](https://blog.greencube.app/blog/es/mejor-chatbot-ia-sin-internet). ¿Dejas una página de chat autoalojada? Mira [alternativas a Open WebUI](https://blog.greencube.app/blog/es/alternativas-a-open-webui).

## ¿Irá más rápido que LM Studio?

La mayoría de estas apps usan por debajo el mismo motor abierto, llama.cpp, así que en el mismo PC con el mismo modelo la velocidad la marca sobre todo tu hardware, no la app. No las hemos medido una al lado de otra, así que no diremos que una es más rápida. Lo que sí medimos es GreenCube en 10 PCs reales:

| Tu PC | Escribe |
| --- | --- |
| Portátil de 8 GB, sin tarjeta gráfica | **5–7** tokens/s, más o menos a la velocidad a la que lees |
| Portátil de 16 GB, sin tarjeta gráfica | **14–18** tokens/s |
| PC gaming con tarjeta de 6 GB o más | **37–76** tokens/s en la mayoría de tarjetas |

Tu tarjeta exacta está en [¿Puede mi PC ejecutar IA?](https://blog.greencube.app/blog/es/ia-en-mi-pc#checker) La gran regla de velocidad vale en todas las apps: un modelo que cabe entero en tu tarjeta gráfica va rápido, y uno que se sale de ella va lento ([medimos 6 veces más lento](https://blog.greencube.app/blog/es/cuanta-vram-para-ia)).

## Cómo lo comprobamos

El 21 de octubre de 2026 leímos la web, la documentación, el GitHub y la página de privacidad de cada app, y el 23 de octubre volvimos a comprobar la compatibilidad con Mac en las páginas de instalación de Jan y Ollama. Enlazamos la página de la que sale cada dato y escribimos "no lo dice" cuando una página no lo indica. Hacemos GreenCube, así que nos ceñimos a datos que cualquiera puede comprobar y no ordenamos las apps de mejor a peor. Lo volveremos a comprobar cada mes.

## FAQ

### ¿Cuál es la mejor alternativa de código abierto a LM Studio?

Jan es la más parecida: una app de chat de escritorio que ejecuta los modelos ella misma, con un servidor local compatible con OpenAI, con licencia Apache 2.0, para Windows, Mac y Linux. Ollama (MIT) es la otra gran opción, con línea de comandos y una ventana de chat en Windows y Mac.

### ¿Hay alternativa a LM Studio para Mac con Intel?

LM Studio y Jan necesitan un Mac con chip de Apple. La documentación de Ollama incluye los Mac con Intel (x86), solo con el procesador, en macOS 14 Sonoma o posterior.

### ¿Hay alternativa a LM Studio para Android?

LM Studio no tiene app para móvil. PocketPal AI (Android e iPhone), Atomic Chat (Android e iPhone) y la app de AnythingLLM para Android ejecutan los modelos en el propio móvil.

### ¿LM Studio es gratis?

Sí, también para el trabajo, pero es de código cerrado. En Windows necesita un procesador con AVX2; en Mac, un chip de Apple y macOS 14 o posterior.

### ¿Hay alguna alternativa a LM Studio que elija el modelo por mí?

GreenCube (Windows 10 y 11, 9,99 € una vez) mira tu tarjeta gráfica y tu RAM y descarga la IA que encaja, así que no hay lista de modelos que elegir. Las alternativas gratis te dejan, y te piden, elegir el modelo tú.
