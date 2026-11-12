# Alternativas a LM Studio: 9 opciones para Windows, Mac, Linux y móvil (2026)

> LM Studio es gratis pero de código cerrado, necesita AVX2 en Windows y un chip de Apple en Mac. Las alternativas para código abierto, Mac con Intel, Android y Windows sin complicaciones: Jan, Ollama, GPT4All, AnythingLLM, Msty, KoboldCpp, PocketPal AI, Atomic Chat y GreenCube, según sus propias páginas.

Canonical: https://blog.greencube.app/blog/es/alternativas-a-lm-studio  
Published: 2026-10-23  
Author: Hector Gras

La alternativa a LM Studio que te conviene depende de por qué la dejas. Para código abierto, Jan es el cambio más parecido (Apache 2.0, ejecuta los modelos ella misma, en Windows, Mac y Linux), y Ollama (MIT) es la otra grande. En un Mac con Intel, Ollama es la que sigue incluyendo Intel en su documentación. En el móvil, prueba PocketPal AI o Atomic Chat.

Yo hago GreenCube, una de las nueve, así que ten eso en cuenta con mi opinión; no las he ordenado de mejor a peor. Los datos salen de la web, la documentación o la página de GitHub de cada app, leídas el 21 de octubre de 2026, y el 23 de octubre volvimos a comprobar la compatibilidad con Mac en las páginas de instalación de Jan y de Ollama. "No lo dice" significa que las páginas de esa app no lo indican. No hemos comparado el rendimiento de estas apps entre sí.

## Por qué la gente busca una alternativa a LM Studio

LM Studio es una buena app. Es gratis, también para el trabajo, tiene ventana de chat y un servidor local al estilo de OpenAI, y lee PDF ([LM Studio](https://lmstudio.ai/blog/free-for-work)). Los motivos para buscar otra cosa salen de sus propias páginas.

Es de código cerrado, así que si quieres código que puedas leer o compilar tú, necesitas otra cosa. También tiene límites de hardware: en Windows el procesador necesita AVX2, y en Mac hace falta un chip de Apple y macOS 14 o posterior ([requisitos](https://lmstudio.ai/docs/app/system-requirements)). Eso deja fuera los PCs antiguos y los Mac con Intel.

No tiene app para móvil. Y el modelo lo eliges tú, lo que es libertad si conoces los modelos y un muro de nombres si no.

## Elige según el motivo por el que la dejas

### Quieres código abierto

Jan es el cambio más parecido: una app de chat de escritorio que ejecuta los modelos ella misma, lee PDF y archivos de Office y sirve una API local compatible con OpenAI, con licencia Apache 2.0 ([GitHub](https://github.com/janhq/jan)). Ollama (MIT) es un motor de línea de comandos con ventana de chat de escritorio en Windows y Mac desde julio de 2025 ([Ollama](https://ollama.com/blog/new-app)). AnythingLLM (MIT) está pensada para chatear con tus documentos.

### Tienes un Mac con Intel

LM Studio y Jan necesitan un chip de Apple ([Jan](https://jan.ai/docs/desktop/install/mac)). La página de macOS de Ollama incluye los Apple serie M y x86 (solo procesador), en macOS 14 Sonoma o posterior ([documentación de Ollama](https://docs.ollama.com/macos)). Cuenta con que vaya lento, porque un Mac con Intel ejecuta el modelo solo con el procesador.

### La quieres en el móvil

PocketPal AI (iPhone y Android, MIT) y Atomic Chat (iPhone y Android, Apache 2.0) ejecutan los modelos en el propio móvil, y AnythingLLM tiene app para Android. En un móvil caben modelos más pequeños que en un PC, así que las respuestas son más sencillas.

### Usas Windows y no quieres elegir modelos

Este es el caso para el que hice GreenCube. Lee tu tarjeta gráfica y tu RAM y descarga la IA que encaja, y luego chatea, lee PDF y fotos, hace tarjetas de estudio y genera imágenes, sin internet. Cuesta 9,99 € una vez y funciona en Windows 10 y 11. Hay más sobre [lo que necesita un PC con Windows](https://blog.greencube.app/blog/local-ai-chatbot-windows).

## Las 9 alternativas, una al lado de otra

| App | Funciona en | Licencia y precio | ¿Elige el modelo por ti? | Tus PDF |
| --- | --- | --- | --- | --- |
| Jan ([GitHub](https://github.com/janhq/jan)) | Windows 10+, Mac con chip de Apple (macOS 13.6+), Linux | Apache 2.0, gratis | No | Sí: PDF, archivos de Office |
| Ollama ([web](https://ollama.com/download)) | Windows, Mac (chip de Apple, o Intel solo con procesador, macOS 14+), Linux | MIT, gratis en tu PC; planes en la nube desde 20 $ al mes | No | Sí, arrastrando |
| GPT4All ([GitHub](https://github.com/nomic-ai/gpt4all)) | Windows, macOS 12.6+, Linux (no PCs ARM) | MIT, gratis; última versión de escritorio el 25 de febrero de 2025 | No | Sí, con LocalDocs |
| AnythingLLM ([web](https://anythingllm.com/desktop)) | Windows, macOS, Linux; app para Android | MIT, escritorio gratis | No | Sí: PDF, TXT, DOCX |
| Msty ([web](https://msty.ai/pricing)) | Windows 10/11, macOS 11+, Linux | Plan gratuito; Aurum 149 $ al año o 349 $ una vez; licencia no indicada | No | Sí, Knowledge Stacks |
| KoboldCpp ([GitHub](https://github.com/LostRuins/koboldcpp)) | Windows, Linux, Mac con chip de Apple | AGPL-3.0, gratis; un solo .exe, chat en el navegador | No | Búsqueda en texto; PDF no lo dice |
| PocketPal AI ([GitHub](https://github.com/a-ghorbani/pocketpal-ai)) | iPhone/iPad (iOS 15.1+), Android | MIT, gratis | No | No lo dice |
| Atomic Chat ([web](https://atomic.chat/offline-ai)) | Windows, macOS 13.6+, Linux; iPhone y Android | Apache 2.0, gratis | No | Sí: archivos y PDF |
| GreenCube ([web](https://greencube.app)) | Windows 10 y 11 | 9,99 € (9,99 US$) una vez; código cerrado | **Sí**, según tu tarjeta y tu RAM | Sí: PDF, apuntes, fotos |

Ocho de las nueve se pueden probar gratis. Si quieres saber qué envía cada una a internet, según sus páginas de privacidad, mira [nuestra comparativa de 12 chatbots de IA sin internet](https://blog.greencube.app/blog/best-offline-ai-chatbot). Si lo que dejas es una página de chat autoalojada y no una app de escritorio, [alternativas a Open WebUI](https://blog.greencube.app/blog/openwebui-alternatives) es la lista que te sirve.

## ¿Irá más rápido que LM Studio?

La mayoría de estas apps usan por debajo el mismo motor abierto, llama.cpp, así que en el mismo PC y con el mismo modelo la velocidad la marca sobre todo tu hardware, no la app. No hemos cronometrado las apps una al lado de otra, así que no voy a decir que una sea más rápida. Lo que sí medimos es GreenCube en 10 PCs reales:

| Tu PC | Escribe |
| --- | --- |
| Portátil de 8 GB, sin tarjeta gráfica | **5–7** tokens/s, más o menos a la velocidad a la que lees |
| Portátil de 16 GB, sin tarjeta gráfica | **14–18** tokens/s |
| PC gaming con tarjeta de 6 GB o más | **37–76** tokens/s en la mayoría de tarjetas |

Tu tarjeta exacta está en [¿Puede mi PC ejecutar IA?](https://blog.greencube.app/blog/can-my-pc-run-ai#checker) La regla de velocidad más importante se cumple en todas las apps: un modelo que cabe entero en tu tarjeta gráfica va rápido, y uno que se sale va lento ([lo medimos 6 veces más lento](https://blog.greencube.app/blog/how-much-vram-for-ai)).

## FAQ

### ¿Cuál es la mejor alternativa de código abierto a LM Studio?

Jan es la más parecida: una app de chat de escritorio que ejecuta los modelos ella misma, con un servidor local compatible con OpenAI, con licencia Apache 2.0, para Windows, Mac y Linux. Ollama (MIT) es la otra gran opción, con línea de comandos y una ventana de chat de escritorio en Windows y Mac.

### ¿Hay alternativa a LM Studio para Mac con Intel?

LM Studio y Jan necesitan un Mac con chip de Apple. La propia documentación de Ollama incluye los Mac con Intel (x86) como compatibles, solo con el procesador, en macOS 14 Sonoma o posterior.

### ¿Hay alternativa a LM Studio para Android?

LM Studio no tiene app para móvil. PocketPal AI (Android e iPhone), Atomic Chat (Android e iPhone) y la app de AnythingLLM para Android ejecutan los modelos en el propio móvil.

### ¿LM Studio es gratis?

Sí, también para el trabajo, pero es de código cerrado. En Windows necesita un procesador con AVX2; en Mac, un chip de Apple y macOS 14 o posterior.

### ¿Hay alguna alternativa a LM Studio que elija el modelo por mí?

GreenCube (Windows 10 y 11, 9,99 € una vez) mira tu tarjeta gráfica y tu RAM y descarga la IA que encaja, así que no hay lista de modelos que elegir. Las alternativas gratis te dejan, y te piden, elegir el modelo tú.
