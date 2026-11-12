# ChatGPT offline? The AI that works without internet (2026)

> ChatGPT needs internet. Here's how to get an AI that runs with Wi-Fi off: OpenAI's own gpt-oss-20b or a local AI app, what your PC needs, and measured speeds.

Canonical: https://blog.greencube.app/blog/chatgpt-offline  
Published: 2026-10-23  
Author: Hector Gras

No, ChatGPT doesn't work offline. Every message you type goes to OpenAI's servers and the answer comes back from there, so without a connection the app has nothing to answer you with. That goes for the website, the phone app and the Windows and Mac apps too.

What does work offline is an AI that lives on your own computer. You download it once, and after that you can switch the Wi-Fi off and keep going. I make one of these apps, GreenCube, so read my opinion with that in mind. Below are the free options as well, and what your PC needs to run any of them.

## Why ChatGPT can't run without internet

The ChatGPT apps are a window onto OpenAI's data centres, not a copy of the model. The model itself is far too big for a laptop, so it stays on their machines and your device only sends and receives text.

One warning: app stores are full of apps with "ChatGPT" and "offline" in the name. None of them are from OpenAI. If one really works offline, it's running a different, smaller model on your phone or PC, and it's worth checking who made it.

## What you can use instead

### OpenAI's open model, gpt-oss-20b

In August 2025 OpenAI released gpt-oss, a pair of models anyone can download under the Apache 2.0 licence. The smaller one, gpt-oss-20b, runs on a computer with about 16 GB of memory ([OpenAI's announcement](https://openai.com/index/introducing-gpt-oss/)). You run it through an app like [Ollama or LM Studio](https://blog.greencube.app/blog/ollama-vs-lm-studio). It's made by OpenAI, but it isn't ChatGPT: it can't search the web and it doesn't know your account. We haven't timed it on our own PCs yet.

### A free local AI app

**LM Studio**, **Jan**, **Ollama** and **[GPT4All](https://blog.greencube.app/blog/gpt4all-alternatives)** are free. You pick a model from a long list, download it and chat with it, with the Wi-Fi off if you like. They're great if you enjoy trying models and settings. If you don't know what "Q4_K_M" means, expect some reading first. There's a longer list in [12 offline AI apps compared](https://blog.greencube.app/blog/best-offline-ai-chatbot).

### GreenCube

GreenCube is the app I build, for people who want the result without the setup. You install it, it checks your PC and picks the model that fits: Cube 2B on smaller laptops, Cube 4B on PCs with a graphics card, both built on Google's Gemma. Then it works offline. Besides chatting, it makes slide decks, flashcards, quizzes and images, and it reads your PDFs and photos, all on your computer. It's for Windows and costs €9.99 once. You sign in once to activate it, and the first launch downloads the model.

An image GreenCube made on a 16 GB laptop with Intel graphics, in about 2 minutes, with no internet.

## Will it run on your computer?

Here's how fast GreenCube writes on 10 real PCs we tested. Reading speed is about 5 tokens a second, so anything above that feels quick.

| Your PC | Writes | Feels like |
| --- | --- | --- |
| 8 GB laptop, no graphics card | **5–7** tokens/s | about reading speed |
| 16 GB laptop, no graphics card | **14–18** tokens/s | faster than you read |
| Gaming PC with a 6 GB+ card | **37–76** tokens/s on most cards | many times faster than you read |

To check your exact graphics card, try [Can my PC run AI?](https://blog.greencube.app/blog/can-my-pc-run-ai#checker) For the Windows details, see [what your PC needs to run AI offline](https://blog.greencube.app/blog/local-ai-chatbot-windows).

## What you give up

An AI on your laptop is smaller than the one behind ChatGPT, and it shows on the hardest problems: long chains of maths, tricky code, very niche facts. It also doesn't know today's news, only what it learned before it was released.

What you get back: it works on a plane, it has no daily caps on files or images ([ChatGPT's free limits](https://blog.greencube.app/blog/chatgpt-free-limits)), and your chats are saved on your own computer instead of someone's server.

|  | ChatGPT | AI on your PC |
| --- | --- | --- |
| Works with no internet | No | Yes, after one download |
| Hardest problems | Stronger | Good for study, writing and everyday questions |
| Today's news | Yes, with search | No |
| Where your chats are kept | OpenAI's servers | Your PC |
| Price | Free, or $20 a month for Plus | Free apps, or GreenCube €9.99 once |

Plenty of people use both: ChatGPT when they're online and need the strongest model, and an offline AI on the train, in a library with bad Wi-Fi, or for notes they'd rather keep to themselves.

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
