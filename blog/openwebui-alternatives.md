# Open WebUI alternatives: 11 options checked, from LibreChat to LM Studio (October 2026)

> LibreChat, Onyx, LobeHub, AnythingLLM, Chatbox, LM Studio, Jan, Msty, text-generation-webui, llama.cpp's own web UI and GreenCube: licence, price, how you install each and whether it needs a separate engine, from their own pages.

Canonical: https://blog.greencube.app/blog/openwebui-alternatives  
Published: 2026-09-15 · Updated: 2026-10-21  
Author: Hector Gras

The best Open WebUI alternative depends on why you're leaving it. For a self-hosted chat page for a team, LibreChat (MIT, Docker) is the closest swap, and Onyx adds search across your company's documents. If it's just you on one computer and you'd rather skip Docker and a separate engine, LM Studio, Jan and text-generation-webui run models themselves, and Msty brings local engines and cloud models together in one desktop app.

I make GreenCube, which is one of the eleven, so I haven't ranked them. Every fact comes from the project's own website, docs, pricing page or licence, read on 21 October 2026 and linked in each row. Where a page doesn't say, we wrote "not stated", and we haven't benchmarked the apps against each other.

## Why people look for an Open WebUI alternative

Open WebUI is a self-hosted chat page you install with pip (Python 3.11) or Docker. It usually sits on top of an engine like Ollama or an OpenAI-compatible API ([docs](https://docs.openwebui.com/getting-started/)). It's a capable tool: it reads documents, can run "entirely offline", and has a desktop app with an optional built-in llama.cpp engine ([GitHub](https://github.com/open-webui/open-webui)).

The first reason people leave is the licence. It's now the "Open WebUI License": BSD-style terms plus a clause that you may not remove or replace the "Open WebUI" branding, unless you have 50 or fewer end users in any rolling 30 days, written permission, or an enterprise licence ([LICENSE](https://github.com/open-webui/open-webui/blob/main/LICENSE)).

The second is setup: a server, Docker or a Python environment, plus a separate engine for the models. The third is fit. Some people want something bigger, with company search and permissions, and others want something smaller, like one app on one PC.

## The 11 alternatives, side by side

| App | What it is | Licence and price | How you install it | Runs models itself? | Your documents |
| --- | --- | --- | --- | --- | --- |
| LibreChat ([GitHub](https://github.com/LibreChat-AI/LibreChat)) | Self-hosted chat page for many AI providers; multi-user login (OAuth2, LDAP, email) and an admin panel | MIT, free | Docker (about 5 minutes, its docs say), npm or Helm; "not a native desktop app" ([docs](https://www.librechat.ai/docs)) | No: connects to cloud APIs or local engines like Ollama and koboldcpp | Yes, chat with files and file search |
| Onyx ([GitHub](https://github.com/onyx-dot-app/onyx)) | AI chat plus search across your team's documents and apps | Community Edition MIT, free; Business $20 per user a month, yearly ([pricing](https://onyx.app/pricing)) | Install script, Docker, Kubernetes; a Lite mode under 1 GB can't index documents | No: connects to Ollama, vLLM and others, or cloud APIs | Yes, its main job; can run fully air-gapped ([site](https://onyx.app)) |
| LobeHub (formerly LobeChat, [GitHub](https://github.com/lobehub/lobehub)) | Agent and chat platform, self-hosted or hosted | LobeHub Community License (Apache 2.0 with extra conditions on derivatives); hosted plans from free ([pricing](https://lobehub.com/pricing)) | Docker, or one-click deploy to cloud hosts | No: connects to AI providers | Not described on the pages we read |
| AnythingLLM ([GitHub](https://github.com/Mintplex-Labs/anything-llm)) | Chat with your documents; desktop app or team server | MIT, desktop free | Desktop installer (Windows, Mac, Linux), or Docker for multiple users | Connects to many providers, local (Ollama, LM Studio) and cloud | Yes: PDF, TXT, DOCX |
| Chatbox ([GitHub](https://github.com/chatboxai/chatbox)) | Desktop and phone chat client for many AI models | Community Edition GPL-3.0; hosted plans Lite $3.99 to Pro+ $39.99 a month ([pricing](https://chatboxai.app/pricing)) | Installer for Windows, Mac, Linux; iPhone and Android apps | No: cloud APIs, its hosted service, or Ollama for local models | Yes, a local knowledge base |
| LM Studio ([site](https://lmstudio.ai)) | Desktop app with chat and a local OpenAI-style server | Free, also for work; closed source | Installer; Windows needs AVX2, Mac needs Apple chip ([requirements](https://lmstudio.ai/docs/app/system-requirements)) | Yes | Yes: PDF, DOCX, TXT |
| Jan ([GitHub](https://github.com/janhq/jan)) | Desktop chat app, plus a local OpenAI-compatible server | Apache 2.0, free | Installer for Windows, Mac, Linux | Yes; optional cloud models | Yes: PDF, Office files |
| Msty ([site](https://msty.ai/products/studio/)) | Desktop app that brings local engines and cloud models together | Free plan; Aurum $149 a year or $349 once ([pricing](https://msty.ai/pricing)); licence not stated | Installer for Windows, Mac, Linux | Uses local engines (MLX, llama.cpp, Ollama) and hosted providers | Yes, Knowledge Stacks |
| text-generation-webui (now "textgen", [GitHub](https://github.com/oobabooga/textgen)) | Local web UI for models, with an OpenAI/Anthropic-compatible API | AGPL-3.0, free | Portable build: unzip and run; or one-click scripts, Conda, Docker | Yes: llama.cpp, ExLlamaV3, Transformers and others | Yes: PDF, DOCX and text attachments |
| llama.cpp server ([GitHub](https://github.com/ggml-org/llama.cpp)) | The engine itself; its server includes a browser chat page | MIT, free | Install script, prebuilt binaries, Docker or build from source | Yes | Not stated |
| GreenCube ([site](https://greencube.app)) | Desktop app for one person: chat, study from PDFs, code, pictures | €9.99 once; closed source | Installer for Windows 10 and 11; no server or Docker | Yes, and picks the model that fits your PC | Yes: PDFs, notes, photos |

Where pages disagreed, we went with the licence file. LobeHub is the example: its README badge says Apache 2.0, but its LICENSE file adds conditions. We re-check these pages every month and update the date at the top.

## Which one fits you?

### A chat page for a team, self-hosted

LibreChat is the closest swap. It has an MIT licence, runs in Docker, comes with multi-user login and an admin panel, and connects to cloud APIs or your own engine. If the main job is answering questions from your company's documents and apps, Onyx is built for that (MIT Community Edition, or $20 per user a month on the Business plan). AnythingLLM's Docker version is a good fit if document chat is what you need most, and LobeHub suits people who want agents and don't mind its licence conditions.

### Just you, on one computer, no Docker

LM Studio and Jan install like normal apps and run the models themselves, and both can serve a local OpenAI-style API for other tools. Msty mixes local engines and cloud models. GreenCube, the one I make, is for Windows: it picks and downloads the model that fits your PC, reads PDFs and photos and makes pictures, for €9.99 once.

### You like tinkering and want full control

text-generation-webui supports several back ends (llama.cpp, ExLlamaV3, Transformers) and says it runs with "zero telemetry". llama.cpp's own server gives you a browser chat page with nothing else on top. KoboldCpp, a single .exe built on llama.cpp, is another option ([GitHub](https://github.com/LostRuins/koboldcpp)).

### You want the same chat on your phone

Chatbox has desktop and phone apps and can use Ollama for local models. It's also worth knowing that Open WebUI itself can be added to a phone's home screen as a web app, so this alone may not be a reason to switch.

## How fast are local models on a normal PC?

Whichever interface you choose, the speed comes from your hardware, because the model runs on your graphics card or processor. We measured GreenCube on 10 real PCs; we haven't measured the other apps on the same machines.

| Your PC | Writes |
| --- | --- |
| 8 GB laptop, no graphics card | **5–7** tokens/s, about reading speed |
| 16 GB laptop, no graphics card | **14–18** tokens/s |
| Gaming PC with a 6 GB+ card | **37–76** tokens/s on most cards |

Each card's numbers are in [Can my PC run AI?](https://blog.greencube.app/blog/can-my-pc-run-ai#checker) If you care most about privacy and what each desktop app sends online, [our comparison of 12 offline AI chatbots](https://blog.greencube.app/blog/best-offline-ai-chatbot) covers that.

## FAQ

### What is the best Open WebUI alternative?

It depends why you're leaving. For a self-hosted team chat page: LibreChat (MIT, Docker); for searching company documents: Onyx; for one person on one computer with no Docker: LM Studio, Jan, Msty or text-generation-webui, which run the models themselves. GreenCube (Windows, €9.99 once) picks the model for your PC by itself.

### Is Open WebUI still open source?

Not under a standard licence anymore. It now uses the "Open WebUI License": BSD-style terms plus a ban on removing or replacing its branding, unless you have 50 or fewer users in a rolling 30 days, written permission or an enterprise licence. Code released earlier keeps its old licence.

### Is there an Open WebUI alternative without Docker?

Yes. LM Studio, Jan, Msty, Chatbox and GreenCube install like normal apps, text-generation-webui has portable builds you unzip and run, and llama.cpp's server has its own web chat page.

### Which Open WebUI alternatives run models themselves?

LM Studio, Jan, text-generation-webui, llama.cpp and GreenCube, with no separate engine needed. LibreChat, Onyx, LobeHub and Chatbox connect to one, like Ollama, or to cloud APIs.

### Which alternative is best for a team?

LibreChat (MIT): multi-user login with OAuth2, LDAP and email, plus an admin panel. Onyx adds search across your company's documents (Business plan $20 per user a month), and AnythingLLM's Docker version also handles multiple users.
