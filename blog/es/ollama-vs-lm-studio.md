# Ollama vs LM Studio: diferencias y cuál va más rápido (2026)

> Ollama frente a LM Studio, según sus propias páginas: código abierto frente a cerrado, línea de comandos frente a app de escritorio, requisitos en Mac con Intel y Windows, qué envía cada uno a internet y qué decide la velocidad. Y la opción que elige el modelo por ti.

Canonical: https://blog.greencube.app/blog/es/ollama-vs-lm-studio  
Published: 2026-10-23  
Author: Hector Gras

**Respuesta corta:** **Ollama** es de código abierto (MIT) y pensado para programadores: línea de comandos, API local y, desde julio de 2025, una ventana de chat sencilla. **LM Studio** es una app de escritorio de código cerrado, con ventana de chat completa, buscador de modelos y servidor local, gratis también para el trabajo. La **velocidad** la marca sobre todo tu hardware y que el modelo quepa en tu tarjeta gráfica, no cuál de los dos elijas.

- **MIT** la licencia de Ollama; LM Studio es de código cerrado
- **Mac con Intel** solo Ollama lo sigue incluyendo (solo procesador, macOS 14+)
- **6×** más lento en cualquier app cuando el modelo se sale de tu tarjeta gráfica

## Ollama frente a LM Studio, uno al lado del otro

Según la web, la documentación y la página de privacidad de cada app, comprobado el 21 y el 23 de octubre de 2026.

|  | Ollama | LM Studio |
| --- | --- | --- |
| **Licencia** | Código abierto, MIT ([web](https://ollama.com/download)) | Código cerrado; gratis, también para el trabajo ([LM Studio](https://lmstudio.ai/blog/free-for-work)) |
| **Cómo se usa** | Línea de comandos y API local; ventana de chat en Windows y Mac desde julio de 2025 ([Ollama](https://ollama.com/blog/new-app)) | App de escritorio con chat, búsqueda y descarga de modelos, y servidor local estilo OpenAI |
| **Windows** | Sí | Sí; el procesador necesita AVX2 ([requisitos](https://lmstudio.ai/docs/app/system-requirements)) |
| **Mac** | Chip de Apple con GPU, o Intel solo con procesador; macOS 14+ ([documentación](https://docs.ollama.com/macos)) | Solo chip de Apple; macOS 14+ |
| **Linux** | Sí | Sí |
| **Tus PDF** | Arrastrar texto o PDF | PDF, DOCX, TXT ([documentación](https://lmstudio.ai/docs/app/basics/rag)) |
| **Qué sale a internet** | No ve los prompts en local; puede recoger metadatos limitados del dispositivo y del uso ([privacidad](https://ollama.com/privacy)) | No envía mensajes ni documentos en local, sin telemetría; actualizaciones y descargas de modelos sí salen ([privacidad](https://lmstudio.ai/app-privacy)) |
| **Opción en la nube** | Planes en la nube desde 20 $ al mes ([precios](https://ollama.com/pricing)) | Modelos en la nube y búsqueda web de pago como extras |

## ¿Cuál va más rápido?

Los dos usan por debajo motores abiertos de la familia de llama.cpp, así que en el mismo PC, con el mismo archivo de modelo y los mismos ajustes, el hardware decide casi toda la velocidad. No hemos medido las dos apps una al lado de otra, así que no daremos un ganador. Lo que sí hemos medido, con GreenCube en 10 PCs, es lo que más mueve la velocidad:

- **Si el modelo cabe en la tarjeta gráfica.** El mismo modelo 12B escribía 35,6 tokens por segundo entero en una tarjeta de 8 GB y 5,9 con parte fuera: [6 veces más lento](https://blog.greencube.app/blog/es/cuanta-vram-para-ia).
- **Tarjeta frente a procesador.** La misma IA en el mismo sobremesa: 5 tokens por segundo con el procesador, 72 con una RX 5700 XT.
- **Lo nueva que es la tarjeta.** Cuatro tarjetas de 8 GB fueron de unos 11 a 72 tokens por segundo con el mismo modelo.

Así que, en cualquiera de las dos, elige un modelo que quepa en tu VRAM con unos 1,5 GB de margen: [qué modelo cabe en tu PC](https://blog.greencube.app/blog/es/mejor-modelo-ia-local).

## ¿Cuál te conviene?

#### Eres programador

Ollama: código abierto, un servicio en segundo plano y una API a la que se conectan otras herramientas.

#### Quieres una ventana y un buscador de modelos

LM Studio: buscar, descargar y chatear sin terminal.

#### Tienes un Mac con Intel

Ollama, solo con el procesador. LM Studio no se instala.

#### No quieres elegir modelos

GreenCube (Windows, 9,99 € una vez) mira tu tarjeta y tu RAM y elige el modelo que cabe. [Más alternativas a LM Studio](https://blog.greencube.app/blog/es/alternativas-a-lm-studio).

## Cómo lo comprobamos

Leímos la web, la documentación, los requisitos y la página de privacidad de Ollama y LM Studio el 21 y el 23 de octubre de 2026 y enlazamos cada dato. Las velocidades de esta página son de nuestras propias pruebas con GreenCube, no de estas dos apps. Hacemos GreenCube, así que nos ceñimos a datos que cualquiera puede comprobar.

## FAQ

### ¿Qué va más rápido, Ollama o LM Studio?

En el mismo PC, con el mismo modelo y los mismos ajustes, la velocidad la marca sobre todo tu hardware: los dos usan por debajo motores abiertos de la familia de llama.cpp. Lo que más cambia la velocidad es si el modelo cabe entero en tu tarjeta gráfica. No hemos medido las dos apps una al lado de otra, así que no diremos cuál es más rápida.

### ¿Qué diferencia hay entre Ollama y LM Studio?

Ollama es de código abierto (MIT), pensado en torno a la línea de comandos y una API local, con ventana de chat en Windows y Mac desde julio de 2025. LM Studio es una app de escritorio de código cerrado con ventana de chat, buscador de modelos y servidor local estilo OpenAI, gratis también para el trabajo.

### ¿Cuál es mejor para empezar, Ollama o LM Studio?

LM Studio, si quieres buscar y descargar modelos en una ventana. Ollama es más sencillo para programadores que quieren un servicio en segundo plano y una API. Si prefieres no elegir modelo, GreenCube (Windows, 9,99 € una vez) elige uno para tu PC.

### ¿Ollama o LM Studio funcionan en un Mac con Intel?

La documentación de Ollama incluye los Mac con Intel, solo con el procesador, en macOS 14 o posterior. LM Studio necesita un Mac con chip de Apple.

### ¿Ollama y LM Studio envían datos a internet?

LM Studio dice que no transmite mensajes ni documentos cuando funciona en local y que no tiene telemetría; comprobar actualizaciones y descargar modelos sí sale a internet. Ollama dice que no ve tus prompts en local, pero puede recoger metadatos limitados del dispositivo y del uso. Los dos pueden usar modelos en la nube si los eliges.
