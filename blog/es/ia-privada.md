# IA privada: 10 asistentes comprobados (2026)

> ¿Qué IA es la más privada? Comprobamos ChatGPT, Gemini, Claude, Copilot, Perplexity, NotebookLM, Mistral, DeepSeek, Meta AI y una IA local: quién entrena con tus chats por defecto, quién los guarda, quién puede leerlos, y la única opción en la que nada sale de tu PC.

Canonical: https://blog.greencube.app/blog/es/ia-privada  
Published: 2026-10-23  
Author: Hector Gras

La IA más privada es la que funciona en tu propio ordenador. Tus chats no llegan nunca al servidor de nadie, así que no hay nada con lo que una empresa pueda entrenar, que pueda guardar o que puedan revisar personas. Entre los asistentes en la nube, 5 de los 9 que comprobamos entrenan con tus chats por defecto en una cuenta personal gratis. Desactivarlo ayuda, pero tus chats siguen viajando a la empresa.

Yo hago GreenCube, uno de los asistentes que funcionan en tu PC, así que ten eso en cuenta con mis opiniones. Los datos sobre los demás salen de las páginas de ayuda y de privacidad de cada empresa, enlazadas en la tabla.

## Tres niveles de "privado"

"Privado" puede significar tres cosas bastante distintas. El nivel más flojo es un asistente que no entrena con tus chats. Está bien, pero los chats siguen guardados en los servidores de la empresa, y allí alguien puede leer algunos.

El siguiente es uno que no guarda tus chats, y eso es más raro de lo que parece. Incluso los modos "temporales" conservan las conversaciones un tiempo para controlar abusos: ChatGPT borra los chats temporales a los 30 días.

El más fuerte es un asistente cuyos chats no salen nunca de tu PC. Eso solo es posible cuando la propia IA funciona en tu ordenador, y entonces no hay nada con lo que entrenar, nada que guardar y nadie que lo lea.

## Los 10 asistentes, comprobados

Para una cuenta gratis, personal y de adulto. Las reglas de entrenamiento se comprobaron el 18 de octubre de 2026, y la retención de los chats temporales otra vez el 23 de octubre de 2026.

| Asistente | ¿Entrena con tus chats? | Qué más hay que saber | Tus chats van a |
| --- | --- | --- | --- |
| ChatGPT | **Sí, por defecto**; desactiva "Improve the model for everyone" | Un pulgar arriba o abajo puede seguir enviando el chat entero a entrenamiento; los chats temporales no se usan y se borran a los 30 días ([OpenAI](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance)) | Servidores de OpenAI |
| Gemini | **Sí, mientras "Keep Activity" esté activado** | Los chats revisados por personas se guardan hasta 3 años, aunque borres la actividad ([Google](https://support.google.com/gemini/answer/13594961?hl=en)) | Servidores de Google |
| Claude | **Solo si lo permites** | Si lo permites, los chats se guardan hasta 5 años ([Anthropic](https://www.anthropic.com/news/updates-to-our-consumer-terms)) | Servidores de Anthropic |
| NotebookLM | **No**, salvo que envíes valoraciones | Con valoraciones, lo que subes puede revisarse y guardarse hasta 3 años ([Google](https://support.google.com/notebooklm/answer/17004255?hl=en)) | Servidores de Google |
| Microsoft Copilot (app nueva) | **No lo dice** | La exclusión solo está descrita para la app antigua ([Microsoft](https://support.microsoft.com/en-us/privacy/microsoft-copilot/overview)) | Servidores de Microsoft |
| Perplexity | **Sí, por defecto** | Desactivar "AI data retention" no borra los datos anteriores ([Perplexity](https://www.perplexity.ai/help-center/en/articles/11564572-data-collection-at-perplexity)) | Servidores de Perplexity |
| Mistral Le Chat | **Sí, por defecto** | Las valoraciones se usan elijas lo que elijas ([Mistral](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training)) | Servidores de Mistral |
| DeepSeek | **Sí, por defecto** (anonimizado) | Desactiva "Improve the model for everyone" ([DeepSeek](https://cdn.deepseek.com/policies/en-US/deepseek-terms-of-use.html)) | Servidores de DeepSeek |
| Meta AI | **Sí** | En la UE puedes oponerte con el formulario de Meta ([Meta](https://about.fb.com/news/2025/04/making-ai-work-harder-for-europeans/)) | Servidores de Meta |
| GreenCube (en tu PC) | **No** | "Nunca recibimos tus chats, archivos, recuerdos ni imágenes"; la búsqueda Online, apagada en cada arranque, envía términos de búsqueda ([privacidad](https://legal.greencube.app/privacy)) | A ningún sitio, se queda en tu PC |

Cada fila con más detalle, y cómo desactivar cada cosa, está en [qué IA no entrena con tus chats](https://blog.greencube.app/blog/ai-that-doesnt-train-on-your-data). Cuando una página no responde a la pregunta, como pasa con la app nueva de Copilot de Microsoft, hemos puesto "no lo dice". Las políticas cambian a menudo, así que lo volvemos a comprobar cada mes.

## Cómo dejar un asistente en la nube lo más privado posible

Desactiva el entrenamiento antes de pegar nada delicado, no después, porque lo que ya se ha usado, usado queda. Y no valores los chats delicados: un pulgar arriba o abajo puede mandar la conversación entera a revisión, aunque tengas el entrenamiento desactivado.

Si hay un modo temporal o incógnito, úsalo, sabiendo que el chat se sigue guardando un tiempo. Si tienes una cuenta del centro de estudios o del trabajo, usa esa, porque normalmente quedan fuera del entrenamiento por defecto.

## Un asistente de IA privado en tu propio PC

Una IA que funciona en local es un archivo en tu ordenador. Tus preguntas las responde tu propia tarjeta gráfica o tu procesador, sin ninguna empresa en medio. Lo que pierdes es velocidad, que depende de tu PC. Medimos GreenCube en 10 PCs reales:

| Tu PC | Escribe |
| --- | --- |
| Portátil de 8 GB, sin tarjeta gráfica | **5–7** tokens/s, más o menos a la velocidad a la que lees |
| Portátil de 16 GB, sin tarjeta gráfica | **14–18** tokens/s |
| PC gaming con tarjeta de 6 GB o más | **37–76** tokens/s en la mayoría de tarjetas |

Si la quieres gratis, LM Studio, Jan, Ollama y GPT4All funcionan en local y no cuestan nada, aunque el modelo lo eliges y lo descargas tú ([12 apps de IA sin internet comparadas](https://blog.greencube.app/blog/best-offline-ai-chatbot)). GreenCube es la que hago yo para quien prefiere saltarse ese paso: es para Windows, cuesta 9,99 € una vez, elige el modelo que encaja con tu PC, lee PDF y fotos y crea imágenes.

Para un equipo, una página de chat alojada en vuestro propio servidor mantiene los chats en casa; [Open WebUI y sus alternativas](https://blog.greencube.app/blog/openwebui-alternatives) trata esas opciones.

Instales lo que instales, hay una prueba fácil. Apaga el wifi y pregúntale algo. Si sigue respondiendo, la IA está de verdad en tu PC ([más sobre cómo comprobarlo en Windows](https://blog.greencube.app/blog/local-ai-chatbot-windows)).

## FAQ

### ¿Cuál es la IA más privada?

Una que funciona en tu propio ordenador, porque tus chats no llegan nunca a un servidor de ninguna empresa. GreenCube, LM Studio, Jan y GPT4All funcionan así. Entre las de la nube, NotebookLM dice que no entrena con lo que subes salvo que envíes valoraciones, y Claude solo entrena si lo permites, pero tus chats siguen yendo a sus servidores.

### ¿Qué IAs entrenan con tus chats por defecto?

De los 9 asistentes en la nube que comprobamos para una cuenta personal gratis en octubre de 2026, 5 entrenan con lo que escribes por defecto: ChatGPT, Perplexity, Mistral Le Chat, DeepSeek y Meta AI. Gemini entrena mientras "Keep Activity" esté activado; Claude, solo si lo permites.

### ¿Es privada una IA si desactivo el entrenamiento?

No del todo. Las valoraciones que envías pueden seguir usándose, algunos servicios guardan chats para revisión humana (Gemini guarda los chats revisados hasta 3 años) y los datos ya usados no se borran. Desactivarlo solo cubre lo que envías a partir de entonces.

### ¿Hay una IA privada gratis?

Sí: LM Studio, Jan, Ollama y GPT4All son gratis y ejecutan la IA en tu propio PC, así que no se envía nada; eliges y descargas tú el modelo. GreenCube cuesta 9,99 € una vez y elige el modelo por ti.

### ¿Una IA privada funciona sin internet?

Sí, si funciona en local. Tras la primera descarga, GreenCube y las demás apps locales responden con el wifi apagado. Las IAs en la nube no funcionan sin internet.
