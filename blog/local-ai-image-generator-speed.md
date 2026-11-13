# Local AI image generator on your PC: how long one picture takes

> We timed a local AI image generator on a 12 GB graphics card, a laptop with Intel graphics and a laptop processor: from 28 seconds to 11 minutes per picture. What your PC needs.

Canonical: https://blog.greencube.app/blog/local-ai-image-generator-speed  
Published: 2026-10-18  
Author: Hector Gras

On a PC with a decent graphics card, about half a minute per picture. On an ordinary 16 GB laptop, 2 to 3 minutes. On an 8 GB laptop it doesn't work at all, because the picture AI needs more memory than the laptop can spare.

We timed the same picture on three kinds of PC, and the gap is bigger than most people expect: from 28 seconds to more than 11 minutes.

## The test

We used the same picture AI on every PC (Z-Image Turbo, running inside GreenCube) and made one 512 by 512 picture with 8 steps. We timed from pressing the button to the finished picture, in September and October 2026.

| PC | What did the work | Time per picture |
| --- | --- | --- |
| Desktop, 12 GB card, 32 GB RAM | Graphics card | **28 s** |
| Laptop, Core Ultra 5, 16 GB | Built-in Intel graphics | **2 min 22 s – 2 min 38 s** |
| Same laptop | Processor only | **11 min 27 s** |
| Laptop, 8 GB | Not enough memory to start | **Can't** |

## Any graphics helps a lot

The laptop was the surprise. Even the small graphics chip built into its processor made pictures about 4 times faster than the processor alone. Making a picture is heavy, repetitive maths, and that's exactly what graphics chips are built for.

A real graphics card is another 5 times faster on top of that. If you want to make a lot of pictures, the graphics card is the part of the PC that matters.

## Why 8 GB isn't enough

The picture AI asks Windows for about 7 GB while it works, and an 8 GB laptop can't free that much. That's why GreenCube only makes pictures on PCs with at least 12 GB of RAM, and checks there's room before it starts instead of crashing halfway. Chat and study still work on 8 GB, just slowly ([our 8 GB test](https://blog.greencube.app/blog/run-ai-on-8gb-ram)).

## Do other apps slow it down?

Not much, in our test. On the 16 GB laptop we made the same picture with a code editor and a browser open, and once with 4 GB of memory taken up on purpose. It still took about 2 minutes every time, because Windows moves idle programs aside to make room.

## What to expect on your PC

With a graphics card, a picture takes under a minute, so you can make several and keep the best one. On a 16 GB laptop with no card, 2 to 3 minutes is fine for a few pictures: start one and get on with something else while it works.

Nothing counts how many pictures you make, so the only limit is how long you're willing to wait. To see what your own card can do, try [Can my PC run AI?](https://blog.greencube.app/blog/can-my-pc-run-ai#checker) The same laptop's chat speeds are in [AI on a laptop without a graphics card](https://blog.greencube.app/blog/ai-on-laptop-without-gpu).

## FAQ

### How long does it take to make an AI picture on my PC?

It depends on your PC. In our tests a 512 by 512 picture took 28 seconds on a desktop with a 12 GB graphics card, about 2 and a half minutes on a 16 GB laptop using its Intel graphics, and about 11 and a half minutes on the same laptop's processor alone.

### Can I make AI pictures on a laptop without a graphics card?

Yes, if it has 16 GB of RAM, and built-in Intel graphics make it about 4 times faster than the processor alone. With 8 GB it won't work: the picture AI needs about 7 GB by itself.

### Do I need to close other apps to make AI pictures?

Not on a 16 GB laptop: with a code editor and a browser open, the picture took the same time. What matters is that Windows can set aside about 7 GB for it.
