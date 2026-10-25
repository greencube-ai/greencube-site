# Local AI image generator on your PC: how long one picture takes

> We timed a local AI image generator on a 12 GB graphics card, a laptop with Intel graphics and a laptop processor: from 28 seconds to 11 minutes per picture. What your PC needs.

Canonical: https://blog.greencube.app/blog/local-ai-image-generator-speed  
Published: 2026-10-18  
Author: Hector Gras

**Short answer:** on a gaming PC with a decent graphics card, about **half a minute**. On a normal 16 GB laptop, **2 to 3 minutes**. On an 8 GB laptop, it won't work.

- **28 s** on a desktop with a 12 GB graphics card
- **2.5 min** on a 16 GB laptop using its Intel graphics
- **11.5 min** on the same laptop's processor alone

## The test

Same picture AI on every PC (Z-Image Turbo, run inside GreenCube), a 512 by 512 picture, 8 steps. We timed from pressing the button to the finished picture, in September and October 2026.

| PC | What did the work | Time per picture |
| --- | --- | --- |
| Desktop, 12 GB card, 32 GB RAM | Graphics card | **28 s** |
| Laptop, Core Ultra 5, 16 GB | Built-in Intel graphics | **2 min 22 s – 2 min 38 s** |
| Same laptop | Processor only | **11 min 27 s** |
| Laptop, 8 GB | — | **Can't** |

The bars show speed, so longer is faster.

## What we learned

### 1. Any graphics helps a lot

Even the small graphics chip built into the laptop made pictures **about 4 times faster** than the processor alone. A real graphics card is another 5 times faster on top of that.

### 2. It needs about 7 GB of room

The picture AI asks Windows for about 7 GB while it works. That's why an 8 GB laptop can't do it, and why GreenCube checks there's room before it starts instead of crashing halfway.

### 3. Your other apps don't matter much

On the 16 GB laptop we made the same picture with a code editor and a browser open, and even with 4 GB taken up on purpose. It still took about 2 minutes every time. Windows moves idle stuff aside.

## What your PC will feel like

#### Graphics card

Under a minute per picture. Make lots and pick the best one.

#### 16 GB laptop, no card

2 to 3 minutes. Fine for a few pictures; start one and keep studying.

#### 8 GB laptop

No pictures. Chat and study still work.

#### No limit either way

Nothing counts your pictures. The only limit is how long you want to wait.

## FAQ

### How long does it take to make an AI picture on my PC?

In our tests, a 512 by 512 picture took 28 seconds on a desktop with a 12 GB graphics card, about 2 and a half minutes on a 16 GB laptop using its Intel graphics, and about 11 and a half minutes on the same laptop's processor alone.

### Can I make AI pictures on a laptop without a graphics card?

Yes, if it has 16 GB of RAM. Built-in Intel graphics made it about 4 times faster than the processor alone. With 8 GB of RAM it won't work: the picture AI needs about 7 GB by itself.

### Do I need to close other apps to make AI pictures?

Not on a 16 GB laptop. With a code editor and a browser open, the picture took the same time. What matters is that Windows can set aside about 7 GB for it.
