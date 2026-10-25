# Best local AI model for your PC, by RAM and VRAM (measured)

> The best local AI model is the biggest one that fits whole on your graphics card with room to spare. Which model for 8 GB and 16 GB laptops and for 4, 6, 8 and 12 GB cards, with real speeds for Gemma 4 E2B, E4B and 12B measured on 10 PCs.

Canonical: https://blog.greencube.app/blog/best-local-ai-models  
Published: 2026-08-03 · Updated: 2026-10-23  
Author: Hector Gras

**Short answer:** the best local AI model for *your* PC is the **biggest one that fits whole on your graphics card, with about 1.5 GB to spare**. No card? A **small model** in your RAM. A smaller model fully on the card beats a bigger one that spills over: we measured spilling at **6 times slower**. Below, the pick for each kind of PC, with speeds we measured on 10 real PCs.

- **+1.5 GB** model file plus about 1.5 GB must fit in your VRAM
- **6×** slower when part of the model doesn't fit on the card
- **10** real PCs we measured, laptops to gaming desktops

## The best model for your PC

| Your PC | Model size that fits | What we measured |
| --- | --- | --- |
| 8 GB laptop, no graphics card | Small, about 2–3 GB (Gemma 4 E2B, 2.6 GB) | **5–7** tokens/s in real chats; close other apps first |
| 16 GB laptop, no graphics card | Small for speed; about 4 GB works but slowly | E2B **14–18** tokens/s; E4B **8–10** |
| 4 GB graphics card | About 2–3 GB fits whole; 4 GB spills | E4B (4.2 GB, partly in RAM) about **20** tokens/s on a GTX 1650 |
| 6 GB graphics card | About 4–4.5 GB | E4B **35–38** tokens/s on a GTX 1660 Super |
| 8 GB graphics card | About 4–6 GB | E4B **56–72** on recent cards (about 11 on an old RX 580) |
| 12 GB+ graphics card | About 6–10 GB: 12B-class models | E4B **50–55** on 12 GB; 12B needs 10 GB+ for long chats |

Every card with its own page: [Can my PC run AI?](https://blog.greencube.app/blog/can-my-pc-run-ai) Or type your card into [the checker](https://blog.greencube.app/blog/can-my-pc-run-ai#checker).

## Why "fits" matters more than "biggest"

### Spill over and it's slower than no card at all

On an 8 GB RX 5700 XT, Gemma 4 12B wrote 35.6 tokens a second fully on the card, 5.9 with part of it off the card, and 4.3 with even less on it: slower than a smaller model running with no card. [The full VRAM test](https://blog.greencube.app/blog/how-much-vram-for-ai).

### Fits for one question, crashes in a long chat

The same 12B model fit the 8 GB card for a short question, then crashed every time the chat grew: the conversation needs room too. That's what the 1.5 GB of headroom is for.

### Small is often good enough

On a 16 GB laptop, Gemma 4 E2B gave a complete study answer in 20 seconds and got 5 of 5 quick fact checks right; E4B explained better but took 112 seconds. [E2B vs E4B, measured](https://blog.greencube.app/blog/gemma-4-e2b-vs-e4b).

## The models we measured

| Model | File size | Best on | Licence |
| --- | --- | --- | --- |
| **Gemma 4 E2B** | 2.6 GB | Laptops, 8–16 GB RAM | Apache 2.0 |
| **Gemma 4 E4B** | 4.2 GB | Graphics cards with 6 GB or more | Apache 2.0 |
| **Gemma 4 12B** | about 6.4 GB | Graphics cards with 10–12 GB or more | Apache 2.0 |

These are the files GreenCube ships and the only ones we've timed, so they're the only ones we give speeds for. Other model families follow the same rule: check the file size, add about 1.5 GB, compare with your VRAM. [Gemma 4 requirements in detail](https://blog.greencube.app/blog/gemma-4-requirements).

## How to check your VRAM

1. Press **Ctrl + Shift + Esc** to open Task Manager.
2. Go to **Performance**, then **GPU**.
3. **Dedicated GPU memory** is your VRAM. No dedicated memory? Use a small model in RAM.

Rather not pick at all? GreenCube reads your card and RAM and chooses the model that fits, with room to spare. Free apps like LM Studio, Jan and Ollama let you choose yourself: [12 apps compared](https://blog.greencube.app/blog/best-offline-ai-chatbot).

## FAQ

### What is the best local AI model?

The biggest model that fits whole on your graphics card with about 1.5 GB to spare. A smaller model fully on the card beats a bigger one that spills into RAM: in our test, a model with part of it off an 8 GB card ran 6 times slower.

### What is the best local AI model for a laptop without a graphics card?

A small one. Gemma 4 E2B (2.6 GB) wrote 14 to 18 tokens a second on a 16 GB laptop and 5 to 7 on an 8 GB laptop in real chats; the bigger E4B took 112 seconds for an answer E2B gave in 20.

### What is the best local AI model for an 8 GB graphics card?

A model of about 4 to 5 GB, like Gemma 4 E4B (4.2 GB): it wrote 56 to 72 tokens a second on 8 GB gaming cards. A 12-billion-parameter model fit for short questions but crashed in long chats.

### How do I know if a model fits my graphics card?

Take the model file's size and add about 1.5 GB for the conversation and Windows. If that's less than your card's dedicated GPU memory (Task Manager, Performance, GPU), it fits.

### Do I need to pick a model myself?

In free apps like LM Studio, Jan or Ollama, yes. GreenCube reads your card and RAM and picks the model that fits for you.
