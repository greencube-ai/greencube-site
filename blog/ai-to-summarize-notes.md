# AI to summarize your notes: which to pick for limits and privacy (2026)

> NotebookLM, ChatGPT, Gemini or an AI on your own PC to summarize notes: how many files each lets you upload for free, whether it trains on them, and how long it takes locally, checked in October 2026.

Canonical: https://blog.greencube.app/blog/ai-to-summarize-notes  
Published: 2026-10-18  
Author: Hector Gras

**Short answer: it depends on whether you care more about free or about your notes never leaving your computer.** NotebookLM is free, cites where each sentence comes from and doesn't train on your notes, but you upload them to Google. Free ChatGPT and Gemini are fine for quick summaries, but cap your files and train on what you upload unless you switch it off. If you don't want to upload your notes anywhere, or hit limits, you need an AI that runs on your own PC, and we measured it: about 15 minutes to summarize a whole chapter on a normal laptop.

- **50** sources per notebook on free NotebookLM
- **10** files per message on free Gemini, with limits that refresh every 5 hours
- **0** files an AI on your own PC uploads

## The options, from their own help pages (October 2026)

For a free, personal account. We haven't measured the quality of each one's summaries; these are their limits and what they do with your uploads, from their own help pages, linked in each row.

| Tool | Free upload limit | Trains on your uploads? | Works offline? |
| --- | --- | --- | --- |
| **NotebookLM** (Gemini Notebook) | 100 notebooks, 50 sources per notebook ([Google](https://support.google.com/notebooklm/answer/16213268?hl=en)) | No, unless you send feedback ([Google](https://support.google.com/notebooklm/answer/17004255?hl=en)) | No |
| **ChatGPT** free | Limited, no number published; stricter than paid plans ([OpenAI](https://help.openai.com/en/articles/9275245-chatgpt-free-tier-faq)) | Yes, by default; can be turned off ([OpenAI](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance)) | No |
| **Gemini** free | Up to 10 files per message, 100 MB each, limits refresh every 5 hours up to a weekly cap ([Google](https://support.google.com/gemini/answer/14903178?hl=en)) | Yes, while Keep Activity is on ([Google](https://support.google.com/gemini/answer/13594961?hl=en)) | No |
| **An AI on your PC** (GreenCube) | No limit: nothing is uploaded; only your computer's time counts | No: your files never reach us ([GreenCube](https://legal.greencube.app/privacy)) | Yes, once installed |

What about other AIs? We checked whether 9 of them train on your chats: [Which AI doesn't train on your chats?](https://blog.greencube.app/blog/ai-that-doesnt-train-on-your-data)

## Which to pick

### Pick NotebookLM if…

You want it free, with each answer citing the part of your notes it comes from ([Google](https://support.google.com/notebooklm/answer/16179559?hl=en)), and you don't mind uploading your notes to Google. Google says it doesn't train on your uploads unless you rate an answer with thumbs up or down. It needs internet and a Google account.

### Pick free ChatGPT or Gemini if…

You only summarize a few pages now and then by pasting the text. Free ChatGPT text chats are no longer limited, but files are, and both train on what you type unless you switch it off (ChatGPT: "Improve the model for everyone"; Gemini: Keep Activity).

### Pick an AI on your own PC if…

You don't want to upload your notes anywhere, you want to add as many chapters as you need with no limits, or you study where the connection is bad. The cost is time: your computer does the work. The times we measured are below.

## How long summarizing takes on your own PC

We measured it with GreenCube on a normal 16 GB laptop with no graphics card, using the small AI (Gemma 4 E2B), on long study documents. The details are in [our PDF study test](https://blog.greencube.app/blog/ai-to-study-from-pdf).

| What you ask for | Measured time |
| --- | --- |
| A full study guide of a chapter of about 5,000 words | **about 15 min** |
| The same for a text almost twice as long | **about 29 min** |
| One specific question about a long document | **about 15 s** (11 of 12 right) |

A full summary takes a while because the AI has to read every part of the chapter: on a laptop, let it run while you take a break. With a graphics card it's much faster; see your card's measured speed in [Can my PC run AI?](https://blog.greencube.app/blog/can-my-pc-run-ai)

## Is there an AI with no file upload limit?

Not in the cloud. Every one we checked caps the free plan: ChatGPT limits uploads without saying how many, Gemini allows up to 10 files per message with 5-hour and weekly limits, and NotebookLM allows 50 sources per notebook and 100 notebooks. Paid plans raise those limits, but they're monthly subscriptions.

An AI that runs on your computer doesn't have that problem, because it uploads nothing: it reads files from your disk. The only limit is how long your PC takes to read them. GreenCube costs €9.99 once, with no limits on messages or files.

## Make the summary actually useful

- **Ask for the format you'll use:** "in 10 bullet points", "dates in a table", "explained like I'm 15".
- **Ask questions, don't just summarize:** ask for exam-style questions or flashcards on the chapter, and answer them yourself without looking.
- **Check what matters:** in our test the AI missed 1 question in 12. Anything that will be on the exam, check against your notes.
- **If they're someone else's notes,** or your school's, check whether you're allowed to upload them to a cloud service first.

## FAQ

### What's the best free AI to summarize notes?

It depends on what matters to you. NotebookLM is free, cites which part of your notes each answer comes from, and doesn't train on your uploads unless you send feedback, but your notes go to Google. If you don't want to upload them anywhere, you need an AI that runs on your own computer.

### Is there an AI with no file upload limit?

Not in the cloud: free ChatGPT limits uploads without publishing a number, free Gemini allows up to 10 files per message with limits that refresh every 5 hours, and NotebookLM allows 50 sources per notebook. An AI on your own PC uploads nothing, so the only limit is how long your computer takes.

### Does ChatGPT train on the notes I upload?

On Free, Go, Plus and Pro accounts, yes by default, unless you turn off "Improve the model for everyone" in Settings, Data controls.

### How long does a local AI take to summarize a chapter?

In our test, a 16 GB laptop with no graphics card took about 15 minutes to write a full study guide of a 5,000-word chapter, and about 15 seconds to answer each specific question about it.
