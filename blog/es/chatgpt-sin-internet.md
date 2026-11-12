# ¿ChatGPT sin internet? La IA que funciona sin conexión (2026)

> ChatGPT necesita internet. Así puedes tener una IA que funciona con el Wi-Fi apagado: gpt-oss-20b, el modelo abierto de OpenAI, o una app de IA local. Qué necesita tu PC y velocidades medidas.

Canonical: https://blog.greencube.app/blog/es/chatgpt-sin-internet  
Published: 2026-10-23  
Author: Hector Gras

No, ChatGPT no funciona sin internet. Cada mensaje que escribes viaja a los servidores de OpenAI y la respuesta vuelve desde allí, así que sin conexión la app no tiene con qué contestarte. Pasa lo mismo con la web, la app del móvil y las apps de Windows y Mac.

Lo que sí funciona sin conexión es una IA que vive en tu propio ordenador. La descargas una vez y a partir de ahí puedes apagar el wifi y seguir. Yo hago una de estas apps, GreenCube, así que ten eso en cuenta al leer mi opinión. Más abajo están también las opciones gratuitas y lo que necesita tu PC para usar cualquiera de ellas.

## Por qué ChatGPT no puede funcionar sin internet

Las apps de ChatGPT son una ventana a los centros de datos de OpenAI, no una copia del modelo. El modelo es demasiado grande para un portátil, así que se queda en sus máquinas y tu dispositivo solo envía y recibe texto.

Un aviso: las tiendas de apps están llenas de aplicaciones con "ChatGPT" y "sin internet" en el nombre. Ninguna es de OpenAI. Si alguna funciona de verdad sin conexión, está ejecutando otro modelo, más pequeño, en tu móvil o tu PC, y conviene mirar quién la ha hecho.

## Qué puedes usar en su lugar

### El modelo abierto de OpenAI, gpt-oss-20b

En agosto de 2025 OpenAI publicó gpt-oss, dos modelos que cualquiera puede descargar con licencia Apache 2.0. El pequeño, gpt-oss-20b, funciona en un ordenador con unos 16 GB de memoria ([anuncio de OpenAI](https://openai.com/index/introducing-gpt-oss/)). Se usa con una app como [Ollama o LM Studio](https://blog.greencube.app/blog/ollama-vs-lm-studio). Lo hace OpenAI, pero no es ChatGPT: no busca en la web ni conoce tu cuenta. Todavía no lo hemos cronometrado en nuestros PCs.

### Una app de IA local gratuita

**LM Studio**, **Jan**, **Ollama** y **[GPT4All](https://blog.greencube.app/blog/gpt4all-alternatives)** son gratis. Eliges un modelo de una lista larga, lo descargas y hablas con él, con el wifi apagado si quieres. Están muy bien si te gusta probar modelos y ajustes. Si no sabes qué significa "Q4_K_M", cuenta con tener que leer un poco antes. Hay una lista más larga en [12 apps de IA sin internet comparadas](https://blog.greencube.app/blog/best-offline-ai-chatbot).

### GreenCube

GreenCube es la app que hago yo, pensada para quien quiere el resultado sin la configuración. La instalas, revisa tu PC y elige el modelo que le va bien: Cube 2B en portátiles más modestos y Cube 4B en PCs con tarjeta gráfica, los dos basados en Gemma de Google. Después funciona sin conexión. Además de chatear, hace presentaciones, tarjetas de estudio, tests e imágenes, y lee tus PDF y fotos, todo en tu ordenador. Es para Windows y cuesta 9,99 € una sola vez. Inicias sesión una vez para activarla, y el primer arranque descarga el modelo.

Una imagen que hizo GreenCube en un portátil de 16 GB con gráficos Intel, en unos 2 minutos y sin internet.

## ¿Funcionará en tu ordenador?

Esta es la velocidad a la que escribe GreenCube en 10 PCs reales que probamos. Leemos en inglés a unos 5 tokens por segundo, así que todo lo que pase de ahí se nota rápido.

| Tu PC | Escribe | Se nota como |
| --- | --- | --- |
| Portátil de 8 GB, sin tarjeta gráfica | **5–7** tokens/s | más o menos a la velocidad a la que lees |
| Portátil de 16 GB, sin tarjeta gráfica | **14–18** tokens/s | más rápido de lo que lees |
| PC gaming con tarjeta de 6 GB o más | **37–76** tokens/s en la mayoría de tarjetas | muchas veces más rápido de lo que lees |

Para comprobar tu tarjeta gráfica exacta, prueba [¿Puede mi PC ejecutar IA?](https://blog.greencube.app/blog/can-my-pc-run-ai#checker) Para los detalles de Windows, mira [qué necesita tu PC para usar IA sin internet](https://blog.greencube.app/blog/local-ai-chatbot-windows).

## Lo que pierdes

Una IA en tu portátil es más pequeña que la que hay detrás de ChatGPT, y se nota en los problemas más difíciles: cadenas largas de matemáticas, código enrevesado, datos muy de nicho. Tampoco sabe las noticias de hoy, solo lo que aprendió antes de salir.

Lo que ganas a cambio: funciona en un avión, no tiene topes diarios de archivos ni de imágenes ([los límites gratuitos de ChatGPT](https://blog.greencube.app/blog/chatgpt-free-limits)) y tus chats se guardan en tu ordenador, no en el servidor de otro.

|  | ChatGPT | IA en tu PC |
| --- | --- | --- |
| Funciona sin internet | No | Sí, tras una descarga |
| Problemas más difíciles | Más fuerte | Buena para estudiar, escribir y dudas del día a día |
| Noticias de hoy | Sí, con búsqueda | No |
| Dónde se guardan tus chats | En los servidores de OpenAI | En tu PC |
| Precio | Gratis, o 20 $ al mes con Plus | Apps gratis, o GreenCube 9,99 € una vez |

Mucha gente usa las dos: ChatGPT cuando tiene conexión y necesita el modelo más potente, y una IA sin internet en el tren, en una biblioteca con mal wifi o para apuntes que prefiere guardarse para sí.

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
