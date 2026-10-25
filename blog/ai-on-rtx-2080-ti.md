# Can an RTX 2080 Ti run AI? Measured: 65–71 tokens a second

> Real test: Gemma 4 E4B wrote 65–71 tokens a second on a desktop with an NVIDIA RTX 2080 Ti (11 GB) and 128 GB of RAM. What it means for chat, study and pictures.

Canonical: https://blog.greencube.app/blog/ai-on-rtx-2080-ti  
Published: 2026-10-14  
Author: Hector Gras

**Yes.** On a desktop with an NVIDIA RTX 2080 Ti (11 GB) and 128 GB of RAM, Gemma 4 E4B wrote 65–71 tokens a second. You read about 5, so answers come out faster than you can read them.

- **65–71** tokens a second with Gemma 4 E4B
- **5.6×** faster on the card than on the processor
- **8–9 s** to make a picture

## What that means in practice

| Task | Time on this PC |
| --- | --- |
| Write a normal answer (400 tokens, about 300 words) | **6 s** |
| Read a long document you give it (5,000 tokens, about 7 pages) | **3–4 s** |
| Make a picture (512×512) | **8–9 s (first: 83 s)** |

Worked out from the speeds measured on this PC: time is length divided by speed, and a real answer also spends a moment getting started. For scale, most people read about 4 words a second ([Brysbaert, 2019](https://doi.org/10.1016/j.jml.2019.104047)), so a 400-token answer takes you over a minute just to read.

## What we measured

**Writing** is how fast the AI types its answer, in tokens a second; a token is about three quarters of an English word. **Reading** is how fast it takes in what you give it: your question, a pasted text or a PDF. Reading is always much faster than writing, because the AI can read many tokens at once but has to write them one by one.

| What | Ran on | Result | Measured |
| --- | --- | --- | --- |
| Gemma 4 E4B | graphics card | **65–71** tokens a second writing · 1,380–1,800 reading | 14 October 2026 [1] |
| Gemma 4 E4B | graphics card | **75.6** tokens a second writing | 14 October 2026 [2] |
| Gemma 4 E4B | processor only | **13.5** tokens a second writing | 14 October 2026 [2] |
| Picture (512×512) | graphics card | **8–9 s** (the first took 83 s while it loaded) | 12 October 2026 [3] |

How each number was measured: [More on how we measure](https://blog.greencube.app/blog/how-we-measure-ai-speed)

1. Real chats in GreenCube 0.1.44: the speed of every answer of 100 tokens or more, read from the app's log. The range leaves out the slowest and the fastest tenth.
2. GreenCube 0.1.44's own speed test, which it runs at startup to choose between the graphics card and the processor: a short answer written once on each.
3. GreenCube's picture engine (Z-Image Turbo), 512×512 pixels, 8 steps, timed from the click to the finished picture.

Where we have several runs we show the range: speeds move a little between runs on the same PC.

## What it means

### The graphics card does the work

Same PC, same AI (Gemma 4 E4B): 13.5 tokens a second on the processor alone, 75.6 on the graphics card, about **5.6 times faster**. A graphics card is built to do thousands of small sums at once for games, and running an AI is mostly that same kind of maths. GreenCube times both when it starts and uses the faster one.

### The whole AI fits on the card

Gemma 4 E4B is a 4.2 GB file and the card has 11 GB of its own memory (VRAM). All of it fits, with room left for the conversation, so the card never waits for the slower memory in the rest of the PC. That is the biggest reason it runs this fast.

### The bigger Gemma 4 12B

It should. Gemma 4 12B is a 6.4 GB file and this card has 11 GB, which leaves room for a long conversation too. We haven't measured it on this card yet.

### Pictures

Yes. One picture (512×512) took 8–9 s on the graphics card (the first took 83 s while it loaded). A picture uses its own AI of about 6 GB and far more maths than a chat answer, so the graphics matter even more here.

## How it compares

Of the 8 PCs we measured with Gemma 4 E4B, this one is **number 1** for writing speed. The [RX 5700 XT](https://blog.greencube.app/blog/ai-on-rx-5700-xt) writes 63–72, so this one is about as fast.

## The test PC

A real tester's own PC, used the way they normally use it, not a lab machine:

- Desktop
- **Graphics:** NVIDIA RTX 2080 Ti
- **Graphics memory (VRAM):** 11 GB
- **RAM:** 128 GB
- **Processor:** 32 threads

## Check your own PC

Not sure what your PC has? It takes 30 seconds:

1. Press **Ctrl + Shift + Esc** to open Task Manager.
2. Go to **Performance**.
3. Click **Memory**: the number at the top right is your RAM.
4. Click **GPU**: the name at the top right is your card, and **Dedicated GPU memory** is your VRAM. Only see Intel or AMD graphics with no dedicated memory? Then you have no separate card.

Then find the closest card in [the full table](https://blog.greencube.app/blog/can-my-pc-run-ai). The same card with more VRAM can fit a bigger AI; a newer card of the same size is usually faster.

## Other PCs we measured

- [RX 5700 XT](https://blog.greencube.app/blog/ai-on-rx-5700-xt): 63–72 tokens a second (Gemma 4 E4B)
- [RTX 5060](https://blog.greencube.app/blog/ai-on-rtx-5060): 56 tokens a second (Gemma 4 E4B)
- [RTX 3060](https://blog.greencube.app/blog/ai-on-rtx-3060): 53–55 tokens a second (Gemma 4 E4B)
- [RX 6600](https://blog.greencube.app/blog/ai-on-rx-6600): 42–44 tokens a second (Gemma 4 E4B)
- [GTX 1660 Super](https://blog.greencube.app/blog/ai-on-gtx-1660-super): 37–38 tokens a second (Gemma 4 E4B)
- [GTX 1650](https://blog.greencube.app/blog/ai-on-gtx-1650): about 20 tokens a second (Gemma 4 E4B)
- [Intel Core Ultra 5 laptop](https://blog.greencube.app/blog/ai-on-intel-core-ultra-5-laptop): 14–18 tokens a second (Gemma 4 E2B)
- [RX 580](https://blog.greencube.app/blog/ai-on-rx-580): 10–11 tokens a second (Gemma 4 E4B)
- [Intel Iris Xe laptop](https://blog.greencube.app/blog/ai-on-intel-iris-xe-laptop): 5–7 tokens a second (Gemma 4 E2B)

[Can my PC run AI?](https://blog.greencube.app/blog/can-my-pc-run-ai) All 10 PCs in one table, and what your PC will feel like.

## FAQ

### Can an RTX 2080 Ti run AI locally?

Yes. On a desktop with an NVIDIA RTX 2080 Ti (11 GB) and 128 GB of RAM, Gemma 4 E4B wrote 65–71 tokens a second. You read about 5, so answers come out faster than you can read them.

### Can an RTX 2080 Ti make AI pictures?

Yes. One picture (512×512) took 8–9 s on the graphics card (the first took 83 s while it loaded).

### Is AI faster on the RTX 2080 Ti or on the processor?

On the card, by far: 75.6 tokens a second against 13.5 on the processor, about 5.6 times faster.

### Can an RTX 2080 Ti run Gemma 4 12B?

It should. Gemma 4 12B is a 6.4 GB file and this card has 11 GB, which leaves room for a long conversation too. We haven't measured it on this card yet.
