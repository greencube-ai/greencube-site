# Alternativas a Open WebUI: 11 opciones comprobadas, de LibreChat a LM Studio (octubre 2026)

> LibreChat, Onyx, LobeHub, AnythingLLM, Chatbox, LM Studio, Jan, Msty, text-generation-webui, la web propia de llama.cpp y GreenCube: licencia, precio, cómo se instala cada una y si necesita un motor aparte, según sus propias páginas.

Canonical: https://blog.greencube.app/blog/es/alternativas-a-open-webui  
Published: 2026-10-21  
Author: Hector Gras

La mejor alternativa a Open WebUI depende de por qué la dejas. Para una página de chat autoalojada para un equipo, LibreChat (MIT, Docker) es el cambio más directo, y Onyx añade búsqueda en los documentos de tu empresa. Si eres tú solo en un ordenador y prefieres ahorrarte Docker y un motor aparte, LM Studio, Jan y text-generation-webui ejecutan los modelos ellas mismas, y Msty junta motores locales y modelos en la nube en una sola app de escritorio.

Yo hago GreenCube, que es una de las once, así que no las he ordenado de mejor a peor. Cada dato sale de la web, la documentación, la página de precios o la licencia del propio proyecto, leídas el 21 de octubre de 2026 y enlazadas en cada fila. Cuando una página no dice algo, hemos puesto "no lo dice", y no hemos comparado el rendimiento de las apps entre sí.

## Por qué la gente busca una alternativa a Open WebUI

Open WebUI es una página de chat autoalojada que se instala con pip (Python 3.11) o Docker. Normalmente va encima de un motor como Ollama o de una API compatible con OpenAI ([documentación](https://docs.openwebui.com/getting-started/)). Es una herramienta capaz: lee documentos, puede funcionar "totalmente sin conexión" y tiene una app de escritorio con un motor llama.cpp integrado opcional ([GitHub](https://github.com/open-webui/open-webui)).

El primer motivo para dejarla es la licencia. Ahora es la "Open WebUI License": términos de estilo BSD más una cláusula que prohíbe quitar o sustituir la marca "Open WebUI", salvo que tengas 50 usuarios finales o menos en cualquier periodo móvil de 30 días, permiso por escrito o una licencia enterprise ([LICENSE](https://github.com/open-webui/open-webui/blob/main/LICENSE)).

El segundo es la instalación: un servidor, Docker o un entorno de Python, más un motor aparte para los modelos. El tercero es el encaje. Hay quien quiere algo más grande, con búsqueda en la empresa y permisos, y hay quien quiere algo más pequeño, como una sola app en un solo PC.

## Las 11 alternativas, una al lado de otra

| App | Qué es | Licencia y precio | Cómo se instala | ¿Ejecuta los modelos ella misma? | Tus documentos |
| --- | --- | --- | --- | --- | --- |
| LibreChat ([GitHub](https://github.com/LibreChat-AI/LibreChat)) | Página de chat autoalojada para muchos proveedores de IA; inicio de sesión multiusuario (OAuth2, LDAP, email) y panel de administración | MIT, gratis | Docker (unos 5 minutos, según su documentación), npm o Helm; "no es una app de escritorio nativa" ([documentación](https://www.librechat.ai/docs)) | No: se conecta a APIs en la nube o a motores locales como Ollama y koboldcpp | Sí, chat con archivos y búsqueda en archivos |
| Onyx ([GitHub](https://github.com/onyx-dot-app/onyx)) | Chat con IA más búsqueda en los documentos y apps de tu equipo | Community Edition MIT, gratis; Business 20 $ por usuario al mes, pago anual ([precios](https://onyx.app/pricing)) | Script de instalación, Docker, Kubernetes; un modo Lite de menos de 1 GB no puede indexar documentos | No: se conecta a Ollama, vLLM y otros, o a APIs en la nube | Sí, es su función principal; puede funcionar totalmente aislado de la red ([web](https://onyx.app)) |
| LobeHub (antes LobeChat, [GitHub](https://github.com/lobehub/lobehub)) | Plataforma de agentes y chat, autoalojada o alojada por ellos | LobeHub Community License (Apache 2.0 con condiciones extra para derivados); planes alojados desde gratis ([precios](https://lobehub.com/pricing)) | Docker, o despliegue con un clic en servicios en la nube | No: se conecta a proveedores de IA | No lo describen las páginas que leímos |
| AnythingLLM ([GitHub](https://github.com/Mintplex-Labs/anything-llm)) | Chat con tus documentos; app de escritorio o servidor para equipos | MIT, escritorio gratis | Instalador de escritorio (Windows, Mac, Linux), o Docker para varios usuarios | Se conecta a muchos proveedores, locales (Ollama, LM Studio) y en la nube | Sí: PDF, TXT, DOCX |
| Chatbox ([GitHub](https://github.com/chatboxai/chatbox)) | Cliente de chat de escritorio y de móvil para muchos modelos de IA | Community Edition GPL-3.0; planes alojados de Lite 3,99 $ a Pro+ 39,99 $ al mes ([precios](https://chatboxai.app/pricing)) | Instalador para Windows, Mac, Linux; apps para iPhone y Android | No: APIs en la nube, su servicio alojado u Ollama para modelos locales | Sí, una base de conocimiento local |
| LM Studio ([web](https://lmstudio.ai)) | App de escritorio con chat y un servidor local al estilo de OpenAI | Gratis, también para el trabajo; código cerrado | Instalador; en Windows necesita AVX2, en Mac un chip de Apple ([requisitos](https://lmstudio.ai/docs/app/system-requirements)) | Sí | Sí: PDF, DOCX, TXT |
| Jan ([GitHub](https://github.com/janhq/jan)) | App de chat de escritorio, más un servidor local compatible con OpenAI | Apache 2.0, gratis | Instalador para Windows, Mac, Linux | Sí; modelos en la nube opcionales | Sí: PDF, archivos de Office |
| Msty ([web](https://msty.ai/products/studio/)) | App de escritorio que junta motores locales y modelos en la nube | Plan gratuito; Aurum 149 $ al año o 349 $ una vez ([precios](https://msty.ai/pricing)); licencia no indicada | Instalador para Windows, Mac, Linux | Usa motores locales (MLX, llama.cpp, Ollama) y proveedores alojados | Sí, Knowledge Stacks |
| text-generation-webui (ahora "textgen", [GitHub](https://github.com/oobabooga/textgen)) | Interfaz web local para modelos, con una API compatible con OpenAI y Anthropic | AGPL-3.0, gratis | Versión portable: descomprimir y ejecutar; o scripts de un clic, Conda, Docker | Sí: llama.cpp, ExLlamaV3, Transformers y otros | Sí: PDF, DOCX y adjuntos de texto |
| Servidor de llama.cpp ([GitHub](https://github.com/ggml-org/llama.cpp)) | El propio motor; su servidor incluye una página de chat en el navegador | MIT, gratis | Script de instalación, binarios ya compilados, Docker o compilar desde el código | Sí | No lo dice |
| GreenCube ([web](https://greencube.app)) | App de escritorio para una persona: chat, estudiar con PDF, código, imágenes | 9,99 € una vez; código cerrado | Instalador para Windows 10 y 11; sin servidor ni Docker | Sí, y elige el modelo que encaja con tu PC | Sí: PDF, apuntes, fotos |

Cuando las páginas no coincidían, nos quedamos con el archivo de licencia. LobeHub es el ejemplo: la insignia de su README dice Apache 2.0, pero su archivo LICENSE añade condiciones. Volvemos a revisar estas páginas cada mes y actualizamos la fecha de arriba.

## ¿Cuál encaja contigo?

### Una página de chat para un equipo, autoalojada

LibreChat es el cambio más directo. Tiene licencia MIT, funciona en Docker, trae inicio de sesión multiusuario y panel de administración, y se conecta a APIs en la nube o a tu propio motor. Si lo principal es responder preguntas a partir de los documentos y las apps de tu empresa, Onyx está hecho para eso (Community Edition MIT, o 20 $ por usuario al mes en el plan Business). La versión Docker de AnythingLLM encaja bien si lo que más necesitas es chatear con documentos, y LobeHub le va a quien quiere agentes y no le importan las condiciones de su licencia.

### Solo tú, en un ordenador, sin Docker

LM Studio y Jan se instalan como apps normales y ejecutan los modelos ellas mismas, y las dos pueden servir una API local al estilo de OpenAI para otras herramientas. Msty mezcla motores locales y modelos en la nube. GreenCube, la que hago yo, es para Windows: elige y descarga el modelo que encaja con tu PC, lee PDF y fotos y crea imágenes, por 9,99 € una vez.

### Te gusta trastear y quieres control total

text-generation-webui admite varios motores (llama.cpp, ExLlamaV3, Transformers) y dice que funciona con "cero telemetría". El servidor propio de llama.cpp te da una página de chat en el navegador sin nada más encima. KoboldCpp, un solo .exe basado en llama.cpp, es otra opción ([GitHub](https://github.com/LostRuins/koboldcpp)).

### Quieres el mismo chat en el móvil

Chatbox tiene apps de escritorio y de móvil y puede usar Ollama para modelos locales. También conviene saber que el propio Open WebUI se puede añadir a la pantalla de inicio del móvil como app web, así que esto solo puede que no sea motivo para cambiar.

## ¿Qué velocidad tienen los modelos locales en un PC normal?

Elijas la interfaz que elijas, la velocidad la pone tu hardware, porque el modelo funciona en tu tarjeta gráfica o tu procesador. Medimos GreenCube en 10 PCs reales; no hemos medido las demás apps en las mismas máquinas.

| Tu PC | Escribe |
| --- | --- |
| Portátil de 8 GB, sin tarjeta gráfica | **5–7** tokens/s, más o menos a la velocidad a la que lees |
| Portátil de 16 GB, sin tarjeta gráfica | **14–18** tokens/s |
| PC gaming con tarjeta de 6 GB o más | **37–76** tokens/s en la mayoría de tarjetas |

Los números de cada tarjeta están en [¿Puede mi PC ejecutar IA?](https://blog.greencube.app/blog/can-my-pc-run-ai#checker) Si lo que más te importa es la privacidad y qué envía a internet cada app de escritorio, [nuestra comparativa de 12 chatbots de IA sin internet](https://blog.greencube.app/blog/best-offline-ai-chatbot) lo cubre.

## FAQ

### ¿Cuál es la mejor alternativa a Open WebUI?

Depende de por qué la dejas. Para una página de chat autoalojada para un equipo: LibreChat (MIT, Docker). Para buscar en los documentos de tu empresa: Onyx. Para una persona en un ordenador sin Docker: LM Studio, Jan, Msty o text-generation-webui, que ejecutan los modelos ellas mismas. GreenCube (Windows, 9,99 € una vez) elige sola el modelo para tu PC.

### ¿Open WebUI sigue siendo de código abierto?

Su licencia ahora es la "Open WebUI License": términos de estilo BSD más una cláusula que prohíbe quitar o sustituir su marca, salvo que tengas 50 usuarios o menos en un periodo móvil de 30 días, permiso por escrito o una licencia enterprise. El código publicado antes mantiene su licencia original.

### ¿Hay alguna alternativa a Open WebUI sin Docker?

Sí. LM Studio, Jan, Msty, Chatbox y GreenCube se instalan como apps normales; text-generation-webui tiene versiones portables que descomprimes y ejecutas; el servidor de llama.cpp trae su propia página de chat.

### ¿Qué alternativas ejecutan los modelos ellas mismas?

LM Studio, Jan, text-generation-webui, llama.cpp y GreenCube ejecutan modelos sin motor aparte. LibreChat, Onyx, LobeHub y Chatbox se conectan a un motor como Ollama o a APIs en la nube.

### ¿Cuál es mejor para un equipo?

LibreChat (MIT) tiene inicio de sesión multiusuario con OAuth2, LDAP y email, y un panel de administración. Onyx añade búsqueda en los documentos de tu empresa; su plan Business cuesta 20 $ por usuario al mes. La versión Docker de AnythingLLM también admite varios usuarios.
