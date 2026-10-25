# Can an Intel Core Ultra 5 laptop run AI? Measured: 14–18 tokens a second

> Real test: Gemma 4 E2B wrote 14–18 tokens a second on a laptop with no graphics card (Intel Core Ultra 5 125U) and 16 GB of RAM. What it means for chat, study and pictures.

Canonical: https://blog.greencube.app/blog/ai-on-intel-core-ultra-5-laptop  
Published: 2026-10-14  
Author: Hector Gras

**Yes.** On a laptop with no graphics card (Intel Core Ultra 5 125U) and 16 GB of RAM, Gemma 4 E2B wrote 14–18 tokens a second. You read about 5, so answers come out faster than you can read them.

- **14–18** tokens a second with Gemma 4 E2B
- **2:02–2:38 min** to make a picture
- **8–10** with Gemma 4 E4B

## What that means in practice

| Task | Time on this PC |
| --- | --- |
| Write a normal answer (400 tokens, about 300 words) | **22–29 s** |
| Make a picture (512×512, built-in graphics) | **2:02–2:38 min** |
| Make a picture (512×512, processor alone) | **11:27–13:32 min** |

Worked out from the speeds measured on this PC: time is length divided by speed, and a real answer also spends a moment getting started. For scale, most people read about 4 words a second ([Brysbaert, 2019](https://doi.org/10.1016/j.jml.2019.104047)), so a 400-token answer takes you over a minute just to read.

## What we measured

**Writing** is how fast the AI types its answer, in tokens a second; a token is about three quarters of an English word. **Reading** is how fast it takes in what you give it: your question, a pasted text or a PDF. Reading is always much faster than writing, because the AI can read many tokens at once but has to write them one by one.

| What | Ran on | Result | Measured |
| --- | --- | --- | --- |
| Gemma 4 E2B | processor only | **14–18** tokens a second writing | 28 September 2026 [1] |
| Gemma 4 E4B | processor only | **8–10** tokens a second writing | 28 September 2026 [1] |
| Picture (512×512) | built-in Intel graphics | **2:02–2:38 min** | 27 September 2026 [2] |
| Picture (512×512) | processor only | **11:27–13:32 min** | 14 October 2026 [2] |

How each number was measured: [More on how we measure](https://blog.greencube.app/blog/how-we-measure-ai-speed)

1. llama.cpp's own speed test (llama-bench), the engine GreenCube runs on, with the same AI files: 128 tokens written, a 512-token text read.
2. GreenCube's picture engine (Z-Image Turbo), 512×512 pixels, 8 steps, timed from the click to the finished picture.

Where we have several runs we show the range: speeds move a little between runs on the same PC.

## What it means

### No graphics card? It still works

With no graphics card, the AI runs on the processor. It is slower than on a gaming PC, but the smaller Gemma 4 E2B still writes 14–18 tokens a second, enough to study, summarise and write with. The bigger Gemma 4 E4B works too, at 8–10: smarter, but you will feel the wait on long answers.

### Pictures

Yes. One picture (512×512) took 2:02–2:38 min on the built-in Intel graphics, and 11:27–13:32 min on the processor alone. A picture uses its own AI of about 6 GB and far more maths than a chat answer, so the graphics matter even more here.

## How it compares

Of the 2 PCs we measured with Gemma 4 E2B, this one is **number 1** for writing speed. The [Intel Iris Xe laptop](https://blog.greencube.app/blog/ai-on-intel-iris-xe-laptop) writes 5–7, so this one is about 2.5 times as fast.

## The test PC

A real tester's own PC, used the way they normally use it, not a lab machine:

- Laptop
- **Graphics:** built-in Intel graphics only
- **Graphics memory (VRAM):** none (no separate graphics card)
- **RAM:** 16 GB
- **Processor:** Intel Core Ultra 5 125U, 14 threads

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
- [RX 580](https://blog.greencube.app/blog/ai-on-rx-580): 10–11 tokens a second (Gemma 4 E4B)
- [Intel Iris Xe laptop](https://blog.greencube.app/blog/ai-on-intel-iris-xe-laptop): 5–7 tokens a second (Gemma 4 E2B)

[Can my PC run AI?](https://blog.greencube.app/blog/can-my-pc-run-ai) All 10 PCs in one table, and what your PC will feel like.

## FAQ

### Can an Intel Core Ultra 5 laptop run AI locally?

Yes. On a laptop with no graphics card (Intel Core Ultra 5 125U) and 16 GB of RAM, Gemma 4 E2B wrote 14–18 tokens a second. You read about 5, so answers come out faster than you can read them.

### Can an Intel Core Ultra 5 laptop make AI pictures?

Yes. One picture (512×512) took 2:02–2:38 min on the built-in Intel graphics, and 11:27–13:32 min on the processor alone.
