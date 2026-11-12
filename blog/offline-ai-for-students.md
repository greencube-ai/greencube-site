# Offline AI for students: what works on your laptop with no internet (tested)

> What an AI on your own laptop can do for studying with no internet: questions about your PDFs, study guides, flashcards and explanations, with measured times on 8 GB and 16 GB laptops and gaming PCs.

Canonical: https://blog.greencube.app/blog/offline-ai-for-students  
Published: 2026-07-28 · Updated: 2026-10-18  
Author: Hector Gras

Yes, an AI on your own laptop works as a study tool with the Wi-Fi off. It answers questions about your PDFs, writes study guides, makes flashcards and explains things step by step, all on your computer. What changes from one laptop to the next is speed, and we measured it: about reading speed on an 8 GB laptop, many times faster on a gaming PC. The one thing it can't do offline is anything that needs today's news.

I build one of these apps, GreenCube, and the times below come from it, so weigh my opinion with that in mind. Where we haven't timed something on a machine, the table says so instead of guessing.

## What you can do offline, and how long it takes

We ran these on ordinary student-type machines, with the AIs GreenCube uses: Cube 2B (built on Google's Gemma 4 E2B) on smaller laptops, and Cube 4B (built on Gemma 4 E4B) on PCs with a graphics card.

| Task | 8 GB laptop, no card | 16 GB laptop, no card | Gaming PC (6 GB+ card) |
| --- | --- | --- | --- |
| Chat: how fast it writes | **5–7** tokens/s | **14–18** tokens/s | **37–76** tokens/s on most cards |
| A full explanation plus three exam questions | not timed | **about 20 s** | not timed |
| A question about a long PDF | not timed | **about 15 s** | not timed |
| A study guide of a 5,000-word chapter | not timed | **about 15 min** | not timed |
| A picture (diagram, illustration) | can't: needs about 7 GB free | **2–2.5 min** | **8–89 s** |

A token is about three quarters of an English word, and most people read about 4 words a second ([Brysbaert, 2019](https://doi.org/10.1016/j.jml.2019.104047)), which is roughly 5 tokens. So even the 8 GB laptop keeps up with your eyes. Every PC we measured, with its full numbers, is in [Can my PC run AI?](https://blog.greencube.app/blog/can-my-pc-run-ai), where you can also check yours.

## What it's good at

### Questions about your own documents

Give it a long chapter and ask something specific, like who financed Watt, about a history of the Industrial Revolution. In [our test with three long documents](https://blog.greencube.app/blog/ai-to-study-from-pdf), the small AI on a 16 GB laptop got 11 of 12 questions right, in about 15 seconds each. It finds the paragraphs that hold the words of your question and answers from those, so it sticks to your material rather than the internet's.

### Study guides and flashcards from a whole chapter

A guide of a whole chapter means reading every part of it, so it takes longer: about 15 minutes for 5,000 words on a 16 GB laptop with no graphics card. Start it before a break and it's waiting when you come back.

### Explanations and practice questions, at any hour

Asking it to explain photosynthesis to a 14-year-old and then write three exam questions took about 20 seconds on the same laptop. There's no message limit, so you can ask for the same idea five different ways until it clicks, even at 2 a.m. the night before the exam.

### Places where the Wi-Fi doesn't work

The train, a library with terrible Wi-Fi, a village with no signal. Once it's installed, studying with it needs no connection at all.

## What it's not good at

It doesn't know what happened recently. An offline AI knows what it learned in training, not this week's news or today's results. GreenCube has an Online switch for that, and it starts off every time you open the app.

It isn't right every time. In our PDF test it missed 1 question in 12: asked where a cell stores calcium, it named the wrong part. For anything that matters in an exam, check it against your notes.

It won't beat the biggest cloud AIs on the hardest problems. A model small enough for your laptop has limits. For studying, summarising, testing yourself and everyday questions, it's more than enough.

Old laptops are slow. On 8 GB it works, but slowly, and you'll want to close other apps first. [Our 8 GB test](https://blog.greencube.app/blog/run-ai-on-8gb-ram) has the details.

## Will it run on your laptop?

You can check in 30 seconds. Press **Ctrl + Shift + Esc**, open **Performance**, and look at **Memory** (your RAM) and **GPU** (your graphics card, if you have one). Type them into [our checker](https://blog.greencube.app/blog/can-my-pc-run-ai#checker) and it tells you what runs and how fast it ran on a real PC like yours.

As a rough guide, 8 GB with no graphics card works for chat and study, slowly, but can't make pictures. 16 GB with no card is comfortable for chat, PDFs and study guides, and pictures take a couple of minutes. A gaming PC is fast on most cards we measured, because the graphics card does most of the work. We haven't measured a gaming laptop yet.

## Is it cheating?

It depends on what you do with it and on your school's rules. Using AI to understand a topic, test yourself or get feedback on a draft is usually fine. Handing in AI-written work as your own usually isn't. Check your course's academic integrity policy, and when in doubt, ask your teacher.

## What it costs

Free ChatGPT now allows unlimited everyday text chats, but it caps file uploads and pictures and is starting to show ads in some countries ([we checked the details](https://blog.greencube.app/blog/chatgpt-free-limits)). ChatGPT Plus is $20 a month, about 23 euros in Spain, so more than 200 euros over a school year.

GreenCube is €9.99 once, with no limits on messages, files or pictures, because it all runs on your own computer. It also doesn't train on what you type. Most cloud AIs do by default, and [we checked 9 of them](https://blog.greencube.app/blog/ai-that-doesnt-train-on-your-data).

## FAQ

### Does offline AI for students really work without internet?

Yes. Once the app and its AI are downloaded, chatting, asking about your PDFs, study guides and flashcards all run on your own computer with no connection. Only things that need today's information, like news or live results, need internet.

### Will offline AI run on my student laptop?

Very likely. On our tests, an 8 GB laptop with no graphics card wrote 5 to 7 tokens a second, about reading speed, and a 16 GB laptop 14 to 18. A gaming PC with a graphics card wrote 37 to 76 on most cards we measured.

### Is using AI to study cheating?

That depends on your school's rules. Using AI to understand material, test yourself and get feedback is usually fine; handing in AI-written work as your own usually is not. Check your course's academic integrity policy.

### Do I need an account to use GreenCube?

You sign in once with Google or Microsoft to activate it, and the first launch downloads the AI. After that it works offline, and your chats and files stay on your PC.

### How much disk space does offline AI need?

The AI files GreenCube downloads are 2.6 GB for the smaller model, 4.2 GB for the bigger one and about 6 GB more if you want pictures. Leave some extra room beyond that.
