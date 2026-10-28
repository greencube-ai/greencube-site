# Gemma 4 requirements: what PC you need to run it locally

> Gemma 4 requirements for E2B, E4B and 12B, measured on real PCs: how much RAM and VRAM each needs, and how fast it runs on laptops and gaming graphics cards.

Canonical: https://blog.greencube.app/blog/gemma-4-requirements  
Published: 2026-10-18  
Author: Hector Gras

**Short answer:** the small **Gemma 4 E2B** runs on an **8 GB laptop**. **E4B** wants 16 GB of RAM, or flies on any **6 GB+ graphics card**. **12B** needs **10 GB+ of VRAM** to hold a real conversation.

- **8 GB** of RAM is enough for Gemma 4 E2B, no graphics card needed
- **56–72** tokens a second for E4B on 8 GB gaming cards
- **10 GB** of VRAM before we'd trust 12B in a long chat

## Gemma 4 requirements at a glance

| Model | File size | Minimum we'd suggest | Best on |
| --- | --- | --- | --- |
| **Gemma 4 E2B** | 2.6 GB | 8 GB RAM, no card | Laptops |
| **Gemma 4 E4B** | 4.2 GB | 16 GB RAM, or a 6 GB card | Gaming PCs, 16 GB laptops |
| **Gemma 4 12B** | 6.7 GB | 10 GB+ VRAM | Cards with 12 GB or more |

## Measured speeds

How fast each one writes its answer, in tokens per second (a token is about three quarters of a word; you read about 5 a second). Measured with GreenCube in September and October 2026.

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

### 1. E2B is the laptop model

On a 16 GB laptop with no graphics card it finished a full study answer in about 20 seconds, where E4B took 112. In five quick fact checks it got none wrong. [E2B vs E4B, measured.](https://blog.greencube.app/blog/gemma-4-e2b-vs-e4b)

### 2. E4B is the gaming PC model

Once the whole model sits on a graphics card, E4B is **7 to 9 times faster** than on a laptop, and its answers are better. Any 6 GB+ card does it.

### 3. 12B needs real VRAM, not just RAM

On an 8 GB card, 12B answered one short question fine, then crashed every time the chat grew. That PC had 48 GB of RAM and it didn't help. [Why the model must fit on your card.](https://blog.greencube.app/blog/how-much-vram-for-ai)

## Which Gemma 4 for your PC?

#### 8 GB laptop

E2B. Close other apps first.

#### 16 GB laptop, no card

E2B for speed. E4B works but is slow.

#### Gaming PC, 6–8 GB card

E4B, fully on the card.

#### 12 GB+ card

E4B is fast; 12B becomes an option.

Gemma 4 is released by Google under the Apache 2.0 licence. GreenCube picks the right one for your PC automatically. [See all 10 PCs we measured.](https://blog.greencube.app/blog/can-my-pc-run-ai)

## FAQ

### What are the minimum requirements to run Gemma 4 locally?

The smallest one, Gemma 4 E2B (a 2.6 GB file), ran on a laptop with 8 GB of RAM and no graphics card, at 5 to 7 tokens a second in real chats. It needs a couple of GB of free memory to start.

### How much VRAM does Gemma 4 E4B need?

E4B is a 4.2 GB file. It fits fully on a 6 GB graphics card, where it wrote 35 to 38 tokens a second on a GTX 1660 Super. On 8 GB cards it wrote 56 to 72. It also runs without a card on 16 GB of RAM, at about 8 tokens a second.

### Can Gemma 4 12B run on an 8 GB graphics card?

For one short question, yes: 20 to 35 tokens a second on an RX 5700 XT. But it crashed once the conversation got longer, because the card had almost no room left. We'd want at least 10 GB of VRAM for it.

### Is Gemma 4 free to use?

Yes. Google released Gemma 4, including E2B and E4B, under the Apache 2.0 licence, which allows commercial use.
