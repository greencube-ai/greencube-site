# IA sin internet en Mac: apps para chip de Apple y Mac con Intel (2026)

> Apps de IA sin internet para Mac, comprobadas en sus propias páginas: LM Studio, Jan, Ollama, GPT4All, Msty, AnythingLLM, Atomic Chat y KoboldCpp. Cuáles necesitan chip de Apple, cuáles siguen funcionando en Mac con Intel, qué macOS pide cada una y si Apple Intelligence funciona sin conexión.

Canonical: https://blog.greencube.app/blog/es/ia-sin-internet-mac  
Published: 2026-10-23  
Author: Hector Gras

Sí, un Mac puede usar IA sin internet. En un Mac con chip de Apple, LM Studio, Jan, Ollama, GPT4All, Msty y AnythingLLM funcionan sin conexión una vez descargado un modelo, y LM Studio y Jan son las más fáciles para empezar. En un Mac antiguo con Intel, la lista se reduce a Ollama, funcionando solo con el procesador. Apple Intelligence funciona sin internet solo en parte.

Yo mismo hago una app de IA sin internet, GreenCube, pero es solo para Windows, así que no es una de las opciones de aquí. Todo lo de abajo sale de las propias páginas de cada app, que leímos el 21 y el 23 de octubre de 2026.

## Apps de IA sin internet para Mac, comprobadas

"No lo dice" significa que las páginas de la app no lo aclaran ni en un sentido ni en otro.

| App | Chip de Apple | Mac con Intel | macOS | Precio |
| --- | --- | --- | --- | --- |
| **LM Studio** ([requisitos](https://lmstudio.ai/docs/app/system-requirements)) | Sí | No | 14+ | Gratis; código cerrado |
| **Jan** ([instalación](https://jan.ai/docs/desktop/install/mac)) | Sí | No | 13.6+ | Gratis, Apache 2.0 |
| **Ollama** ([documentación](https://docs.ollama.com/macos)) | Sí (GPU) | **Sí, solo procesador** | 14+ | Gratis, MIT |
| **GPT4All** ([GitHub](https://github.com/nomic-ai/gpt4all)) | Sí | No lo dice | 12.6+ | Gratis, MIT; última versión feb. 2025 |
| **Msty** ([web](https://msty.ai/pricing)) | Sí | No lo dice | 11+ | Plan gratis |
| **AnythingLLM** ([web](https://anythingllm.com/desktop)) | Sí | No lo dice | No lo dice | Gratis, MIT |
| **Atomic Chat** ([web](https://atomic.chat/offline-ai)) | Sí | No lo dice | 13.6+ | Gratis, Apache 2.0 |
| **KoboldCpp** ([GitHub](https://github.com/LostRuins/koboldcpp)) | Sí | No lo dice | No lo dice | Gratis, AGPL-3.0 |

Si quieres una ventana de app normal y nada de terminal, empieza por LM Studio o Jan: eliges un modelo de la lista, lo descargas y a chatear. Ollama es la que debes probar si te manejas con la línea de comandos, y es la única de aquí que sigue prometiendo funcionar en un Mac con Intel. La última versión de GPT4All es de febrero de 2025, algo que conviene saber antes de elegirla.

Lo que envía cada app a internet, según sus páginas de privacidad, está en [12 chatbots de IA sin internet comparados](https://blog.greencube.app/blog/best-offline-ai-chatbot). Si lo que quieres es dejar LM Studio, mira [alternativas a LM Studio](https://blog.greencube.app/blog/lm-studio-alternatives).

## ¿Apple Intelligence funciona sin internet?

En parte. Apple dice que Apple Intelligence atiende las peticiones primero en el Mac y envía las más exigentes a Private Cloud Compute, sus propios servidores, que necesitan conexión ([Apple](https://support.apple.com/guide/mac-help/mchlfc0d4779)). La extensión opcional de ChatGPT también necesita internet.

Apple no publica una lista de qué funciones se quedan siempre en el dispositivo. Así que la prueba honesta es la sencilla: activa el modo avión y prueba la función que te interesa.

## ¿Qué Mac va bien con IA local?

Casi todo lo decide la memoria. Un chip de Apple comparte su memoria entre el procesador y los gráficos, así que la IA puede usar la mayor parte, y con 16 GB o más va cómodo. Con 8 GB funcionan modelos pequeños, siempre que cierres antes las demás apps, igual que en cualquier ordenador de 8 GB.

Un Mac con Intel solo puede usar Ollama con el procesador, así que cuenta con respuestas lentas. En cualquier Mac, el modelo tiene que caber en la memoria con sitio de sobra para la conversación, y un modelo más grande no es mejor si no cabe: [un modelo que no cabe va mucho más lento](https://blog.greencube.app/blog/how-much-vram-for-ai).

Nosotros medimos en PCs con Windows, así que no tenemos velocidades propias de Mac que darte.

## ¿Tienes un PC con Windows?

Si también tienes un PC con Windows 10 u 11, ahí es donde funciona GreenCube. Elige la IA que encaja con el PC, lee PDFs y fotos y hace imágenes, todo sin internet, por 9,99 € una vez. No hay versión para Mac a la venta. La parte de Windows, con velocidades, está en [IA sin internet en Windows, medida en 10 PCs](https://blog.greencube.app/blog/local-ai-chatbot-windows).

## FAQ

### ¿Cuál es la mejor IA sin internet para Mac?

En un Mac con chip de Apple, LM Studio (gratis) y Jan (gratis, código abierto) son las apps de escritorio más sencillas; Ollama es la principal opción de línea de comandos, con ventana de chat. En un Mac con Intel, la documentación de Ollama sigue incluyendo Intel, solo con el procesador, en macOS 14 o posterior.

### ¿Apple Intelligence funciona sin internet en Mac?

En parte. Apple dice que las peticiones se procesan primero en el dispositivo, y las más exigentes van a sus servidores Private Cloud Compute, que necesitan internet; la extensión de ChatGPT también. Apple no publica una lista función por función de lo que funciona sin internet, así que la prueba fiable es activar el modo avión y probar.

### ¿Puedo usar IA local en un Mac con Intel?

Sí, con límites. LM Studio y Jan necesitan chip de Apple. Ollama incluye los Mac con Intel (x86), solo con el procesador, en macOS 14 Sonoma o posterior, así que cuenta con que irá lento.

### ¿GreenCube funciona en Mac?

No, GreenCube es para Windows 10 y 11. En un Mac, usa una de las apps de esta página.
