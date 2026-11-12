# Gemma 4 requirements: what PC you need to run it locally

> Gemma 4 requirements for E2B, E4B and 12B, measured on real PCs: how much RAM and VRAM each needs, and how fast it runs on laptops and gaming graphics cards.

Canonical: https://blog.greencube.app/blog/gemma-4-requirements  
Published: 2026-10-18  
Author: Hector Gras

The smallest Gemma 4, E2B, runs on an 8 GB laptop with no graphics card. E4B wants 16 GB of RAM, or any graphics card with 6 GB or more, where it's fast. Gemma 4 12B needs at least 10 GB of VRAM to hold a real conversation.

These numbers come from our own tests. GreenCube, the app I build, runs on Gemma 4 (Cube 2B is built on Gemma 4 E2B and Cube 4B on Gemma 4 E4B), so we've timed these models on 10 real PCs, in September and October 2026. Gemma 4 itself is free: Google released it under the Apache 2.0 licence, which allows commercial use.

## Gemma 4 requirements at a glance

| Model | File size | Minimum we'd suggest | Best on |
| --- | --- | --- | --- |
| Gemma 4 E2B | 2.6 GB | 8 GB RAM, no card | Laptops |
| Gemma 4 E4B | 4.2 GB | 16 GB RAM, or a 6 GB card | Gaming PCs, 16 GB laptops |
| Gemma 4 12B | 6.7 GB | 10 GB+ VRAM | Cards with 12 GB or more |

The file size is only the start. While you chat, the conversation needs memory too, so leave a couple of GB free on top. On an 8 GB laptop that means closing other apps first.

## Measured speeds

This is how fast each model writes its answer, in tokens per second. A token is about three quarters of a word, and most people read about 5 a second, so anything above that feels quick.

| PC | Model | Writes (tokens/s) |
| --- | --- | --- |
| Desktop, AMD RX 5700 XT 8 GB | E4B | **63–72** |
| Desktop, NVIDIA RTX 5060 8 GB | E4B | **56** |
| Desktop, 12 GB graphics card | E4B | **50–55** |
| Desktop, NVIDIA GTX 1660 Super 6 GB | E4B | **35–38** |
| Desktop, AMD RX 5700 XT 8 GB | 12B | **20–35** (short chats only) |
| Desktop, NVIDIA GTX 1650 4 GB | E4B | **about 20** |
| Laptop, Intel Core Ultra 5, 16 GB | E2B | **14–18** |
| Same laptop | E4B | **8–10** |
| Laptop, Intel Iris Xe, 8 GB | E2B | **5–7** |

## What we learned

### E2B is the laptop model

On a 16 GB laptop with no graphics card, E2B finished a full study answer in about 20 seconds. E4B took 112 seconds for the same thing. E2B also got all five of our quick fact checks right. The full comparison is in [E2B vs E4B, measured](https://blog.greencube.app/blog/gemma-4-e2b-vs-e4b).

### E4B is the gaming PC model

Once the whole model sits on a graphics card, E4B is 7 to 9 times faster than on a laptop, and its answers are better than E2B's. Any card with 6 GB or more holds it completely.

### 12B needs real VRAM, not just RAM

On an 8 GB card, 12B answered one short question fine, then crashed every time the chat grew. That PC had 48 GB of RAM, and it didn't help, because the model and the conversation both have to fit on the card. There's more on this in [why the model must fit on your card](https://blog.greencube.app/blog/how-much-vram-for-ai).

## Which Gemma 4 for your PC?

| Your PC | Use |
| --- | --- |
| 8 GB laptop | E2B, with other apps closed |
| 16 GB laptop, no graphics card | E2B for speed; E4B works but is slow |
| Gaming PC with a 6–8 GB card | E4B, fully on the card |
| 12 GB+ card | E4B is fast; 12B becomes an option |

If you'd rather not choose, GreenCube checks your PC and picks the right one for you. The speeds for every PC we tested are in [Can my PC run AI?](https://blog.greencube.app/blog/can-my-pc-run-ai)

## FAQ

### What are the minimum requirements to run Gemma 4 locally?

The smallest one, Gemma 4 E2B (a 2.6 GB file), ran on a laptop with 8 GB of RAM and no graphics card, at 5 to 7 tokens a second in real chats. It needs a couple of GB of free memory to start.

### How much VRAM does Gemma 4 E4B need?

E4B is a 4.2 GB file. It fits fully on a 6 GB graphics card, where it wrote 35 to 38 tokens a second on a GTX 1660 Super. On 8 GB cards it wrote 56 to 72. It also runs without a card on 16 GB of RAM, at about 8 tokens a second.

### Can Gemma 4 12B run on an 8 GB graphics card?

For one short question, yes: 20 to 35 tokens a second on an RX 5700 XT. But it crashed once the conversation got longer, because the card had almost no room left. We'd want at least 10 GB of VRAM for it.

### Is Gemma 4 free to use?

Yes. Google released Gemma 4, including E2B and E4B, under the Apache 2.0 licence, which allows commercial use.
