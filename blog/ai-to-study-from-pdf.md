# AI to study from a PDF: we asked 12 questions about 3 long documents

> We tested an AI that studies from your PDFs on your own laptop: 12 questions about 3 long documents, right 11 times out of 12 in about 15 seconds. Full study guides take longer.

Canonical: https://blog.greencube.app/blog/ai-to-study-from-pdf  
Published: 2026-10-18  
Author: Hector Gras

**Short answer:** for **specific questions** ("who financed Watt?", "what year did…?"), an AI on your own laptop got **11 out of 12 right in about 15 seconds each**. A **full study guide** of a whole chapter is slower: about 15 minutes on a laptop.

- **11/12** questions answered right, about facts deep inside long documents
- **15 s** median per question, on a 16 GB laptop
- **~15 min** for a full study guide of a 5,000-word document

## The test

Three long documents a student might study: the Industrial Revolution (English, about 5,000 words), Spain's Second Republic (Spanish, about 5,000 words) and mitochondria (English, about twice as long). We asked 12 questions about small facts buried deep inside them, including one question in Spanish about an English text. October 2026, on a 16 GB laptop without a graphics card, with the small AI (Gemma 4 E2B) and a second AI from another family to check it wasn't a one-model fluke.

| AI | Before we rebuilt it | After |
| --- | --- | --- |
| Gemma 4 E2B | 5/12 right, median 78 s | **11/12 right, median 15 s** |
| A second AI (Mellum 2) | 8/12 right, median 108 s | **11/12 right, median 21 s** |

## What we learned

### 1. Ask specific questions

The old way skimmed the document and often said "the document doesn't mention it" when it did. Now GreenCube finds the paragraphs that hold your question's rarest words and answers from those. Same AI, **more than twice as many right answers, 5 times faster**.

### 2. It still slips sometimes

Gemma's one miss: asked where a cell stores calcium, it named the wrong part of the cell. On anything that matters for an exam, check the answer against your notes.

### 3. Full study guides take time, on purpose

A guide of the whole document means reading every part: about 15 minutes on the laptop for 5,000 words, 29 for twice that. We tried a version 4 to 5 times faster, but on the dense biology text it lost the basics the chapter opens with. We kept the slower, complete one.

## How to study from a PDF with AI

1. **Ask questions first.** "What caused X?", "Define Y", "What happened in 1785?" Fast and accurate.
2. **Start the full guide when you take a break.** On a laptop, let it run while you eat.
3. **Turn the guide into flashcards** and test yourself.
4. **Check anything exam-critical** against your notes or the PDF.

Want to know how fast your own PC is? [We measured 10 PCs here.](https://blog.greencube.app/blog/can-my-pc-run-ai)

## FAQ

### Can AI answer questions about a long PDF?

Yes. In our test, a small AI on a 16 GB laptop answered 11 of 12 questions about facts buried deep in three long documents correctly, in a median of 15 seconds per question.

### Can I ask in Spanish about an English PDF?

Yes. One of our test questions was asked in Spanish about an English document, and it was answered correctly.

### How long does an AI study guide of a whole PDF take?

On a 16 GB laptop without a graphics card, about 15 minutes for a document of about 5,000 words and about 29 for one twice that size, because the AI has to read every part. Specific questions are much faster.

### Is there a limit on how many PDFs I can study with?

Not with an AI that runs on your own PC: nothing counts your files. Cloud AI free plans cap file uploads.
