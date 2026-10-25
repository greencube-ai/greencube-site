# Alternativas a Open WebUI: 11 opciones comprobadas, de LibreChat a LM Studio (octubre 2026)

> LibreChat, Onyx, LobeHub, AnythingLLM, Chatbox, LM Studio, Jan, Msty, text-generation-webui, la web propia de llama.cpp y GreenCube: licencia, precio, cómo se instala cada una y si necesita un motor aparte, según sus propias páginas.

Canonical: https://blog.greencube.app/blog/es/alternativas-a-open-webui  
Published: 2026-10-21  
Author: Hector Gras

**Respuesta corta: depende de por qué dejas Open WebUI.** Para una página de chat autoalojada para un equipo, LibreChat (MIT, Docker) es el cambio más directo; Onyx añade búsqueda en los documentos de tu empresa. Si eres tú solo en un ordenador y no quieres Docker ni un motor aparte, LM Studio, Jan, Msty y text-generation-webui ejecutan los modelos ellas mismas. GreenCube (Windows, 9,99 € una vez) también, y elige el modelo que encaja con tu PC.

- **11** alternativas comprobadas en sus propias páginas, 21 de octubre de 2026
- **50** usuarios: por encima, la licencia de Open WebUI obliga a mantener su marca
- **5** de las 11 ejecutan los modelos ellas mismas, sin motor aparte

## Por qué se busca una alternativa a Open WebUI

Open WebUI es una página de chat autoalojada que se instala con pip (Python 3.11) o Docker, y que normalmente va encima de un motor como Ollama o de una API compatible con OpenAI ([docs](https://docs.openwebui.com/getting-started/)). Es potente: lee documentos, puede funcionar totalmente sin internet y tiene una app de escritorio con un motor llama.cpp integrado opcional ([GitHub](https://github.com/open-webui/open-webui)). Los tres motivos más habituales para buscar otra:

- **La licencia.** Ahora es la "Open WebUI License": términos de estilo BSD más una cláusula que prohíbe quitar o sustituir la marca "Open WebUI", salvo que tengas 50 usuarios finales o menos en cualquier periodo de 30 días, permiso por escrito o una licencia enterprise ([LICENSE](https://github.com/open-webui/open-webui/blob/main/LICENSE)).
- **La instalación.** Un servidor, Docker o un entorno de Python, más un motor aparte para los modelos.
- **El tamaño.** Hay quien quiere algo más grande (búsqueda en la empresa, permisos) y quien quiere algo más pequeño (una app en un PC).

## Las 11 alternativas, una al lado de otra

Cada dato sale de la web, la documentación o la página de GitHub del propio proyecto, enlazada en cada fila, leídas el 21 de octubre de 2026. Cuando una página no lo dice, ponemos "no lo dice". No hemos comparado su rendimiento entre sí.

| App | Qué es | Licencia y precio | Cómo se instala | ¿Ejecuta los modelos ella misma? | Tus documentos |
| --- | --- | --- | --- | --- | --- |
| **LibreChat** ([GitHub](https://github.com/LibreChat-AI/LibreChat)) | Página de chat autoalojada para muchos proveedores de IA; inicio de sesión multiusuario (OAuth2, LDAP, email) y panel de administración | MIT, gratis | Docker (unos 5 minutos, según su documentación), npm o Helm; "no es una app de escritorio nativa" ([docs](https://www.librechat.ai/docs)) | No: se conecta a APIs en la nube o a motores locales como Ollama y koboldcpp | Sí, chat con archivos y búsqueda en archivos |
| **Onyx** ([GitHub](https://github.com/onyx-dot-app/onyx)) | Chat de IA más búsqueda en los documentos y apps de tu equipo | Community Edition MIT, gratis; Business 20 $ por usuario al mes, anual ([precios](https://onyx.app/pricing)) | Script de instalación, Docker, Kubernetes; un modo Lite de menos de 1 GB no indexa documentos | No: se conecta a Ollama, vLLM y otros, o a APIs en la nube | Sí, es su función principal; puede funcionar totalmente aislado de la red ([web](https://onyx.app)) |
| **LobeHub** (antes LobeChat, [GitHub](https://github.com/lobehub/lobehub)) | Plataforma de agentes y chat, autoalojada o alojada | LobeHub Community License (Apache 2.0 con condiciones extra para derivados); planes alojados desde gratis ([precios](https://lobehub.com/pricing)) | Docker, o despliegue en un clic en proveedores en la nube | No: se conecta a proveedores de IA | No lo describen las páginas que leímos |
| **AnythingLLM** ([GitHub](https://github.com/Mintplex-Labs/anything-llm)) | Chat con tus documentos; app de escritorio o servidor para equipos | MIT, escritorio gratis | Instalador de escritorio (Windows, Mac, Linux), o Docker para varios usuarios | Se conecta a muchos proveedores, locales (Ollama, LM Studio) y en la nube | Sí: PDF, TXT, DOCX |
| **Chatbox** ([GitHub](https://github.com/chatboxai/chatbox)) | Cliente de chat de escritorio y móvil para muchos modelos de IA | Community Edition GPL-3.0; planes alojados de Lite 3,99 $ a Pro+ 39,99 $ al mes ([precios](https://chatboxai.app/pricing)) | Instalador para Windows, Mac, Linux; apps para iPhone y Android | No: APIs en la nube, su servicio alojado u Ollama para modelos locales | Sí, una base de conocimiento local |
| **LM Studio** ([web](https://lmstudio.ai)) | App de escritorio con chat y servidor local estilo OpenAI | Gratis, también para el trabajo; código cerrado | Instalador; en Windows necesita AVX2, en Mac chip Apple ([requisitos](https://lmstudio.ai/docs/app/system-requirements)) | Sí | Sí: PDF, DOCX, TXT |
| **Jan** ([GitHub](https://github.com/janhq/jan)) | App de chat de escritorio, más un servidor local compatible con OpenAI | Apache 2.0, gratis | Instalador para Windows, Mac, Linux | Sí; modelos en la nube opcionales | Sí: PDF, archivos de Office |
| **Msty** ([web](https://msty.ai/products/studio/)) | App de escritorio que junta motores locales y modelos en la nube | Plan gratis; Aurum 149 $ al año o 349 $ una vez ([precios](https://msty.ai/pricing)); licencia: no lo dice | Instalador para Windows, Mac, Linux | Usa motores locales (MLX, llama.cpp, Ollama) y proveedores alojados | Sí, Knowledge Stacks |
| **text-generation-webui** (ahora "textgen", [GitHub](https://github.com/oobabooga/textgen)) | Interfaz web local para modelos, con API compatible con OpenAI y Anthropic | AGPL-3.0, gratis | Versión portable: descomprimir y ejecutar; o scripts de un clic, Conda, Docker | Sí: llama.cpp, ExLlamaV3, Transformers y otros | Sí: adjuntos PDF, DOCX y texto |
| **Servidor de llama.cpp** ([GitHub](https://github.com/ggml-org/llama.cpp)) | El propio motor; su servidor incluye una página de chat en el navegador | MIT, gratis | Script de instalación, binarios, Docker o compilar | Sí | No lo dice |
| **GreenCube** ([web](https://greencube.app/es/)) | App de escritorio para una persona: chat, estudiar con PDF, código, imágenes | 9,99 € una vez; código cerrado | Instalador para Windows 10 y 11; sin servidor ni Docker | Sí, y elige el modelo que encaja con tu PC | Sí: PDF, apuntes, fotos |

## ¿Cuál encaja contigo?

### Una página de chat para un equipo, autoalojada

**LibreChat** es el cambio más directo: licencia MIT, Docker, inicio de sesión multiusuario y panel de administración, conectado a APIs en la nube o a tu propio motor. **Onyx** si lo principal es responder con los documentos y apps de tu empresa (Community Edition MIT, o 20 $ por usuario al mes alojado). La versión Docker de **AnythingLLM** si lo que más necesitas es chatear con documentos. **LobeHub** si quieres agentes y te encajan las condiciones de su licencia.

### Solo tú, en un ordenador, sin Docker

**LM Studio** y **Jan** se instalan como apps normales y ejecutan los modelos ellas mismas; las dos pueden servir además una API local estilo OpenAI para otras herramientas. **Msty** mezcla motores locales y modelos en la nube. **GreenCube** (Windows) elige y descarga el modelo que encaja con tu PC, lee PDF y fotos y crea imágenes, por 9,99 € una vez.

### Te gusta trastear y quieres control total

**text-generation-webui** admite varios motores (llama.cpp, ExLlamaV3, Transformers) y dice funcionar con "cero telemetría". El servidor de **llama.cpp** te da una página de chat en el navegador sin nada más encima. KoboldCpp, un solo .exe basado en llama.cpp, es otra opción ([GitHub](https://github.com/LostRuins/koboldcpp)).

### Quieres el mismo chat en el móvil

**Chatbox** tiene apps de escritorio y de móvil y puede usar Ollama para modelos locales. Open WebUI también se puede añadir a la pantalla de inicio del móvil como app web.

## ¿Qué velocidad tienen los modelos locales en un PC normal?

Elijas la interfaz que elijas, la velocidad depende de tu hardware: el modelo se ejecuta en tu tarjeta gráfica o en tu procesador. Medimos GreenCube en 10 PCs reales (las demás apps no las hemos medido en las mismas máquinas):

| Tu PC | Escribe |
| --- | --- |
| Portátil de 8 GB, sin tarjeta gráfica | **5–7** tokens/s, más o menos a velocidad de lectura |
| Portátil de 16 GB, sin tarjeta gráfica | **14–18** tokens/s |
| PC gaming con tarjeta de 6 GB o más | **37–76** tokens/s en la mayoría de tarjetas |

Los números de cada tarjeta están en [¿Puedo usar IA en mi PC?](https://blog.greencube.app/blog/es/ia-en-mi-pc#checker), y los datos en bruto en [cómo medimos](https://blog.greencube.app/blog/es/como-medimos-la-velocidad-de-la-ia). Para apps de escritorio comparadas por privacidad y por lo que sale a internet, mira [nuestra comparativa de 12 chatbots de IA sin internet](https://blog.greencube.app/blog/es/mejor-chatbot-ia-sin-internet).

## Cómo lo comprobamos

El 21 de octubre de 2026 leímos la página de GitHub, la documentación, la página de precios y la licencia de cada proyecto, no reseñas ni otras listas, y enlazamos la página de la que sale cada dato. Cuando las páginas no coincidían (la insignia del README de LobeHub dice Apache 2.0 y su archivo LICENSE añade condiciones) nos quedamos con el archivo de licencia. GreenCube la hacemos nosotros, así que nos hemos ceñido a datos que cualquiera puede comprobar y no hemos puesto las apps en un ranking. Lo revisaremos cada mes y actualizaremos la fecha de arriba.

## FAQ

### ¿Cuál es la mejor alternativa a Open WebUI?

Depende de por qué la dejas. Para una página de chat autoalojada para un equipo: LibreChat (MIT, Docker). Para buscar en los documentos de tu empresa: Onyx. Para una persona en un ordenador sin Docker: LM Studio, Jan, Msty o text-generation-webui, que ejecutan los modelos ellas mismas. GreenCube (Windows, 9,99 € una vez) elige sola el modelo para tu PC.

### ¿Open WebUI sigue siendo de código abierto?

Su licencia ahora es la "Open WebUI License": términos de estilo BSD más una cláusula que prohíbe quitar o sustituir su marca, salvo que tengas 50 usuarios o menos en 30 días, permiso por escrito o una licencia enterprise. El código publicado antes mantiene su licencia original.

### ¿Hay alguna alternativa a Open WebUI sin Docker?

Sí. LM Studio, Jan, Msty, Chatbox y GreenCube se instalan como apps normales; text-generation-webui tiene versiones portables que descomprimes y ejecutas; el servidor de llama.cpp trae su propia página de chat.

### ¿Qué alternativas ejecutan los modelos ellas mismas?

LM Studio, Jan, text-generation-webui, llama.cpp y GreenCube ejecutan modelos sin motor aparte. LibreChat, Onyx, LobeHub y Chatbox se conectan a un motor como Ollama o a APIs en la nube.

### ¿Cuál es mejor para un equipo?

LibreChat (MIT) tiene inicio de sesión multiusuario con OAuth2, LDAP y email, y un panel de administración. Onyx añade búsqueda en los documentos de tu empresa; su plan Business cuesta 20 $ por usuario al mes. La versión Docker de AnythingLLM también admite varios usuarios.
