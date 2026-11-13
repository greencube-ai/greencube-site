# Can my PC run AI? We measured 10 real gaming PCs and laptops

> Can your PC run AI locally? Real speeds from 10 PCs, from a GTX 1650 to an RTX 2080 Ti and laptops with no graphics card, and what your graphics card, VRAM and RAM mean.

Canonical: https://blog.greencube.app/blog/can-my-pc-run-ai  
Published: 2026-10-18  
Author: Hector Gras

Yes. If your PC runs games, it can run AI. We measured 10 real PCs, from gaming desktops with an old GTX 1650 up to an RTX 2080 Ti, plus two laptops with no graphics card at all, and every one of them chatted with an AI running entirely on the PC, with no internet. What changes from one PC to the next is how fast it goes.

We ran every test with GreenCube, the app I build, because it's the one we can measure in detail. The speeds depend on the hardware far more than on the app. Type your graphics card below to see what we found for it.

## Will AI run on your PC?

Type your graphics card and pick your RAM: you get what runs, how fast it ran on real PCs, and what we haven't measured yet. Interactive, on the page: https://blog.greencube.app/blog/can-my-pc-run-ai#checker

## The numbers

"Writes" is how fast the AI types its answer, in tokens per second. A token is about three quarters of a word. Most people read about 4 words a second ([Brysbaert, 2019](https://doi.org/10.1016/j.jml.2019.104047)), which is roughly 5 tokens, so anything above 5 is faster than your eyes.

| PC | Graphics | RAM | AI model | Writes (tokens/s) |
| --- | --- | --- | --- | --- |
| Desktop | [NVIDIA RTX 2080 Ti, 11 GB](https://blog.greencube.app/blog/ai-on-rtx-2080-ti) | 128 GB | Cube 4B (Gemma 4 E4B) | **65–71** |
| Desktop | [AMD RX 5700 XT, 8 GB](https://blog.greencube.app/blog/ai-on-rx-5700-xt) | 48 GB | Cube 4B (Gemma 4 E4B) | **63–72** |
| Desktop | [NVIDIA RTX 5060, 8 GB](https://blog.greencube.app/blog/ai-on-rtx-5060) | 32 GB | Cube 4B (Gemma 4 E4B) | **56** |
| Desktop | [NVIDIA RTX 3060, 12 GB](https://blog.greencube.app/blog/ai-on-rtx-3060) | 32 GB | Cube 4B (Gemma 4 E4B) | **53–55** |
| Desktop | [AMD RX 6600, 8 GB](https://blog.greencube.app/blog/ai-on-rx-6600) | 16 GB | Cube 4B (Gemma 4 E4B) | **42–44** |
| Desktop | [NVIDIA GTX 1660 Super, 6 GB](https://blog.greencube.app/blog/ai-on-gtx-1660-super) | 16 GB | Cube 4B (Gemma 4 E4B) | **37–38** |
| Desktop | [NVIDIA GTX 1650, 4 GB](https://blog.greencube.app/blog/ai-on-gtx-1650) | 16 GB | Cube 4B (Gemma 4 E4B) | **about 20** |
| Laptop | [Intel graphics only (Core Ultra 5)](https://blog.greencube.app/blog/ai-on-intel-core-ultra-5-laptop) | 16 GB | Cube 2B (Gemma 4 E2B) | **14–18** |
| Desktop | [AMD RX 580, 8 GB](https://blog.greencube.app/blog/ai-on-rx-580) | 16 GB | Cube 4B (Gemma 4 E4B) | **10–11** |
| Laptop | [Intel Iris Xe only](https://blog.greencube.app/blog/ai-on-intel-iris-xe-laptop) | 8 GB | Cube 2B (Gemma 4 E2B) | **5–7** |

Click a graphics card to see its full test. We measured in September and October 2026, in real chats and in GreenCube's own speed tests. Speeds move a little between runs on the same PC, so where we have several runs we show the range.

## What we learned

### The graphics card does the heavy lifting, like in a game

On the RX 5700 XT desktop, the same AI wrote 5 tokens a second on the processor and 72 on the graphics card. That's 14 times faster, on the same PC, with the same AI. AI is mostly the kind of maths graphics cards are built for, so any card from the last few years helps a lot. Even an old 4 GB GTX 1650 wrote about 20 tokens a second.

### VRAM decides how big an AI fits

The AI has to fit in the card's own memory (VRAM) to run at full speed. That same desktop had 48 GB of RAM, and it didn't save a bigger model: a 12-billion-parameter AI fitted on the 8 GB card for one short question, then crashed once the chat got longer, with the card almost full. For AI, VRAM matters more than RAM ([the full VRAM test](https://blog.greencube.app/blog/how-much-vram-for-ai)).

VRAM isn't speed, though. Four 8 GB cards we measured wrote anywhere from about 11 tokens a second (RX 580) to 72 (RX 5700 XT). That's why GreenCube checks your card and picks an AI that fits, rather than the biggest one.

### No graphics card still works

A normal 16 GB laptop with only Intel graphics wrote 14 to 18 tokens a second with the smaller AI, and finished a full answer (an explanation plus three exam questions) in about 20 seconds. That's plenty for studying and writing. An 8 GB laptop works too, at 5 to 7 tokens a second in real chats, as long as other apps leave it some free memory.

### Pictures are the heavy part

Making a picture takes far more than chatting. It took 8 to 9 seconds on an 11 GB RTX 2080 Ti (the first one took 83 while it loaded), 28 seconds on a 12 GB RTX 3060, about a minute on an 8 GB RX 6600, a minute and a half on a 6 GB GTX 1660 Super, and about two and a half minutes on the 16 GB laptop. An 8 GB laptop can't make pictures at all, because the picture AI alone needs about 7 GB.

## Check your PC in 30 seconds

1. Press Ctrl + Shift + Esc to open Task Manager.
2. Go to Performance.
3. Click Memory. The number at the top right is your RAM.
4. Click GPU. The name at the top right is your card, and Dedicated GPU memory is your VRAM. If you only see Intel graphics, you have no separate card.

## What your PC will feel like

| Your PC | What to expect |
| --- | --- |
| Graphics card with 6 GB or more | Fast on most cards from the last few years: 37 to 76 tokens a second in our tests, and pictures in seconds to a minute and a half. The exception was an old RX 580 at about 11, still faster than you read. |
| 4 GB card, 16 GB RAM | Good: about 20 tokens a second in our test. |
| No card, 16 GB RAM | Fine for chat and study with a smaller AI. Pictures take a couple of minutes. |
| No card, 8 GB RAM | Works for chat, slowly. Close other apps first. No pictures. |

## Why run AI on your own PC at all?

An AI on your own PC has no message limits and no monthly subscription, and it keeps working with no internet, on a train or in a library with terrible Wi-Fi. It won't beat the biggest cloud AIs at everything, and it's only as quick as your hardware. But for studying, writing, summarising and everyday questions, the AI on a normal PC does the job, and it never runs out.

If you're setting one up on Windows, [what a Windows PC needs to run AI offline](https://blog.greencube.app/blog/local-ai-chatbot-windows) goes through the details.

## FAQ

### Does AI on my PC work with an AMD graphics card?

Yes. GreenCube uses Vulkan, which works on AMD and NVIDIA, and we measured AMD cards too (RX 5700 XT, RX 6600, RX 580).

### How much VRAM do I need to run AI?

None is required, but 4 GB or more makes a big difference. On our test PCs a 4 GB GTX 1650 wrote about 20 tokens a second and an 8 GB RTX 5060 about 56, and more VRAM lets a bigger model fit.

### Can I run AI on a laptop with no graphics card?

Yes. A 16 GB laptop with only Intel graphics wrote 14 to 18 tokens a second with a small model, faster than you read. An 8 GB laptop works too, more slowly, but can't make pictures.

### Does more RAM make AI faster?

Not on its own. On a desktop with 48 GB of RAM, the same model ran 14 times faster on its 8 GB graphics card than on the processor. RAM matters when you have no card; with one, VRAM matters most.

### Do I need internet to run AI on my PC?

Only once, to download the app and the AI and to activate it. After that, chatting works with no internet at all.
