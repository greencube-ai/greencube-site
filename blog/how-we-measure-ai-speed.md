# How we measure AI speed on real PCs, and why we don't guess

> Every speed on the GreenCube blog comes from one of 10 real PCs. How we measure, every PC we tested, the data as a CSV, and the test that shows why we don't estimate the rest.

Canonical: https://blog.greencube.app/blog/how-we-measure-ai-speed  
Published: 2026-10-14  
Author: Hector Gras

Every speed on this blog comes from a real PC running GreenCube: 10 PCs so far, measured between 22 September 2026 and 14 October 2026. We don't estimate speeds for cards we haven't measured: when we tested estimates on the cards we have, the typical one was off by 19% and the worst by 239%.

- **10** real PCs measured, desktops and laptops
- **34** measurements, all in the CSV below
- **239%** how far off the worst speed estimate was

## What we measure

Three things, because they are what you feel when you use an AI on your own PC:

- **Writing speed:** how fast the AI types its answer, in tokens a second. A token is about three quarters of an English word, and most people read about 5 tokens a second, so anything above that comes out faster than you can read.
- **Reading speed:** how fast it takes in what you give it: your question, a pasted text or a PDF. It is always much faster than writing, because the AI reads many tokens at once but writes them one by one.
- **Picture time:** how long one 512×512 picture takes, from the click to the finished image.

We measure the AIs GreenCube ships, the same files every user downloads: Google's Gemma 4 E2B (2.6 GB), Gemma 4 E4B (4.2 GB) and Gemma 4 12B (6.4 GB) for chat, and Z-Image Turbo for pictures. A different AI, or the same one compressed differently, would give different numbers, so we only compare like with like.

## How we measure

Four ways, and every number on the blog says which one it came from:

### Real chats

Real chats in GreenCube: the speed of every answer of 100 tokens or more, read from the app's log. The range leaves out the slowest and the fastest tenth.

Used for: [RTX 2080 Ti](https://blog.greencube.app/blog/ai-on-rtx-2080-ti), [RTX 3060](https://blog.greencube.app/blog/ai-on-rtx-3060), [RX 6600](https://blog.greencube.app/blog/ai-on-rx-6600), [GTX 1660 Super](https://blog.greencube.app/blog/ai-on-gtx-1660-super), [GTX 1650](https://blog.greencube.app/blog/ai-on-gtx-1650), [RX 580](https://blog.greencube.app/blog/ai-on-rx-580), [Intel Iris Xe laptop](https://blog.greencube.app/blog/ai-on-intel-iris-xe-laptop).

### GreenCube's startup test

GreenCube's own speed test, which it runs at startup to choose between the graphics card and the processor: a short answer written once on each.

Used for: [RTX 2080 Ti](https://blog.greencube.app/blog/ai-on-rtx-2080-ti), [RTX 5060](https://blog.greencube.app/blog/ai-on-rtx-5060), [RTX 3060](https://blog.greencube.app/blog/ai-on-rtx-3060), [RX 6600](https://blog.greencube.app/blog/ai-on-rx-6600), [GTX 1660 Super](https://blog.greencube.app/blog/ai-on-gtx-1660-super), [RX 580](https://blog.greencube.app/blog/ai-on-rx-580), [Intel Iris Xe laptop](https://blog.greencube.app/blog/ai-on-intel-iris-xe-laptop).

### llama.cpp's speed test

llama.cpp's own speed test (llama-bench), the engine GreenCube runs on, with the same AI files: 128 tokens written, a 512-token text read.

Used for: [RX 5700 XT](https://blog.greencube.app/blog/ai-on-rx-5700-xt), [Intel Core Ultra 5 laptop](https://blog.greencube.app/blog/ai-on-intel-core-ultra-5-laptop).

### Picture test

GreenCube's picture engine (Z-Image Turbo), 512×512 pixels, 8 steps, timed from the click to the finished picture.

Used for: [RTX 2080 Ti](https://blog.greencube.app/blog/ai-on-rtx-2080-ti), [RTX 3060](https://blog.greencube.app/blog/ai-on-rtx-3060), [RX 6600](https://blog.greencube.app/blog/ai-on-rx-6600), [GTX 1660 Super](https://blog.greencube.app/blog/ai-on-gtx-1660-super), [Intel Core Ultra 5 laptop](https://blog.greencube.app/blog/ai-on-intel-core-ultra-5-laptop).

Real chats are the best evidence, because that is what you will feel, so the main number on every page comes from real chats whenever we have them. The startup test is one short answer, so we use it for the card-versus-processor comparison (it times both the same way), and as the main number only where a tester sent no long answers.

## Every PC we measured

Real testers' own PCs, used the way they normally use them, not lab machines. We don't publish their names.

| PC | Type | VRAM | RAM | Main number from | GreenCube | Date | Writes (tokens/s) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [RTX 2080 Ti](https://blog.greencube.app/blog/ai-on-rtx-2080-ti) | Desktop | 11 GB | 128 GB | Real chats | 0.1.44 | 14 October 2026 | **65–71** |
| [RX 5700 XT](https://blog.greencube.app/blog/ai-on-rx-5700-xt) | Desktop | 8 GB | 48 GB | llama.cpp's speed test | – | 22 September 2026 | **63–72** |
| [RTX 5060](https://blog.greencube.app/blog/ai-on-rtx-5060) | Desktop | 8 GB | 32 GB | GreenCube's startup test | 0.1.42 | 1 October 2026 | **56** |
| [RTX 3060](https://blog.greencube.app/blog/ai-on-rtx-3060) | Desktop | 12 GB | 32 GB | Real chats | 0.1.42–0.1.43 | 6 October 2026 | **53–55** |
| [RX 6600](https://blog.greencube.app/blog/ai-on-rx-6600) | Desktop | 8 GB | 16 GB | Real chats | 0.1.42–0.1.44 | 9 October 2026 | **42–44** |
| [GTX 1660 Super](https://blog.greencube.app/blog/ai-on-gtx-1660-super) | Desktop | 6 GB | 16 GB | Real chats | 0.1.42 | 1 October 2026 | **37–38** |
| [GTX 1650](https://blog.greencube.app/blog/ai-on-gtx-1650) | Desktop | 4 GB | 16 GB | Real chats | 0.1.40 | 23 September 2026 | **about 20** |
| [Intel Core Ultra 5 laptop](https://blog.greencube.app/blog/ai-on-intel-core-ultra-5-laptop) | Laptop | – | 16 GB | llama.cpp's speed test | – | 28 September 2026 | **14–18** |
| [RX 580](https://blog.greencube.app/blog/ai-on-rx-580) | Desktop | 8 GB | 16 GB | Real chats | 0.1.42 | 1 October 2026 | **10–11** |
| [Intel Iris Xe laptop](https://blog.greencube.app/blog/ai-on-intel-iris-xe-laptop) | Laptop | – | 8 GB | Real chats | 0.1.42 | 4 October 2026 | **5–7** |

## Why the numbers come as ranges

- **Other apps.** A browser, a game launcher or a video call uses the same memory and graphics card.
- **The first time is slower.** The first answer after installing, or the first picture, includes loading and setting up the card. We say so where it matters (for example "the first took 83 s while it loaded").
- **Short answers measure slower.** Every answer has a small fixed start, which weighs more on a 20-token reply than on a 400-token one. That is why real-chat ranges count answers of 100 tokens or more, and we flag it where a tester only sent short ones.
- **We leave out the extremes.** Real-chat ranges go from the 10th to the 90th percentile, so one odd answer cannot move them.

## Can you guess a card's speed from its specs?

It would be handy: there are hundreds of cards and we have measured 10 PCs. The usual way is memory bandwidth. To write each token, the AI reads its whole model from the card's memory, so in theory speed is roughly bandwidth divided by model size, times some efficiency. Many online calculators work like this.

So we tested it on our own data. We hid one card at a time, worked out the speed per GB/s from the others, predicted the hidden card from its bandwidth (from the makers' specs, collected in the [TechPowerUp GPU database](https://www.techpowerup.com/gpu-specs/)), and compared with what we measured. Same AI on all of them (Gemma 4 E4B, whole on the card).

| Card | Memory bandwidth | Measured (tokens/s) | Predicted | Off by |
| --- | --- | --- | --- | --- |
| [RTX 2080 Ti](https://blog.greencube.app/blog/ai-on-rtx-2080-ti) | 616 GB/s | 68 | 79 | **+17%** |
| [RX 5700 XT](https://blog.greencube.app/blog/ai-on-rx-5700-xt) | 448 GB/s | 68 | 55 | **−19%** |
| [RTX 5060](https://blog.greencube.app/blog/ai-on-rtx-5060) | 448 GB/s | 56 | 57 | **+1%** |
| [RTX 3060](https://blog.greencube.app/blog/ai-on-rtx-3060) | 360 GB/s | 54 | 44 | **−19%** |
| [RX 6600](https://blog.greencube.app/blog/ai-on-rx-6600) | 224 GB/s | 43 | 26 | **−41%** |
| [GTX 1660 Super](https://blog.greencube.app/blog/ai-on-gtx-1660-super) | 336 GB/s | 38 | 43 | **+14%** |
| [RX 580](https://blog.greencube.app/blog/ai-on-rx-580) | 256 GB/s | 11 | 36 | **+239%** |

The typical estimate was off by 19%. The worst was the [RX 580](https://blog.greencube.app/blog/ai-on-rx-580): its memory suggests about 36 tokens a second, but it wrote 11. Run the test again without it and the others are still off by up to 33%. The newer AMD RX 6600 went the other way, faster than its bandwidth suggests; its large on-chip cache (AMD calls it Infinity Cache) may be part of why. Each measured number is that card's main number, so they don't all come from the same kind of test; that adds some noise, but it can't explain missing by three times.

**That is not good enough.** A guess that can be 33% off on a modern card, or 239% on an older one, would tell some people their PC is fine when it is slow, or the other way round. So the checker and the card pages only ever show cards we measured, and say clearly when yours isn't one of them. We run this test again with every new card, and if the error gets small, we will say so here before we show a single estimate.

## What we haven't measured yet

- A laptop with a gaming card.
- Gemma 4 12B on a card with 10 GB or more.
- Pictures on the [RX 5700 XT](https://blog.greencube.app/blog/ai-on-rx-5700-xt), the [RTX 5060](https://blog.greencube.app/blog/ai-on-rtx-5060), the [GTX 1650](https://blog.greencube.app/blog/ai-on-gtx-1650), the [RX 580](https://blog.greencube.app/blog/ai-on-rx-580).
- Other AIs than the ones GreenCube ships, and Linux or Mac (GreenCube is for Windows).

## Get the data

Every measurement on this page, one row each, is in [greencube-ai-speeds.csv](https://blog.greencube.app/blog/greencube-ai-speeds.csv): the PC, the AI, where it ran, writing and reading speeds, picture times, how it was measured, the GreenCube version and the date. If you use it, please cite "GreenCube, AI speed measurements on real PCs, 2026" and link to this page.

## Add your PC

Already using GreenCube? Send your log to [support@greencube.app](mailto:support@greencube.app). We add your PC to the tests, without your name, and a new card gets its own page. Not sure what your PC has? [Check it here](https://blog.greencube.app/blog/can-my-pc-run-ai#checker).

## FAQ

### Where do GreenCube's AI speed numbers come from?

From 10 real PCs running GreenCube, measured in real chats, with GreenCube's startup speed test, with llama.cpp's speed test and with a picture test. Every number says which.

### Can you estimate AI speed from a graphics card's specs?

Not reliably yet. Predicting from memory bandwidth, our estimates were typically 19% off and up to 239% off, so we only show cards we measured.

### Can I download the data?

Yes: every measurement is in greencube-ai-speeds.csv, linked on this page.
