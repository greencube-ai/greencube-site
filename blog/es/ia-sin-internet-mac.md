# IA sin internet en Mac: apps para chip de Apple y Mac con Intel (2026)

> Apps de IA sin internet para Mac, comprobadas en sus propias páginas: LM Studio, Jan, Ollama, GPT4All, Msty, AnythingLLM, Atomic Chat y KoboldCpp. Cuáles necesitan chip de Apple, cuáles siguen funcionando en Mac con Intel, qué macOS pide cada una y si Apple Intelligence funciona sin conexión.

Canonical: https://blog.greencube.app/blog/es/ia-sin-internet-mac  
Published: 2026-10-23  
Author: Hector Gras

**Respuesta corta:** en un **Mac con chip de Apple**, LM Studio, Jan, Ollama, GPT4All, Msty y AnythingLLM funcionan sin internet una vez descargado el modelo; LM Studio y Jan son las más sencillas. En un **Mac con Intel**, LM Studio y Jan quedan fuera; la documentación de Ollama sigue incluyendo Intel, solo con el procesador, en macOS 14 o posterior. **Apple Intelligence** trabaja primero en el dispositivo, pero las peticiones más pesadas van a los servidores de Apple, así que solo funciona sin internet en parte.

- **8** apps para Mac comprobadas en sus propias páginas, octubre 2026
- **macOS 14** lo que piden LM Studio y Ollama
- **1** de ellas sigue incluyendo los Mac con Intel: Ollama, solo procesador

## Apps de IA sin internet para Mac, comprobadas

Según las páginas de cada app, comprobado el 21 y el 23 de octubre de 2026. "No lo dice" significa que sus páginas no lo indican.

| App | Chip de Apple | Mac con Intel | macOS | Precio |
| --- | --- | --- | --- | --- |
| **LM Studio** ([requisitos](https://lmstudio.ai/docs/app/system-requirements)) | Sí | No | 14+ | Gratis; código cerrado |
| **Jan** ([instalación](https://jan.ai/docs/desktop/install/mac)) | Sí | No | 13.6+ | Gratis, Apache 2.0 |
| **Ollama** ([documentación](https://docs.ollama.com/macos)) | Sí (GPU) | **Sí, solo procesador** | 14+ | Gratis, MIT |
| **GPT4All** ([GitHub](https://github.com/nomic-ai/gpt4all)) | Sí | No lo dice | 12.6+ | Gratis, MIT; última versión feb 2025 |
| **Msty** ([web](https://msty.ai/pricing)) | Sí | No lo dice | 11+ | Plan gratuito |
| **AnythingLLM** ([web](https://anythingllm.com/desktop)) | Sí | No lo dice | No lo dice | Gratis, MIT |
| **Atomic Chat** ([web](https://atomic.chat/offline-ai)) | Sí | No lo dice | 13.6+ | Gratis, Apache 2.0 |
| **KoboldCpp** ([GitHub](https://github.com/LostRuins/koboldcpp)) | Sí | No lo dice | No lo dice | Gratis, AGPL-3.0 |

Qué envía cada una a internet, según sus páginas de privacidad: [12 chatbots de IA sin internet comparados](https://blog.greencube.app/blog/es/mejor-chatbot-ia-sin-internet). ¿Dejas LM Studio? [Alternativas a LM Studio](https://blog.greencube.app/blog/es/alternativas-a-lm-studio).

## ¿Apple Intelligence funciona sin internet?

En parte. Apple dice que Apple Intelligence procesa primero las peticiones en el dispositivo y manda las más exigentes a Private Cloud Compute, sus propios servidores, que necesitan internet ([Apple](https://support.apple.com/es-es/guide/mac-help/mchlfc0d4779)). La extensión opcional de ChatGPT también necesita internet. Apple no publica qué funciones se quedan siempre en el dispositivo, así que la prueba honesta es sencilla: activa el modo avión y prueba la función que te interesa.

## ¿Qué Mac mueve bien la IA local?

#### Chip de Apple, 16 GB o más

La opción cómoda: el chip de Apple comparte la memoria entre procesador y gráficos, así que la IA puede usar casi toda.

#### Chip de Apple, 8 GB

Los modelos pequeños funcionan; cierra antes las demás apps, como en cualquier ordenador de 8 GB.

#### Mac con Intel

Ollama solo con el procesador. Cuenta con respuestas lentas.

#### Cualquier Mac

El modelo tiene que caber en memoria con sitio para la conversación; más grande no es mejor si no cabe.

Nosotros medimos en PCs con Windows, así que no tenemos velocidades propias en Mac; la regla que más importa es la misma en todas partes: [un modelo que no cabe va mucho más lento](https://blog.greencube.app/blog/es/cuanta-vram-para-ia).

## ¿Y en un PC con Windows?

GreenCube es solo para Windows: elige la IA que encaja con tu PC, lee PDF y fotos y crea imágenes, sin internet, por 9,99 € una vez. [IA sin internet en Windows, medida en 10 PCs](https://blog.greencube.app/blog/es/ia-sin-internet-windows).

## FAQ

### ¿Cuál es la mejor IA sin internet para Mac?

En un Mac con chip de Apple, LM Studio (gratis) y Jan (gratis, código abierto) son las apps de escritorio más sencillas; Ollama es la principal opción de línea de comandos, con ventana de chat. En un Mac con Intel, la documentación de Ollama sigue incluyendo Intel, solo con el procesador, en macOS 14 o posterior.

### ¿Apple Intelligence funciona sin internet en Mac?

En parte. Apple dice que las peticiones se procesan primero en el dispositivo, y las más exigentes van a sus servidores Private Cloud Compute, que necesitan internet; la extensión de ChatGPT también. Apple no publica una lista función por función, así que la prueba fiable es activar el modo avión y probar.

### ¿Puedo usar IA local en un Mac con Intel?

Sí, con límites. LM Studio y Jan necesitan chip de Apple. Ollama incluye los Mac con Intel (x86), solo con el procesador, en macOS 14 Sonoma o posterior, así que cuenta con que irá lento.

### ¿GreenCube funciona en Mac?

No, GreenCube es para Windows 10 y 11. En un Mac, usa una de las apps de esta página.
