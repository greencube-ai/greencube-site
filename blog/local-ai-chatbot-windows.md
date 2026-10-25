# Offline AI for Windows 10 and 11: what you need, measured on 10 PCs

> How to run a local AI chatbot on Windows 10 or 11 with no internet: the RAM and graphics card you need, real speeds measured on 10 Windows PCs, the apps that work offline, and how to check nothing leaves your PC.

Canonical: https://blog.greencube.app/blog/local-ai-chatbot-windows  
Published: 2026-08-11 · Updated: 2026-10-23  
Author: Hector Gras

**Short answer:** any Windows 10 or 11 PC with **8 GB of RAM** can run a local AI chatbot with no internet, and **16 GB or a gaming graphics card** makes it comfortable. You download the app and the AI model once; after that it works with Wi-Fi off. We measured it on 10 real Windows PCs: from about reading speed on an 8 GB laptop to many times faster on a gaming PC.

- **10** real Windows PCs we measured, laptops and gaming desktops
- **8 GB** of RAM is enough to start, no graphics card needed
- **0** internet needed after the first download

## What your Windows PC needs

|  | Minimum | Comfortable |
| --- | --- | --- |
| **Windows** | Windows 10 (64-bit) | Windows 11 |
| **RAM** | 8 GB, with other apps closed | 16 GB or more |
| **Graphics card** | None needed | Any 6 GB+ card from the last few years |
| **Disk space** | About 3 GB for a small model | About 11 GB for a bigger model plus pictures |
| **Internet** | Once, to download the app and the model |  |

Not sure what your PC has? Press **Ctrl + Shift + Esc**, open **Performance**, and look at **Memory** and **GPU**. Or type your card into [our checker](https://blog.greencube.app/blog/can-my-pc-run-ai#checker): it tells you what runs and how fast it ran on a real PC like yours.

## How fast it runs on real Windows PCs

Every number below comes from GreenCube running on a real Windows PC in September and October 2026, mostly in real chats. A token is a piece of a word; most people read about 5 a second.

| Your Windows PC | Writes | One picture (512×512) |
| --- | --- | --- |
| 8 GB laptop, no graphics card | **5–7** tokens/s, about reading speed | can't (needs about 7 GB free) |
| 16 GB laptop, no graphics card | **14–18** tokens/s | **2–2.5 min** |
| Gaming PC with a 6 GB+ card | **37–76** tokens/s on most cards | **8–89 s** |

The exception: an older AMD RX 580 wrote about 11 tokens a second, still faster than you read. Every card, with its own page, is in [Can my PC run AI?](https://blog.greencube.app/blog/can-my-pc-run-ai)

### The graphics card does the heavy lifting

On the same Windows desktop, the same AI wrote **5 tokens a second on the processor and 72 on an RX 5700 XT**. Running an AI is mostly the kind of maths a graphics card is built for, so any recent gaming card makes a big difference. What decides how big an AI fits is the card's own memory (VRAM), not your RAM: [why the model must fit on the card](https://blog.greencube.app/blog/how-much-vram-for-ai).

### No graphics card? Still fine for study and chat

A normal 16 GB laptop with only Intel graphics finished a full study answer, an explanation plus three exam questions, in about 20 seconds. On an 8 GB laptop it works too, slower, as long as other apps leave some memory free: [our 8 GB test](https://blog.greencube.app/blog/run-ai-on-8gb-ram).

## Apps that run AI offline on Windows

From each app's own website, checked on 21 October 2026. We haven't timed the other apps on our PCs, so this table doesn't compare speed.

| App | Windows | Price | Picks the model for you? | Reads your PDFs |
| --- | --- | --- | --- | --- |
| **GreenCube** | Windows 10 and 11 | €9.99 once | Yes, from your card and RAM | Yes |
| **LM Studio** | Needs a processor with AVX2 | Free | No, you choose from a list | Yes |
| **Jan** | Windows 10 or newer | Free, open source | No | Yes |
| **Ollama** | Windows; chat window since July 2025 | Free on your PC | No | Yes |
| **GPT4All** | Windows (not ARM PCs) | Free, open source | No | Yes, with LocalDocs |
| **AnythingLLM** | Windows | Desktop free | No | Yes |
| **Msty** | Windows 10 and 11 | Free plan | No | Yes |
| **KoboldCpp** | One .exe, chat in your browser | Free, open source | No | Text only |

Want to see what each one sends online, plus Mac and phone apps? See [our comparison of 12 offline AI chatbots](https://blog.greencube.app/blog/best-offline-ai-chatbot).

## Windows 10 or Windows 11?

The AI runs the same on both: what matters is your RAM and graphics card, not the Windows version. One thing to know: Microsoft ended support for Windows 10 on 14 October 2025, so a Windows 10 PC no longer gets security updates unless you sign up for extended updates. An offline AI keeps your chats on your PC either way, but keeping Windows itself updated is still worth it.

## How to check it really stays offline

1. **Turn on airplane mode** (or unplug the cable) after the first download, and chat. If it answers, the AI is running on your PC.
2. **Watch the network:** press **Windows + R**, type **resmon**, open the **Network** tab. "Processes with Network Activity" lists every program sending or receiving data while you chat.
3. **Read what the app says goes online.** In GreenCube: you sign in once to activate, it downloads the AI and its updates, and Online search (which starts off every time you open the app) sends search terms to search engines. Nothing else: "We never receive your chats, files, memories or images."

## What offline AI on Windows can't do

- **Today's news.** The model knows what it learned in training. For anything current you need a web search, and that part goes online.
- **Beat the biggest cloud AIs at everything.** Models that fit on a PC handle study, writing and everyday questions well, but the largest cloud models are still stronger at the hardest problems.
- **Run fast on any PC.** Your PC does the work: an 8 GB laptop is about as fast as you read, a gaming PC is far faster.

Studying with it? See [what offline AI can do for students](https://blog.greencube.app/blog/offline-ai-for-students), with times for PDFs, study guides and flashcards.

## FAQ

### Can I run AI offline on Windows 11?

Yes. Apps like GreenCube, LM Studio, Jan, Ollama and GPT4All run the AI model on your own PC. You need internet once to download the app and the model; after that, chat works with Wi-Fi off.

### Does offline AI work on Windows 10?

Yes. GreenCube, Jan and Msty list Windows 10 as supported. Microsoft ended Windows 10 support on 14 October 2025, so the AI still runs, but your PC no longer gets security updates unless you join extended updates.

### How much RAM do I need to run AI locally on a Windows PC?

8 GB works with a small model: our 8 GB laptop wrote 5 to 7 tokens a second in real chats, about reading speed. 16 GB is comfortable: our 16 GB laptop with no graphics card wrote 14 to 18.

### Do I need a graphics card to run a local AI chatbot on Windows?

No, but it helps a lot. On gaming PCs with a 6 GB or bigger card we measured 37 to 76 tokens a second on most cards, several times faster than the same PCs on the processor alone. Pictures need either a graphics card or 16 GB of RAM.

### Is there a free offline AI for Windows?

Yes: LM Studio, Jan, Ollama, GPT4All and AnythingLLM are free, and you pick and download a model yourself. GreenCube costs €9.99 once and picks the model that fits your PC for you.
