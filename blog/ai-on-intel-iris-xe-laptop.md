# Can an Intel Iris Xe laptop run AI? Measured: 5–7 tokens a second

> Real test: Gemma 4 E2B wrote 5–7 tokens a second on a laptop with no graphics card (Intel processor with Iris Xe graphics) and 8 GB of RAM. What it means for chat, study and pictures.

Canonical: https://blog.greencube.app/blog/ai-on-intel-iris-xe-laptop  
Published: 2026-10-04  
Author: Hector Gras

**Yes.** On a laptop with no graphics card (Intel processor with Iris Xe graphics) and 8 GB of RAM, Gemma 4 E2B wrote 5–7 tokens a second. You read about 5, so answers come out at about reading speed.

- **5–7** tokens a second with Gemma 4 E2B

## What that means in practice

| Task | Time on this PC |
| --- | --- |
| Write a normal answer (400 tokens, about 300 words) | **55–75 s** |
| Read a long document you give it (5,000 tokens, about 7 pages) | **51–85 s** |

Worked out from the speeds measured on this PC: time is length divided by speed, and a real answer also spends a moment getting started. For scale, most people read about 4 words a second ([Brysbaert, 2019](https://doi.org/10.1016/j.jml.2019.104047)), so a 400-token answer takes you over a minute just to read.

## What we measured

**Writing** is how fast the AI types its answer, in tokens a second; a token is about three quarters of an English word. **Reading** is how fast it takes in what you give it: your question, a pasted text or a PDF. Reading is always much faster than writing, because the AI can read many tokens at once but has to write them one by one.

| What | Ran on | Result | Measured |
| --- | --- | --- | --- |
| Gemma 4 E2B | processor only | **5.3–7.3** tokens a second writing · 59–98 reading | 4 October 2026 [1] |
| Gemma 4 E2B | processor only | **9.3** tokens a second writing | 4 October 2026 [2] |
| Gemma 4 E2B | built-in Intel graphics | **5** tokens a second writing | 4 October 2026 [2] |

How each number was measured: [More on how we measure](https://blog.greencube.app/blog/how-we-measure-ai-speed)

1. Real chats in GreenCube 0.1.42: the speed of every answer of 100 tokens or more, read from the app's log. The range leaves out the slowest and the fastest tenth.
2. GreenCube 0.1.42's own speed test, which it runs at startup to choose between the graphics card and the processor: a short answer written once on each.

Where we have several runs we show the range: speeds move a little between runs on the same PC.

## What it means

### No graphics card? It still works

With no graphics card, the AI runs on the processor. It is slower than on a gaming PC, but the smaller Gemma 4 E2B still writes 5–7 tokens a second, enough to study, summarise and write with. GreenCube's startup test also tried the built-in Intel graphics for writing: 5, against 9.3 on the processor, so it writes on the processor here.

### Pictures

No. The picture AI needs about 7 GB of memory to itself, more than an 8 GB laptop can free up. Chat and study work fine.

## How it compares

Of the 2 PCs we measured with Gemma 4 E2B, this one is **number 2** for writing speed. The [Intel Core Ultra 5 laptop](https://blog.greencube.app/blog/ai-on-intel-core-ultra-5-laptop) writes 14–18, about 2.5 times as fast.

## The test PC

A real tester's own PC, used the way they normally use it, not a lab machine:

- Laptop
- **Graphics:** built-in Intel graphics only
- **Graphics memory (VRAM):** none (no separate graphics card)
- **RAM:** 8 GB
- **Processor:** Intel, 8 threads

## Check your own PC

Not sure what your PC has? It takes 30 seconds:

1. Press **Ctrl + Shift + Esc** to open Task Manager.
2. Go to **Performance**.
3. Click **Memory**: the number at the top right is your RAM.
4. Click **GPU**: the name at the top right is your card, and **Dedicated GPU memory** is your VRAM. Only see Intel or AMD graphics with no dedicated memory? Then you have no separate card.

Then find the closest card in [the full table](https://blog.greencube.app/blog/can-my-pc-run-ai). The same card with more VRAM can fit a bigger AI; a newer card of the same size is usually faster.

## Other PCs we measured

- [RTX 2080 Ti](https://blog.greencube.app/blog/ai-on-rtx-2080-ti): 65–71 tokens a second (Gemma 4 E4B)
- [RX 5700 XT](https://blog.greencube.app/blog/ai-on-rx-5700-xt): 63–72 tokens a second (Gemma 4 E4B)
- [RTX 5060](https://blog.greencube.app/blog/ai-on-rtx-5060): 56 tokens a second (Gemma 4 E4B)
- [RTX 3060](https://blog.greencube.app/blog/ai-on-rtx-3060): 53–55 tokens a second (Gemma 4 E4B)
- [RX 6600](https://blog.greencube.app/blog/ai-on-rx-6600): 42–44 tokens a second (Gemma 4 E4B)
- [GTX 1660 Super](https://blog.greencube.app/blog/ai-on-gtx-1660-super): 37–38 tokens a second (Gemma 4 E4B)
- [GTX 1650](https://blog.greencube.app/blog/ai-on-gtx-1650): about 20 tokens a second (Gemma 4 E4B)
- [Intel Core Ultra 5 laptop](https://blog.greencube.app/blog/ai-on-intel-core-ultra-5-laptop): 14–18 tokens a second (Gemma 4 E2B)
- [RX 580](https://blog.greencube.app/blog/ai-on-rx-580): 10–11 tokens a second (Gemma 4 E4B)

[Can my PC run AI?](https://blog.greencube.app/blog/can-my-pc-run-ai) All 10 PCs in one table, and what your PC will feel like.

## FAQ

### Can an Intel Iris Xe laptop run AI locally?

Yes. On a laptop with no graphics card (Intel processor with Iris Xe graphics) and 8 GB of RAM, Gemma 4 E2B wrote 5–7 tokens a second. You read about 5, so answers come out at about reading speed.

### Can an Intel Iris Xe laptop make AI pictures?

No. The picture AI needs about 7 GB of memory to itself, more than an 8 GB laptop can free up. Chat and study work fine.
