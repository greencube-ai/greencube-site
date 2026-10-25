# Can you use ChatGPT offline? No, but here's what works without internet (2026)

> ChatGPT has no offline mode: the app and the desktop version need internet, because the model runs on OpenAI's servers. What works offline instead: OpenAI's own open-weight gpt-oss-20b, and local AI apps, with the RAM you need and measured speeds.

Canonical: https://blog.greencube.app/blog/chatgpt-offline  
Published: 2026-10-23  
Author: Hector Gras

**Short answer: no.** ChatGPT runs on OpenAI's servers, so the website, the phone app and the desktop apps all need internet; there's no offline mode. What **does** work offline is an AI model running on your own computer: OpenAI's own open-weight **gpt-oss-20b** (needs about 16 GB of memory), or apps like LM Studio, Jan, Ollama and GreenCube that download a model once and then work with the Wi-Fi off.

- **0** offline modes in ChatGPT: the model runs on OpenAI's servers
- **16 GB** of memory for OpenAI's open-weight gpt-oss-20b
- **8 GB** is enough for a small local model on a laptop (measured)

## Why ChatGPT can't work offline

When you type into ChatGPT, your message travels to OpenAI's data centres, a model there writes the answer, and it travels back. The Windows and Mac apps are a window onto that same service, not a copy of the model. With no connection, there is nothing on your device to answer you.

Watch out for app-store apps that put "ChatGPT" and "offline" in their name: they aren't from OpenAI. If one really works offline, it's running a different model on your phone or PC.

## What works with no internet

### OpenAI's own open-weight model: gpt-oss-20b

In August 2025 OpenAI released gpt-oss, open-weight models under the Apache 2.0 licence. The smaller one, gpt-oss-20b, runs on a computer with about 16 GB of memory ([OpenAI](https://openai.com/index/introducing-gpt-oss/)), through apps like Ollama or LM Studio. It's made by OpenAI, but it isn't ChatGPT: different model, no web search, no memory of your account. We haven't timed it on our PCs.

### A local AI app

Apps that download a model once and run it on your PC: **LM Studio**, **Jan**, **Ollama** and **GPT4All** are free and let you pick the model; **GreenCube** (Windows, €9.99 once) picks the model that fits your PC and also reads PDFs and photos and makes pictures. [12 offline apps compared](https://blog.greencube.app/blog/best-offline-ai-chatbot).

## What you need, and how fast it is

Measured with GreenCube on 10 real PCs (models: Google's Gemma 4 E2B and E4B):

| Your PC | Writes | Feels like |
| --- | --- | --- |
| 8 GB laptop, no graphics card | **5–7** tokens/s | about reading speed |
| 16 GB laptop, no graphics card | **14–18** tokens/s | faster than you read |
| Gaming PC with a 6 GB+ card | **37–76** tokens/s on most cards | many times faster than you read |

Your exact card: [Can my PC run AI?](https://blog.greencube.app/blog/can-my-pc-run-ai#checker) On Windows: [what your PC needs to run AI offline](https://blog.greencube.app/blog/local-ai-chatbot-windows).

## ChatGPT vs an offline AI: the honest trade

|  | ChatGPT | AI on your PC |
| --- | --- | --- |
| **Works with no internet** | No | Yes, after one download |
| **Strength on the hardest problems** | Stronger: much bigger models | Good for study, writing and everyday questions |
| **Today's news** | Yes, with search | No (only what the model learned) |
| **Limits on files and pictures (free)** | Capped ([details](https://blog.greencube.app/blog/chatgpt-free-limits)) | None |
| **Your chats go to** | OpenAI's servers | Nowhere: your PC |
| **Price** | Free, or $20 a month for Plus | Free apps, or GreenCube €9.99 once |

Many people use both: ChatGPT when they're online and need the strongest model, an offline AI on the train, in a library with bad Wi-Fi, or for notes they'd rather not upload.

## FAQ

### Can you use ChatGPT offline?

No. ChatGPT runs on OpenAI's servers, so the website, the phone app and the Windows and Mac desktop apps all need an internet connection. There is no offline mode or offline installer from OpenAI.

### Is there an official offline version of ChatGPT?

Not of ChatGPT itself. The closest thing from OpenAI is gpt-oss-20b, an open-weight model released under Apache 2.0 that runs on a computer with about 16 GB of memory, through apps like Ollama or LM Studio. It isn't the same model as ChatGPT.

### What is the best offline alternative to ChatGPT?

An app that runs an AI model on your own PC: LM Studio, Jan, Ollama and GPT4All are free (you choose the model); GreenCube costs €9.99 once and picks the model for your PC. After the first download they work with Wi-Fi off.

### How fast is an offline ChatGPT alternative?

It depends on your PC. In our tests GreenCube wrote 5 to 7 tokens a second on an 8 GB laptop (about reading speed), 14 to 18 on a 16 GB laptop, and 37 to 76 on most gaming PCs with a 6 GB or bigger graphics card.

### Are 'ChatGPT offline' apps in app stores real?

Be careful: apps using the ChatGPT name for offline use are not from OpenAI. If an app works offline, it runs some other model on your device; check who makes it and which model it runs.
