# IA privada: 10 asistentes comprobados (2026)

> ¿Qué IA es la más privada? Comprobamos ChatGPT, Gemini, Claude, Copilot, Perplexity, NotebookLM, Mistral, DeepSeek, Meta AI y una IA local: quién entrena con tus chats por defecto, quién los guarda, quién puede leerlos, y la única opción en la que nada sale de tu PC.

Canonical: https://blog.greencube.app/blog/es/ia-privada  
Published: 2026-10-23  
Author: Hector Gras

**Respuesta corta:** la IA más privada es **la que funciona en tu propio ordenador**, porque tus chats no llegan al servidor de nadie: no hay nada con lo que entrenar, que guardar ni que revisar. Entre las de la nube, **5 de 9 entrenan con tus chats por defecto** en una cuenta personal gratis; desactivarlo ayuda, pero tus chats siguen viajando a la empresa, y las valoraciones, la revisión humana y los datos antiguos siguen contando.

- **5 de 9** asistentes en la nube entrenan con tus chats por defecto (cuenta personal gratis)
- **3 años** lo que Gemini guarda los chats que ha leído un revisor humano, aunque los borres
- **0** chats que una IA local envía a ningún sitio

## Tres niveles de "privada"

1. **No entrena con tus chats.** Bien, pero tus chats siguen guardados en los servidores de la empresa, y allí puede haber gente que lea algunos.
2. **No guarda tus chats.** Más raro: incluso los modos "temporales" los guardan un tiempo para controlar abusos (los chats temporales de ChatGPT se borran a los 30 días).
3. **Tus chats no salen de tu PC.** Solo es posible cuando la propia IA funciona en tu ordenador. Nada con lo que entrenar, nada que guardar, nadie que lo lea.

## Los 10 asistentes, comprobados

Según las páginas de ayuda y privacidad de cada empresa, para una cuenta personal gratis de un adulto. Reglas de entrenamiento comprobadas el 18 de octubre de 2026; la retención de los chats temporales de ChatGPT, el 23 de octubre de 2026.

| Asistente | ¿Entrena con tus chats? | Qué más conviene saber | Tus chats van a |
| --- | --- | --- | --- |
| **ChatGPT** | **Sí, por defecto**; desactiva "Improve the model for everyone" | Un pulgar arriba o abajo puede enviar el chat entero a entrenamiento; los chats temporales no se usan y se borran a los 30 días ([OpenAI](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance)) | Servidores de OpenAI |
| **Gemini** | **Sí, mientras "Keep Activity" esté activado** | Los chats revisados por personas se guardan hasta 3 años, aunque borres la actividad ([Google](https://support.google.com/gemini/answer/13594961?hl=es)) | Servidores de Google |
| **Claude** | **Solo si lo permites** | Si lo permites, los chats se guardan hasta 5 años ([Anthropic](https://www.anthropic.com/news/updates-to-our-consumer-terms)) | Servidores de Anthropic |
| **NotebookLM** | **No**, salvo que envíes valoraciones | Con valoraciones, lo que subes puede revisarse y guardarse hasta 3 años ([Google](https://support.google.com/notebooklm/answer/17004255?hl=es)) | Servidores de Google |
| **Microsoft Copilot** (app nueva) | **No lo dice** | La exclusión solo está descrita para la app antigua ([Microsoft](https://support.microsoft.com/es-es/privacy/microsoft-copilot/overview)) | Servidores de Microsoft |
| **Perplexity** | **Sí, por defecto** | Desactivar "AI data retention" no borra los datos anteriores ([Perplexity](https://www.perplexity.ai/help-center/en/articles/11564572-data-collection-at-perplexity)) | Servidores de Perplexity |
| **Mistral Le Chat** | **Sí, por defecto** | Las valoraciones se usan elijas lo que elijas ([Mistral](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training)) | Servidores de Mistral |
| **DeepSeek** | **Sí, por defecto** (anonimizado) | Desactiva "Improve the model for everyone" ([DeepSeek](https://cdn.deepseek.com/policies/en-US/deepseek-terms-of-use.html)) | Servidores de DeepSeek |
| **Meta AI** | **Sí** | En la UE puedes oponerte con el formulario de Meta ([Meta](https://about.fb.com/news/2025/04/making-ai-work-harder-for-europeans/)) | Servidores de Meta |
| **GreenCube** (en tu PC) | **No** | "Nunca recibimos tus chats, archivos, recuerdos ni imágenes"; la búsqueda online, apagada al empezar, envía términos de búsqueda ([privacidad](https://legal.greencube.app/privacy)) | **A ningún sitio: tu PC** |

Cada fila en detalle, con cómo desactivarlo en cada una: [qué IA no entrena con tus datos](https://blog.greencube.app/blog/es/ia-que-no-entrena-con-tus-datos).

## Cómo hacer lo más privada posible una IA en la nube

- **Desactiva el entrenamiento antes de pegar nada delicado**, no después: lo que ya se usó, usado queda.
- **No valores los chats delicados.** Un pulgar arriba o abajo puede enviar la conversación entera a revisión, aunque tengas el entrenamiento desactivado.
- **Usa el modo temporal o incógnito** si lo hay, sabiendo que igualmente se guarda un tiempo.
- **Usa la cuenta de tu universidad o tu trabajo** si tienes: normalmente quedan fuera del entrenamiento por defecto.

## Una IA privada en tu propio PC

Una IA que funciona en local es un archivo en tu ordenador: responde tu propia tarjeta gráfica o tu procesador, así que no hay ninguna empresa en medio. El precio es la velocidad, que depende de tu PC. Medimos GreenCube en 10 PCs reales:

| Tu PC | Escribe |
| --- | --- |
| Portátil de 8 GB, sin tarjeta gráfica | **5–7** tokens/s, más o menos a la velocidad a la que lees |
| Portátil de 16 GB, sin tarjeta gráfica | **14–18** tokens/s |
| PC gaming con tarjeta de 6 GB o más | **37–76** tokens/s en la mayoría de tarjetas |

#### Gratis y privada

LM Studio, Jan, Ollama y GPT4All funcionan en local y no cuestan nada; eliges tú el modelo. [12 apps de IA sin internet comparadas](https://blog.greencube.app/blog/es/mejor-chatbot-ia-sin-internet).

#### Privada sin configurar nada

GreenCube (Windows, 9,99 € una vez) elige el modelo que encaja con tu PC y además lee PDF y fotos y crea imágenes.

#### Para un equipo

Una página de chat autoalojada en vuestro propio servidor mantiene los chats en casa: [Open WebUI y sus alternativas](https://blog.greencube.app/blog/es/alternativas-a-open-webui).

#### Compruébalo tú

Apaga el wifi y pregúntale algo. Si responde, la IA está en tu PC. [Cómo comprobarlo en Windows](https://blog.greencube.app/blog/es/ia-sin-internet-windows).

## Cómo lo comprobamos

Leímos las páginas de ayuda y privacidad de cada empresa para una cuenta personal gratis de un adulto, no noticias ni reseñas, y enlazamos la página de la que sale cada dato. Cuando una página no responde, como con la app nueva de Copilot, ponemos "no lo dice". Hacemos GreenCube, así que nos ceñimos a datos que cualquiera puede comprobar. Las políticas cambian a menudo; lo volvemos a comprobar cada mes.

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
