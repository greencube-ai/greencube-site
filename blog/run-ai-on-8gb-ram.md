# Can you run AI with 8 GB of RAM? We tried the weakest laptop we have

> Running an AI model on 8 GB of RAM: 5 to 7 tokens a second in real chats and replies in 30 to 40 seconds on our weakest laptop. It works for chat and study, with one catch: free memory.

Canonical: https://blog.greencube.app/blog/run-ai-on-8gb-ram  
Published: 2026-10-18  
Author: Hector Gras

**Short answer: yes, slowly.** A small AI on an 8 GB laptop writes a bit faster than you read. The catch isn't speed: it's **free memory**. Close your other apps first.

- **9.3** tokens a second on the processor: a bit faster than you read
- **30–40 s** for a full reply
- **~1 GB** free memory left with other apps open, the real problem

## The test

The weakest PC we've measured: a laptop with 8 GB of RAM, Intel Iris Xe graphics, no graphics card, on battery. Small model (Gemma 4 E2B), early October 2026.

| What | Result |
| --- | --- |
| Writing, in real chats | **5–7 tokens/s** |
| Writing, GreenCube's startup test, processor | **9.3 tokens/s** |
| Writing, GreenCube's startup test, Iris Xe graphics | **5.0 tokens/s** (slower) |
| A full reply | **30–40 s** |
| Free memory with other apps open | **about 1 GB** |
| Pictures | **Can't** (the picture AI needs about 7 GB) |

## What we learned

### 1. It works for chat and study

5 to 7 tokens a second in real chats is about reading speed (the short startup test gave 9.3). You'll wait half a minute for a long answer, but it gets there, with no internet and no limits.

### 2. Free memory is the real limit

With the browser and other apps open, the laptop had only about 1 GB free. One day that wasn't enough and the AI couldn't even start. The small model needs a couple of GB to itself.

### 3. The built-in graphics made it slower

On this laptop the Iris Xe graphics wrote at 5.0 tokens a second, the processor at 9.3. On another laptop it was about equal. You can't tell in advance, so GreenCube tests both and uses the faster one.

## Tips for an 8 GB laptop

1. **Close the browser** (or most tabs) before you start. Browsers eat memory.
2. **Restart the laptop** before a long study session. It frees memory other apps forgot to give back.
3. **Ask shorter questions**, or one thing at a time. Shorter answers come back faster.
4. **Skip pictures.** They need about 7 GB; use a bigger PC for those.

See how much faster other PCs are: [we measured 10 PCs here](https://blog.greencube.app/blog/can-my-pc-run-ai).

## FAQ

### Can I run AI on a laptop with 8 GB of RAM?

Yes, a small model. On our 8 GB laptop with Intel Iris Xe graphics it wrote 5 to 7 tokens a second in real chats, about as fast as you read, and replies took 30 to 40 seconds. It can't make pictures.

### Why won't AI start on my 8 GB laptop?

Usually not enough free memory. Our 8 GB laptop had only about 1 GB free with other apps open, and one day the AI couldn't load. Closing the browser and other apps first gives it room.

### Does Intel Iris Xe graphics make AI faster on an 8 GB laptop?

Not for chat. On our laptop the processor wrote at 9.3 tokens a second and the Iris Xe graphics at 5.0. GreenCube tests both on your laptop and uses the faster one.
