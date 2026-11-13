# AI to summarize your notes: which to pick for limits and privacy (2026)

> NotebookLM, ChatGPT, Gemini or an AI on your own PC to summarize notes: how many files each lets you upload for free, whether it trains on them, and how long it takes locally, checked in October 2026.

Canonical: https://blog.greencube.app/blog/ai-to-summarize-notes  
Published: 2026-10-18  
Author: Hector Gras

It depends on which matters more to you: free, or your notes never leaving your computer. NotebookLM is free, cites where each sentence comes from and doesn't train on your notes, but you upload them to Google. Free ChatGPT and Gemini are fine for a quick summary, but they cap your files and train on what you upload unless you switch it off. If you don't want to upload your notes anywhere, you need an AI that runs on your own PC.

I build one of those, GreenCube, so weigh my opinion with that in mind. We measured how long it takes on a normal laptop: about 15 minutes for a whole chapter, and about 15 seconds for a single question.

## The options, from their own help pages (October 2026)

These are the rules for a free, personal account. We haven't measured how good each one's summaries are. What's here is their limits and what they do with your uploads, from their own help pages, linked in each row.

| Tool | Free upload limit | Trains on your uploads? | Works offline? |
| --- | --- | --- | --- |
| **NotebookLM** (Gemini Notebook) | 100 notebooks, 50 sources per notebook ([Google](https://support.google.com/notebooklm/answer/16213268?hl=en)) | No, unless you send feedback ([Google](https://support.google.com/notebooklm/answer/17004255?hl=en)) | No |
| **ChatGPT** free | Limited, no number published; stricter than paid plans ([OpenAI](https://help.openai.com/en/articles/9275245-chatgpt-free-tier-faq)) | Yes, by default; can be turned off ([OpenAI](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance)) | No |
| **Gemini** free | Up to 10 files per message, 100 MB each, limits refresh every 5 hours up to a weekly cap ([Google](https://support.google.com/gemini/answer/14903178?hl=en)) | Yes, while Keep Activity is on ([Google](https://support.google.com/gemini/answer/13594961?hl=en)) | No |
| **An AI on your PC** (GreenCube) | No limit: nothing is uploaded, only your computer's time counts | No, your files never reach us ([GreenCube](https://legal.greencube.app/privacy)) | Yes, once installed |

For other AIs, we checked whether 9 of them train on your chats in [which AI doesn't train on your chats](https://blog.greencube.app/blog/ai-that-doesnt-train-on-your-data).

## Which to pick

### NotebookLM

Pick it if you want something free, with each answer citing the part of your notes it comes from ([Google](https://support.google.com/notebooklm/answer/16179559?hl=en)), and you don't mind uploading your notes to Google. Google says it doesn't train on your uploads unless you rate an answer with thumbs up or down. It needs internet and a Google account.

### Free ChatGPT or Gemini

These are fine if you only summarize a few pages now and then by pasting in the text. Free ChatGPT text chats are no longer limited, but files are. Both train on what you type unless you switch it off: in ChatGPT that's "Improve the model for everyone", in Gemini it's Keep Activity.

### An AI on your own PC

This is the one for you if you don't want to upload your notes anywhere, you want to add as many chapters as you like, or you study where the connection is bad. The cost is time, because your computer does the work.

## How long summarizing takes on your own PC

We measured it with GreenCube on a normal 16 GB laptop with no graphics card, using its smaller AI, Cube 2B (built on [Gemma 4 E2B](https://blog.greencube.app/blog/gemma-4-requirements)), on long study documents. The details are in [our PDF study test](https://blog.greencube.app/blog/ai-to-study-from-pdf).

| What you ask for | Measured time |
| --- | --- |
| A full study guide of a chapter of about 5,000 words | **about 15 min** |
| The same for a text almost twice as long | **about 29 min** |
| One specific question about a long document | **about 15 s** (11 of 12 right) |

A full summary takes a while because the AI has to read every part of the chapter, so on a laptop it's best to let it run while you take a break. With a graphics card it's much faster; your card's measured speed is in [Can my PC run AI?](https://blog.greencube.app/blog/can-my-pc-run-ai)

## Is there an AI with no file upload limit?

Not in the cloud. Every one we checked caps the free plan. ChatGPT limits uploads without saying how many, Gemini allows up to 10 files per message with 5-hour and weekly limits, and NotebookLM allows 50 sources per notebook and 100 notebooks. Paid plans raise those limits, but they're monthly subscriptions.

An AI that runs on your computer doesn't have this problem, because it uploads nothing. It reads files straight from your disk, and the only limit is how long your PC takes. GreenCube costs €9.99 once, with no limits on messages or files.

## Getting a summary you can actually use

Ask for the format you'll study from, such as a list of points, a table of dates, or a simpler explanation. A summary shaped for revision is far more useful than a shorter copy of the chapter.

Better still, don't stop at a summary. Ask for exam-style questions or flashcards on the chapter and answer them without looking. And check anything that will be on the exam against your notes: in our test the AI missed 1 question in 12.

If the notes are someone else's, or your school's, check that you're allowed to upload them to a cloud service before you do.

## FAQ

### What's the best free AI to summarize notes?

NotebookLM, if you're fine with your notes going to Google: it's free, shows which part of your notes each answer comes from, and doesn't train on your uploads unless you send feedback. If you'd rather not upload them anywhere, use an AI that runs on your own computer.

### Is there an AI with no file upload limit?

Not in the cloud. Free ChatGPT limits uploads without saying how many, free Gemini allows up to 10 files per message with limits that refresh every 5 hours, and NotebookLM takes 50 sources per notebook. An AI on your own PC uploads nothing, so the only limit is how long your computer takes.

### Does ChatGPT train on the notes I upload?

Yes, by default on Free, Go, Plus and Pro, unless you switch off "Improve the model for everyone" in Settings, Data controls.

### How long does a local AI take to summarize a chapter?

About 15 minutes for a full study guide of a 5,000-word chapter, and about 15 seconds for each specific question, on a 16 GB laptop with no graphics card in our test.
