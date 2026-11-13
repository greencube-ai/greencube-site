# AI to study from a PDF: we asked 12 questions about 3 long documents

> We tested an AI that studies from your PDFs on your own laptop: 12 questions about 3 long documents, right 11 times out of 12 in about 15 seconds. Full study guides take longer.

Canonical: https://blog.greencube.app/blog/ai-to-study-from-pdf  
Published: 2026-10-18  
Author: Hector Gras

Yes, an AI on your own laptop can study from a PDF with you, as long as you ask specific questions. Asked things like "who financed Watt?" about three long documents, it got 11 out of 12 right, in about 15 seconds each. A full study guide of a whole chapter is slower: about 15 minutes on the same laptop.

The AI we tested is the one inside GreenCube, the app I build. We ran the same questions before and after rebuilding the way it reads PDFs, so you can see both.

## The test

We picked three long documents a student might study: the Industrial Revolution (English, about 5,000 words), Spain's Second Republic (Spanish, about 5,000 words) and mitochondria (English, about twice as long). Then we asked 12 questions about small facts buried deep inside them, including one asked in Spanish about an English text.

It ran in October 2026 on a 16 GB laptop with no graphics card, using the small AI (Gemma 4 E2B). We ran a second AI from another family alongside it, to make sure the result wasn't a one-model fluke.

| AI | Before we rebuilt it | After |
| --- | --- | --- |
| Gemma 4 E2B | 5/12 right, median 78 s | **11/12 right, median 15 s** |
| A second AI (Mellum 2) | 8/12 right, median 108 s | **11/12 right, median 21 s** |

## What we learned

### Specific questions work best

The old version skimmed the document and often said "the document doesn't mention it" when it did. Now GreenCube finds the paragraphs that hold the rarest words in your question and answers from those. With the same AI, that gave more than twice as many right answers, 5 times faster. The question asked in Spanish about the English text was answered correctly too.

### It still slips sometimes

Gemma's one miss: asked where a cell stores calcium, it named the wrong part of the cell. On anything that matters for an exam, check the answer against your notes.

### Full study guides take time, on purpose

A guide of the whole document means reading every part of it: about 15 minutes on the laptop for 5,000 words, and 29 for twice that. We tried a version 4 to 5 times faster, but on the dense biology text it lost the basics the chapter opens with. We kept the slower one, because it's complete.

## How to study from a PDF with AI

1. Ask questions first. "What caused X?", "Define Y", "What happened in 1785?" These are fast and accurate.
2. Start the full guide when you take a break. On a laptop, let it run while you eat.
3. Turn the guide into flashcards and test yourself.
4. Check anything exam-critical against your notes or the PDF.

If you want to know how fast your own PC would be, [we measured 10 PCs here](https://blog.greencube.app/blog/can-my-pc-run-ai).

## FAQ

### Can AI answer questions about a long PDF?

Yes. In our test, a small AI on a 16 GB laptop got 11 of 12 questions about facts buried deep in three long documents right, taking a median of 15 seconds per question.

### Can I ask in Spanish about an English PDF?

Yes. One of our test questions was in Spanish about an English document, and the answer was right.

### How long does an AI study guide of a whole PDF take?

About 15 minutes for a 5,000-word document and 29 for one twice that size, on a 16 GB laptop with no graphics card, because the AI has to read every part. Asking specific questions is much faster.

### Is there a limit on how many PDFs I can study with?

No, not with an AI on your own PC: nothing counts your files. Free plans of cloud AIs do cap uploads.
