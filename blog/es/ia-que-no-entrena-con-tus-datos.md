# ¿Qué IA no entrena con tus chats? Lo comprobamos en 9 (octubre 2026)

> ¿ChatGPT, Gemini, Claude, Copilot, Perplexity, NotebookLM, Mistral, DeepSeek o Meta AI entrenan con lo que escribes? Lo que dicen sus propias páginas de ayuda, cómo desactivarlo y lo que ese ajuste no cubre.

Canonical: https://blog.greencube.app/blog/es/ia-que-no-entrena-con-tus-datos  
Published: 2026-10-18  
Author: Hector Gras

Casi todas, salvo que lo desactives. De 9 IAs populares que comprobamos, 5 entrenan con lo que escribes por defecto en una cuenta personal gratuita: ChatGPT, Perplexity, Mistral, DeepSeek y Meta AI. Gemini y Claude dependen de un ajuste, NotebookLM dice que no lo hace salvo que envíes comentarios, y la nueva app de Copilot de Microsoft no lo dice.

Merece la pena desactivar el entrenamiento, pero eso no hace privado un chat, por motivos que explico más abajo. Yo hago GreenCube, una IA que funciona en tu propio PC, así que ten eso en cuenta al leer mi opinión. Todo lo que digo de los demás servicios sale de sus propias páginas de ayuda, enlazadas en la tabla.

## Qué dice cada una (comprobado el 18 de octubre de 2026)

Leímos las páginas de ayuda de cada empresa para una cuenta personal gratuita. Las cuentas de trabajo y de centros educativos suelen tener normas más estrictas: en la mayoría de estos servicios quedan fuera del entrenamiento por defecto. Las políticas cambian a menudo, así que lo volvemos a comprobar cada mes.

| IA | ¿Entrena con tus chats? | Cómo desactivarlo | Lo que el ajuste no cubre |
| --- | --- | --- | --- |
| **ChatGPT** (Free, Go, Plus, Pro) | **Sí, por defecto** | Configuración → Controles de datos → desactiva "Mejorar el modelo para todos". Los chats temporales no se usan. | Los pulgares arriba o abajo: puede usarse la conversación entera. [OpenAI](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance) |
| **Gemini** | **Sí, mientras "Actividad" esté activada** | Desactiva la opción de guardar actividad. Los chats nuevos no se usan para entrenar, aunque se guardan 72 horas. | Los chats que ha leído un revisor humano se guardan hasta 3 años, aunque borres tu actividad. [Google](https://support.google.com/gemini/answer/13594961?hl=en) |
| **Claude** (Free, Pro, Max) | **Solo si lo permites** (lo eliges al registrarte) | Ajustes de privacidad → desactiva la mejora del modelo. | Si lo permites, los chats se guardan hasta 5 años; desactivarlo después no borra lo que ya se usó. [Anthropic](https://www.anthropic.com/news/updates-to-our-consumer-terms) |
| **NotebookLM** (Gemini Notebook) | **No**, salvo que envíes comentarios | No hay nada que desactivar. No uses los pulgares con apuntes sensibles. | Con comentarios, lo que subes y preguntas puede revisarse y guardarse hasta 3 años. [Google](https://support.google.com/notebooklm/answer/17004255?hl=en) |
| **Microsoft Copilot** (app nueva desde el 18 de agosto de 2026) | **No lo dice** para la app nueva | Microsoft solo describe la opción de no entrenar para la app antigua. Los controles de privacidad de la nueva no incluyen ningún ajuste de entrenamiento. | Revisa los ajustes de la propia app. [Microsoft](https://support.microsoft.com/en-us/privacy/microsoft-copilot/overview) |
| **Perplexity** (Free, Pro, Max) | **Sí, por defecto** | Ajustes → Preferencias → desactiva "AI data retention". | Solo afecta a los datos desde ese momento; lo anterior no se borra. [Perplexity](https://www.perplexity.ai/help-center/en/articles/11564572-data-collection-at-perplexity) |
| **Mistral Le Chat** (gratis) | **Sí, por defecto** | Ajustes → Privacidad → desactiva "Allow your interactions to be used to train our models". | Los pulgares arriba o abajo se usan elijas lo que elijas. [Mistral](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training) |
| **DeepSeek** | **Sí, por defecto** (anonimizado) | Desactiva "Improve the model for everyone". | [DeepSeek](https://cdn.deepseek.com/policies/en-US/deepseek-terms-of-use.html) |
| **Meta AI** | **Sí**, se usan tus preguntas a Meta AI | En la UE, oponte con el formulario de Meta (desde la app o el correo que te envió Meta). | La oposición cubre la cuenta con la que has iniciado sesión y las demás del mismo Centro de cuentas. [Meta](https://about.fb.com/news/2025/04/making-ai-work-harder-for-europeans/) |
| **GreenCube** (funciona en tu PC) | **No**, tus chats nunca nos llegan | No hay nada que desactivar. | La búsqueda Online, que empieza apagada cada vez, envía términos de búsqueda a buscadores. [GreenCube](https://legal.greencube.app/privacy) |

## Lo que no hace "desactivar el entrenamiento"

El ajuste cubre una sola cosa: si lo que escribas a partir de ahora entra en el entrenamiento. Hay tres cosas que se le escapan.

La primera son los comentarios. Pulsar el pulgar arriba o abajo suele enviar la conversación entera a revisión, incluso con el entrenamiento desactivado. OpenAI, Mistral y Google (para NotebookLM y Gemini) lo dicen. Si un chat contiene algo sensible, no lo valores.

La segunda es la revisión humana. Gemini usa revisores humanos mientras la actividad está activada, y guarda los chats que han leído hasta 3 años, desvinculados de tu cuenta, aunque borres tu actividad.

La tercera es lo que ya se ha usado. Anthropic y Perplexity dicen que los datos que ya están en el entrenamiento no se borran cuando lo desactivas. Así que, si vas a desactivarlo, hazlo antes de pegar tus apuntes, no después.

## La única forma de que lo que escribes se quede en tu ordenador

Todos los servicios de arriba ejecutan la IA en sus propios servidores, así que lo que escribes tiene que viajar hasta allí, diga lo que diga el ajuste de entrenamiento. Una IA que funciona en tu propio ordenador va al revés. El modelo es un archivo en tu PC, tus chats y documentos se guardan ahí, y ningún servidor de ninguna empresa los tiene.

Así funciona GreenCube, y su política de privacidad lo dice sin rodeos: "Nunca recibimos tus chats, archivos, recuerdos ni imágenes". Las excepciones, para ser honestos, son que inicias sesión una vez para activarlo, que descarga la IA y sus actualizaciones, y que si activas la búsqueda Online para algo actual, envía a los buscadores términos de búsqueda sacados de tu pregunta. Online empieza apagado cada vez que abres la app.

La contrapartida es que el trabajo lo hace tu ordenador. En los PCs que medimos, escribe más o menos a tu ritmo de lectura en un portátil de 8 GB y muchas veces más rápido en un PC gaming. Puedes [comprobar qué puede ejecutar el tuyo](https://blog.greencube.app/blog/can-my-pc-run-ai#checker).

## Cómo lo comprobamos

El 18 de octubre de 2026 leímos el centro de ayuda y las páginas de privacidad de cada empresa para una cuenta gratuita, personal y de adulto, no artículos de prensa ni reseñas, y enlazamos la página de la que sale cada fila. Donde las páginas actuales de una empresa no responden a la pregunta, como pasa con la nueva app de Copilot de Microsoft, lo decimos en vez de adivinar. Lo volveremos a comprobar cada mes y actualizaremos la fecha de arriba.

## FAQ

### ¿ChatGPT entrena con mis chats?

En Free, Go, Plus y Pro, sí por defecto. Puedes desactivar "Mejorar el modelo para todos" en Configuración, Controles de datos. Si das un pulgar arriba o abajo, OpenAI puede usar igualmente esa conversación entera.

### ¿Qué IA no usa mis datos para entrenar?

De las 9 que comprobamos, NotebookLM dice que no entrena con lo que subes salvo que envíes comentarios, y Claude solo lo hace si lo permites. Una IA que funciona en tu propio ordenador, como GreenCube, nunca envía tus chats a nadie para entrenar.

### ¿Desactivar el entrenamiento hace que una IA sea privada?

No del todo. Los comentarios que des se pueden seguir usando, algunas empresas guardan chats para revisión humana (Gemini guarda hasta 3 años los chats revisados) y lo que ya se usó para entrenar no se borra.

### ¿Hay alguna IA que guarde mis chats en mi ordenador?

Sí: una IA que funciona en local, como GreenCube, guarda los chats y archivos en tu PC. Aparte de iniciar sesión una vez y descargar la IA y sus actualizaciones, su única parte online es una búsqueda web opcional que envía términos de búsqueda, y empieza apagada cada vez.
