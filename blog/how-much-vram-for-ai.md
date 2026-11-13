# How much VRAM do you need for AI? Why the model must fit on your GPU

> How much VRAM do you need for AI? We measured it: a model that spills out of your graphics card runs 6 times slower and crashes in long chats. How to pick one that fits.

Canonical: https://blog.greencube.app/blog/how-much-vram-for-ai  
Published: 2026-10-18  
Author: Hector Gras

You need enough VRAM to hold the whole model plus about 1.5 GB for the conversation and Windows. An AI that fits entirely in your graphics card's memory is fast. One that spills over can end up slower than not using the card at all, and it can crash. Smaller and fully on the card beats bigger and half on.

We didn't take that from a spec sheet. We measured it on a real gaming PC while building GreenCube, the app I make, and the results changed how GreenCube picks a model.

## The test

The PC was a desktop with an AMD RX 5700 XT (8 GB of VRAM) and 48 GB of RAM. We loaded a 12-billion-parameter model (Gemma 4 12B, about 6.7 GB) and put more or less of it on the card, all in one session in September 2026.

| How much of the model was on the card | Writes (tokens/s) |
| --- | --- |
| All of it | **35.6** |
| 28 of its layers | **5.9** |
| 20 of its layers | **4.3** |
| *For comparison: a smaller model (Gemma 4 E4B) on the processor only* | **5.0** |
| *That smaller model, all on the card* | **72.5** |

## What we learned

### It's close to all or nothing

Leaving just part of the model off the card made it 6 times slower. With 20 layers on the card, it was slower than a smaller model running with no card at all. Half on the card gives you the worst of both.

### The biggest model that loads isn't the best

The 12B model did fit entirely on the 8 GB card, for one short question. As the chat grew, it crashed every time, because the card had almost no room left for the conversation. The smaller model had about 3 GB spare and ran at 63 to 72 tokens a second.

### Leave room

On a 4 GB GTX 1650, a 4.2 GB model was squeezed onto a 3.9 GB card, and the very first message failed with "not enough memory". Since then, GreenCube keeps about 1.5 GB of the card free for the chat and for Windows.

## How to pick a model for your card

1. Check your VRAM: Task Manager → Performance → GPU → Dedicated GPU memory.
2. Add about 1.5 GB to the model's file size. That total should fit in your VRAM.
3. When in doubt, go smaller. A smaller model fully on the card beats a bigger one half on it.

If you'd rather not do the sums, GreenCube reads your card and picks a model that fits with room to spare. Real speeds on 10 PCs, from a GTX 1650 to an RTX 5060, are in [Can my PC run AI?](https://blog.greencube.app/blog/can-my-pc-run-ai)

## FAQ

### What happens if an AI model doesn't fit in VRAM?

The part that doesn't fit runs from normal memory, and everything slows down. On our 8 GB card, a model with 28 of its layers on the card wrote 5.9 tokens a second, against 35.6 with all of them: 6 times slower.

### Should I run the biggest AI model my card can load?

No, leave room for the conversation. A 12-billion-parameter model fit on an 8 GB card for a short question, then crashed once the chat got longer, while a smaller one with room to spare was faster and never crashed.

### How much VRAM should I leave free?

About 1.5 GB, for the conversation and Windows; that's what GreenCube leaves. Without that room, a 4 GB card ran out of memory on the first message.
