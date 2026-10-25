# Can an RX 580 run AI? Measured: 10–11 tokens a second

> Real test: Gemma 4 E4B wrote 10–11 tokens a second on a desktop with an AMD RX 580 (8 GB) and 16 GB of RAM. What it means for chat, study and pictures.

Canonical: https://blog.greencube.app/blog/ai-on-rx-580  
Published: 2026-10-01  
Author: Hector Gras

**Yes.** On a desktop with an AMD RX 580 (8 GB) and 16 GB of RAM, Gemma 4 E4B wrote 10–11 tokens a second. You read about 5, so answers come out faster than you can read them.

- **10–11** tokens a second with Gemma 4 E4B
- **2.7×** faster on the card than on the processor

## What that means in practice

| Task | Time on this PC |
| --- | --- |
| Write a normal answer (400 tokens, about 300 words) | **37–38 s** |
| Read a long document you give it (5,000 tokens, about 7 pages) | **30–35 s** |

Worked out from the speeds measured on this PC: time is length divided by speed, and a real answer also spends a moment getting started. For scale, most people read about 4 words a second ([Brysbaert, 2019](https://doi.org/10.1016/j.jml.2019.104047)), so a 400-token answer takes you over a minute just to read.

## What we measured

**Writing** is how fast the AI types its answer, in tokens a second; a token is about three quarters of an English word. **Reading** is how fast it takes in what you give it: your question, a pasted text or a PDF. Reading is always much faster than writing, because the AI can read many tokens at once but has to write them one by one.

| What | Ran on | Result | Measured |
| --- | --- | --- | --- |
| Gemma 4 E4B\* | graphics card | **10.5–10.7** tokens a second writing · 144–169 reading | 1 October 2026 [1] |
| Gemma 4 E4B | graphics card | **10.1** tokens a second writing | 1 October 2026 [2] |
| Gemma 4 E4B | processor only | **3.8** tokens a second writing | 1 October 2026 [2] |

How each number was measured: [More on how we measure](https://blog.greencube.app/blog/how-we-measure-ai-speed)

1. Real chats in GreenCube 0.1.42: the speed of every answer of 100 tokens or more, read from the app's log. The range leaves out the slowest and the fastest tenth.
2. GreenCube 0.1.42's own speed test, which it runs at startup to choose between the graphics card and the processor: a short answer written once on each.

Where we have several runs we show the range: speeds move a little between runs on the same PC. \* This tester mostly asked short questions, so answers under 100 tokens are counted too. Short answers measure a little slower.

## What it means

### The graphics card does the work

Same PC, same AI (Gemma 4 E4B): 3.8 tokens a second on the processor alone, 10.1 on the graphics card, about **2.7 times faster**. A graphics card is built to do thousands of small sums at once for games, and running an AI is mostly that same kind of maths. GreenCube times both when it starts and uses the faster one.

### It fits, but this card is slow at AI

Gemma 4 E4B (4.2 GB) fits whole in the card's 8 GB, yet it writes only 10–11 tokens a second. Older cards are much slower at this kind of maths, and more memory does not change that. For comparison, other 8 GB cards we measured write 63–72 ([RX 5700 XT](https://blog.greencube.app/blog/ai-on-rx-5700-xt)), 56 ([RTX 5060](https://blog.greencube.app/blog/ai-on-rtx-5060)), 42–44 ([RX 6600](https://blog.greencube.app/blog/ai-on-rx-6600)) with the same AI. It still writes faster than you read, so chat and study work; it just feels slower than a newer card.

### The bigger Gemma 4 12B

Not comfortably. GreenCube suggests the bigger Gemma 4 12B only on cards with 10 GB or more of VRAM, and this one has 8. On an 8 GB AMD RX 5700 XT it answered short questions, then crashed in a long chat.

### Pictures

Very likely, but we haven't timed a picture on this card yet. When we do, the number goes here. A picture uses its own AI of about 6 GB and far more maths than a chat answer, so the graphics matter even more here.

## How it compares

Of the 8 PCs we measured with Gemma 4 E4B, this one is **number 8** for writing speed. The [GTX 1650](https://blog.greencube.app/blog/ai-on-gtx-1650) writes about 20, about 90% faster.

We measured 4 cards with 8 GB, and they are far apart:

- [RX 5700 XT](https://blog.greencube.app/blog/ai-on-rx-5700-xt): 63–72 tokens a second
- [RTX 5060](https://blog.greencube.app/blog/ai-on-rtx-5060): 56 tokens a second (startup test)
- [RX 6600](https://blog.greencube.app/blog/ai-on-rx-6600): 42–44 tokens a second
- **RX 580**: 10–11 tokens a second

Memory decides which AI fits. How new the card is decides how fast it runs.

## The test PC

A real tester's own PC, used the way they normally use it, not a lab machine:

- Desktop
- **Graphics:** AMD RX 580
- **Graphics memory (VRAM):** 8 GB
- **RAM:** 16 GB
- **Processor:** 12 threads

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
- [Intel Iris Xe laptop](https://blog.greencube.app/blog/ai-on-intel-iris-xe-laptop): 5–7 tokens a second (Gemma 4 E2B)

[Can my PC run AI?](https://blog.greencube.app/blog/can-my-pc-run-ai) All 10 PCs in one table, and what your PC will feel like.

## FAQ

### Can an RX 580 run AI locally?

Yes. On a desktop with an AMD RX 580 (8 GB) and 16 GB of RAM, Gemma 4 E4B wrote 10–11 tokens a second. You read about 5, so answers come out faster than you can read them.

### Can an RX 580 make AI pictures?

Very likely, but we haven't timed a picture on this card yet. When we do, the number goes here.

### Is AI faster on the RX 580 or on the processor?

On the card, by far: 10.1 tokens a second against 3.8 on the processor, about 2.7 times faster.

### Can an RX 580 run Gemma 4 12B?

Not comfortably. GreenCube suggests the bigger Gemma 4 12B only on cards with 10 GB or more of VRAM, and this one has 8. On an 8 GB AMD RX 5700 XT it answered short questions, then crashed in a long chat.
