# Can you run AI with 8 GB of RAM? We tried the weakest laptop we have

> Running an AI model on 8 GB of RAM: 5 to 7 tokens a second in real chats and replies in 30 to 40 seconds on our weakest laptop. It works for chat and study, with one catch: free memory.

Canonical: https://blog.greencube.app/blog/run-ai-on-8gb-ram  
Published: 2026-10-18  
Author: Hector Gras

Yes, slowly. A small AI on an 8 GB laptop writes at about the speed you read, and a full reply takes 30 to 40 seconds. The real catch isn't speed, it's free memory, so close your other apps before you start.

We tried it on the weakest PC we've measured, because "will it run on my old laptop?" is one of the first questions people ask about local AI. It does run. Here's what that looks like.

## The test

The laptop has 8 GB of RAM and Intel Iris Xe graphics, with no graphics card, and we ran it on battery. We used GreenCube's small model, Cube 2B (built on [Gemma 4 E2B](https://blog.greencube.app/blog/gemma-4-requirements)), in early October 2026.

| What | Result |
| --- | --- |
| Writing, in real chats | **5–7 tokens/s** |
| Writing, GreenCube's startup test, processor | **9.3 tokens/s** |
| Writing, GreenCube's startup test, Iris Xe graphics | **5.0 tokens/s** (slower) |
| A full reply | **30–40 s** |
| Free memory with other apps open | **about 1 GB** |
| Pictures | **Can't** (the picture AI needs about 7 GB) |

## It works for chat and study

5 to 7 tokens a second in real chats is about reading speed. GreenCube's short startup test gave 9.3, but in real chats it came out lower. You'll wait half a minute for a long answer, but it gets there, with no internet and no limits.

## Free memory is the real limit

With the browser and other apps open, the laptop had only about 1 GB of memory free. One day that wasn't enough and the AI couldn't even start. The small model needs a couple of GB to itself, so on 8 GB it has to share carefully with everything else you have open.

## The built-in graphics made it slower

You'd expect the graphics chip to help, but on this laptop the Iris Xe graphics wrote at 5.0 tokens a second and the processor at 9.3. On another laptop the two were about equal. You can't tell in advance from the specs, so GreenCube tests both on your laptop and uses the faster one.

## Tips for an 8 GB laptop

1. Close the browser, or most of its tabs, before you start. Browsers use a lot of memory.
2. Restart the laptop before a long study session. It frees memory that other apps forgot to give back.
3. Ask one thing at a time. Shorter answers come back faster.
4. Leave pictures for a bigger PC. They need about 7 GB on their own.

To see how much faster other PCs are, [we measured 10 PCs here](https://blog.greencube.app/blog/can-my-pc-run-ai).

## FAQ

### Can I run AI on a laptop with 8 GB of RAM?

Yes, with a small model. On our 8 GB laptop with Intel Iris Xe graphics it wrote 5 to 7 tokens a second, about as fast as you read, and replies took 30 to 40 seconds. It can't make pictures.

### Why won't AI start on my 8 GB laptop?

Usually there isn't enough free memory. Our 8 GB laptop had only about 1 GB free with other apps open, and one day the AI couldn't load, so close the browser and other apps first.

### Does Intel Iris Xe graphics make AI faster on an 8 GB laptop?

Not for chat. On our laptop the processor wrote 9.3 tokens a second and the Iris Xe graphics 5.0; GreenCube tests both on your laptop and uses the faster one.
