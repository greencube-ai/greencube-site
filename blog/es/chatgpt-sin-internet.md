# ¿ChatGPT funciona sin internet? No, pero esto sí funciona sin conexión (2026)

> ChatGPT no tiene modo sin conexión: la app y la versión de escritorio necesitan internet, porque el modelo funciona en los servidores de OpenAI. Lo que sí funciona sin internet: el modelo abierto gpt-oss-20b de la propia OpenAI y las apps de IA local, con la RAM que necesitas y velocidades medidas.

Canonical: https://blog.greencube.app/blog/es/chatgpt-sin-internet  
Published: 2026-10-23  
Author: Hector Gras

**Respuesta corta: no.** ChatGPT funciona en los servidores de OpenAI, así que la web, la app del móvil y las de escritorio necesitan internet; no hay modo sin conexión. Lo que **sí** funciona sin internet es un modelo de IA en tu propio ordenador: el modelo abierto **gpt-oss-20b** de la propia OpenAI (necesita unos 16 GB de memoria), o apps como LM Studio, Jan, Ollama y GreenCube, que descargan un modelo una vez y después funcionan con el wifi apagado.

- **0** modos sin conexión en ChatGPT: el modelo está en los servidores de OpenAI
- **16 GB** de memoria para gpt-oss-20b, el modelo abierto de OpenAI
- **8 GB** bastan para un modelo local pequeño en un portátil (medido)

## Por qué ChatGPT no puede funcionar sin internet

Cuando escribes en ChatGPT, tu mensaje viaja a los centros de datos de OpenAI, un modelo escribe allí la respuesta y vuelve. Las apps de Windows y Mac son una ventana a ese mismo servicio, no una copia del modelo. Sin conexión, en tu dispositivo no hay nada que te responda.

Ojo con las apps de las tiendas que ponen "ChatGPT" y "sin internet" en el nombre: no son de OpenAI. Si alguna funciona de verdad sin conexión, está ejecutando otro modelo en tu móvil o tu PC.

## Qué funciona sin internet

### El modelo abierto de la propia OpenAI: gpt-oss-20b

En agosto de 2025 OpenAI publicó gpt-oss, modelos de pesos abiertos con licencia Apache 2.0. El pequeño, gpt-oss-20b, funciona en un ordenador con unos 16 GB de memoria ([OpenAI](https://openai.com/index/introducing-gpt-oss/)), con apps como Ollama o LM Studio. Lo hace OpenAI, pero no es ChatGPT: otro modelo, sin búsqueda web ni memoria de tu cuenta. No lo hemos medido en nuestros PCs.

### Una app de IA local

Apps que descargan un modelo una vez y lo ejecutan en tu PC: **LM Studio**, **Jan**, **Ollama** y **GPT4All** son gratis y te dejan elegir el modelo; **GreenCube** (Windows, 9,99 € una vez) elige el modelo que encaja con tu PC y además lee PDF y fotos y crea imágenes. [12 apps sin internet comparadas](https://blog.greencube.app/blog/es/mejor-chatbot-ia-sin-internet).

## Qué necesitas y cómo de rápido va

Medido con GreenCube en 10 PCs reales (modelos: Gemma 4 E2B y E4B de Google):

| Tu PC | Escribe | Se nota como |
| --- | --- | --- |
| Portátil de 8 GB, sin tarjeta gráfica | **5–7** tokens/s | más o menos a la velocidad a la que lees |
| Portátil de 16 GB, sin tarjeta gráfica | **14–18** tokens/s | más rápido de lo que lees |
| PC gaming con tarjeta de 6 GB o más | **37–76** tokens/s en la mayoría de tarjetas | muchas veces más rápido de lo que lees |

Tu tarjeta exacta: [¿Puede mi PC ejecutar IA?](https://blog.greencube.app/blog/es/ia-en-mi-pc#checker) En Windows: [qué necesita tu PC para usar IA sin internet](https://blog.greencube.app/blog/es/ia-sin-internet-windows).

## ChatGPT frente a una IA sin internet: el intercambio honesto

|  | ChatGPT | IA en tu PC |
| --- | --- | --- |
| **Funciona sin internet** | No | Sí, tras una descarga |
| **Fuerza en los problemas más difíciles** | Mayor: modelos mucho más grandes | Buena para estudiar, escribir y dudas del día a día |
| **Noticias de hoy** | Sí, con búsqueda | No (solo lo que aprendió el modelo) |
| **Límites de archivos e imágenes (gratis)** | Con límite ([detalle](https://blog.greencube.app/blog/es/limite-chatgpt-gratis)) | Ninguno |
| **Tus chats van a** | Los servidores de OpenAI | A ningún sitio: tu PC |
| **Precio** | Gratis, o 20 $ al mes con Plus | Apps gratis, o GreenCube 9,99 € una vez |

Mucha gente usa las dos: ChatGPT cuando tiene conexión y necesita el modelo más potente, y una IA sin internet en el tren, en una biblioteca con mal wifi o para apuntes que prefiere no subir.

## FAQ

### ¿ChatGPT funciona sin internet?

No. ChatGPT funciona en los servidores de OpenAI, así que la web, la app del móvil y las apps de escritorio para Windows y Mac necesitan conexión. OpenAI no ofrece modo sin conexión ni instalador offline.

### ¿Hay una versión oficial de ChatGPT sin internet?

De ChatGPT en sí, no. Lo más parecido de OpenAI es gpt-oss-20b, un modelo de pesos abiertos con licencia Apache 2.0 que funciona en un ordenador con unos 16 GB de memoria, con apps como Ollama o LM Studio. No es el mismo modelo que ChatGPT.

### ¿Cuál es la mejor alternativa a ChatGPT sin internet?

Una app que ejecute un modelo de IA en tu propio PC: LM Studio, Jan, Ollama y GPT4All son gratis (eliges tú el modelo); GreenCube cuesta 9,99 € una vez y elige el modelo para tu PC. Tras la primera descarga funcionan con el wifi apagado.

### ¿Cómo de rápida es una alternativa a ChatGPT sin internet?

Depende de tu PC. En nuestras pruebas GreenCube escribía de 5 a 7 tokens por segundo en un portátil de 8 GB (más o menos a la velocidad a la que lees), de 14 a 18 en uno de 16 GB, y de 37 a 76 en la mayoría de PCs gaming con tarjeta gráfica de 6 GB o más.

### ¿Son de verdad las apps 'ChatGPT sin internet' de las tiendas?

Cuidado: las apps que usan el nombre de ChatGPT para funcionar sin conexión no son de OpenAI. Si una funciona sin internet, ejecuta otro modelo en tu dispositivo; mira quién la hace y qué modelo usa.
