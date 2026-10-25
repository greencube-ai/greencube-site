# Offline AI for students: what works on your laptop with no internet (tested)

> What an AI on your own laptop can do for studying with no internet: questions about your PDFs, study guides, flashcards and explanations, with measured times on 8 GB and 16 GB laptops and gaming PCs.

Canonical: https://blog.greencube.app/blog/offline-ai-for-students  
Published: 2026-07-28 · Updated: 2026-10-18  
Author: Hector Gras

**Short answer: yes, an AI on your own laptop is a real study tool, with no internet.** It answers questions about your PDFs, writes study guides, makes flashcards and explains things step by step, all on your computer. What changes from one laptop to another is speed, and we measured it: from about reading speed on an 8 GB laptop to many times faster on a gaming PC. What it can't do offline is anything that needs today's news.

- **11/12** questions about long PDFs answered right, about 15 s each, on a 16 GB laptop
- **14–18** tokens a second on a normal 16 GB laptop with no graphics card. You read about 5.
- **€9.99** once, for GreenCube. ChatGPT Plus is about 23 euros a month in Spain.

## What you can do offline, and how long it takes

These are our own measurements, on real student-type machines, with the AIs GreenCube runs (Google's Gemma 4 E2B on smaller laptops, E4B with a graphics card). Where we haven't timed something on a machine, we say so rather than guess.

| Task | 8 GB laptop, no card | 16 GB laptop, no card | Gaming PC (6 GB+ card) |
| --- | --- | --- | --- |
| Chat: how fast it writes | **5–7** tokens/s | **14–18** tokens/s | **37–76** tokens/s on most cards |
| A full explanation plus three exam questions | not timed | **about 20 s** | not timed |
| A question about a long PDF | not timed | **about 15 s** | not timed |
| A study guide of a 5,000-word chapter | not timed | **about 15 min** | not timed |
| A picture (diagram, illustration) | can't: needs about 7 GB free | **2–2.5 min** | **8–89 s** |

A token is about three quarters of an English word, and most people read about 4 words a second ([Brysbaert, 2019](https://doi.org/10.1016/j.jml.2019.104047)), roughly 5 tokens. So even the 8 GB laptop writes at about reading speed. Every PC we measured, with its full numbers, is in [Can my PC run AI?](https://blog.greencube.app/blog/can-my-pc-run-ai), where you can also check yours.

## What it's good at

### 1. Questions about your own documents

Give it a long chapter and ask something specific, like "who financed Watt?" about a history of the Industrial Revolution. In [our test with three long documents](https://blog.greencube.app/blog/ai-to-study-from-pdf), the small AI on a 16 GB laptop got **11 of 12 questions right, in about 15 seconds each**. It finds the paragraphs that hold your question's words and answers from those, so it sticks to your material instead of the internet's.

### 2. Study guides and flashcards from a whole chapter

A guide of a whole chapter means reading every part of it, so it takes longer: about **15 minutes for 5,000 words** on a 16 GB laptop with no graphics card. Start it when you take a break.

### 3. Explanations and practice questions, any time

"Explain photosynthesis to me like I'm 14, then give me three exam questions" took **about 20 seconds** on the same laptop. No message limits, so you can ask the same thing five different ways until it clicks, at 2 a.m. the night before the exam.

### 4. It works where the Wi-Fi doesn't

On the train, in a library with terrible Wi-Fi, in a village with no signal. Once it's installed, studying with it needs no connection at all.

## What it's not good at

- **Anything that happened recently.** An offline AI knows what it learned in training, not this week's news or today's results. GreenCube has an Online switch for that; it starts off every time you open the app.
- **Being right every time.** In our PDF test it missed 1 question in 12: asked where a cell stores calcium, it named the wrong part. For anything that matters in an exam, check against your notes.
- **The hardest problems.** A model small enough for your laptop won't beat the biggest cloud AIs at everything. For studying, summarising, quizzing yourself and everyday questions, it's more than enough.
- **Speed on old laptops.** On an 8 GB laptop it works, but slowly, and you'll want to close other apps first. [Our 8 GB test](https://blog.greencube.app/blog/run-ai-on-8gb-ram) has the details.

## Will it run on your laptop?

Check in 30 seconds: press **Ctrl + Shift + Esc**, go to **Performance**, and look at **Memory** (your RAM) and **GPU** (your graphics card, if you have one). Then type them into [our checker](https://blog.greencube.app/blog/can-my-pc-run-ai#checker): it tells you what runs and how fast it ran on a real PC like yours.

- **8 GB, no graphics card:** works for chat and study, slowly. No pictures.
- **16 GB, no graphics card:** comfortable for chat, PDFs and study guides. Pictures take a couple of minutes.
- **A gaming PC:** fast on most cards we measured, because the graphics card does most of the work. (We haven't measured a gaming laptop yet.)

## Is it cheating?

It depends on what you do with it and on your school's rules. Using AI to understand a topic, test yourself or get feedback on a draft is usually fine. Handing in AI-written work as your own usually is not. Check your course's academic integrity policy, and when in doubt, ask your teacher.

## What it costs

Free ChatGPT now allows unlimited everyday text chats, but caps file uploads and pictures, and is starting to show ads in some countries ([we checked the details](https://blog.greencube.app/blog/chatgpt-free-limits)). ChatGPT Plus is $20 a month, about 23 euros in Spain: over a school year, more than 200 euros. GreenCube is €9.99 once, with no limits on messages, files or pictures, because it all runs on your own computer. And it doesn't train on what you type, which most cloud AIs do by default: [we checked 9 of them](https://blog.greencube.app/blog/ai-that-doesnt-train-on-your-data).

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
