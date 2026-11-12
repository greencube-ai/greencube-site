# Run AI on a laptop without a graphics card: do Intel graphics help?

> We ran AI on a laptop without a graphics card, on the processor and on its Intel graphics. Chat speed barely changed, reading got 1.3 times faster and pictures over 4 times faster.

Canonical: https://blog.greencube.app/blog/ai-on-laptop-without-gpu  
Published: 2026-10-18  
Author: Hector Gras

Yes, you can run AI on a laptop with no graphics card, and a 16 GB laptop writes faster than you read. The Intel graphics built into the chip barely help with chatting, help a little with reading long text, and help a lot with pictures, which came out over 4 times faster.

We wanted to know whether the graphics built into most laptops are worth using for AI, so we ran the same tasks on the processor and on the Intel graphics of one ordinary laptop.

## The test

The laptop has an Intel Core Ultra 5 125U, 16 GB of RAM and no graphics card, only the graphics built into the chip. We ran the same AI on the processor and on the Intel graphics, plugged in, twice each, in September and October 2026.

| Task | Processor | Intel graphics | Difference |
| --- | --- | --- | --- |
| Writing an answer (Gemma 4 E2B) | 13.7–15.5 tokens/s | 14.4–14.5 tokens/s | **about the same** |
| Reading pasted text (Gemma 4 E2B) | 160–167 tokens/s | 203–211 tokens/s | **1.3× faster** |
| One picture, 512 by 512 | 11 min 27 s | 2 min 22 s – 2 min 38 s | **over 4× faster** |

## Chat speed comes from memory, not the chip

Writing an answer is limited by how fast the laptop can move the AI through its memory. The processor and the Intel graphics share that same memory, so they end up writing at about the same speed.

## It can even be slower

With an older small model, Phi-4 Mini, writing got 29% slower on the Intel graphics. With a bigger one, [Gemma 4 E4B](https://blog.greencube.app/blog/gemma-4-requirements), it got 26% faster. Same laptop, opposite results. You can't guess this from the specs, so GreenCube tests your laptop and uses whichever is faster.

## Pictures are where it pays off

Making a picture is heavy maths, the kind graphics chips are built for, and here the difference was huge: 11 and a half minutes went down to about 2 and a half. The details are in [how long one picture takes](https://blog.greencube.app/blog/local-ai-image-generator-speed).

## What this means for your laptop

For chat and study, a 16 GB laptop is enough on its own. It writes faster than you read, with or without the graphics. With long PDFs, the graphics read them a little faster, so the first answer comes sooner.

Pictures are possible on a laptop like this, at about 2 to 3 minutes each, while a gaming PC does one in under a minute. And if you work unplugged, in our runs battery and mains power gave about the same chat speed.

For the full picture, gaming PCs included, [we measured 10 PCs here](https://blog.greencube.app/blog/can-my-pc-run-ai).

## FAQ

### Does integrated graphics make AI faster?

For chatting, barely: on our 16 GB laptop the answer was written at about 14 tokens a second either way. For reading long pasted text it was about 1.3 times faster, and for making pictures over 4 times faster.

### Can integrated graphics make AI slower?

Sometimes. With one small model, writing got 29% slower on the Intel graphics than on the processor; with a bigger one it got 26% faster. It depends on the model and the laptop, which is why GreenCube tests your own laptop and picks.

### Is a laptop without a graphics card good enough for AI?

For chat and studying, yes: a 16 GB laptop writes faster than you read with a small model. Pictures work too but take 2 to 3 minutes each.
